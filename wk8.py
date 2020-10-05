#Name - Supriya 10/5/2020 attempt 2
import os
def createfile(filepath):
    file_name=input("Enter the file name:")
    wt=open(filepath+"\\"+file_name+".txt","w")
    Name=input("Enter your name:")
    Address=input("Enter your address:")
    Phone=input("Enter your phone:")
    wt.write(Name+","+Address+","+Phone)
    wt.close()
    rd=open(filepath+"\\"+file_name+".txt","r")
    cont=rd.read()
    print("******File Output****")
    print(cont)
if __name__=="__main__": 
    #Getting user input
    path=input("Enter your directory: ")
    check_path=os.path.exists(path)
    if (check_path==True):
        createfile(path) 
    else:
        print("Do you want to create new directory? Yes or No")
        new_dir=input("")
        if(new_dir =="Yes" or new_dir=="yes"):
            os.mkdir(path)
            createfile(path)
        else:
            exit()
    