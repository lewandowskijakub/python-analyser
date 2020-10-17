# python-analyzes
(fork this project to your github account, if you want imporve the tasks, the readme or add some unit test feel free to create pull request)

This project was created to present the difficulty of interpreting and analyzing
code performed by the interepretes. 

As a developer, your goal is to implement all the functions in python_analyser.py

For those that are interested in the origin of to_analysed.py file:

File "to_analysed.py" is a file that is used to
test implemented code - it is a simple program that perform some truth validation, to run it first run in console:

```
pip install requests
pip install build
pip install google-api-python-client
```

Then you can run it with: python to_analyse.py 
And give some statment that can be validated for example: Peter is good mentor
For the result you have to wait a bit but it should be something like this:

```
Report for statement: Peter is good mentor
------------------------------------------
The truth ratio for: Peter is good mentor is: 0.5
This means that this statement is: not false and not true, cannot say.

```


