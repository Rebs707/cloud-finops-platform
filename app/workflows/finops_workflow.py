from app.agents.cost_analysis_agent import CostAnalysisAgent
from app.agents.optimization_agent import OptimizationAgent
from app.agents.forecasting_agent import ForecastingAgent
from app.agents.budget_agent import BudgetAgent


class FinOpsWorkflow:

    def run(self, account):

        return {
            "cost_analysis": CostAnalysisAgent().analyze(account),
            "optimization": OptimizationAgent().optimize(account),
            "forecast": ForecastingAgent().forecast(account),
            "budget": BudgetAgent().check(account)
        }
