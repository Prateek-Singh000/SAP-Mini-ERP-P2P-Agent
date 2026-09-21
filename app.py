import os
import streamlit as st
import requests
from ai_agent import query_erp_agent

# Dynamically route the API request based on the environment
# Streamlit Cloud will use the 'API_URL' secret; local runs will default to localhost
BASE_API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# Set up the web page
st.set_page_config(page_title="SAP Mini-ERP AI Assistant", page_icon="🤖")
st.title("🤖 SAP Mini-ERP AI Assistant")
st.markdown("Ask natural language questions about your SAP HANA Procurement Database.")

# Sidebar for PO Creation
with st.sidebar:
    st.header("🛒 Create Purchase Order")
    with st.form("create_po_form"):
        # We seed ID 1 and 2 earlier, so these defaults are safe
        vendor_id = st.number_input("Vendor ID", min_value=1, step=1)
        material_id = st.number_input("Material ID", min_value=1, step=1)
        quantity = st.number_input("Quantity", min_value=1, step=1)
        
        submit_button = st.form_submit_button("Generate PO")
        
        if submit_button:
            payload = {
                "vendor_id": vendor_id,
                "items": [{"material_id": material_id, "quantity": quantity}]
            }
            
            # Added a specific spinner to account for Render's 50-second wake-up time
            with st.spinner("Waking up backend API (Render may take ~50s from sleep)..."):
                try:
                    # Dynamically construct the URL using the environment variable
                    response = requests.post(f"{BASE_API_URL}/purchase-orders", json=payload)
                    if response.status_code == 200:
                        st.success(f"✅ {response.json()['message']} (PO ID: {response.json()['po_id']})")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Backend connection failed. Ensure your FastAPI server is running at {BASE_API_URL}")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
if prompt := st.chat_input("E.g., How many vendors do we have?"):
    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show a loading spinner while the LangChain agent queries SAP
    with st.chat_message("assistant"):
        with st.spinner("Querying SAP HANA..."):
            response = query_erp_agent(prompt)
            st.markdown(response)
    
    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response})