from typing import List, Optional

from fastapi import APIRouter, Depends, Header

from core.utils import check_auth
from models.api_models import LayerTypeAPI
from services.layer_type import get_layer_type_service, LayerTypeService

router = APIRouter()


@router.get("/", response_model=List[LayerTypeAPI])
@check_auth
async def get_layer_type_list(
        authorization: Optional[str] = Header(default=None),
        layer_type_service: LayerTypeService = Depends(get_layer_type_service),
) -> List[LayerTypeAPI]:
    layer_types = await layer_type_service.get_list()
    return layer_types
