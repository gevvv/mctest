## Project Name: MC_test
installation: 
           1.clone repozitory 
           2. go to root directory in terminal 
           3. pip3 install -r requirments.txt
## RUN autotests whith HTML_REPORT : $ pytest --html=report.html Tests.py



RUN autotests whith allure report: GO TO allure_2_9_0/allure-2.9.0/bin
                                 $ RUN IN TERMINAL   $ ./allure generate directory-with-results/ -o directory-where-u-want-indexhtmlreport-
                                     -to-be-generated/
# How_to_run with ALLURE        : $ pytest /path_to_directory_to/Tests.py --alluredir=/path_to_directory_to/allure_data
# How to see allure report      : $ ./allure open 'path_to_directory_allure_reports/allure_reports/'
           
