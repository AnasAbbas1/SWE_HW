import unittest
import json
from .math_apis import MathAPIs

class TestMathAPIs(unittest.TestCase):
    def setUp(self):
        self.app = MathAPIs().app.test_client()

    def test_min(self):
        input_data = {'numbers': [5, 3, 8, 2, 9], 'quantifier': 2}
        response = self.app.post('/min', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [2, 3])

    def test_max(self):
        input_data = {'numbers': [5, 3, 8, 2, 9], 'quantifier': 2}
        response = self.app.post('/max', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [9, 8])

    def test_avg(self):
        input_data = {'numbers': [5, 3, 8, 2, 9]}
        response = self.app.post('/avg', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 5.4)

    def test_median(self):
        input_data = {'numbers': [5, 3, 8, 2, 9]}
        response = self.app.post('/median', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 5)

    def test_percentile(self):
        input_data = {'numbers': [5, 3, 8, 2, 9], 'q': 50}
        response = self.app.post('/percentile', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 5)

    def test_missing_parameter(self):
        input_data = {'quantifier': 2}
        response = self.app.post('/min', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), "{'error': 'missing required parameter: numbers'}")

    def test_empty_parameter(self):
        input_data = {'numbers': [], 'quantifier': 2}
        response = self.app.post('/min', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), "{'error': 'required parameter: numbers cannot be empty'}")

    def test_invalid_parameter_type(self):
        input_data = {'numbers': [5, '3', 8, 2, 9], 'quantifier': 2}
        response = self.app.post('/min', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), "{'error': 'numbers list must contain integers only'}")

    def test_invalid_parameter_value(self):
        input_data = {'numbers': [5, 3, 8, 2, 9], 'quantifier': 10}
        response = self.app.post('/min', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), "{'error': 'quantifier parameter must be in range 0 to 5'}")

if __name__ == '__main__':
    unittest