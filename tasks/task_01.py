# -*- coding: utf-8 -*-

"""
HomeWork Task 1
"""

from uuid import uuid4
from queue import Queue, Empty


# Create a request queue
queue = Queue()


class Request:

    def __init__(self):
        self.id = uuid4()

    def __str__(self):
        return f"Request {self.id}"


def generate_request():
    """
    Create a new request and add a request to the queue
    """

    request = Request()
    queue.put(request)
    print(f"Заявку {request} створено та додано до черги")


def process_request():
    """
    Remove a request from the queue and process a request
    """

    try:
        request = queue.get(block=False)
        print(f"Оброблено заявку {request}")
    except Empty:
        print(f"Заявок немає")
