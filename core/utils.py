import json
import requests
from .exceptions import AuthenticationRequiredException, UnknownResponseException, BadRequestResponseException
Response = requests.models.Response


def validate_value(value, cls):
    if not isinstance(value, cls):
        raise TypeError(f'{value} must be in type {cls}')
    return True


def json_decode(s: str) -> list | dict:
    return json.loads(s)


def json_encode(obj: object) -> str:
    return json.dumps(obj, indent=4, ensure_ascii=False)


def validate_get_response(response: Response):
    content = response.json()
    if response.status_code == 200:
        return content
    elif response.status_code == 401:
        raise AuthenticationRequiredException(content['message'])
    elif response.status_code == 400:
        raise BadRequestResponseException(content['message'])
    else:
        raise UnknownResponseException(
            f"status code => {response.status_code} , response => {response.text}")

    # TODO => handle all type of response
