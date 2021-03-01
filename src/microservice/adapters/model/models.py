from .error import InvalidInput
import pickle
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))


class RandomForestModel():

    def __init__(self):
        self._read_models()

    def read_json(self, filename):
        with open(filename,"r") as f:
            data = json.load(f)
        return data
    
    def validate_data(self, data) -> bool:
        if(data==None or len(data)==0):
            raise InvalidInput("Input data should not be empty")
        for row in data:
            if (set(row.keys())!= self._input_cols):
                raise InvalidInput("Invalid input, structure should be: {}".format(self._input_cols))
        return True

    def _read_models(self):
        with open(os.path.join(current_dir,'data/standard_scaler.pkl'), 'rb') as si:
            self._scaler = pickle.load(si)
        with open(os.path.join(current_dir,'data/random_forest.pkl'), 'rb') as fi:
            self._model = pickle.load(fi)
        self._input_cols = set(self.read_json(os.path.join(current_dir, "data/scalar_config.json")))

    def transform(self, data) -> list:
        try:
            data = [[row[k] for k in self._input_cols]  for row in data]
        except KeyError:
            raise InvalidInput("Invalid input, structure should be: {}".format(self._input_cols))
        transform = self._scaler.transform(data)
        return transform
    
    def predict(self, data) -> list:
        x = self.transform(data)
        predict_data = self._model.predict(x).tolist()
        return predict_data

        

