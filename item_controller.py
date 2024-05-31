from fastapi import HTTPException
from datetime import datetime
from fastapi_project.AssignmentModel.models.item_model import RequestPayload, ResponsePayload
from fastapi_project.utils.multiprocess_utils import add_lists
from fastapi_project.utils.logger import logger


def process_payload(payload: RequestPayload) -> ResponsePayload:
    try:
        started_at = datetime.utcnow()
        logger.info(f"Started processing batch {payload.batchid} at {started_at}")

        response = add_lists(payload.payload)

        completed_at = datetime.utcnow()
        logger.info(f"Completed processing batch {payload.batchid} at {completed_at}")

        return ResponsePayload(
            batchid=payload.batchid,
            response=response,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
    except Exception as e:
        logger.error(f"Error processing batch {payload.batchid}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
