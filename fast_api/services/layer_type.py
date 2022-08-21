from functools import lru_cache
from typing import List

from sqlmodel import Session, select

from db.db import engine
from models.api_models import LayerTypeAPI
from models.models import LayerType


class LayerTypeService:
    def __init__(self):
        pass

    async def get_list(self) -> List[LayerTypeAPI]:
        output = []
        with Session(engine) as session:
            statement = select(LayerType)
            res = session.exec(statement)
            for r in res:
                api_model = LayerTypeAPI(id=r.id, name=r.name)
                output.append(api_model)
        return output


@lru_cache()
def get_layer_type_service() -> LayerTypeService:
    return LayerTypeService()
