
import sys 

import project1
# command line arguments are stored in the form 
# of list in sys.argv 

argumentList = sys.argv

print(argumentList)


labels = ["--input","--concept","--output","--stats"]
redact = ["--names","--dates","--places","--phones","--genders","--addresses"]

count = 0

execute = []

for i in range(len(argumentList)):
    if argumentList[i] == "--input":
       a =  project1.readdata(argumentList[i+1])
       print(a)









