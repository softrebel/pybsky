import json


def validate_value(value, cls):
    if not isinstance(value, cls):
        raise TypeError(f'{value} must be in type {cls}')
    return True


def json_decode(s: str) -> list | dict:
    return json.loads(s)


def json_encode(obj: object) -> str:
    return json.dumps(obj, indent=4, ensure_ascii=False)
