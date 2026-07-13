from typing import List

from pydantic import BaseModel


class ActionItem(BaseModel):
    task: str
    owner: str
    due_date: str
    priority: str
    status: str = "Pending"


class MeetingAnalysis(BaseModel):
    meeting_type: str
    summary: str
    health_score: int
    follow_up_required: bool
    risks: List[str]
    recommendations: List[str]
    decisions: List[str]
    action_items: List[ActionItem]