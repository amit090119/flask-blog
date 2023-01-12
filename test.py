import unittest
import requests
import hashlib
from MongoRestAPI import app


class FlaskTest(unittest.TestCase):
    def test_responsecode(self):
        tester=app.test_client(self)

        authkey = 'mysecretkey'
        str_forSha256 = 'mygeterequest' + authkey
        checksum = hashlib.sha256(str_forSha256.encode('UTF-8')).hexdigest()

        headers = {
            'content-type': 'application-json',
            'x-verify': checksum
        }
        response=tester.get('/person/1', headers=headers)
        statuscode=response.status_code
        self.assertEqual(statuscode,200)

    def test_contenttype(self):
        authkey='mysecretkey1'
        str_forSha256 = 'mygeterequest' + authkey
        checksum = hashlib.sha256(str_forSha256.encode('UTF-8')).hexdigest()

        headers={
            'content-type':'application-json',
            'x-verify':checksum
        }
        response=requests.get('http://127.0.0.1:5000/person/3',headers=headers)
        print(response)
        self.assertEqual(response.headers.get('Content-Type'),'application/json')


if __name__=='__main__':
    unittest.main()