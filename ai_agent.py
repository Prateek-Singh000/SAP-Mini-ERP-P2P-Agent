import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from database import DATABASE_URL

# Load environment variables
load_dotenv()

# Initialize a verified Pro model from your authorized list
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

# Connect LangChain to SAP HANA
db = SQLDatabase.from_uri(DATABASE_URL)

# Pass the error handler properly using agent_executor_kwargs
agent_executor = create_sql_agent(
    llm=llm, 
    db=db, 
    verbose=True,
    agent_executor_kwargs={"handle_parsing_errors": True}
)

def query_erp_agent(user_input: str) -> str:
    """Takes a natural language prompt and returns the AI's data-driven answer."""
    try:
        response = agent_executor.invoke({"input": user_input})
        return response["output"]
    except Exception as e:
        return f"Agent Error: {str(e)}"

# Quick local test
if __name__ == "__main__":
    print("Testing AI Agent Connection to SAP HANA...")
    test_prompt = "How many vendors do we have in the system, and what are their names?"
    print(f"\nUser: {test_prompt}")
    print(f"AI: {query_erp_agent(test_prompt)}")