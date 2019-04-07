import unittest
from wiki.web import routes


class Test(unittest.TestCase):
    def setUp(self):
        self.app = routes.app.test_client()

    def result(self):
        response = self.app.get('/comment')
        assert response.status_code == 200
        assert response.data == 'Hello, World!'
    #def result(self):

if __name__ == '__main__':
    unittest.main()