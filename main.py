import requests
import random
import time
import json


print("Choose:\n1. Create 1 account and farm cash.\n2. Create 1 account.\n3. Spam create accounts.")
choice = int(input("Choice: "))





def createAccount():

    url = "https://www.attractionukltd.com/index/user/do_register.html"
    names = ["ali","yoe","ell","eli","ela","oly","ola","olu","tay","lay","duy"]
    user = random.choice(names)
    phone = "07" + str(random.randint(111111111,999999999))
    id = str(random.randint(1000,99999))
    print(user + " : " + phone)
    print("id: " + id)
    data = {"user_name": user, "invite_code": "YQZNCW", "pwd": "123456", "imgverify": "113", "uniqid": id, "tel" : phone, "type" : "Android"}

    request = requests.post(url, data)
    print(request.text)

    print(f"Name: {user}")
    print(f"Phone number: {phone}")
    print(f"Password: 123456")




def farmCash():

    cookies = {'s03378254': 'gp8bnkbt8fpq6nl96qog5s2v1g', "tel" : '07555114993'}

    while True:

        r = requests.post('https://www.attractionukltd.com/index/rot_order/submit_order', cookies=cookies)
        print(r.text)
        res = json.loads(r.text)
        
        if res["code"] == 0:
            oid = res["oid"]
            print(oid)
        else:
            if res["info"] == "Membership level insufficient!Please check with customer service":
                print("30 reviews done!")
                break



        data = {"oid" : oid, "star": "5"}
        r = requests.post('https://www.attractionukltd.com/index/order/do_order', data, cookies=cookies)
        print(r.text)

        time.sleep(0.1)




def SpamCreateAccounts():

    sleep = float(input("Time between gens: ") or 0)

    while True:
        url = "https://www.attractionukltd.com/index/user/do_register.html"
        user = "L " +  str(random.randint(1,99999))
        phone = "07" + str(random.randint(111111111,999999999))
        id = str(random.randint(1000,99999))
        print(user + " : " + phone)
        print("id: " + id)
        data = {"user_name": user, "invite_code": "YQZNCW", "pwd": "123456", "imgverify": "113", "uniqid": id, "tel" : phone, "type" : "Android"}

        request = requests.post(url, data)
        print(request.text)

        print(f"Name: {user}")
        print(f"Phone number: {phone}")
        print(f"Password: 123456")

        time.sleep(sleep)



if choice == 1:
    createAccount()
    input("Press enter to farm cash...")
    farmCash()
elif choice == 2:
    createAccount()
elif choice == 3:
    SpamCreateAccounts()