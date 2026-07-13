# 📝 AI Meeting Intelligence Agent

An AI-powered Meeting Intelligence Agent built using **Streamlit**, **OpenRouter**, and **GPT-4.1 Mini** that automatically analyzes meeting transcripts, extracts key insights, generates action items, identifies risks, and produces downloadable reports.

---

# 🚀 Features

- 📂 Upload Meeting Transcripts
  - TXT
  - PDF
  - DOCX

- 🤖 AI Powered Analysis
  - Executive Summary
  - Meeting Type Detection
  - Meeting Health Score
  - Decisions
  - Action Items
  - Risks
  - AI Recommendations
  - Follow-up Detection

- 📊 Analytics Dashboard
  - Meeting Statistics
  - Priority Distribution
  - Owner Workload
  - Interactive Charts

- 📄 Report Generation
  - Markdown Report
  - JSON Export
  - CSV Export

- 📁 Analysis History

- 📝 Logging

- ✅ Unit Tests

---
## 📚 Sample Meeting Transcripts

To help reviewers evaluate the project quickly, the repository includes sample meeting transcripts.

```
sample_data/
└── meetings/
    ├── project_review.txt
    ├── sprint_planning.txt
    ├── client_meeting.txt
    └── retrospective.txt
```

These examples demonstrate different meeting scenarios and can be uploaded directly into the application.

### Included Examples

| File | Purpose |
|------|---------|
| project_review.txt | Software project review with risks and deployment planning |
| sprint_planning.txt | Agile sprint planning session |
| client_meeting.txt | Client requirements gathering meeting |
| retrospective.txt | Sprint retrospective and process improvements |

### Quick Evaluation

1. Start the application.
2. Upload any transcript from `sample_data/meetings/`.
3. Click **Analyze Meeting**.
4. Review the generated:
   - Executive Summary
   - Meeting Type
   - Health Score
   - Decisions
   - Risks
   - Recommendations
   - Action Items
   - Analytics Dashboard
5. Download the generated JSON, CSV, or Markdown report.
---
# 🏗 Architecture

```
                +------------------+
                |   User Upload    |
                +------------------+
                         |
                         |
          +--------------v--------------+
          | Document Parser             |
          | TXT / PDF / DOCX            |
          +--------------+--------------+
                         |
                         |
          +--------------v--------------+
          | Prompt Builder              |
          +--------------+--------------+
                         |
                         |
          +--------------v--------------+
          | OpenRouter GPT-4.1 Mini     |
          +--------------+--------------+
                         |
                         |
          +--------------v--------------+
          | Structured JSON             |
          +--------------+--------------+
                         |
        +----------------+----------------+
        |                |                |
        |                |                |
   Dashboard         Reports        Analytics
```

---

# 📂 Folder Structure

```
MeetingNotesAgent/

├── app.py
├── config.py
├── README.md
├── requirements.txt
├── .env.example
│
├── models/
│   └── schemas.py
│
├── prompts/
│   └── system_prompt.txt
│
├── sample_data/
│
├── output/
│
├── logs/
│
├── tests/
│
└── utils/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>

cd MeetingNotesAgent
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create

```
.env
```

Add

```env
OPENROUTER_API_KEY=your_api_key

OPENROUTER_MODEL=openai/gpt-4.1-mini
```

Run

```bash
streamlit run app.py
```

---

# 🖥 Usage

1. Upload TXT / PDF / DOCX
2. Click Analyze Meeting
3. Review Summary
4. View Risks
5. View Recommendations
6. Download Reports

---

# 🧪 Running Tests

```bash
pytest
```

---



# 📊 Technologies

- Python 3.11
- Streamlit
- OpenRouter API
- GPT-4.1 Mini
- Pandas
- PyMuPDF
- python-docx
- Pydantic
- Pytest

---

# 📸 Screenshots

Add screenshots here.

Example

```
assets/screenshots/dashboard.png

assets/screenshots/analytics.png
```

---

# 🔮 Future Improvements

- Multi-language Support
- Speaker Identification
- Audio Transcription
- Calendar Integration
- Email Report Delivery
- Meeting Comparison Dashboard

---

# 👨‍💻 Developer

Developed by **Vishal Ladwa**.

