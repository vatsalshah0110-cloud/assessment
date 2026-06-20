FROM python:3.12-slim

WORKDIR /App

ADD  . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]