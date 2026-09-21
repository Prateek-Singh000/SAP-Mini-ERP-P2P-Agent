from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
import models
from database import engine, get_db

# Generate database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="P2P Mini-ERP API")

# --- PYDANTIC SCHEMAS ---
class POItemCreate(BaseModel):
    material_id: int
    quantity: int

class POCreate(BaseModel):
    vendor_id: int
    items: List[POItemCreate]

# --- API ENDPOINTS ---
@app.post("/seed")
def seed_database(db: Session = Depends(get_db)):
    if db.query(models.Vendor).first():
        return {"message": "Database already seeded!"}

    v1 = models.Vendor(name="TechCorp Supplies", rating=4.8)
    v2 = models.Vendor(name="Global Manufacturing Inc", rating=3.5)
    db.add_all([v1, v2])
    db.commit()

    m1 = models.Material(name="ThinkPad T14", price=1200.00, stock_quantity=50)
    m2 = models.Material(name="Dell Monitor 27in", price=300.00, stock_quantity=150)
    db.add_all([m1, m2])
    db.commit()

    return {"message": "Master Data successfully seeded to SAP HANA!"}

@app.post("/purchase-orders")
def create_po(po: POCreate, db: Session = Depends(get_db)):
    # 1. Verify the Vendor exists to prevent SAP HANA foreign key crashes
    vendor = db.query(models.Vendor).filter(models.Vendor.id == po.vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail=f"Vendor ID {po.vendor_id} not found")

    # 2. Create the Purchase Order header
    new_po = models.PurchaseOrder(
        vendor_id=po.vendor_id,
        status="PENDING_APPROVAL",
        total_amount=0.0
    )
    db.add(new_po)
    db.flush() # Flush generates the SAP PO ID temporarily without finalizing the transaction
    
    total = 0.0
    # 3. Create line items and calculate total
    for item in po.items:
        material = db.query(models.Material).filter(models.Material.id == item.material_id).first()
        if not material:
            db.rollback()
            raise HTTPException(status_code=404, detail=f"Material ID {item.material_id} not found")
            
        new_item = models.POItem(
            po_id=new_po.id,
            material_id=item.material_id,
            quantity=item.quantity
        )
        db.add(new_item)
        total += material.price * item.quantity
        
    # 4. Update total and execute a single commit to SAP
    new_po.total_amount = total
    db.commit()
    db.refresh(new_po)
    
    return {
        "message": "Purchase Order created successfully!", 
        "po_id": new_po.id, 
        "total_amount": total, 
        "status": new_po.status
    }

@app.put("/purchase-orders/{po_id}/approve")
def approve_po(po_id: int, db: Session = Depends(get_db)):
    po = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="Purchase Order not found")
    
    po.status = "APPROVED"
    db.commit()
    return {"message": f"PO {po_id} has been approved."}

@app.get("/purchase-orders")
def get_pos(db: Session = Depends(get_db)):
    return db.query(models.PurchaseOrder).all()