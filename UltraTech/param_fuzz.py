#!/bin/python3

import requests
import sys
import signal
import argparse

def Ctrl_C(sig, frame):
        print("\n\n\033[1;31;40m Process Interrupted\033 \033[1;37;40m")
        sys.exit(0)

signal.signal(signal.SIGINT, Ctrl_C)

def param_Fuzzer(wordlist, domain, port):
        file = open(wordlist, "r")

        for param in file.read().split("\n"):
                url = domain + ":" + port + "/ping?" + param + "="
                request = requests.get(url)
                #print("Parameter used: " + param + "\t\t\t" + "Status Code: " + str(request.status_code))

                if request.status_code != 500:
                        print(f"\033[1;33;40m [!] Possible Parameter Found:\033\t\033[1;32;40m{param}\033 \033[1;37;40m")

        file.close()

shellricko = '''
\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033 ||       \033 \033 ||       \033  \033 =======     \033  \033 ========  \033  \033    =======  \033  \033 ||   //    \033  \033   =====
\033[1;32;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||  //     \033  \033 ||     ||
\033[1;32;40m ((        \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||       ))  \033  \033    ||     \033  \033  ((         \033  \033 || //      \033  \033 ||     ||
\033[1;32;40m   =====   \033  )===(  \033  \033  \033   ====    \033 \033 ||       \033 \033 ||      \033  \033 ||      ))   \033  \033    ||     \033  \033  ((         \033  \033 ||((       \033  \033 ||     ||
\033[1;32;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033  =====((     \033  \033    ||     \033  \033  ((         \033  \033 || \\\\      \033  \033 ||     ||
\033[1;32;40m        )) \033 ||   || \033  \033  \033 ((        \033 \033 ||       \033 \033 ||      \033  \033 ||     \\\   \033  \033     ||     \033  \033  ((        \033  \033  ||  \\\\     \033  \033 ||     ||
\033[1;32;40m  =======  \033 ||   || \033  \033  \033  =======  \033 \033  ======= \033 \033  =======\033  \033 ||      \\\  \033  \033  ========  \033  \033    ======= \033  \033  ||   \\\\    \033  \033   =====
'''


if __name__ == "__main__":
        parser = argparse.ArgumentParser(usage="python3 param_fuzz.py [OPTIONS] Host", description="Fuzzing Web Parameters")
        parser.add_argument("Host", help="Help Menu")
        parser.add_argument("--port", "-p", help="Port to use")
        parser.add_argument("--wordlist", "-w", help="Wordlist to use")

        args = parser.parse_args()

        domain = args.Host
        port = args.port
        wordlist = args.wordlist

        print(shellricko)

        param_Fuzzer(wordlist, domain, port)
