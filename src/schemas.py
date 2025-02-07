from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator
from shapely.geometry import Point


class CollisionSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    collision_id: int = Field(alias="COLLISION_ID")
    crash_datetime: datetime
    borough: str | None = Field(None, alias="BOROUGH")
    zip_code: str | None = Field(None, alias="ZIP CODE")
    location: Point | None = None
    on_street_name: str | None = Field(None, alias="ON STREET NAME")
    off_street_name: str | None = Field(None, alias="OFF STREET NAME")
    cross_street_name: str | None = Field(None, alias="CROSS STREET NAME")
    number_of_persons_injured: int = Field(alias="NUMBER OF PERSONS INJURED")
    number_of_persons_killed: int = Field(alias="NUMBER OF PERSONS KILLED")
    number_of_pedestrians_injured: int = Field(alias="NUMBER OF PEDESTRIANS INJURED")
    number_of_pedestrians_killed: int = Field(alias="NUMBER OF PEDESTRIANS KILLED")
    number_of_cyclist_injured: int = Field(alias="NUMBER OF CYCLIST INJURED")
    number_of_cyclist_killed: int = Field(alias="NUMBER OF CYCLIST KILLED")
    number_of_motorist_injured: int = Field(alias="NUMBER OF MOTORIST INJURED")
    number_of_motorist_killed: int = Field(alias="NUMBER OF MOTORIST KILLED")
    contributing_factor_vehicle_1: str | None = Field(
        None, alias="CONTRIBUTING FACTOR VEHICLE 1"
    )
    contributing_factor_vehicle_2: str | None = Field(
        None, alias="CONTRIBUTING FACTOR VEHICLE 2"
    )
    contributing_factor_vehicle_3: str | None = Field(
        None, alias="CONTRIBUTING FACTOR VEHICLE 3"
    )
    contributing_factor_vehicle_4: str | None = Field(
        None, alias="CONTRIBUTING FACTOR VEHICLE 4"
    )
    contributing_factor_vehicle_5: str | None = Field(
        None, alias="CONTRIBUTING FACTOR VEHICLE 5"
    )
    vehicle_type_code1: str | None = Field(None, alias="VEHICLE TYPE CODE 1")
    vehicle_type_code2: str | None = Field(None, alias="VEHICLE TYPE CODE 2")
    vehicle_type_code3: str | None = Field(None, alias="VEHICLE TYPE CODE 3")
    vehicle_type_code4: str | None = Field(None, alias="VEHICLE TYPE CODE 4")
    vehicle_type_code5: str | None = Field(None, alias="VEHICLE TYPE CODE 5")

    @model_validator(mode="before")
    @classmethod
    def parse_combined_fields(cls, data):
        if "CRASH DATE" in data and "CRASH TIME" in data:
            try:
                data["crash_datetime"] = datetime.strptime(
                    f"{data.pop('CRASH DATE')} {data.pop('CRASH TIME')}",
                    "%m/%d/%Y %H:%M",
                )

            except ValueError:
                raise ValueError(f"Invalid date/time format: {data}")

        if "LATITUDE" in data and "LONGITUDE" in data:
            lat, lon = data.pop("LATITUDE"), data.pop("LONGITUDE")

            if lat and lon:
                try:
                    data["location"] = Point(float(lon), float(lat))

                except ValueError:
                    raise ValueError(f"Invalid lat/lon: {lat}, {lon}")

        return data
