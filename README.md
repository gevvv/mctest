## Project Name: MC_test
Installation on MacOS 
Apple’s Mac OS comes with python 2.7 installed by default. You must use python 3.x.x on your machine and also use pip for package management with python 3.x.x. The easiest way to achieve this is by:

NOTE: This tutorial does not use Virtual Environments like virtualenv or pyenv to manage various python versions

1. Installing python3
   Follow this link https://www.python.org/downloads/ and download the latest python3 OS X package
   Run the package and follow the steps to install python3 on your computer.
   Once the installation is done, on your Terminal, run $ python3 --version


2.Installing PIP
   Follow this link https://pip.pypa.io/en/stable/installing/   and download the PIP
3.Clone repozitory 
4.Go to root directory in terminal and run pip3 install -r requirments.txt


## Running Autotests
You have two different ways to run autotest, with HTML REPORT or with ALLURE REPORT

   RUN autotests with HTML_REPORT : $ pytest --html=report.html Tests.py
  
   RUN autotests with allure report: 
   Take  step 1 and 2 only once.    
      1.GO TO allure_2_9_0/allure-2.9.0/bin
      2.RUN IN TERMINAL   $ ./allure generate directory-with-results/ -o directory-where-u-want-indexhtmlreport-
                                     -to-be-generated/                                
      3.Run with ALLURE               : $ pytest /path_to_directory_to/Tests.py --alluredir=/path_to_directory_to/allure_data
      4.How to see allure report      : $ ./allure open 'path_to_directory_allure_reports/allure_reports/
