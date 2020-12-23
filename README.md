## turn

### Prerequisites

1. [Python 3](https://www.python.org/downloads/)
- MacOS: `brew install python`
2. [Allure](https://docs.qameta.io/allure/#_installing_a_commandline)
- MacOS: `brew install allure`

### Install and create a virtual environment

Install virtualenv:

```sh
python -m pip install virtualenv
```

Create a virtual environment in the project's root folder:

```sh
virtualenv env
```

Activate the virtual environment:

```sh
. env/bin/activate
```

### Install the project dependencies:

After activating the virtual environment, run:

```sh
pip install -r requirements.txt
```

### Run the tests:

Run the tests:

```sh
pytest --alluredir=[report folder] [test folder]

E.g: pytest --alluredir=test_report tests
```

### Generate test report:

```sh
allure serve test_report
```

![result](https://i.ibb.co/3vSKs18/Allure-Report-2020-12-23-15-13-58.png)
