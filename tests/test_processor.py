import pytest

from src.processor import transform_and_validate_record
from src.schemas import CollisionSchema


@pytest.mark.parametrize(
    "input_data, expected",
    [
        # ✅ Test: Valid Record (All Fields Present)
        (
            {
                "CRASH DATE": "09/11/2021",
                "CRASH TIME": "02:39",
                "BOROUGH": "QUEENS",
                "ZIP CODE": "11357",
                "LATITUDE": "40.785091",
                "LONGITUDE": "-73.968285",
                "ON STREET NAME": "WHITESTONE EXPRESSWAY",
                "CROSS STREET NAME": "20 AVENUE",
                "OFF STREET NAME": "",
                "NUMBER OF PERSONS INJURED": "2",
                "NUMBER OF PERSONS KILLED": "0",
                "NUMBER OF PEDESTRIANS INJURED": "0",
                "NUMBER OF PEDESTRIANS KILLED": "0",
                "NUMBER OF CYCLIST INJURED": "0",
                "NUMBER OF CYCLIST KILLED": "0",
                "NUMBER OF MOTORIST INJURED": "2",
                "NUMBER OF MOTORIST KILLED": "0",
                "CONTRIBUTING FACTOR VEHICLE 1": "Aggressive Driving/Road Rage",
                "CONTRIBUTING FACTOR VEHICLE 2": "Unspecified",
                "COLLISION_ID": "4455765",
                "VEHICLE TYPE CODE 1": "Sedan",
                "VEHICLE TYPE CODE 2": "Sedan",
            },
            True,
        ),

        # ✅ Test: Missing Optional Fields (Should Still Work)
        (
            {
                "CRASH DATE": "03/26/2022",
                "CRASH TIME": "11:45",
                "BOROUGH": "",
                "ZIP CODE": "",
                "LATITUDE": "",
                "LONGITUDE": "",
                "ON STREET NAME": "QUEENSBORO BRIDGE UPPER",
                "CROSS STREET NAME": "",
                "OFF STREET NAME": "",
                "NUMBER OF PERSONS INJURED": "1",
                "NUMBER OF PERSONS KILLED": "0",
                "NUMBER OF PEDESTRIANS INJURED": "0",
                "NUMBER OF PEDESTRIANS KILLED": "0",
                "NUMBER OF CYCLIST INJURED": "0",
                "NUMBER OF CYCLIST KILLED": "0",
                "NUMBER OF MOTORIST INJURED": "1",
                "NUMBER OF MOTORIST KILLED": "0",
                "CONTRIBUTING FACTOR VEHICLE 1": "Pavement Slippery",
                "COLLISION_ID": "4513547",
                "VEHICLE TYPE CODE 1": "Sedan",
            },
            True,  # Expected result: Successfully parsed
        ),

        # ❌ Test: Missing Required Fields (Should Fail)
        (
            {
                "CRASH DATE": "11/01/2023",
                "CRASH TIME": "01:29",
                "BOROUGH": "BROOKLYN",
                "ZIP CODE": "11230",
                "LATITUDE": "40.62179",
                "LONGITUDE": "-73.970024",
                "ON STREET NAME": "OCEAN PARKWAY",
                "CROSS STREET NAME": "AVENUE K",
                "NUMBER OF PERSONS INJURED": "1",
                "NUMBER OF PERSONS KILLED": "0",
                # ❌ MISSING COLLISION_ID (required)
                "VEHICLE TYPE CODE 1": "Moped",
            },
            False,
        ),
    ],
)
def test_clean_record(input_data, expected):
    """Test that clean_record correctly processes and validates data."""
    result = transform_and_validate_record(input_data)

    if expected:
        assert isinstance(result, CollisionSchema), "Valid record should return a CollisionSchema instance"
    else:
        assert result is None, "Invalid record should return None"