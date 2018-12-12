# JSON Parser using PLY (Python Lex-Yacc)

Python program for checking the validity of a JSON file's syntax using [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/ply.html).

## Structure

The program is structured in three python files:

* lexer.py contains the lexer configuration: tokens names, regular expression rules as well as an error handler. It is formatted as required by [PLY](http://www.dabeaz.com/ply/ply.html). It describes the way the input string will be converted into a token stream.
* parse.py contains the BNF grammar rules that describe how the tokens generated by the lexer will be assembled. The rules are declared in the doctrings of the p_functions. It also contains a syntax error handler, p_error().
* app.py is the user interface for executing the program. First, it imports ply module as well as lexer.py and parser.py. It then builds the lexer `lex.lex()` and the parser `yacc.yacc()`. Then, it uses the sys module to retrieve the target file’s path that is given as an argument and converts its content into a string `open(file).read()`. Finally, it runs the parser with this input. If no error is raised during execution, a message saying that parsing succeeded is printed. Otherwise, it gives information about the type of error that occurred (*LexerError* or *ParserError*) and where the error is located.

## Getting started

### Prerequisites 

** PLY module **

Check that you have it by running:

`$ pip freeze | grep ply`

You should get something like:

`ply==3.11`

Otherwise, download it by running the following command:

`$ pip install ply`

** Python (2 or 3) **

Check that you have it by running:

`$ python -V`

You should get something like:

`Python 3.7.0`

### Execute the program

From your terminal, run:

`$ python3 app.py relative_path_to_file.test`

Please note that the path to the target file have to be relative and not absolute.
