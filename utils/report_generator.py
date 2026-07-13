from datetime import datetime


def generate_markdown_report(analysis):
    report = f"""# Meeting Report

Generated: {datetime.now().strftime("%d-%m-%Y %H:%M")}

---

## Meeting Type

{analysis.meeting_type}

---

## Meeting Health

{analysis.health_score}/100

---

## Follow-up Required

{"Yes" if analysis.follow_up_required else "No"}

---

## Executive Summary

{analysis.summary}

---

## Decisions
"""

    for decision in analysis.decisions:
        report += f"- {decision}\n"

    report += "\n---\n\n## Risks\n"

    if analysis.risks:
        for risk in analysis.risks:
            report += f"- {risk}\n"
    else:
        report += "No significant risks.\n"

    report += "\n---\n\n## AI Recommendations\n"

    for recommendation in analysis.recommendations:
        report += f"- {recommendation}\n"

    report += "\n---\n\n## Action Items\n"

    for item in analysis.action_items:
        report += (
            f"- **Task:** {item.task}\n"
            f"  - Owner: {item.owner}\n"
            f"  - Due Date: {item.due_date}\n"
            f"  - Priority: {item.priority}\n\n"
        )

    return report