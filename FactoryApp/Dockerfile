FROM python:3

RUN echo "FactoryApp started"

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "main.py"]
RUN echo "FactoryApp is up"