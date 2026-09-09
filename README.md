# latency-tester

A Python script to ping a server (Google by default) to test for latency issues. Includes a threshold setting allowing you to log entries that take longer than X seconds, 0.25 by default. Created with love by FlipperPA fueled by his loathing of Comcast. Here's what it looks like; it logs any line shown in red to a text file to share with your ISP.

<img width="808" height="567" alt="image" src="https://github.com/user-attachments/assets/a01ce3cc-710e-4481-a1eb-c9b95cd3b968" />

## Install & Running

To install dependencies:

```bash
pip install -r requirements.txt
```

To run:

```bash
python latency-tester.py
```

## Building Docker Container

$ docker build -t latency-tester .

## Running Docker Container

```bash
docker run --name latency-tester latency-tester
```

With log files mapped to host:

```bash
docker run --name latency-tester -v <host_dir>:/root/logs/. latency-tester
```
