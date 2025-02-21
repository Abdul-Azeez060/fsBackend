from crewai import Agent, LLM
from dotenv import load_dotenv
import os
from tools import scrape_tool, search_tool  # Ensure these tools are defined in tools.py

# Load environment variables
load_dotenv()

# Initialize LLM
llm = LLM(
    model="gemini/gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    api_key="AIzaSyDgqBClWnTZ3_tP6IkgUc3eeqOJH5G-KdU"
)

# Manager Agent (Central Coordinator)
from tools import (
    scrape_tool, search_tool, get_current_stock_price_tool, plot_stock_trend_tool,
    analyze_news_sentiment_tool, optimize_portfolio_tool, loan_repayment_calculator_tool,
    prioritize_expenses_tool, plan_savings_for_goals_tool, assess_risk_tool
)

# Manager Agent
manager_agent = Agent(
    role="Manager Agent",
    goal="Coordinate all operations across data, risk, planning, and investment layers.",
    backstory="Central coordinator ensuring seamless communication and alignment.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool, optimize_portfolio_tool, assess_risk_tool],
    human_input=True,
    llm=llm
)

# Data Collection Agent
data_collection_agent = Agent(
    role="Data Collection Agent",
    goal="Collect user input and financial data from various sources for analysis.",
    backstory="Gathers raw financial data including user inputs, transactions, and market data.",
    verbose=True,
    tools=[scrape_tool, search_tool],
    memory=True,
    llm=llm
)

# Data Analyst Agent
data_analyst_agent = Agent(
    role="Data Analyst Agent",
    goal="Analyze collected data for actionable financial insights.",
    backstory="Uses statistical modeling and ML to find patterns and anomalies.",
    verbose=True,
    tools=[plot_stock_trend_tool, analyze_news_sentiment_tool],
    memory=True,
    llm=llm
)

# Debt Management Agent
debt_management_agent = Agent(
    role="Debt Management Agent",
    goal="Manage loan repayment plans for optimized debt reduction.",
    backstory="Creates repayment plans to minimize interest costs.",
    verbose=True,
    tools=[loan_repayment_calculator_tool, assess_risk_tool],
    human_input=True,
    llm=llm
)

# Budget Optimization Agent
budget_optimization_agent = Agent(
    role="Budget Optimization Agent",
    goal="Optimize budget allocations based on financial goals.",
    backstory="Analyzes spending and income streams to recommend budget adjustments.",
    verbose=True,
    tools=[prioritize_expenses_tool],
    memory=True,
    llm=llm
)

# Goal-Based Planning Agent
goal_based_planning_agent = Agent(
    role="Goal-Based Planning Agent",
    goal="Create financial plans for life goals.",
    backstory="Designs strategies for specific milestones within a timeline.",
    verbose=True,
    tools=[plan_savings_for_goals_tool],
    memory=True,
    llm=llm
)

# Risk Advisor Agent
risk_advisor_agent = Agent(
    role="Risk Advisor Agent",
    goal="Evaluate risks of financial decisions.",
    backstory="Assesses risks in investments, taxes, and retirement plans.",
    verbose=True,
    tools=[assess_risk_tool],
    memory=True,
    llm=llm
)

# Trading Strategy Developer Agent
trading_strategy_agent = Agent(
    role="Trading Strategy Developer Agent",
    goal="Develop trading strategies for various assets.",
    backstory="Uses insights to devise and refine trading strategies.",
    verbose=True,
    tools=[optimize_portfolio_tool, plot_stock_trend_tool],
    memory=True,
    llm=llm
)

# Execution Agent
execution_agent = Agent(
    role="Execution Agent",
    goal="Execute trades with optimal timing and pricing.",
    backstory="Implements strategies considering timing, price, and logistics.",
    verbose=True,
    tools=[get_current_stock_price_tool],
    memory=True,
    llm=llm
)

# Investment Agents
crypto_investment_agent = Agent(
    role="Crypto Investment Agent",
    goal="Manage cryptocurrency investments.",
    backstory="Focuses on crypto markets and portfolio management.",
    verbose=True,
    tools=[get_current_stock_price_tool, plot_stock_trend_tool, analyze_news_sentiment_tool],
    memory=True,
    llm=llm
)

real_estate_investment_agent = Agent(
    role="Real Estate Investment Agent",
    goal="Oversee real estate investments.",
    backstory="Evaluates real estate opportunities and manages portfolios.",
    verbose=True,
    tools=[assess_risk_tool],
    memory=True,
    llm=llm
)

gold_investment_agent = Agent(
    role="Gold Investment Agent",
    goal="Manage gold and precious metal investments.",
    backstory="Analyzes market conditions for safe-haven asset investments.",
    verbose=True,
    tools=[get_current_stock_price_tool],
    memory=True,
    llm=llm
)

mutual_funds_agent = Agent(
    role="Mutual Funds Agent",
    goal="Optimize mutual fund and ETF investments.",
    backstory="Ensures diversification and alignment with financial goals.",
    verbose=True,
    tools=[optimize_portfolio_tool],
    memory=True,
    llm=llm
)

fixed_income_agent = Agent(
    role="Fixed Income Agent",
    goal="Manage low-risk fixed income investments.",
    backstory="Focuses on stability and predictable returns for conservative investors.",
    verbose=True,
    tools=[get_current_stock_price_tool],
    memory=True,
    llm=llm
)
