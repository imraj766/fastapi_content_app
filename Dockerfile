FROM python:3.10.14

WORKDIR usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY . .    
RUN chmod +x alembic-upgrade.sh


# CMD ["uvicorn", "app.main:app", "--host" "0.0.0.0", "--port","8000"]
CMD ["./alembic-upgrade.sh"]
