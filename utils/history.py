from datetime import datetime
from pathlib import Path


OUTPUT_DIR = Path("output/history")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_json(result: str):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S_analysis.json")

    path = OUTPUT_DIR / filename

    path.write_text(result, encoding="utf-8")


def save_csv(df):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S_action_items.csv")

    path = OUTPUT_DIR / filename

    df.to_csv(path, index=False)


def save_report(report: str):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S_report.md")

    path = OUTPUT_DIR / filename

    path.write_text(report, encoding="utf-8")