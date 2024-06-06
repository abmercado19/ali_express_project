# ali_express_project

### Pre-requisites

- Install Git
- Install Python (Tested with Python 3.9)
- Install pipenv: https://pypi.org/project/pipenv
- Install allure
- Install the solution:
  - Open a command line in a folder where you want to store the testing solution and clone the ali_express_project solution

### Install testing solution dependencies
From root project folder execute the following command: ```pipenv install```

### To execute tests opening the browser:

- Execute the following command:

    ```behave -f allure_behave.formatter:AllureFormatter -o allure-results```

- Once the execution is finished, you can generate the allure report executing the following command:
    
    ```allure serve allure-results```

### To execute tests in headless mode:

- Execute the following command:

    ```behave -D headless=true -f allure_behave.formatter:AllureFormatter -o allure-results```

- Once the execution is finished, you can generate the allure report executing the following command:
    
    ```allure serve allure-results```