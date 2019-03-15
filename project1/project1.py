import glob 
import nltk 
import re
import nltk 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('wordnet')

from nltk.corpus import wordnet 
from mosestokenizer import MosesTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import project1
import os.path
import os
import pickle
import ntpath


total_data = []
all_files = []


def readdata(files):
    
    # for checking all text files together
    #checking all the .txt files present in the directory
    
    all_text_files = glob.glob(files)
    #print(len(all_text_files))
    all_files.append(all_text_files)
    #print(len(all_text_files))

    for i in range(len(all_text_files)):
        #my_file = open(all_text_files[i],'r')
        data = open(all_text_files[i]).read()
        #print(data)
        #lines = data.readlines()
        total_data.append(data)
    
   #print(len(total_data))
    return total_data



#############################################################3

#extracting names

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        #print(t.label)
        if t.label() == 'PERSON':
            entity_names.append(' '.join([child[0] for child in t.leaves()]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

def red_names(a):
    entity_names = []
    final_file = []
    total_data = a
    for i in range(len(total_data)):
        redaction_file = total_data[i]
        sentences = nltk.sent_tokenize(redaction_file)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary = False)
        for tree in chunked_sentences:
            entity_names.extend(extract_entity_names(tree))
        for e in entity_names:
            redaction_file = redaction_file.replace(e,'██')
        final_file.append(redaction_file)
    return final_file



###########################




# removing dates
def remove_dates(file):    
    date_file = []
    all_dates = []
    final_file = file
    for i in range(len(final_file)):
        redaction_file = final_file[i]
       
        final_dates1 = re.findall(r"([A-Z]\w\w\w+\s\d+,\s\d\d\d\d)", redaction_file)
        all_dates.append(final_dates1)
        
        final_dates2 = re.findall(r"([A-Z]\w\w\w+\s\d\d\d\d)", redaction_file)
        all_dates.append(final_dates2)
        
        
        final_dates3 = re.findall(r"([A-Z]\w\w\w+,\s\d\d\d\d)", redaction_file)
        all_dates.append(final_dates3)
        
        for d in range(len(all_dates)) :
            for j in all_dates[d]:
                redaction_file = redaction_file.replace(j,'██')
        date_file.append(redaction_file)
    
    return date_file
#######################################################################################
                         
#removing genders
def rem_genders(file):
    genders=['him','her','hers','male',
              'man','woman','women','men','she','he','his',
              'female', 'himself', 'herself','wife','husband']
    genders_file = []
    concept_file = file
    for d in range(len(concept_file)):
            red_gen = concept_file[d]
            #gen_sen = nltk.sent_tokenize(red_gen)
            #gen_tok = [nltk.word_tokenize(sentence) for sentence in gen_sen]
            gen_tok = nltk.word_tokenize(red_gen)
            #print(gen_tok)
        
            
            for n, i in enumerate(gen_tok):
                 for g in range(len(genders)):
                     if i.lower() == genders[g]:
                         gen_tok[n] = '██'
            gen_tok = TreebankWordDetokenizer().detokenize(gen_tok)
            genders_file.append(gen_tok)
    return genders_file       
########################################################################

#removing phone numbers
def remove_phones(file):
    phones_file = []
    genders_file = file
    for i in range(len(genders_file)):
        red_phone = genders_file[i]
        find_numbers = re.findall(r"(\+\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}|\d{2}[-\.\s]??\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4})",red_phone)
        for j in range(len(find_numbers)):
            red_phone = red_phone.replace(find_numbers[j],'██')
        phones_file.append(red_phone)
    return phones_file  


#######################################################################            
            
    
#removing addresses

def remove_address(file):
    address_file = []
    phones_file = file
    for i in range(len(phones_file)):        
        red_address = phones_file[i]   
        #find_address = re.findall(r"[0-9].+[0-9]{5}", red_address) 
        find_address= re.findall(r"[0-9]{1,4}.{1,40}[0-9]{5}",red_address)
        for j in range(len(find_address)):
            #print(find_address[j])
            red_address = red_address.replace(find_address[j],'██')
        address_file.append(red_address)
    return address_file





###################################################################3

def removeDuplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList  


def concept(word,file1):
    
    final_sentences =[]
    concept_file = []
    
    synonyms = [] 
      
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            
    synonyms = project1.removeDuplicates(synonyms)      
        
    date_file = file1        
    for i in range(len(date_file)):
        red_syn = date_file[i]
        sentences = nltk.sent_tokenize(red_syn)
        for s in range(len(sentences)):
            for j in range(len(synonyms)):
                if synonyms[j] in sentences[s].lower():
                   final_sentences.append(sentences[s])
                   
    for i in range(len(date_file)):
        red_syn = date_file[i]               
        for d in range(len(final_sentences)):
                if final_sentences[d] in red_syn:
                    red_syn = red_syn.replace(final_sentences[d],'██')
        concept_file.append(red_syn)
    return concept_file                 


def stats(a,order):

    final_data = a
    stats = {}
    redaction_order = order
    for item in redaction_order:
        if item == "--names":
            final_data=red_names(final_data)
            name_count={}
            for i in range(len(final_data)):
                count=len(re.findall('██',final_data[i]))
                name_count[i]=count
            #print(name_count)
            stats[item] = name_count


        if item == "--dates":
            final_data = remove_dates(final_data)
            dates_count = {}
            for i in range(len(final_data)):
                count=len(re.findall('██',final_data[i]))
                dates_count[i]=count
            #print(dates_count)
            stats[item] = dates_count


        if item == "--phones":
            final_data = remove_phones(final_data)
            phones_count = {}
            for i in range(len(final_data)):
                count=len(re.findall('██',final_data[i]))
                phones_count[i]=count
            #print(phones_count)
            stats[item] = phones_count

        if item == "--genders":
            final_data = rem_genders(final_data)
            gender_count = {}
            for i in range(len(final_data)):
                count=len(re.findall('██',final_data[i]))
                gender_count[i]=count
            #print(gender_count)
            stats[item] = gender_count


        if item == "--addresses":
            final_data = remove_address(final_data)
            address_count = {}
            for i in range(len(final_data)):
                count=len(re.findall('██',final_data[i]))
                address_count[i]=count
            #print(address_count)
            stats[item] = address_count

    return stats



def finalstats(stats,order):

    redaction_order = order
    c=0
    finalstats={}
    for it in redaction_order:
       # print(c)
        x={}
        d1=0
        if c==0:
            temp1dict=stats[it]
            finalstats[it]=temp1dict
        if c==1:
            temp2dict=stats[it]
            for key,value in temp2dict.items():
                d1=temp2dict[key]-temp1dict[key]
                x[key]=d1
            finalstats[it]=x
        if c==2:
            temp3dict=stats[it]
            for key,value in temp3dict.items():
                d1=temp3dict[key]-temp2dict[key]
                x[key]=d1
            finalstats[it]=x
        if c==3:
            temp4dict=stats[it]
            for key,value in temp4dict.items():
                d1=temp4dict[key]-temp3dict[key]
                x[key]=d1
            finalstats[it]=x
        if c==4:
            temp5dict=stats[it]
            for key,value in temp5dict.items():
                d1=temp5dict[key]-temp4dict[key]
                x[key]=d1
            finalstats[it]=x
            
        c+=1
        
    #print(finalstats)
    return finalstats


def output(complete_data):
        
    outputfiles = []

    import ntpath
    for i in range(len(all_files)):
        for j in range(len(all_files[i])):
            path=os.path.splitext(all_files[i][j])[0]
            path=ntpath.basename(path)+ '.redacted.txt'
            outputfiles.append(path)
           
    for i in range(len(outputfiles)):
        completeName = os.path.join('files/', outputfiles[i])
        with open(completeName, 'w', encoding = 'utf-8') as file1:
            file1.write(complete_data[i])
            file1.close()  


def extractstatoutput(statsdict):
    file1=open('stderr/stder.txt', 'w', encoding = 'utf-8')
    print(statsdict)
    for key,value in statsdict.items():
        list=[str(item) for item in value]
        string=' '.join(list)
        file1.write(str(key))
        file1.write(str(string))
    file1.close()
