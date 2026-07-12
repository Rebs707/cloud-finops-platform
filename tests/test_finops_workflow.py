from app.workflows.finops_workflow import FinOpsWorkflow


def test_finops_workflow():

    result = FinOpsWorkflow().run("production-account")

    assert result["cost_analysis"]["status"] == "analyzed"
    assert result["optimization"]["recommendation"] == "optimization review completed"
    assert result["budget"]["status"] == "compliant"
