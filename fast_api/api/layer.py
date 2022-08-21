from typing import List, Optional

from fastapi import APIRouter, Depends, Header

from core.utils import check_auth
from models.api_models import LayerAPI
from services.layer import get_layer_service, LayerService

router = APIRouter()


@router.get("/", response_model=List[LayerAPI])
@check_auth
async def get_layer_list(
        layer_type_id: Optional[int] = None,
        authorization: Optional[str] = Header(default=None),
        layer_service: LayerService = Depends(get_layer_service),
) -> List[LayerAPI]:
    layers = await layer_service.get_list(layer_type_id)
    return layers
