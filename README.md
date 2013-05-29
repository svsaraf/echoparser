This is a python parser for echocardiographic data from NMFF / NMH.
===================================================================

*ACTUAL DATA IS NOT VERSION CONTROLLED*

Right now, it opens a file or folder in python, reads it, tokenizes the data it can understand, and outputs an excel file with the results. 

Installation instructions:
--------------------------

First you need to have access to the terminal, so you need either Mac / Linux. You also need python and the github terminal client installed. In the terminal:

    easy_install pip
    git clone git://github.com/svsaraf/echoparser.git
    cd echoparser
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    open .

Now just drop in a folder or file of echocardiographic text files. In the terminal again, run:

    python parser.py sample.txt

Where sample.txt is any text file or folder of files. For a folder, you have to append the flag 'folder' to the request.

    python parser.py sampledata folder
    
Output will be written to an excel file. 

Contact svsaraf90@gmail.com for questions.
