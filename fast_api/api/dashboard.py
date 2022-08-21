from typing import List, Optional

from fastapi import APIRouter, Depends, Header

from core.utils import check_auth
from models.api_models import DashboardAPI
from services.dashboard import get_dashboard_service, DashboardService

router = APIRouter()


@router.get("/", response_model=List[DashboardAPI])
@check_auth
async def get_dashboard_list(
        layer_id: int,
        authorization: Optional[str] = Header(default=None),
        dashboard_service: DashboardService = Depends(get_dashboard_service),
) -> List[DashboardAPI]:
    dashboards = await dashboard_service.get_list(layer_id)
    return dashboards
