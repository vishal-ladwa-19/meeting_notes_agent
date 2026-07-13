import json

from utils.validator import validate_response


def test_validate_response():

    sample = {
        "meeting_type": "Project Review",
        "summary": "Sample summary",
        "health_score": 90,
        "follow_up_required": True,
        "risks": ["Authentication delay"],
        "recommendations": ["Review deployment"],
        "decisions": ["Deploy Friday"],
        "action_items": [
            {
                "task": "Finish testing",
                "owner": "Sarah",
                "due_date": "Thursday",
                "priority": "High",
                "status": "Pending"
            }
        ]
    }

    result = validate_response(json.dumps(sample))

    assert result.meeting_type == "Project Review"
    assert result.health_score == 90
    assert len(result.action_items) == 1