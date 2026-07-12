class CostAnalysisAgent:

    def analyze(self, account):
        return {
            "account": account,
            "status": "analyzed",
            "spend": "within limits"
        }
