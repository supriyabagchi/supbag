import requests
def getContent(url):
    count = 1
    while True:
        try:
            reqObj = requests.get(url)
            print('Code :: ' + str(reqObj.status_code))
            if(reqObj.status_code ==200):
                return reqObj.json()
            else:
                return "Failed to get the Response"
        except Exception as exp:
            if count <= 5:
                count += 1
            else:
                restart=input("Would you like to restart")
                if(restart=="Yes"):
                    break
if __name__=="__main__":
    print("welcome")
    Check="YES"
    while (Check == 'yes' or Check == 'y' or Check == "YES"):
        try:
            zipcode=input("Enter The Zip Code:")
            if (zipcode.isnumeric() == True and len(zipcode)==5):
                url="https://openweathermap.org/data/2.5/find?q="+str(zipcode)+"&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric"
                jsonData=getContent(url)
                count=jsonData["list"]
                if(len(count)>0):
                    for i in range(len(count)):
                        print("Id::",count[i]["id"])
                        print("Name::",count[i]["name"])
                        print("Temp::",count[i]["main"]["temp"])
                        print("Min Temp::",count[i]["main"]["temp_min"])
                        print("Max Temp::",count[i]["main"]["temp_max"])
                        print("Pressure::",count[i]["main"]["pressure"])
                        print("Humidity::",count[i]["main"]["humidity"])
                    Check=input("Do you want to continue - YES OR NO::")
                else:
                    print("No data available for zip::{}".format(zipcode))
            else:
                print("Please Valid Zip Code")
            
        except Exception as e:
            print("Please Valid Zip Code as numbers")
    print("Thank you")