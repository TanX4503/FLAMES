'''
RUN THIS PYTHON FILE IN ANY INTERPRETER TO USE THIS BOT
Enter 2 Names in the console as directed and get your FLAMES Result
'''

# Importing required libraries
import sys
import time

# Setting this file to only work on Windows, MacOS or Linux
assert('win32' or 'linux' or 'linux2' or 'darwin' in sys.platform), "Unfortunately, your device is not supported by this code, yet. Contact the creator of this programme for furthur help"

# List Intersection (Credits for this function: GeeksforGeeks)
def intersection(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3
  
# Splitting a String into a List
def split(name):
    name=name.lower()
    length=len(name)
    list=[]
    i=0
    for i in range(0,length):
        str = name[i]
        list.append(str)
        i+=1
    return list

try:
    # Taking 2 names as input from the user
    print()
    name1=str(input("Enter First Name:  "))
    name2=str(input("Enter Second Name:  "))

    # Splitting these names into 2 lists and intersecting them
    list1=split(name1)
    list2=split(name2)
    intlist=intersection(list1,list2)

    # Calculating a FLAMES Value
    p=int(len(list1))
    q=int(len(list2))
    r=int(len(intlist))
    flame=int((p+q-2*r)%6)

except ValueError:
    print("\n\nA ValueError was encountered. Kindly restart the file\n")
except NameError:
    print("\n\nA NameError was encountered. Kindly restart the file\n")
except:
    print("\n\nAn unidentified error was encountered. Kindly restart the file or debug\n")

# Getting the output as required
print()

print("The FLAMES result is...", end=" ", flush="True")
time.sleep(3)

if flame==0:
    print("Friendship")

elif flame==1:
    print("Love")

elif flame==2:
    print("Affection")

elif flame==3:
    print("Marriage")

elif flame==4:
    print("Enemy")

elif flame==5:
    print("Sibling")

else:
    print("\n\nAn unidentified error was encountered. Kindly restart the file or debug\n")

print()
time.sleep(2)

'''
Coded by
Yours Truly
TanX
'''
