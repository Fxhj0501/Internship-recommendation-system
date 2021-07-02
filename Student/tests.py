from django.test import TestCase

# Create your tests here.
import  requests,pprint

payload = {
    'username': '冯子健',
    'password': 'mark506715'
}

response = requests.post('http://localhost/index',
                         data=payload)

pprint.pprint(response.json())