from models.schemas import ActionItem, MeetingAnalysis
from utils.report_generator import generate_markdown_report


def test_report_generation():

    analysis = MeetingAnalysis(
        meeting_type="Project Review",
        summary="Summary",
        health_score=95,
        follow_up_required=True,
        risks=["Risk"],
        recommendations=["Recommendation"],
        decisions=["Decision"],
        action_items=[
            ActionItem(
                task="Testing",
                owner="Sarah",
                due_date="Tomorrow",
                priority="High",
                status="Pending"
            )
        ]
    )

    report = generate_markdown_report(analysis)

    assert "Meeting Report" in report
    assert "Project Review" in report
    assert "Testing" in report