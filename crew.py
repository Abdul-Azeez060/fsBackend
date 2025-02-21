import sys
sys.path.append('/Users/abdulazeez/Desktop/fsBackend/.venv/lib')
from dotenv import load_dotenv
load_dotenv()
from crewai import Crew, Process, LLM
from agents import (
    manager_agent,
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
from tasks import (
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
)
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Manager LLM
llm_manager = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.5,
    api_key="AIzaSyDgqBClWnTZ3_tP6IkgUc3eeqOJH5G-KdU"
)

# Create Crew
crew = Crew(
    agents=[
        manager_agent,
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
    ],
    tasks=[
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
    ],
    verbose=True,
    manager_llm=llm_manager,
    process=Process.hierarchical,
)

# Example Input Data: User's Salary, Expenses, Goals, and Risk Tolerance
user_inputs = {
   "user_data" : "The user has a monthly salary of ₹100,000 and incurs monthly expenses of ₹15,000 on rent, ₹4,000 on groceries, ₹3,000 on utilities, ₹2,000 on entertainment, and ₹1,000 on miscellaneous needs.  while also aiming to maintain an emergency fund of at least 6 months' worth of expenses.", 
   "user_query": "I want to start investing my money in different asset classes like mutual funds, stocks, crypto, gold"
}

__all__=[user_inputs]

# Validate User Inputs
def validate_user_inputs(user_inputs):
    if user_inputs['monthly_salary'] <= 0:
        raise ValueError("Monthly salary must be greater than zero.")
    if any(expense < 0 for expense in user_inputs['monthly_expenses'].values()):
        raise ValueError("Expenses cannot be negative.")
    if not user_inputs['life_goals']:
        raise ValueError("At least one life goal must be provided.")

# validate_user_inputs(user_inputs)

# Kickoff the Crew Process
result = crew.kickoff(inputs=user_inputs)

print(result)

with open("final_report.txt", "w", encoding="utf-8") as file:
    file.write(str(result))
print("Final report saved to final_report.txt.")


# logging.info(f"Raw result from crew.kickoff(): {result}")

# # Convert Result to Serializable Format
# def serialize_crew_output(output, visited=None):
#     if visited is None:
#         visited = set()
#     obj_id = id(output)
#     if obj_id in visited:
#         return f"<CircularReference: {type(output).__name__}>"
#     visited.add(obj_id)
#     try:
#         if isinstance(output, dict):
#             return {k: serialize_crew_output(v, visited) for k, v in output.items()}
#         elif isinstance(output, (list, tuple)):
#             return [serialize_crew_output(item, visited) for item in output]
#         elif isinstance(output, (int, float, str, bool, type(None))):
#             return output
#         elif hasattr(output, '__dict__'):
#             return serialize_crew_output(output.__dict__, visited)
#         else:
#             return str(output)
#     except Exception as e:
#         logging.error(f"Error serializing object: {e}")
#         return f"<SerializationError: {type(output).__name__}>"

# # Serialize the result
# serializable_result = serialize_crew_output(result)

# # Save Results to JSON File
# output_file_path = "crewai_output.json"
# with open(output_file_path, "w", encoding="utf-8") as file:
#     json.dump(serializable_result, file, indent=4)
#     print(f"Results saved to {output_file_path}")

# # Function to Generate Final Report
# def generate_final_report(results):
#     # Extract Results
#     monthly_salary = results.get('monthly_salary', 0)
#     monthly_expenses = results.get('monthly_expenses', {})
#     life_goals = results.get('life_goals', [])
#     risk_tolerance = results.get('risk_tolerance', 'Medium')
#     investment_strategies = results.get('investment_strategies', [])
#     debt_repayment_plan = results.get('debt_repayment_plan', {})
#     budget_recommendations = results.get('budget_recommendations', {})

#     # Generate Summary
#     summary = f"""
#     Financial Planning Report
#     ---------------------------------
#     Monthly Salary: ₹{monthly_salary:.2f}
#     Monthly Expenses:
#         - Rent: ₹{monthly_expenses.get('rent', 0):.2f}
#         - Groceries: ₹{monthly_expenses.get('groceries', 0):.2f}
#         - Utilities: ₹{monthly_expenses.get('utilities', 0):.2f}
#         - Entertainment: ₹{monthly_expenses.get('entertainment', 0):.2f}
#         - Miscellaneous: ₹{monthly_expenses.get('miscellaneous', 0):.2f}
#     Life Goals:
#     """
#     for goal in life_goals:
#         summary += f"        - {goal['goal']}: ₹{goal['estimated_cost']:.2f} in {goal['timeline_years']} years\n"
#     summary += f"""
#     Risk Tolerance: {risk_tolerance}
#     Debt Repayment Plan:
#         - Monthly EMI: ₹{debt_repayment_plan.get('monthly_emi', 0):.2f}
#         - Total Payment: ₹{debt_repayment_plan.get('total_payment', 0):.2f}
#         - Total Interest: ₹{debt_repayment_plan.get('total_interest', 0):.2f}
#     Budget Recommendations:
#     """
#     for category, details in budget_recommendations.items():
#         summary += f"        - {category}: ₹{details['amount']:.2f} ({details['priority']})\n"
#     summary += "\nInvestment Strategies:\n"
#     for strategy in investment_strategies:
#         summary += f"        - {strategy}\n"
#     print(summary)

#     # Save Report to File
#     with open("final_report.txt", "w", encoding="utf-8") as file:
#         file.write(summary)
#     print("Final report saved to final_report.txt.")

# # Generate Final Report
# # generate_final_report(serializable_result)
# generate_final_report(result)