FROM python:3

WORKDIR /root/.

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "latency-tester.py"]
