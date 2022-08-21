from functools import lru_cache
from typing import List, Optional

from sqlmodel import Session, select, SQLModel
from sqlalchemy.orm import selectinload

from db.db import engine
from models.api_models import DashboardAPI, DashboardFilterAPI
from models.models import Dashboard, DashboardFilter


class DashboardService:
    def __init__(self):
        pass

    async def get_list(self, layer_id: int) -> List[DashboardAPI]:
        output = []
        with Session(engine) as session:
            statement = select(Dashboard).where(Dashboard.layer_id == layer_id).options(selectinload(Dashboard.filters))
            res = session.exec(statement)
            for r in res:
                api_model = DashboardAPI(
                    id=r.superset_dashboard_id,
                    name=r.name,
                    layer_id=r.layer_id,
                    filters=r.filters,
                )
                output.append(api_model)
        return output


@lru_cache()
def get_dashboard_service() -> DashboardService:
    return DashboardService()
