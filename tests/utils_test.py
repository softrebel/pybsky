import unittest

from pybsky import (
    validate_value,
    validate_get_response,
    BadRequestResponseException,
    AuthenticationRequiredException,
)


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class UtilsTest(unittest.TestCase):
    def test_validate_value_success(self):
        self.assertTrue(validate_value("salam", str))

    def test_validate_value_failed(self):
        self.assertRaises(TypeError, validate_value, "salam", int)

    def test_response_200(self):
        mock_response = MockResponse({"feed": []}, 200)
        response = validate_get_response(mock_response)
        self.assertEqual(response, {"feed": []})

    def test_response_400(self):
        mock_response = MockResponse(
            {"error": "InvalidToken", "message": "Token could not be verified"}, 400
        )
        self.assertRaises(
            BadRequestResponseException, validate_get_response, mock_response
        )

    def test_response_401(self):
        mock_response = MockResponse(
            {"error": "AuthMissing", "message": "Authentication Required"}, 401
        )
        self.assertRaises(
            AuthenticationRequiredException, validate_get_response, mock_response
        )
