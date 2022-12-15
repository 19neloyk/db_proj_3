## General Setup

To set up, first make sure you have `postgresql` installed. Make sure that your password for the master
user (the username of this user is literally postgres) is `password`

You must then run `pip install psycopg2` in this directory (we can ignore virtual environments for now).
If this doesn't work, check if you have Python3 installed, and do `pip3 install psycopg2` instead.


## Running our demo in main

In order to run our current main, you must enter the python shell. To do this, type either `python` or
`python3` in the terminal (as long as you are already in this directory).

Then, run `exec(open('db.py').read())` in the python shell. This will load the `db.py` file's functions.

After that, type `main()` in the shell. This will run the `main` function loaded from `db.py`, which basically
loads the initial values of our database and allows us to play around with real SQL queries in a shell we coded! For example, you can type `select firstname,lastname from student where major = 'Computer Science'` and see real results from the current state of the database.

## LEKSO! Look at the code

All the code you need to examine in order to write your own code is located in `db.py`. You can load your own functions and play around with them inside the python shell. Just remember to firstly activate the python shell once in this directory by running either `python` or `python3` and then loading them with `exec(open('your-file-name.py').read())`.
