FROM python:3

RUN echo "findme gateway started"

ENV HOST=0.0.0.0
ENV PORT=8000
ENV SECRET_KEY=ASS
ENV MONGO_HOST=mongodb://127.0.0.1:27017
ENV MONGO_DB_NAME=test

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "App.py"]
RUN echo "findme gateway build succeded"