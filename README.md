### Study Notes
[OO Python](https://github.com/getfutureproof/fp_guides_wiki/wiki/OO-Python)

# Exercises
- Create a CLI with an Object Oriented design
  - On starting the app, User is asked for their GitHub username
  - A request is made to `https://api.github.com/users/<username>/repos`
  - API data is turned into instances of Repository class
  - User is shown a numbered list their repos by name
  - User can input a number to see more details on the corresponding repository

# Running Demo

_Note: make sure you have [pipenv installed](https://github.com/getfutureproof/fp_guides_wiki/wiki/Virtual-Environment) before continuing._

- `cd` into my_demo
- `pipenv shell` to activate your virtual environment for the project
- `pipenv install` to install dependencies
- `pipenv run start` or `python main.py` to run program
- currently no error handling for incorrectly entered github username!