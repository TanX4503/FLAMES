'''
RUN THIS PYTHON FILE TO USE THIS PROGRAMME
Enter 2 Names in the console as directed and get your FLAMES Result
'''

# Functions that I can thank GeeksforGeeks for
# List intersection
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Functions that I made myself
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
    name1=str(input("Enter First Name:"))
    name2=str(input("Enter Second Name:"))

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

if flame==0:
    print("The FLAMES result is\nFriendship")

elif flame==1:
    print("The FLAMES result is\nLove")

elif flame==2:
    print("The FLAMES result is\nAffection")

elif flame==3:
    print("The FLAMES result is\nMarriage")

elif flame==4:
    print("The FLAMES result is\nEnemy")

elif flame==5:
    print("The FLAMES result is\nSibling")

else:
    print("\n\nAn unidentified error was encountered. Kindly restart the file or debug\n")

print()

'''
Coded by
Yours Truly
TanX
'''