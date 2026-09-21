from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    rating = Column(Float, default=5.0)

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    total_amount = Column(Float, default=0.0)
    status = Column(String(50), default="PENDING_APPROVAL")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    vendor = relationship("Vendor")
    items = relationship("POItem", back_populates="po")

class POItem(Base):
    __tablename__ = "po_items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    quantity = Column(Integer, nullable=False)
    
    po = relationship("PurchaseOrder", back_populates="items")
    material = relationship("Material")