from langchain_community.llms import Ollama
from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory

# Local LLM (no API keys required)
llm = Ollama(model="llama2")

# -------------------------
# Agent 1: Data Collector
# -------------------------

def fetch_company_data(company: str):
    return f"""
Company: {company}

Recent News:
- Revenue increased by 12%
- New AI product launched

Stock Performance:
- Current Price: $150
- Monthly Growth: +5%
"""

collector_tool = Tool(
    name="CompanyDataFetcher",
    func=fetch_company_data,
    description="Fetches latest company news and stock data"
)

collector_agent = initialize_agent(
    tools=[collector_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# -------------------------
# Agent 2: Analyst
# -------------------------

def analyze_company(data: str):
    return f"""
INSIGHTS:
- Strong financial growth.
- AI product may boost valuation.

RISKS:
- Competitive AI market.
- General market volatility.

Based on:
{data}
"""

analyst_tool = Tool(
    name="CompanyAnalyzer",
    func=analyze_company,
    description="Analyzes company data and produces insights"
)

analyst_agent = initialize_agent(
    tools=[analyst_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# -------------------------
# Memory + Orchestrator
# -------------------------

memory = ConversationBufferMemory()

def run_pipeline(company):
    data = collector_agent.run(company)
    memory.save_context({"input": company}, {"output": data})

    analysis = analyst_agent.run(data)
    memory.save_context({"input": data}, {"output": analysis})

    return analysis


if __name__ == "__main__":
    company = input("Enter company name: ")
    result = run_pipeline(company)

    print("\nFINAL REPORT\n")
    print(result)
