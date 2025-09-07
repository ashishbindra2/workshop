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
