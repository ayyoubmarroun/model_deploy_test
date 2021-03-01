import unittest
import json
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))

from microservice.app import app

class PredictTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_predict_ok(self):
        payload = json.dumps([
            {
                "Asymmetry coefficient": 1.018, 
                "Perimeter": 14.57, 
                "Length of kernel": 5.554, 
                "Compactness": 0.8811, 
                "Area": 14.88, 
                "Length kernel groove": 4.956, 
                "Width of kernel": 3.333
            }, {
                "Asymmetry coefficient": 4.972, 
                "Perimeter": 14.89, 
                "Length of kernel": 5.776, 
                "Compactness": 0.8823, 
                "Area": 15.56, 
                "Length kernel groove": 5.847,
                "Width of kernel": 3.408
            }
        ])
        response = self.app.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response.headers["Content-Type"])
        self.assertTrue(response.is_json)
        data = response.get_json()
    
    def test_predict_invalid_input(self):
        payload = json.dumps([
            {
                "Asymmetry coefficient": 1.018, 
                "Perimeter": 14.57, 
                "Length of kernel": 5.554, 
                "Compactness": 0.8811, 
                "Length kernel groove": 4.956, 
                "Width of kernel": 3.333
            }, {
                "Asymmetry coefficient": 4.972, 
                "Perimeter": 14.89, 
                "Length of kernel": 5.776, 
                "Area": 15.56, 
                "Length kernel groove": 5.847,
                "Width of kernel": 3.408
            }
        ])
        response = self.app.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(400, response.status_code)
        self.assertEqual("application/json", response.headers["Content-Type"])
        self.assertTrue(response.is_json)

    
    def test_predict_invalid_request(self):
        payload = json.dumps([
            {
                "Asymmetry coefficient": 1.018, 
                "Perimeter": 14.57, 
                "Length of kernel": 5.554, 
                "Compactness": 0.8811, 
                "Length kernel groove": 4.956, 
                "Width of kernel": 3.333
            }, {
                "Asymmetry coefficient": 4.972, 
                "Perimeter": 14.89, 
                "Length of kernel": 5.776, 
                "Area": 15.56, 
                "Length kernel groove": 5.847,
                "Width of kernel": 3.408
            }
        ])
        response = self.app.post("/predict", headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(400, response.status_code)
        self.assertEqual("application/json", response.headers["Content-Type"])
        self.assertTrue(response.is_json)
    

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()
