import unittest
from .util import app

class TestCompareVersionsApi(unittest.TestCase):

    def test_versions_equal(self):
        data = {'version1': '1.0.0', 'version2': '1.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 0)

    def test_version1_greater(self):
        data = {'version1': '2.0.0', 'version2': '1.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 1)

    def test_version2_greater(self):
        data = {'version1': '1.0.0', 'version2': '2.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], -1)

    def test_version1_missing(self):
        data = {'version2': '1.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 400)

    def test_version2_missing(self):
        data = {'version1': '1.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 400)

    def test_version1_invalid(self):
        data = {'version1': '1.x', 'version2': '2.0.0'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 400)

    def test_version2_invalid(self):
        data = {'version1': '1.0.0', 'version2': '2.z'}
        response = app.test_client().post('/compare-versions', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()