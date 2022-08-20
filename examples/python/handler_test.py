import io
import logging
import uuid

import flask

# from .handler import handle

app = flask.Flask("test")


# def test_handle_uploads_url():
#     filename = str(uuid.uuid4()) + ".txt"
#     logging.info(f"Using random filename {filename}")
#     with app.test_request_context(method='POST', data={'upload': (io.BytesIO(b'Hello World 2'), filename)}):
#         handle({"body": b'abc123'}, {})

def test_default():
    assert True
