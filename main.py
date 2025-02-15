from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    search_query = "Java Developer site:linkedin.com/jobs location:Turkey"
    agent = Agent(
        task=f"Go to Google and search '{search_query}', then extract job listings with their URLs.",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()
    print("\n--- Job Listings ---\n")
    print(result)

asyncio.run(main())
