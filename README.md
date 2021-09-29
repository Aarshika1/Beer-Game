# Sprint 4 Team 19
Aarshika Singh, Alba Lokaj

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


## Improvements made in Sprint 4:

## Frontend:

1. Linked Instructor authentication to backend. When an instructor logins then the instructor page is diplayed. The instructor page has the option to go to Create Game page or Instructor dashboard.
2. Create Game is linked to the backend. The instructor can enter the credentials and number of games. If the crdentials entered are complete and correct, then the instructor redirected to Instructor dashboard.
3. Instructor dashboard is partially connected to backend. The delete and reset all games are functional.
4. Player authentication has been created. When players login through the main page, then they are redirected student dashboard, where they can select a game through the link. The dashboard shows the name and email of the instructor of the game.
5. The players can use the filter on the student dashboard to filter the game according to the instructor email and name.
6. Once the player chooses a game usign the link, they are redirected to the chosen_role page: (It allows user to chose either factory, distibutor, wholesaler, retailer)
7. After chosing the role, players are directed to the Player Screen according to the chosen role.

## Backend:

1. The authentication was created (for instructor, player and game creation) with inclusion of error handling and redirecting to a specific page if the entered credentials are missing or wrong.
3. Delete game and reset all games were added to the instructor dashbaord.
4. A player an only choose roles and go to game screen, if authenticated.

## Tests

1. Authentication was tested using Mock pytest
2. Page loading and redirections were tested using pytest and their respective status code.

## Documentation

1. The documentation has been re-created using Sphinx and the steps included at the top.

## How do I work on front-end?

The frontend templates is contained in the folder templates

## How to work on back-end?

All the views are present in main.py and all the models are on the file models.py