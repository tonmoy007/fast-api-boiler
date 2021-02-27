from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
