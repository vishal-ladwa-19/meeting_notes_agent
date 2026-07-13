import json

from models.schemas import MeetingAnalysis


def validate_response(response: str) -> MeetingAnalysis:
    """
    Converts JSON returned by LLM
    into a strongly typed object.
    """

    data = json.loads(response)

    return MeetingAnalysis(**data)