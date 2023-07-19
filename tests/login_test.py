from tests.base import TestBase

from core import AuthenticationRequiredException


class LoginTest(TestBase):
    def test_login_failed(self):
        username = 'onlycode'
        password = '1234'
        self.assertRaises(AuthenticationRequiredException, self.client.login,
                          username=username, password=password)

    def test_username_type_error(self):

        self.assertRaises(TypeError,self.client.login,username=123,password='')
        self.assertRaises(ValueError,self.client.login,username='',password='')

    def test_password_type_error(self):
        self.assertRaises(TypeError,self.client.login,username='test',password=123)
        self.assertRaises(ValueError,self.client.login,username='test',password='')

