# # from unittest.mock import patch
# import io
#
# import flask
# from werkzeug.datastructures import FileStorage
#
from .handler import handle
#
# app = flask.Flask("test")
#
#
# # def test_handle_uploads_url():
# #     # with patch('foo.config'):
# #     with app.test_request_context(
# #             path='/login',
# #             method='POST',
# #             data={'name': 'demo', 'password': 'demo123', "file": open("requirements.txt", "r")}):
# #         handle({"body": b'abc123'}, {})
#

def test_tmp():
    assert True
