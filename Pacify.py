#!/usr/bin/python3
#Author: Nicholas Roddy
#The goal of this program is to take a malicious URL and defang it inorder to allow it to be shared safely, or for it to be refanged for further analysis.
#Additionally, this program takes the refanged URL and runs scans against it using the Virus Total API and returns the results for initial analysis.

#Imports modules for menu and defanging process
import argparse
from pprint import pprint
from defang import defang, refang
from pyfiglet import Figlet
from colorama import init, Fore, Style
from virustotal_python import Virustotal
from virustotal_python.virustotal import VirustotalError

init(convert=True) #Allows colorama to be initialized
vtotal = Virustotal(API_KEY = "ENTER API KEY") #imports Virus Total API

#Takes a Malcious URL and defangs them
def defang_func():
        #Determines fonts
        custom_fig = Figlet(font='doom')
        subtext_fig = Figlet(font='digital')

        sub = "With all the stuff you care about & none of the stuff you don\'t!" #Subtext for menu

        #Main Menu
        print(Fore.CYAN + custom_fig.renderText('URL Pacifier v4.1'))
        print(Style.DIM + Fore.YELLOW + subtext_fig.renderText(sub.center(40)))
        print(Fore.CYAN + "---------------------------------------------------------------------------")
        print("\n")

        uput = input("Would you like to pacify or depacify the URL?\nPress 1.) to pacify or 2.) to depacify: ")

        if uput == '1':
            malURL = input("\nInsert your Malicious URL: ")

            output = defang(malURL, all_dots=True, colon=True)

            print("\nHere's the pacified link:\n" + output + "\n")
            user_choice()

        elif uput == '2':
            malURL = input("\nInsert your Malicious URL: ")

            output = refang(malURL)

            #Takes refanged URL and submits it to the VT DB in order to see if it's malicious or not
            try:
                resp = vtotal.request("url/scan", params={"url": output}, method="POST")
                url_resp = resp.json()
                scan_id = url_resp["scan_id"]
                analysis_resp = vtotal.request("url/report", params={"resource": scan_id})
                #outputs the results JSON data
                jdata = analysis_resp.json()

                #Next, we need to filter the information so that way we know whether or not a URL us malicious
                #If positives are more than 0, then it outputs the reason for it being malicious
                if jdata['positives'] > 0:
                    
                    #Outputs how many positives are found out of the total scans
                    print(Fore.RED + "\nVirus Total has detected that " + str(jdata['positives']) + " out of " + str(jdata['total']) + " scan engines have detected this URL as malicious.\n")
                    print("Anti-Virus findings listed below: \n")
                    
                    #for loop that takes each value within the JSON scan dictionary and outputs the results as long as 'detected' is equal to true
                    for value in jdata['scans']:
                        
                        if jdata['scans'][value]['detected'] == True:
                            pprint(jdata['scans'][value]['result'])
        
                #If positives == 0, then VT will think that its safe
                else:
                    print(Fore.GREEN + "\nVirus Total does not think the link is malicious - further testing advised.")
            
            #catches any keyerrors
            except KeyError as e:
                print(Fore.MAGENTA + f"\nKey Error - retry running URL.\nReason for Error: {e}")
            #catches any errors occured by VT
            except VirustotalError as err:
                print(Fore.MAGENTA + f"\nAn error occured: {err} \nCatching and continuing with program.")

            print(Fore.CYAN + "\nHere's the depacified link (be careful!):\n" + output + "\n") #returns refanged url for further testing
            user_choice()

        else:
            print("Please input a valid option!\n")
            defang_func()

#Allows user to decide to loop again, or close the program
def user_choice():
    close = input("Would you like to handle another URL (Y/N)? ")
    if close == "Y" or close == "y":
        print("\n")
        defang_func()
    else:
        exit()


#Defines Parser
parser = argparse.ArgumentParser(description= 'Command Line Defanger')
#Adds argument for URL
parser.add_argument("-u", type=str, help="accepts url and defangs it", nargs='?', action="store", dest="url" , default=None, const=None)
#Passes the -d flag for depacifying the url
parser.add_argument("-d", help="allows the url to be refanged" , action="store_true", dest="depacify")
#Passes the -vt flag for sending to Virus Total's DB
parser.add_argument("-vt", help="runs a Virus Total Scan" , action="store_true", dest="vt")
#Store values in args table
args = parser.parse_args()

#if/else statement to traffic whether or not the program will open or execute from the command line
#Handles if -d and -vt are not in use
if args.url != None and args.depacify == False and args.vt == False:
    badURL = args.url
    output = defang(badURL, all_dots=True, colon=True)

    print("Here's the safe link:\n" + output)
    exit()

#Allows -d flag to be in use and "depacifies" the URL
elif args.depacify == True:
    badURL = args.url
    output = refang(badURL)

    print("Here's the depacified link (be careful!):\n" + output)
    exit()

#Runs a scan of VT DB and refangs the URL
elif args.vt == True:
    badURL = args.url

    output = refang(badURL)

    try:
        resp = vtotal.request("url/scan", params={"url": output}, method="POST")
        url_resp = resp.json()
        scan_id = url_resp["scan_id"]
        analysis_resp = vtotal.request("url/report", params={"resource": scan_id})
        jdata = analysis_resp.json()

            #Next, we need to filter the information so that way we know whether or not a URL us malicious
            #If positives are more than 0, then it outputs the reason for it being malicious
        if jdata['positives'] > 0:
                    
            #Outputs how many positives are found out of the total scans
            print(Fore.RED + "\nVirus Total has detected that " + str(jdata['positives']) + " out of " + str(jdata['total']) + " scan engines have detected this URL as malicious. \n")
            print("AntiVirus findings listed below: \n")
                    
            #for loop that takes each value within the JSON scan dictionary and outputs the results as long as 'detected' is equal to true
            for value in jdata['scans']:
                        
                if jdata['scans'][value]['detected'] == True:
                    pprint(jdata['scans'][value]["result"])

        #If positives == 0, then VT will think that its safe
        else:
            print(Fore.GREEN + "\nVirus Total does not think the link is malicious - further testing advised.")

    except VirustotalError as err:
        print(f"An error occured: {err} \nCatching and continuing with program.")

    print(Fore.CYAN + "\nHere's the depacified link (be careful!):\n" + output + "\n") #returns refanged url for further testing
    exit()

#Runs the main prgrm
else:
    defang_func()
