# latency-tester

A simple Python script to ping a server (Google by default) to test for latency issues. Includes a threshold setting allowing you to log entries that take longer than X milliseconds. Created with love by FlipperPA fueled by his loathing of Comcast.

Requires Python and the Python library pexpect, available by pip install.

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
