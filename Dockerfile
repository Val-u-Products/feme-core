FROM python:3.8
WORKDIR /feme-core
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8080"]