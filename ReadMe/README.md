# boats_group_dt_22_feb_2020
Runnable on: Windows 10 Browser: Chrome Tools: Pycharm, Selenium Webdriver, Allure

=========================================================================================== 
If you will install allure(java should be here)-you would be able to see the visual report. 
See steps: $ pip install allure-behave 

$ pip install allure-pytest 
$ pip install pytest-allure-adaptor

to launch tests and generate reports folder: 
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/ 

to extract report into browser: 
$ allure serve test_results/
