from enum import Enum
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
import requests

from config import API_KEY

router = APIRouter(
    prefix="/distance",
    tags=["distance"]
)

class ResponseDistance(BaseModel):
    distance: str
    duration: str


@router.get("/", response_model=ResponseDistance)
async def distance(
        origin: str = Query(..., description="Starting point", example="Madrid"),
        destination: str = Query(..., description="Destination point", example="Budapest"),
        mode: str = Query(..., description="Transport mode: driving, walking, bicycling, transit "
                                           "(by default: driving)", example="driving"),
        units: str = Query(..., description="Measurement units: metric, imperial "
                                            "(by default: metric)", example="metric")
):
    """
    Calculate the distance between two addresses considering the transport type and the measure units.
    :param origin: Start address
    :param destination: Final address
    :param mode: Transport type: Driving/Walking/Bicycling/Transit
    :param units: Metric/Imperial
    :return: {distance, duration}
    """

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode={mode}&units={units}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        distance = data["rows"][0]["elements"][0]["distance"]["text"]
        duration = data["rows"][0]["elements"][0]["duration"]["text"]
    except:
        raise HTTPException(status_code=400, detail="Invalid Origin or Destination")

    return ResponseDistance(distance=distance, duration=duration)
