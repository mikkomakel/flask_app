import json
import requests


mittaus = {"x": 6,
           "y": 12}

viesti = json.dumps(mittaus)
vastaus = requests.post('http://localhost:5000/api', data=viesti)