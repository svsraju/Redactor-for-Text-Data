import sys

import project1


def main(url):
    # Download data
    a = project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents(a)
	
    # Create Dataase
    db =  project0.createdb()
	
    # Insert Data
    project0.populatedb(db,incidents)
	
    # Print Status
    project0.status(db)


if __name__ == '__redactor__':

    argument_list=[]
    argument_list = sys.argv
    input_flag='--input'
    flags=["--names","--genders","--dates","--addresses","--phones"]
    concept_flag='--concept'
    output_flag='--output'
    stats_flag = '--stats'
    not_concept=["--input","--names","--dates","--places","--phones","--genders",
            "--addresses","--output","--stats"]
    
    count=0
    input_commands=[]
    flags_commands=[]
    concepts_commands=[]
    output_commands=''
    stats_commands=[]
    for i in a_list:
        if i == input_flag:
            input_commands.append(argument_list[count+1])
        elif i in flags:
            f=str(argument_list[count])[2:]
            flags_commands.append(f)
        elif i == concept_flag:
            for k in range(count,len(argument_list)):
                if argument_list[k] in not_concept:
                    break
                else:
                    concepts_commands.append(argument_list[k])
        elif i==output_flag:
            output_commands=argument_list[count+1][:-1]
        elif i == "stats_flag":
            for k in range(argument_list.index(i),len(argument_list)):
                stats_commands.append(argument_list[k])
        count+=1




