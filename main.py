import json
import re
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

async def main():
    search_query = "Java Developer site:linkedin.com/jobs location:Turkey"
    agent = Agent(
        task=f"Go to Google and search '{search_query}', then extract job listings with their URLs. Listed maximum 5 jobs. ",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    result_str = str(result)
    messages = [
        (
            "system",
            "Please this text format: 'job title', 'company name', 'location', 'url'. And convert it to JSON format.",
        ),
        ("human", result_str),
    ]

    ai_message = llm.invoke(messages)

    cleaned_json_str = re.sub(r'```json|```', '', ai_message.content).strip()

    try:
        json_data = json.loads(cleaned_json_str)

        with open("jobs.json", "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print("JSON dosyası başarıyla oluşturuldu: jobs.json")
    except json.JSONDecodeError as e:
        print("JSON dönüşüm hatası:", e)


asyncio.run(main())
