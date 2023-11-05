from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException



class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'Bad Request Body'

    def __init__(self, detail=None, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {'detail': detail}
        else:
            self.detail = {'detail': self.default_detail}