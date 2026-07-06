# Veridict (Ai-legal-assistant)
Demo-https://youtu.be/slSgxj0Z3Cs
## Project Structure
```
AI-LEGAL-ASSISTANT-CREWAI
│
├── agents/
│      case_intake_agent.py
│      ipc_section_agent.py
│      legal_precedent_agent.py
│      legal_drafter_agent.py
│
├── tasks/
│      case_intake_task.py
│      ipc_section_task.py
│      legal_precedent_task.py
│      legal_drafter_task.py
│
├── tools/
│      ipc_sections_search_tool.py
│      legal_precedent_search_tool.py
│
├── ipc.json
├── ipc_vectordb_builder.py
├── query_vectordb.py
├── crew.py
├── main.py
├── app.py
├── requirements.txt
└── README.md
```
## Agent Flow
```
User
   │
   ▼
main.py / app.py
   │
   ▼
crew.py
   │
   ▼
CrewAI
   │
   ├───────────────┐
   ▼               ▼
Case Intake Agent
        │
        ▼
IPC Section Agent
        │
        ▼
Legal Precedent Agent
        │
        ▼
Legal Drafter Agent
        │
        ▼
Final Legal Report
```
setup
```
git clone <repo>

cd AI-LEGAL-ASSISTANT-CREWAI

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

copy env_template.txt .env

# Add API keys to .env

python ipc_vectordb_builder.py

python query_vectordb.py

streamlit run app.py
```
