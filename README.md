# latency-tester

A Python script to ping a server (Google by default) to test for latency issues. It includes a threshold setting allowing you to log dropped packets and pings that take longer than X seconds, 0.25 by default. Created with love by FlipperPA fueled by his loathing of Comcast. Here's what it looks like; it logs any line shown in red to a text file to share with your ISP.

<img width="804" height="362" alt="image" src="https://github.com/user-attachments/assets/cc1fd923-2cac-41c3-b9a7-15c323fda537" />

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
