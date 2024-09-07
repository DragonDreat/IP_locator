import urllib.request #This is used for requests
import json #This is used to decode JSON files
import socket #Imports socket

name = socket.gethostname() #Name of device
ip = socket.gethostbyname(name) #IP adress

while ip: #Just testing
 def locate(victim): #Function to locate a victim
    api = "http://ip-api.com/json/" #API of ip-api.com that can locate anyones IP address
    response = urllib.request.urlopen(api+victim) #Response variable that sends request to API and Requests victims Information
    data = json.loads(response.read()) #Data Variable that uses json import to decode response to readleable text
    if data["status"] == "fail": #sees if datas status failed (couldnt find it in database)
     return "Sorry, Your Ip address doesnt exist, or we have some problems!" #Returns answer
    return "Status: " + data["status"] + ", IP address: " + data["query"] + ", Country: " + data["country"] + ", Region: " + data["regionName"] + ", City: " + data["city"] + ", Timezone: " + data["timezone"] #Returns data but modified
 while True:
  print("Welcome to lookup locator!") #Prints welcome message
  victim = input("Enter yours victim ip....  ") #gives you to input victims IP Address
  print(locate(victim)) #Prints and calls locate function
 
#There was problem about this command up I writed print on return, and it returned on print so it writed me Result and then None, because there was 2 prints, and I just deleted 1 print 


    ##DragonDreat - Creator
