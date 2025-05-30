
FROM python:3.12

WORKDIR /codebuddy

COPY . /codebuddy

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "codebuddy.py"]

CMD []
