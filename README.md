# Frans' search machine

Frans' search machine (FSM) is a Python application that allows Frans to search
Google. Frans inputs keywords, the app searches Google an stores the results locally.

## Installation

### Set up Python, pip and virtualenv
Make sure to have python3 and install additional packages:
* pip (to manage packages)
* virtualenv

```
$ mkdir fsm
$ cd fsm
$ python3 -m venv env
```

### Start virtualenvironment
```
$ source env/bin/activate
```

### Install packages
```
$ pip3 install wheel
$ pip3 install --upgrade google-api-python-client
```

### Download source code
```
$ git clone https://github.com/LukV/fsm.git
```
