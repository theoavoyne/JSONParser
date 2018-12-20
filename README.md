# JSON Parser using PLY (Python Lex-Yacc)

JSON to Python dictionnary converter using [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/ply.html).

## Structure

The program is structured in three Python files:

### lexer.py

Contains the lexer configuration: tokens names, regular expression rules as well as an error handler. It is formatted as required by [ply](http://www.dabeaz.com/ply/ply.html). It describes the way the input string will be converted into a token stream.

### parse.py

Contains the BNF grammar rules that describe how the tokens generated by the lexer will be assembled. The rules are declared in the *doctrings* of the `p_functions`. It also contains a syntax error handler, `p_error()`.

### app.py

User interface for executing the program. First, it imports **ply** as well as lexer.py and parser.py. It then builds the lexer–`lex.lex()`–and the parser–`yacc.yacc()`. Then, it uses the sys module to retrieve the target file’s path—given as the second argument—and try to parse its content-`parser.parse(file)`. 

If no error is raised during execution—meaning that the syntax is valid—the result of this operation is stored in variable `result`. It is a Python dictionnary that corresponds to the JSON object. To print it to the console, set the `print_dict` variable to `True` in app.py (l. 12). The variable `result` is then *serialized* using [pickle](https://docs.python.org/3/library/pickle.html) and saved in a file named `dict.pickle`(generated in the same directory). Any program can now load it by using pickle's `load()` method-for example, `my_dict = pickle.load(dict)` (don't forget to set the correct path to the file).

However, if an error is raised during execution—meaning that the syntax is not valid—the program stops executing. Information is given about the type of error that occurred (*LexerError* or *ParserError*) and its location.

## JSON specifications

[ECMA-404](https://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf)

## Getting started

### Prerequisites

`Python 3.6.0` or higher.

**Packages**
* [ply](http://www.dabeaz.com/ply/ply.html)
* [pickle](https://docs.python.org/3/library/pickle.html)


### Executing the program

From your terminal, run:

```
$ python app.py relative_path_to_file.test
```

If the syntax is correct, you will get:

```
Parsing Succeeded: JSON Syntax OK
```
