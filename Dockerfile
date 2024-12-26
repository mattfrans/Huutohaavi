FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=web/app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["python", "web/app.py"]
