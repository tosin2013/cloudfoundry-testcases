import csv
import datetime
import requests
import time
import argparse
import sys
import string
import random

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

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def  writetoCSV(fileName, timestamp,  action,responsecode, requesttime):
    newvalues = [timestamp, action,responsecode, requesttime]
    if responsecode == "":
        print  bcolors.FAIL + "Time: "+str(timestamp)+" Action: "+str(action)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
        print bcolors.FAIL + "ERROR: Failed to connect to endpoint." + bcolors.ENDC
    elif responsecode != 200 or responsecode != 201:
        print  bcolors.WARNING + "Time: "+str(timestamp)+" Action: "+str(action)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
        print bcolors.WARNING + "Warning response code is "+str(responsecode)+"." + bcolors.ENDC
    else:
        print bcolors.OKGREEN + "Time: "+str(timestamp)+" Action: "+str(action)+" Response Code: "+str(responsecode)+" Request Time: "+str(requesttime)+"." + bcolors.ENDC
    with open(r''+fileName+'', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newvalues)


def csvheader(fileName):
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Timestamp', 'Action', 'ResponseCode', "ResponseTime"])

def checkappping(url, fileName):
    try:
        print  bcolors.BOLD + "Verifing that the application is up and responding, and can connect to the RabbitMQ backend service" + bcolors.ENDC
        headers = {
            'cache-control': "no-cache",
            }

        response = requests.request("GET", url+"/ping", headers=headers, verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "ping_queue",response.status_code, response.elapsed.total_seconds())
    except Exception as e:
        print bcolors.FAIL + "FAILED TO CONNECT TO ENDPOINT "+str(url)+"." + bcolors.ENDC
        print bcolors.FAIL + str(e) + bcolors.ENDC
        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "", "-1")
        pass


def checkappqueues(url, fileName):
    try:
        print  bcolors.BOLD + "Prints the queues that have been defined so far. " + bcolors.ENDC
        headers = {
            'cache-control': "no-cache",
            }

        response = requests.request("GET", url+"/queues", headers=headers, verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "print_queue",response.status_code, response.elapsed.total_seconds())
        print response.text
    except Exception as e:
        print bcolors.FAIL + "FAILED TO CONNECT TO ENDPOINT "+str(url)+"." + bcolors.ENDC
        print bcolors.FAIL + str(e) + bcolors.ENDC
        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "", "-1")
        pass

def posttoappqueues(url, fileName):
    try:
        headers = {
            'cache-control': "no-cache",
            }
        data= {
            'name': 'TestQueue',
        }
        response = requests.request("POST", url+"/queues", headers=headers, data=data,verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "post_new_queue",response.status_code, response.elapsed.total_seconds())
        print response.text
    except Exception as e:
        print bcolors.FAIL + "FAILED TO CONNECT TO ENDPOINT "+str(url)+"." + bcolors.ENDC
        print bcolors.FAIL + str(e) + bcolors.ENDC
        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "", "-1")
        pass

def puttoappqueuesname(url, fileName):
    try:
        print  bcolors.BOLD + "Pushes a message, passed in the 'data' field, into the named message queue." + bcolors.ENDC
        headers = {
            'cache-control': "no-cache",
            }

        data= {
            'data': randomword(10),
        }
        response = requests.request("PUT", url+"/queue/TestQueue", headers=headers, data=data,verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "random_item",response.status_code, response.elapsed.total_seconds())
        print response.text
    except Exception as e:
        print bcolors.FAIL + "FAILED TO CONNECT TO ENDPOINT "+str(url)+"." + bcolors.ENDC
        print bcolors.FAIL + str(e) + bcolors.ENDC
        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "", "-1")
        pass

def checkappqueuesitem(url, fileName):
    try:
        print  bcolors.BOLD + "Pulls a single message from the named message queue. " + bcolors.ENDC
        headers = {
            'cache-control': "no-cache",
            }

        response = requests.request("GET", url+"/queue/TestQueue", headers=headers, verify=False)

        writetoCSV(fileName, datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), "print_queue_item",response.status_code, response.elapsed.total_seconds())
        print response.text
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
    my_functions = [checkappqueues, puttoappqueuesname, checkappqueuesitem,checkappping]
    try:
        checkappping(args.url,args.filename)
        print  bcolors.BOLD + "Define a queue, passed in the 'name' field." + bcolors.ENDC
        posttoappqueues(args.url,args.filename)
        while True:
            random.choice(my_functions)(args.url,args.filename)
            print bcolors.BOLD + "Press Ctrl-C to exit " + bcolors.ENDC
            time.sleep(5)
    except KeyboardInterrupt:
        pass
else:
    print "Please use the following command to run script."
    print "python test-rabbitmq-app.py  --filename output.csv --url https://api.sys.yourendpoint.com"
    sys.exit()
