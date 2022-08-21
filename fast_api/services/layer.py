from functools import lru_cache
from typing import List, Optional

from sqlmodel import Session, select, SQLModel

from db.db import engine
from models.api_models import LayerAPI
from models.models import Layer


class LayerService:
    def __init__(self):
        pass

    async def get_list(self, layer_type_id: Optional[int]) -> List[LayerAPI]:
        output = []
        with Session(engine) as session:
            statement = select(Layer)
            if layer_type_id:
                statement = statement.where(Layer.layer_type_id == layer_type_id)
            res = session.exec(statement)
            for r in res:
                api_model = LayerAPI(
                    id=r.id,
                    name=r.name,
                    nextgis_layer_id=r.id,
                    type_id=r.layer_type_id,
                    icons=r.icons,
                    search_fields=r.search_fields.split(', ') if r.search_fields else [],
                    view_fields=r.view_fields.split(', ') if r.view_fields else [],
                )
                output.append(api_model)
        return output


@lru_cache()
def get_layer_service() -> LayerService:
    return LayerService()
