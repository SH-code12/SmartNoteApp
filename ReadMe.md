## Draft
1. python --version

2. python -m venv venv
.\venv\Scripts\Activate.ps1

3. pip install fastapi

4. pip list | grep -E 'fastapi|uvicorn'

5. uvicorn main:app --reload


6. python.exe -m pip install --upgrade pip

5. pip install "uvicorn[standard]"


8. sudo apt update
sudo apt install postgresql postgresql-contrib

10. psql --version
11. sudo systemctl start postgresql
sudo systemctl enable postgresql
12. sudo systemctl status postgresql
13. sudo -i -u postgres

14. psql
15. CREATE DATABASE notes_db;
16. CREATE USER mido WITH PASSWORD 'midojr';
17. GRANT ALL PRIVILEGES ON DATABASE notes_db TO mido;


7. pip install fastapi uvicorn sqlalchemy asyncpg pydantic requests python-dotenv

-----------------------------------------------------------------------------------

11. Frondend
1. sudo apt update
2. curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
3. sudo apt install -y nodejs
4. node -v
5. npm -v
6. sudo npm install axios react-router-dom
7. npm start
