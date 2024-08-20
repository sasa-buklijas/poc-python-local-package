This is just proof of concept(example), how to import local file in python, if that file is in another directory.

This is common problem for beginners, so to have it documented as reference.

# 1. Everthing in one file
This is how everybody starts.

Problem is when file becomes too large (in lines of code), then code base is separated in multiple files.

So usually next step is:

# 2. Multiples files is in same directory
If file/files that you want to import are in same directory check [all_code_in_one_directory](all_code_in_one_directory) directory with files [file_in_same_directory.py](all_code_in_one_directory/file_in_same_directory.py) and [run_file_from_same_directory](all_code_in_one_directory/run_file_from_same_directory).
 
If both file are in same directory then you can just use `from file_in_same_directory import double`.

Problem with this approach is that if you have many in same directory it is getting messy and hard to understand.

Sooner or later, you would want to organise files in some kind of directory structure. Even if you just put them one directory like `lib`.

# 3. Files are not in same directory

Common setup is to have [main.py](main.py) in top level directory (file that will be executed and additional file/files in some other sub directory like [lib](lib).

Then, in order to import [m1.py](lib/m1) that is in [lib](lib) directory from [main.py](main.py). File that have Python code are called modules in Python terminology. 

Easy solution is to make empty file [__init__.py](lib/__init__.py) in [lib](lib) directory. In Python3 it is possible even without `___init__.py` file, but not in Python2, I will to go in details why.

Next problems starts when you have [m2.py](lib/m2) file in same [lib](lib) directory any you want to import [m2.py](lib/m2) from [m1.py](lib/m1).



# Practice

For how to do in practice check [https://github.com/IanHopkinson/mypackage](https://github.com/IanHopkinson/mypackage)