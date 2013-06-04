This is a python parser for echocardiographic data from NMFF / NMH.
===================================================================

*ACTUAL DATA IS NOT VERSION CONTROLLED*

Right now, it opens a file or folder in python, reads it, tokenizes the data it can understand, and outputs an excel file with the results. 

Installation instructions:
--------------------------

First you need to have access to the terminal, so you need either Mac / Linux. You also need python. Look here:

http://www.python.org/getit/mac/

In the terminal:

    easy_install pip
    sudo easy_install virtualenv
    git clone git://github.com/svsaraf/echoparser.git

If you don't have github, you can always just copy the folder with the code in it from github manually.

    cd echoparser
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    open .

Now just drop in a folder of echocardiographic text files. In the terminal again, run:

    python parser.py sampledata folder

Where sampledata is any folder of files of text files. 
    
Output will be written to an excel file that has the name output_ + whatever the name of your data folder is. In the example, the output will be output_sampledata.xls.

Adding variables to grab is as easy as adding lines to inputparameters.xls file and bolding it. Your variables have to be 'n' 'st' or 'ss' otherwise the program will break.  

Contact svsaraf90@gmail.com for questions.
