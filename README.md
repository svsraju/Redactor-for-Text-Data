The Redactor
===
Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.

In this project you will see me using the knowledge of Python and the Linux command line tools to wrangle through all the files which we are interested in.So we use different nltk inbuilt libraries and make sure our desired output file is redacted.

----
Project Source can viewed from  https://oudalab.github.io/textanalytics/projects/project1

-------------
Author 
---
**Venkata Subbaraju Sagi**
All known Bugs and fixes can be sent to subbaraju.v@ou.edu
Packages required for the project : glob,nltk,
imports required from nltk: wordnet,MosesTokenizer,TreebankWordDetokenizer

------
File List
----
```

```
-------
Platform used
---
I used Google cloud platform to run the file. I have created an instance in google cloud, which I used for cloning 
the git repository, then for running the file
Your code should take a url from the command line and perform each operation.

---
Once you have cloned the directory, follow these instructions
----------------
**The Pipfile and Pipfile.lock**
Create the Pipfile using the command `pipenv install --python 3.7`. Note for this project we will use Python 3.7 so
 be sure to install it using pyenv.
If you do not have python 3.7 on your system, revisit the start up script given in the document config file:
https://oudalab.github.io/textanalytics/instance/startup.sh
You can create each initial file and folder using the touch and mkdir commands. The Python packaging how to page ha
s more example of proper python packages https://python-packaging.readthedocs.io/en/latest/minimal.html
you will get more insights of running your project0.py file, but to make it clear
After the code is installed, you should be able to run the code using the command below.
**pipenv run python redactor.py --input '*.txt' \
                    --input 'otherfiles/*.txt' \
                    --names --dates --addresses --phones \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr **

Running the program with this command line argument should read all files ending with .txt in in the current folder and also all files ending in .txt from the folder called otherfiles/. All these files will be redacted by the program. The program will look to redact all names, dates, addresses and phone numbers. Notice the flag --concept, this flag asks the system to redact all portions of text that have anything to do with a particular concept. In this case, all paragraphs or sentences that contain information about “kids” should be redacted. It is up you to determine what represents a concept. All the redacted files should be transformed to new .txt files and written to the location described by --output flag. The final parameter, --stats, describes the file or location to write the statistics of the redacted files. Below we discuss each of the parameter in additional detail.

Description of Functions Used
---
I have two files to run the program, in `project1/project1.py'` I have written all function definitions and in `project1/redactor.py`, I have called these functions.

Parameters
**–input**
This parameter takes a glob that represents the files that can be accepted. More than one input flag may be used to specify groups of files. If a file cannot be read or redacted an appropriate error message should be displayed to the user.

**–output**
This flag should specify a directory to store all the redacted files. The redacted files, regardless of their input type should be written to txt files. Each file should have the same name as the original file with the extension .redacted appended to the file name.

**Redaction flags**
The redaction flags list the entity types that should be extracted from all the input documents. The list of flags you are required to implements are:

--names
--genders
--dates
--addresses
--phones
You are free to add you own! Note: gender should be any term that reveals the gender of a person (e.g. him, her, etc.). The other definitions of the rest of the terms should be straight forward. In your README.md discussion file clearly give the parameters you apply to each of the flags — be clear what constitutes a an address and phone number. The redacted characters in the document should be replaced upon with a character of your choice. Some popular characters include the unicode full block character █ (U+2588). You should redact only the words, not the whitespaces. If you believe that one should also redact whitespaces between words (e.g. in a first and last name) please discuss why in your README.md.

**–concept**
This flag, which can be repeated one or more times, takes one word or phrase that represents a concept. A concept is either an idea or theme. Any section of the input files that refer to this concept should be redacted. For example, if the given concept word is prison, a sentence (or paragraph) either containing the word or similar concepts, such as jail or incarcerated, that whole sentence should be redacted. In your README.md file, make your definition of a concept clear. Also, clearly state how you create the context of a concept and justify your method. You may be creative here!

**—stats**
Stats takes either the name of a file, or special files (stderr, stdout), and writes a summary of the redaction process. Some statistics to include are the types and counts of redacted terms and the statistics of each redacted file. Be sure to describe the format of your outfile to in your README file. Stats should help you while developing your code.

---
List of external links that I used for help
--

----------------------------


------
**Assumptions/Bugs**
--
```

```
------
