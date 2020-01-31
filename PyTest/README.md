
### UnitTest Limitations:

+ Test cases will execute in alphabetical order, It's not possible to customize execution order

    - Example:

            import unittest
            
            class TestOrder(unittest.TestCase):
        
                def test_B(self):
                    print('Test B')
            
                def test_C(self):
                    print('Test C')
            
                def test_A(self):
                    print('Test A')
                    
                unittest.main()
       
    - Execution Result:

            /usr/bin/python3 /Users/garepall/Desktop/selenium-tutorial/Unittest/002_test_fb_login.py
            ...
            ----------------------------------------------------------------------
            Ran 3 tests in 0.000s
            
            OK
            Test A
            Test B
            Test C
            
            Process finished with exit code 0
+ Test results will be displayed to console only and it is not possible to generate reports

+ It is not possible to execute selected test cases

+ Only limited setup and teardown methods available, Unittest has only class level methods ```setUpClass()``` and ```tearDownClass()``` and test case level methods ```setUp()``` and ```tearDown()```. It doesn't have test suite level methods.


* In Order to overcome above limitations of unittest we use PyTest framework


### PyTest:

+ PyTest is the improved and advanced version of unittest
+ PyTest doesn't have setUp and tearDown methods and classes, but we can implement setup and teardown using fixtures
+ PyTest executes the test cases from top to bottom and it allows customization to change the execution order
+ Using pytest-ordering we can change the test cases execution order ```@pytest.mark.run(order=n)```
+ In PyTest we can generate test results in HTML format using following commandline parameter
        
        pytest test_suite.py -vss --html=report.html    

### PyTest Naming Conventions:

+ File name eaither should start or end with test Ex: test_file.py
+ Class name should start with Test Ex: TestClass
+ Test method name should start with test_ Ex: test_one
