# PyTest Framework

Advanced version of unittest framework
built on top of unittest framework

> pip install pytest

## Pytest Naming Rules

1. File Name should start or end with 'test'
   - test_google_search.py
   - google_search_test.py
2. Class Name should start with 'Test'
   - TestGoogleSearch.py
   - TestCaseDemo
3. test method name should start with 'test_'
   - test_method1()
   - test_method2()

Q. How to run test scripts
> py.test
> it execute all those scripts prest in the folder
> to run a particular test script py.test filename

By default, pytest won't test and won't display print statement on console
`-s` to display print statement in other languages like java `-v` used for verbose output
`py.test -s filename` -> pretreatment out we can see
`py.test -s -v filename` -> every detail will show

-s ==> meant for print statement output
-v ==> meant for verbose

pytest: there are no setUp(), tearDown(), setUpClass() and tearDownClass()

### Q How to implement setUp() method in pytest

By using some decorator

@pytest.fixture() -> to implement setup machina
we can implement setUp() by using `@pytest.fixture()`
decorator

### How to implement teatDown() machanism

@pytest.fixture() ==> meant for setUp mechanism
@pytest.yield_fixture() ==> meant for both setUp and tearDown
`

```py
@pytest.yield_fixture()
def ma():
   setUp activity
   yield
   tearDown activity`

@pytest.yield_fixture() is deprecated use @pytest.fixture() instead with yield
```

### How to implement setUpClass() and tearDownClass() in pytest

@pytest.yield_fixture(scope='module')

### How to implement setUp,tearDown and setUpClass,tearDownClass functionality simultaneously in pytest

>
>link

`conftest.py`

code re-usability
common setUp and tearDown activities, we have to define in this file
automatically available for all test scripts

Various possible ways to run pytest scripts

1. py.test -v -s
   - to run all methods present in all test scripts of current working directory
2. py.test -v -s test.py
   - to run all test methods of a particular test scripts
3. py.test -v -s test.py test1.py
   - to run multiple test scripts
4. py.test -v -s test.py test1.py::test_method
   - To run a particular test method

it will follow top to down approach

How to customize order of tests in pytest

we have to install module pytest-ordering

`@pytest.mark.run(order=n)`
in unittesting this type of facility not define
