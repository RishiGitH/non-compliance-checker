import openai
import requests
import os
from typing import Union, List, Dict, Any
from django.conf import settings
from requests.exceptions import Timeout
from django.core.exceptions import ValidationError
from api.utills.exceptions import CustomAPIException



class OpenAIAPI:
    def __init__(self, model: Union[str, None] = None):
        self.api_key = getattr(settings, "OPENAI_API_KEY", None)
        self.model = "gpt-3.5-turbo-0613" if model is None else model
        openai.api_key = self.api_key

    def call_gpt3(self, messages: List[Dict[str, Union[str, Dict[str, str]]]]) -> Any:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=2000
            )

            return response
        except Timeout:
            raise ValidationError("Request Timeout. Please try again later.")
        except requests.exceptions.RequestException as e:
            raise ValidationError("GPT API request error. Please try again later")
        except Exception as e:
            raise ValidationError("An unexpected error has occured.")

    def get_response(self, messages: List[Dict[str, Union[str, Dict[str, str]]]]) -> Union[str, None]:
        try:
            response = self.call_gpt3(messages)
            if response['choices']:
                return response['choices'][0]['message']['content']
        except ValidationError as ve:
            raise CustomAPIException(ve, status_code=500)