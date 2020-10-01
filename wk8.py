#Name - Supriya 9/30/2020
import os
#Getting user input
path=input("Enter your directory: ")
check_path=os.path.exists(path)
if (check_path==True):
    file_name=input("Enter the file name:")
    wt=open(path+"\\"+file_name+".txt","w")
    Name=input("Enter your name:")
    Address=input("Enter your address:")
    Phone=input("Enter your phone:")
    wt.write(Name+","+Address+","+Phone)
    wt.close()
    rd=open(path+"\\"+file_name+".txt","r")
    cont=rd.read()
    print("******File Output****")
    print(cont) 
else:
    print("please enter the valid path")
    