# UNITTEST

## How to perform unittesting in python

- module name: unittest (predefine in python)
- class name: TestCase
- instance methods: contains 3 instance method

1. setUp() -->open browser , database connectivity
2. test()
3. tearDown() --> close connection,close browser

4. ### setUpClass(cls)

   - for all test method setUPClass will execute only one

5. ### tearDownClass(cls)

    - tearDownClass(cls) will execute only once
    - these two method are class level methods

### manual testing ---

    - google search functionality (manually use application and after that use Excel shell )
    - test no , testing steps, expected Result, original result, status

### Automation Testing ---

    - Selenium(automation), QTP(these day gone ), Load Runner( performance automation),epl,self
    - python/java/ruby script program to perform these activities automatically

## Unit testing api

module: unittesting
class: TestCase

instance methods:
   setUp() --> Before every test method
   test_method()
   tearDown() --> After every test method

class methods:

   setUpClass() --> before executing all test method of a TestCase Class
   tearDownClass() --> after executing all test method of a TestCase class

- TestSuite --> Collection of testcases
  - By using unittest framework we can execute a group of test cases which nothing test suite.

- compulsory all test class method will execute in alphabetical order
- it the biggest limitation is that it is not follow top to bottom approach

## Limitation Of unittesting

1. Test result will be display to console only and it is not possible to generate reports
2. unittest framework always execute test methods in alphabetical order only, and it is not possible to customize execution order
3. As the part of batch execution(TestSuite), all test methods from the specified TestCase classes will be executed, and it is not possible to specify particular methods.
4. In unittesting only limited setUp and tearDown methods are available.
5. If we want to perform any activity before executing testsuite and after executing testsuite, unittest framework does not define any methods.

> To overcome more advance framework which is pytest
