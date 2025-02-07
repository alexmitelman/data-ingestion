from datetime import datetime

from geoalchemy2 import Geometry
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape
from pydantic import field_serializer
from shapely.geometry import mapping
from sqlmodel import Column, Field, SQLModel


class CollisionModel(SQLModel, table=True):
    __tablename__ = "collisions"
    __table_args__ = {"schema": "nyc"}

    model_config = {"arbitrary_types_allowed": True}

    collision_id: int = Field(primary_key=True)
    crash_datetime: datetime
    borough: str | None = None
    zip_code: str | None = None
    location: Column = Field(
        sa_column=Column(Geometry("POINT", srid=4326, nullable=True))
    )
    on_street_name: str | None = None
    off_street_name: str | None = None
    cross_street_name: str | None = None
    number_of_persons_injured: int
    number_of_persons_killed: int
    number_of_pedestrians_injured: int
    number_of_pedestrians_killed: int
    number_of_cyclist_injured: int
    number_of_cyclist_killed: int
    number_of_motorist_injured: int
    number_of_motorist_killed: int
    contributing_factor_vehicle_1: str | None = None
    contributing_factor_vehicle_2: str | None = None
    contributing_factor_vehicle_3: str | None = None
    contributing_factor_vehicle_4: str | None = None
    contributing_factor_vehicle_5: str | None = None
    vehicle_type_code1: str | None = None
    vehicle_type_code2: str | None = None
    vehicle_type_code3: str | None = None
    vehicle_type_code4: str | None = None
    vehicle_type_code5: str | None = None

    @field_serializer("location")
    def serialize_location(self, location: WKBElement | None):
        """Convert PostGIS `WKBElement` into GeoJSON."""
        if location:
            return mapping(to_shape(location))
        return None
