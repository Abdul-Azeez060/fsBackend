from crewai import Task

# Import Agents
from agents import (
    data_collection_agent,
    data_analyst_agent,
    debt_management_agent,
    budget_optimization_agent,
    goal_based_planning_agent,
    risk_advisor_agent,
    trading_strategy_agent,
    execution_agent,
    crypto_investment_agent,
    real_estate_investment_agent,
    gold_investment_agent,
    mutual_funds_agent,
    fixed_income_agent
)


# # Example Input Data: User's Salary, Expenses, Goals, and Risk Tolerance
# user_inputs = {
#     'monthly_salary': 100000,  # Monthly income
#     'monthly_expenses': {
#         'rent': 15000,
#         'groceries': 4000,
#         'utilities': 3000,
#         'entertainment': 2000,
#         'miscellaneous': 1000
#     },
#     'life_goals': [
#         {'goal': 'Marriage', 'timeline_years': 3, 'estimated_cost': 500000},
#         {'goal': 'Car Purchase', 'timeline_years': 5, 'estimated_cost': 1000000}
#     ],
#     'risk_tolerance': 'High',  # Low, Medium, High
#     'investment_preferences': ['Stocks', 'Real Estate', 'Gold'],  # Preferred asset classes
#     'debt_details': {
#         'loan_amount': 200000,
#         'interest_rate': 9.5,
#         'tenure_years': 3
#     }
# }

# Task for Data Collection Agent: Collect Financial Data
# Task for Data Collection Agent: Collect Financial Data
data_collection_task = Task(
    description=(
        "Collect user-provided financial data, including income, expenses, life goals, "
        "investment preferences, and debt details from {user_data}."
    ),
    expected_output=(
        "A structured dataset containing the user's financial information, ready for analysis."
    ),
    agent=data_collection_agent,
    async_execution=False,
)

# Task for Data Analyst Agent: Analyze Financial Data
data_analysis_task = Task(
    description=(
        "Analyze {user_data} to identify spending patterns, savings potential, and investment opportunities. "
        "Provide actionable insights based on {user_query}."
    ),
    expected_output=(
        "Insights into the user's financial health, including surplus income, spending priorities, "
        "and recommendations for savings and investments."
    ),
    agent=data_analyst_agent,
    async_execution=False,
)

# Task for Debt Management Agent: Manage Loan Repayment
debt_management_task = Task(
    description=(
        "Evaluate loans in {user_data} and create a structured repayment plan "
        "that minimizes interest costs while considering the user's financial capacity."
    ),
    expected_output=(
        "A detailed loan repayment plan, including EMI, total payment, and total interest over the tenure."
    ),
    agent=debt_management_agent,
    async_execution=False,
)

# Task for Budget Optimization Agent: Prioritize Expenses
budget_optimization_task = Task(
    description=(
        "Analyze expenses from {user_data} and prioritize them based on importance "
        "and alignment with financial goals. Suggest adjustments to optimize spending."
    ),
    expected_output=(
        "A prioritized budget plan categorizing expenses with recommendations for reducing non-essential spending."
    ),
    agent=budget_optimization_agent,
    async_execution=False,
)

# Task for Goal-Based Planning Agent: Plan for Life Goals
goal_based_planning_task = Task(
    description=(
        "Create personalized financial plans for life goals using {user_data}. "
        "Incorporate timelines and required savings."
    ),
    expected_output=(
        "A step-by-step plan for each life goal, including required monthly savings "
        "and feasibility based on the user's financial situation."
    ),
    agent=goal_based_planning_agent,
    async_execution=False,
)

# Task for Risk Advisor Agent: Assess Risks
risk_assessment_task = Task(
    description=(
        "Evaluate financial risks using {user_data}, including investments, loans, "
        "and retirement planning. Provide safeguards to mitigate risks."
    ),
    expected_output=(
        "A risk assessment report detailing potential risks and recommended mitigation strategies."
    ),
    agent=risk_advisor_agent,
    async_execution=False,
)

# Task for Trading Strategy Agent: Develop Investment Strategies
strategy_development_task = Task(
    description=(
        "Develop investment strategies based on {user_data} and {user_query}, considering asset classes like stocks,mutual funds,real estate, Commodities like gold, silver, Cryptocurrencies and fixed income."
    ),
    expected_output=(
        "A set of personalized investment strategies optimized for the user's financial goals."
    ),
    agent=trading_strategy_agent,
    async_execution=False,
)

# Task for Execution Agent: Implement Strategies
execution_planning_task = Task(
    description=(
        "Implement approved investment strategies by allocating funds across asset classes "
        "using {user_data}."
    ),
    expected_output=(
        "A detailed execution plan outlining fund allocation and management."
    ),
    agent=execution_agent,
    async_execution=False,
)

# Task for Crypto Investment Agent: Manage Crypto Investments
crypto_investment_task = Task(
    description=(
        "Manage cryptocurrency investments using {user_data}. Identify opportunities and optimize portfolios."
    ),
    expected_output=(
        "A cryptocurrency portfolio with recommendations for entry/exit points."
    ),
    agent=crypto_investment_agent,
    async_execution=False,
)

# Task for Real Estate Investment Agent: Manage Real Estate Investments
real_estate_investment_task = Task(
    description=(
        "Oversee real estate investments from {user_data}. Evaluate opportunities and manage portfolios."
    ),
    expected_output=(
        "A real estate investment plan with property recommendations and expected returns."
    ),
    agent=real_estate_investment_agent,
    async_execution=False,
)

# Task for Gold Investment Agent: Manage Gold Investments
gold_investment_task = Task(
    description=(
        "Manage gold and precious metal investments using {user_data}. Recommend safe-haven asset allocations."
    ),
    expected_output=(
        "A gold investment strategy with allocation percentages and performance metrics."
    ),
    agent=gold_investment_agent,
    async_execution=False,
)

# Task for Mutual Funds Agent: Optimize Mutual Fund Investments
mutual_funds_task = Task(
    description=(
        "Select and monitor mutual funds and ETFs from {user_data} to ensure diversification and alignment with goals."
    ),
    expected_output=(
        "A mutual fund portfolio with fund selections and performance projections."
    ),
    agent=mutual_funds_agent,
    async_execution=False,
)

# Task for Fixed Income Agent: Manage Fixed Income Investments
fixed_income_task = Task(
    description=(
        "Recommend fixed-income products from {user_data} for capital preservation and predictable returns."
    ),
    expected_output=(
        "A fixed-income investment plan with product recommendations and return estimates."
    ),
    agent=fixed_income_agent,
    async_execution=False,
)


__all__ = [
    data_collection_task,
    data_analysis_task,
    debt_management_task,
    budget_optimization_task,
    goal_based_planning_task,
    risk_assessment_task,
    strategy_development_task,
    execution_planning_task,
    crypto_investment_task,
    real_estate_investment_task,
    gold_investment_task,
    mutual_funds_task,
    fixed_income_task
]