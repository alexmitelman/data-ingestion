import logging

from geoalchemy2.shape import from_shape

from db import get_session
from models import CollisionModel
from schemas import CollisionSchema

logger = logging.getLogger(__name__)

def insert_records_to_db(records: list[CollisionSchema]):
    """Inserts processed records into the database in batch."""
    with get_session() as session:
        objects = []

        for record in records:
            if record:
                try:
                    location_geom = from_shape(record.location, srid=4326) if record.location is not None else None
                    collision_obj = CollisionModel(
                        **record.model_dump(exclude_unset=True, exclude={"location"}),
                        location=location_geom
                    )

                    objects.append(collision_obj)

                except Exception as e:
                    logger.error(f"Skipping record {record}: {e}")

        if objects:
            session.bulk_save_objects(objects)
            session.commit()
            logger.info(f"Inserted {len(objects)} collision records successfully.")
