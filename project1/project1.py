import glob 
import nltk 
import re
import nltk 
from nltk.corpus import wordnet 
from mosestokenizer import MosesTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

def readdata(files):
    
    # for checking all text files together
    #checking all the .txt files present in the directory
    
    all_text_files = glob.glob(files)
    #all_text_files = glob.glob("*.txt")
    
    #reading all these files
    total_data = []
    
    for i in range(len(all_text_files)):
        my_file = open(all_text_files[i],'r')
        data = my_file.read()
        #lines = data.readlines()
        total_data.append(data)

    return total_data


