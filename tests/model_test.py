
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))
from microservice.adapters import RandomForestModel, InvalidInput


class RandomForestModelTest(unittest.TestCase):

    def test_validate_data_ok(self):
        data =[
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
        ]
        model = RandomForestModel()
        self.assertTrue(model.validate_data(data))

    def test_validate_data_invalid(self):
        data =[
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
            }
        ]
        model = RandomForestModel()
        self.assertRaises(InvalidInput, model.validate_data, data)

if __name__=="__main__":
    unittest.main()