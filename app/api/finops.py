from fastapi import APIRouter
from app.workflows.finops_workflow import FinOpsWorkflow

router = APIRouter()

workflow = FinOpsWorkflow()


@router.get("/finops/{account}")
def finops_check(account: str):
    return workflow.run(account)
