from tests.base import TestBase

from pybsky import BSKY_BASE_URL, FEED_URL, BadRequestResponseException
import requests_mock


class FeedTest(TestBase):
    def test_login_success(self):
        with requests_mock.mock() as m:
            m.get(f"{BSKY_BASE_URL}{FEED_URL}", text='{"feed":[]}')
            result = self.client.get_author_feed("iooobp2.bsky.social")
            self.assertEqual({"feed": []}, result)

    def test_login_failed(self):
        with requests_mock.mock() as m:
            m.get(
                f"{BSKY_BASE_URL}{FEED_URL}",
                text="""{
                            "error": "InvalidToken",
                            "message": "Token could not be verified"
                        }""",
                status_code=400,
            )
            self.assertRaises(
                BadRequestResponseException,
                self.client.get_author_feed,
                "iooobp2.bsky.social",
            )
