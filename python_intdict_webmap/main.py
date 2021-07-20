import json
import difflib
#from pr1 import *
from DB_connector import *

data=json.load(open("data.json"))
def finding(word,args):
    mylist=[]
    #print(len(args),len(word))
    for x in args:
        if len(word)<=len(x):
            ctr=0
            flag=1
            for g in word:
                if (g!='*' and g!=x[ctr]):
                    flag=0
                    break
                ctr+=1
            if flag==1:
                mylist.append(x)
    #print(len(mylist))
    if len(mylist)>0:
        for i in mylist:
            print("Does the word show resemblance to {0} ? yes/no".format(i))
            grv=input().lower()
            if grv=="yes":
                return data[i]

        return "cannot find any match! SORRY..."
def evaluate(w):
    if w in data:
        return data[w]
    elif len(difflib.get_close_matches(w, data.keys())) > 0:
        for i in difflib.get_close_matches(w, data.keys()):
            print("Did you mean {0} ? yes/no".format(i))
            x = input().lower()
            if x == "yes":
                return data[difflib.get_close_matches(w, data.keys())[0]]

        return "Your word was not found in the dictionary"
    else:
        s = difflib.get_close_matches(w, data.keys())
        return "Your word was not found in the dictionary"

#sequenceMatcher(string1,string 2) -->helps to check matching of two strings
#.ratio() -->used to give the % matching
def inp():
    print("Hii, welcome to your learning friend dictionary...")
    while 1:
        x=int(input("Have words?:1:yes,0:no "))
        if(x>0):
            f = input("Did you remember the word exactly as it is ? yes/no ").lower()
            if f == "no":
                print("OK , lets try finding the word first!")
                # wdl=input("Enter the length of the word")
                wd = input("enter the word,mark '*' at positions where you don't remember the character ").rstrip()
                gr=finding(wd, data.keys())
                print(gr)
            else:
                print(evaluate(input("ENTER WORD: ").lower()))
        else:
            print("Thanks for visiting!")
            break


if __name__ == '__main__':
    inp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
