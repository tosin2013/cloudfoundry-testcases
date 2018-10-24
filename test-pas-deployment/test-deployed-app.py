import csv
import datetime
import requests
import time
import argparse
import sys
requests.packages.urllib3.disable_warnings()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def  writetoCSV(fileName, timestamp, responsecode, requesttime):
    newvalues = [timestamp, responsecode, requesttime]
    if responsecode == "":
        print  bcolors.FAIL + "Time: "+str(timestamp)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
        print bcolors.FAIL + "ERROR: Failed to connect to endpoint." + bcolors.ENDC
    elif responsecode != 200:
        print  bcolors.WARNING + "Time: "+str(timestamp)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
        print bcolors.WARNING + "Warning response code is "+str(responsecode)+"." + bcolors.ENDC
    else:
        print bcolors.OKGREEN + "Time: "+str(timestamp)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
    with open(r''+fileName+'', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newvalues)


def csvheader(fileName):
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Timestamp', 'ResponseCode', "ResponseTime"])

def checkappstatus(url, fileName):
    try:
        headers = {
            'cache-control': "no-cache",
            }

        response = requests.request("GET", url, headers=headers, verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), response.status_code, response.elapsed.total_seconds())
    except Exception as e:
        print bcolors.FAIL + "FAILED TO CONNECT TO ENDPOINT "+str(url)+"." + bcolors.ENDC
        print bcolors.FAIL + str(e) + bcolors.ENDC
        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "", "-1")
        pass



#main
parser = argparse.ArgumentParser(description='Test PCF Application.')
parser.add_argument('--filename', help='Provide filename for csv')
parser.add_argument('--url', help='Provide url point to be used.')

args = parser.parse_args()
if args.filename != None:
    csvheader(args.filename)
    yesChoice = ['yes', 'y']

    try:
        while True:
            checkappstatus(args.url,args.filename)
            print bcolors.BOLD + "Press Ctrl-C to exit " + bcolors.ENDC
            time.sleep(5)
    except KeyboardInterrupt:
        pass
else:
    print "Please use the following command to run script."
    print "python test-deployed-app.py  --filename output.csv --url https://api.sys.yourendpoint.com"
    sys.exit()
