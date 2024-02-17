#!/usr/bin/python3
import datetime
import random
import sys
from time import sleep

"""Simulated HTTP request log generator"""
for i in range(10000):
    """Introduce random delay to mimic real-world request intervals"""
    sleep(random.random())

    """Generate and write a log entry to stdout"""
    sys.stdout.write(
        "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
        .format(
            """Generate a random IP address"""
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            """Record the current timestamp"""
            datetime.datetime.now(),
            """Choose a random HTTP status code"""
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            """Generate a random response size"""
            random.randint(1, 1024)
        )
    )
    sys.stdout.flush
