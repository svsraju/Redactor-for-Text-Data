
import sys 

import project1
# command line arguments are stored in the form 
# of list in sys.argv 

argumentList = sys.argv
print(argumentList)


labels = ["--input","--concept","--output","--stats"]
redact = ["--names","--dates","--phones","--genders","--addresses"]

count = 0

execute = []
redaction_order = []

for i in range(len(argumentList)):
    if argumentList[i] == "--input":
        file_red =  project1.readdata(argumentList[i+1])

#print(len(file_red))

a = file_red

#print(len(file_red))

for i in range(len(argumentList)):
    if argumentList[i] in redact:
        redaction_order.append(argumentList[i])
    
for item  in redaction_order:
    if item == "--names":
        file_red = project1.red_names(file_red)
       # print(file_red)
    if item == "--dates":
        file_red = project1.remove_dates(file_red)
    if item == "--genders":
        file_red= project1.rem_genders(file_red)
    if item == "--addresses":
        file_red = project1.remove_address(file_red)
    if item == "--phones":
        file_red = project1.remove_phones(file_red)

#print(len(file_red))

for i in range(len(argumentList)):
    if argumentList[i] == '--concept':
        concept = project1.concept(argumentList[i+1],file_red)

#print(len(concept))


for i in range(len(argumentList)):
    if argumentList[i] == '--stats':
        final_stats = project1.stats(a,redaction_order)
        complete_stats = project1.finalstats(final_stats,redaction_order)
   
project1.extractstatoutput(complete_stats)

for i in range(len(argumentList)):
    if argumentList[i] == '--output':
        final_output = project1.output(concept)





