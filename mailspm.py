import os
import sys
import time

def slow(ab):
	for c in ab:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)

os.system("clear")

print("\n\n\n")
slow("		System Loading....")

print("\n\n\n")
time.sleep(3)

os.system("clear")
print("\n\n\n")
slow("		\33[1;32mSuccessfully Loaded...\33[0m")


print("\n\n\n")
time.sleep(3)
#os.system("clear")

os.system('xdg-open https://www.facebook.com/fahim.bhai.RQ')
name=input("	Enter Your Name: \33[1;32m")

slow("	\33[1;33mWELCOME \33[1;32m"+name+" \33[1;33mTO THE WORLD OF RADIAN QUADRO")

print("\n")
os.system("clear")

print("""

░█████████     ░███    ░███████   ░██████   ░███    ░███    ░██          
░██     ░██   ░██░██   ░██   ░██    ░██    ░██░██   ░████   ░██          
░██     ░██  ░██  ░██  ░██    ░██   ░██   ░██  ░██  ░██░██  ░██          
░█████████  ░█████████ ░██    ░██   ░██  ░█████████ ░██ ░██ ░██          
░██   ░██   ░██    ░██ ░██    ░██   ░██  ░██    ░██ ░██  ░██░██          
░██    ░██  ░██    ░██ ░██   ░██    ░██  ░██    ░██ ░██   ░████          
░██     ░██ ░██    ░██ ░███████   ░██████░██    ░██ ░██    ░███          
                                                                         
                                                                         
                                                                         
  ░██████   ░██     ░██    ░███    ░███████   ░█████████    ░██████      
 ░██   ░██  ░██     ░██   ░██░██   ░██   ░██  ░██     ░██  ░██   ░██     
░██     ░██ ░██     ░██  ░██  ░██  ░██    ░██ ░██     ░██ ░██     ░██    
░██     ░██ ░██     ░██ ░█████████ ░██    ░██ ░█████████  ░██     ░██    
░██     ░██ ░██     ░██ ░██    ░██ ░██    ░██ ░██   ░██   ░██     ░██    
 ░██   ░██   ░██   ░██  ░██    ░██ ░██   ░██  ░██    ░██   ░██   ░██     
  ░██████     ░██████   ░██    ░██ ░███████   ░██     ░██   ░██████      
       ░██                                                               
        ░██                                                              
                                                                         
                                                            
""")

print("""\033[93m===============================================================\n\033[0m
\33[1;92m\tCREATED BY   :  RADIAN QUADRO\n
\tON GITHUB    :  RADIANQUADRO\n
\tTOOL VERSION :  PREMIUM\n
\tNETWORK      :  4G,5G\n
\tTOOL STATUS  :  PAID\n
\tTOOL-S NAME  :  Mail Spaming Tools
\tFACEBOOK     :  RADIAN QUADRO\n                       
\n\033[93m===============================================================\033[0m\n\n  """)


import smtplib
import time

# ইনপুট নেওয়া
fmail = input("\33[1;32mEnter Your Gmail: ")
apss = input("\nEnter Your Gmail App Password (Cut the space also : ")
tmail = input("\nEnter Receiver's Mail: ")
repeat = int(input("How many times to send?: "))

# মেইলের কনটেন্ট
msg = input("\nEnterYour Massage : ")

print("\n\n\n")
slow("\33[2;33mPlease Wait some Seconds....\33[1;32m")
# SMTP সার্ভার সেটআপ 
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(fmail, apss)
except Exception as e:
    print("Login failed:", e)
    exit()

# বার বার মেইল পাঠানো
for i in range(repeat):
    try:
        server.sendmail(fmail, tmail, msg)
        print(f"[{i+1}]✅ qEmail sent to {tmail}🥰,Say tnx to RADIAN")
        time.sleep(10)  # ৩ সেকেন্ড বিরতি
    except Exception as e:
        print(f"🚫Failed to send email #{i+1}:", e)


slow("\n\n\n\t\tTnx For Using Radian's Tools")

os.system("clear")
# সার্ভার বন্ধ
server.quit()