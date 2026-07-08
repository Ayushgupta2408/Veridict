# Veridict (Ai-legal-assistant)
Demo- https://youtu.be/slSgxj0Z3Cs
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
---

<div align="center">

## 💙 Thank You for Visiting!

If you found this project useful...

# ⭐ Please consider giving it a Star ⭐

It inspires me to create more open-source AI projects.

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&pause=1000&color=36BCF7&center=true&vCenter=true&width=650&lines=Built+with+Passion.;Powered+by+Innovation.;Created+by+Ayush+Kumar+Gupta."/>

<br>

### 🚀 Built with ❤️ by **Ayush Kumar Gupta**

<a href="https://github.com/Ayushgupta2408">
<img src="https://img.shields.io/badge/GitHub-Ayushgupta2408-black?style=for-the-badge&logo=github"/>
</a>

</div>
