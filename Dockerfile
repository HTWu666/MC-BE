FROM python:3.10.0-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
