
import requests
from .mixins.login import LoginMixin


class Client(LoginMixin):
    def __init__(
        self,

        proxies=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        self.session = requests.Session()
        self.session.timeout = 20

        self.proxies = None
        if proxies:
            self.proxies = proxies
            self.session.proxies = proxies
