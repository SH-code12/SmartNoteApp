1. python --version

2. python -m venv venv
.\venv\Scripts\Activate.ps1

3. pip install fastapi

4. python.exe -m pip install --upgrade pip

5. pip install "uvicorn[standard]"

6. uvicorn main:app --reload

7. pip install fastapi uvicorn sqlalchemy asyncpg pydantic requests python-dotenv


├── frontend/             # React SPA
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── NoteInput.js
│   │   │   ├── NoteList.js
│   │   │   └── NoteSummary.js
│   └── package.json

