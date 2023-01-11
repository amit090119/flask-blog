import requests
import base64
import hashlib
import json

url = 'https://mercury-uat.phonepe.com/v3/qr/init'
MID = 'UATMERCHANT101'
saltkey = '8289e078-be0b-484d-ae60-052f117f8deb'
keyindex = '1'

def qrInit(txnid):


    payload = {
        'merchantId': MID,
        'transactionId': txnid,
        "merchantOrderId": "ORDER123",
        'amount': 100,
        'expiresIn': 120,
        "message": "DQR for XXX order",
        #"merchantUserId": "1605686960849",
        'storeId': 'store1',
        'terminalId': None
    }

    # for base64 encoded payload
    strjson = json.dumps(payload)
    encoded_dict = strjson.encode('UTF-8')
    encodeddata = base64.b64encode(encoded_dict)
    encodeddata = encodeddata.decode('UTF-8')

    data = {
        "request": encodeddata
    }

    # print(url)
    # print(json.dumps(data))

    str_forSha256 = encodeddata + '/v3/qr/init' + saltkey

    sha_value = hashlib.sha256(str_forSha256.encode('UTF-8')).hexdigest()

    x_verify = sha_value + '###' + keyindex
    # print(x_verify);

    headers = {
        "Content-Type": "application/json",
        "X-VERIFY": x_verify
    }

    #print(headers)
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    return res


with open("/Users/amit.aricent/Documents/flask_env/Flask_Blog/qrstring.csv", 'a') as f:
    print('wait..')
    for i in range(1,150):
        res=qrInit('Check'+str(i))
        f.write(res.text+"\n")
    print('done')




