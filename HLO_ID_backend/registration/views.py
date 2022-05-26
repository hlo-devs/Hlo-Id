from hashlib import sha256
from django.shortcuts import render, redirect, HttpResponse
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from cryptography.fernet import Fernet
import requests

client = MongoClient("mongodb+srv://abishekvp:since13062003@cluster0.x4ozo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.HLO
collection = db.users

def otp_auth(contact_no):
    url = "https://verificationapi-v1.sinch.com/verification/v1/verifications"
    payload="{\n  \"identity\": {\n  \"type\": \"number\",\n  \"endpoint\": \"{contact_no}\"\n  },\n  \"method\": \"sms\"\n}"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic MjQzNGUwMTYtZjIwZS00OGQwLTljNzktMDhiY2FiNGU2YTIzOnhxSzdIVXhEdVVxUCthejVMckFpWFE9PQ=='
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())

def encrypt(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encdata = fernet.encrypt(data.encode())
    return encdata

def decrypt():
    pass

def push_data(usd_lt):
    collection.insert_many(usd_lt)

# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def privacy(request):
    return render(request,"privacy.html")

def terms(request):
    return render(request,"terms.html")

def sign_up_org (request):
    if request.method == "POST":
        org = request.POST["organization"]
        dom_name = request.POST["domain_name"]
        user_id = request.POST["user_id"]
        passcode = encrypt(request.POST["passcode"])
        print(org,dom_name,user_id,passcode
        )
        push_data(usd_lt=[{'oganization':org,'domain_name':dom_name,'user_id':user_id,'passcode':passcode}])

    return render(request,'sign-up-org.html')

def sign_up_myself(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        contact_num = request.POST["pnumber"]
        # UserDetails.objects.create(
        #     first_name = first_name,
        #     last_name = last_name,
        #     contact_num = contact_num
        # )
        push_data(usd_lt=[{'firs_name':first_name,"last_name":last_name,"contact_no":contact_num}])
        print(first_name, last_name, contact_num)
        return render(request,'s_ms_f2.html')
    else:
        return render(request,'sign-up-myself.html')
        # otp_auth(contact_no=contact_num)
        # otp = request.POST["one_time_passcode"]
        # return render(request,'s_ms_f2.html')

def form1(request):
    return render(request,"form1.html")

def s_ms_f2(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        contact_num = request.POST["pnumber"]
        # UserDetails.objects.create(
        #     first_name = first_name,
        #     last_name = last_name,
        #     contact_num = contact_num
        # )
        push_data(usd_lt=[{'firs_name':first_name,"last_name":last_name,"contact_no":contact_num}])
        return render(request,'s_ms_f2.html')
    return render(request,"s_ms_f2.html")
