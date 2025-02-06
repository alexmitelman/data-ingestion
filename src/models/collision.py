from sqlmodel import Field, SQLModel
from datetime import datetime
from shapely.geometry import Point


class CollisionModel(SQLModel, table=True):
    __tablename__ = "collisions"
    __table_args__ = {"schema": "nyc"}

    collision_id: int = Field(primary_key=True)
    crash_datetime: datetime
    borough: str | None = None
    zip_code: str | None = None
    location: Point | None = None
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