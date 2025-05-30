
FROM python:3.12

WORKDIR /CodeBuddy

COPY . /CodeBuddy

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "codebuddy.py"]

CMD []
