import logging

from pydantic import ValidationError

from schemas import CollisionSchema

logger = logging.getLogger(__name__)

def transform_and_validate_record(record: dict) -> CollisionSchema | None:
    """Cleans and transforms a single record using Pydantic aliases."""
    try:
        return CollisionSchema.model_validate(record)
    
    except (ValueError, KeyError, ValidationError) as e:
        logger.error(f"Skipping record due to error: {e} | Data: {record}")

        return None
