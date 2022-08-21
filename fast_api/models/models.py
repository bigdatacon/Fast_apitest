from typing import Optional, Dict, Any, List

from sqlmodel import Field, Relationship, SQLModel, Column, JSON
from sqlalchemy import UniqueConstraint


class LayerType(SQLModel, table=True):

    __tablename__ = "layer_type"

    # Optional because if we use this field as auto id increment
    # the value would be None before it gets to the database
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()


class Layer(SQLModel, table=True):

    __tablename__ = "layer"
    # __table_args__ = (UniqueConstraint("nextgis_layer_id"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    layer_type_id: Optional[int] = Field(default=None, foreign_key="layer_type.id")
    icons: Optional[Dict[Any, Any]] = Field(index=False, sa_column=Column(JSON))
    search_fields: Optional[str] = Field(default=None)
    view_fields: Optional[str] = Field(default=None)


class Dashboard(SQLModel, table=True):

    __tablename__ = "dashboard"

    id: Optional[int] = Field(default=None, primary_key=True)
    superset_dashboard_id: int = Field()
    name: str = Field()
    layer_id: int = Field(default=None, foreign_key="layer.id")
    filters: List["DashboardFilter"] = Relationship(back_populates="dashboard")


class DashboardFilter(SQLModel, table=True):

    __tablename__ = "dashboard_filter"

    id: Optional[int] = Field(default=None, primary_key=True)
    dashboard_id: int = Field(default=None, foreign_key="dashboard.id")
    filter_id: str = Field()
    field_name: str
    value: Optional[str]
    dashboard: Dashboard = Relationship(back_populates="filters")
