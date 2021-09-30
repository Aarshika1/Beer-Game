Aarshika Singh

## Introduction

**Beer Game Project:** Software Engineering Project to create a supply chain game I,e, Beer Game. 

### The Beer Game Documentation

This project is built on Flask Python Framework and plain HTML/CSS (Changed from previous React JS for Frontend).


## Software Requirements
Python 3.8.5

## Setup and Deployment:

Download the folder to your respective device. 
### Install project dependencies

```
pip3 install -r requirements.txt
```

Then,

```
source venv/bin/activate
python3 main.py 
```
If needed, create a new venv using:-
```
virtualenv venv
```

Also, the credentials for the local MySQL installation must be set at the variable SQLALCHEMY_DATABASE_URI in the Config class in config.py and the database must already be created.

## For Tests:

1. To Run the tests, run
   ```
   pytest
   ```

## For Documentation:

1. To make the html documentation and then clean it:

```
cd docs
make html
make clean
```

2. The documentation will be then created under docs/\_build/html/index.html To recompile the Sphinx documentation:

```
cd docs
sphinx-apidoc --ext-autodoc -o . ..
```


Note that sphinx must be installed for this to work.


## How do I work on front-end?

The frontend templates is contained in the folder templates

## How to work on back-end?

All the views are present in main.py and all the models are on the file models.py
