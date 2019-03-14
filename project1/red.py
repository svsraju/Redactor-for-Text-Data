
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


'''
for count in range()
    if redaction_order[count] == "--names":
        file0 = project1.red_names(a)
    elif redaction_order[count] == "--dates":
        file0 = project1.remove_dates(a)
    elif redaction_order[count] == "--genders":
        file0 = project1.rem_genders(a)
    elif redaction_order[count] == "--addresses":
        file0 = project1.remove_address(a)
    elif redaction_order[count] == "--phones":
        file0 = project1.remove_phones(a)    
    
    print(file0)
    count+1

    if redaction_order[count] == "--names":
        file1 = project1.red_names(file0)
    elif redaction_order[count] == "--dates":
        file1 = project1.remove_dates(file0)
    elif redaction_order[count] == "--genders":
        file1 = project1.rem_genders(file0)
    elif redaction_order[count] == "--addresses":
        file1 = project1.remove_address(file0)
    elif redaction_order[count] == "--phones":
        file1 = project1.remove_phones(file0)   
    count+1


if len(redaction_order) <= count:
    
    if redaction_order[count] == "--names":
        file2 = project1.red_names(file1)
    elif redaction_order[count] == "--dates":
        file2 = project1.remove_dates(file1)
    elif redaction_order[count] == "--genders":
        file2 = project1.rem_genders(file1)
    elif redaction_order[count] == "--addresses":
        file2 = project1.remove_address(file1)
    elif redaction_order[count] == "--phones":
        file2 = project1.remove_phones(file1) 
    count+1


if len(redaction_order) <= count:

    if redaction_order[count] == "--names":
        file3 = project1.red_names(file2)
    elif redaction_order[count] == "--dates":
        file3 = project1.remove_dates(file2)
    elif redaction_order[count] == "--genders":
        file3 = project1.rem_genders(file2)
    elif redaction_order[count] == "--addresses":
        file3 = project1.remove_address(file2)
    elif redaction_order[count] == "--phones":
        file3 = project1.remove_phones(file2)     
    count+1


if len(redaction_order) <= count:

    if redaction_order[count] == "--names":
        file4 = project1.red_names(file3)
    elif redaction_order[count] == "--dates":
        file4 = project1.remove_dates(file3)
    elif redaction_order[count] == "--genders":
        file4 = project1.rem_genders(file3)
    elif redaction_order[count] == "--addresses":
        file4 = project1.remove_address(file3)
    elif redaction_order[count] == "--phones":
        file4 = project1.remove_phones(file3) 
    count+1
'''


for i in range(len(argumentList)):
    #if len(argumentList) == 5:
    if argumentList[i] == '--concept':
        concept = project1.concept(argumentList[i+1],file_red)

'''
    if len(argumentList) == 4:
        if argumentList[i] == '--concept':
            concept = project1.concept(argumentList[i+1],file3)

    if len(argumentList) == 3:
        if argumentList[i] == '--concept':
            concept = project1.concept(argumentList[i+1],file2)
     
    if len(argumentList) == 2:
        if argumentList[i] == '--concept':
            concept = project1.concept(argumentList[i+1],file1)
      
    if len(argumentList) == 1:
        if argumentList[i] == '--concept':
            concept = project1.concept(argumentList[i+1],file0)

'''
complete_stats = {}

for i in range(len(argumentList)):
    if argumentList[i] == "--input":
        a =  project1.readdata(argumentList[i+1])


for i in range(len(argumentList)):
    if argumentList[i] == '--stats':
        final_stats = project1.stats(a,redaction_order)
        print(final_stats)
        complete_stats = project1.finalstats(final_stats,redaction_order)



for i in range(len(argumentList)):
    if argumentList[i] == '--output':
        final_output = project1.output(argumentList[i+1],concept)

#print(file_red)


#for i in range(len(concept)):
#    print(concept[i])

#print(complete_stats)







