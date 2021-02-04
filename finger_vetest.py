from pyfingerprint.pyfingerprint import PyFingerprint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json
import pyrebase

config = {
    "apiKey" : "AlzaSyBMwqwdVHK5i8hWD9AbUpLA8AHvqo9Ccyw",
    "authDomain" : "ibl-app",
    "databaseURL": "https://ibl-app.firebaseio.com/",
    "storageBucket": "ibl-app.appspot.com"
}
firebase = pyrebase.initialize_app(config)
# initializations
cred = credentials.Certificate('/home/pi/IBLProject/ibl-app-firebase-adminsdk-taa9l-755e11dd6b.json')
firebase_admin.initialize_app(cred)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)
try:
    print('Waiting for finger...')
    ## 지문이 읽힐때까지 기다림
    while ( f.readImage() == False ):
        pass
    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    db = firestore.client()
    doc_ref = db.collection('Control').document('FingerprintResult')

    doc = doc_ref.get(field_paths = {'result'}).to_dict().get('result')
    
    print(doc)
    print("@@@@@")
    print(f.uploadCharacteristics(0x02,eval(doc)))
    score=f.compareCharacteristics()
    print(score)
    print("!!!!!!")


except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
