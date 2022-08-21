from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class LayerTypeAPI(BaseModel):
    id: int
    name: str


class LayerAPI(BaseModel):
    id: int
    name: str
    nextgis_layer_id: int
    type_id: Optional[int]
    icons: Optional[Dict[Any, Any]]
    search_fields: List[str]
    view_fields: List[str]


class DashboardFilterAPI(BaseModel):
    filter_id: str
    field_name: str
    value: Optional[str]


class DashboardAPI(BaseModel):
    id: int
    name: str
    layer_id: int
    filters: List[DashboardFilterAPI]
