In this tutorial, we will start with writing python code using the python interpretter.
Pre req: Python should be installed on your machine.link to download python:  https://www.python.org/downloads/
To start with, open your terminal and type in python
Python interpretter will start in the interactive mode. you can type in commands and the interpreter will execute them.
Try some commands on your own , like print('Hey!'), 2+2, 4 == 3, bin(45), hex(18)... etc., If you don't know any as of now, take a look at tut2.py, and try searching what each of those commands do.
Great, so now we know how to activate the python interpretter in interactive mode. (looks just like a terminal right?)
now create a file ending with the extension .py (look at tut2.py in this directory)
type in any commands you know of till now.
save the file. Congrats , you just created a python module!. This can be interpretted by the python interpreter.
type in :
python -m <your_file_name>
the string passed after the -m flag is recognised as the filename.
If you carefully look at the first line of tut2.py, it is #!/usr/bin/python3, This is called the shebang line, It tells the unix operating system that this file is a script. If the user has correct permissions to execute the file, the user can do so. the shebang characters are #!. the following string is the path of the interpretter to be used. You can find so by typing 'which python3' and you'll get the location of the python interpretter binary in your system. (revision of tut1: binary is the machine level code which a cpu can directly execute.)
One more way to execute a python command is to use the -c flag.:
python -c 'command'
Notice the use of inverted commas wrapping the command. 
Congrats on making and executing your first python module as a script!
Now you know what to do to write a script.
