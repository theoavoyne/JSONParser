import ply.lex as lex
import ply.yacc as yacc
import sys

from lexer import *
from parser import *

lexer = lex.lex() # Build the lexer
parser = yacc.yacc() # Build the parser


def main():
    if len(sys.argv) == 2:
        file = open(sys.argv[1]).read()
        try:
            parser.parse(file) # Run the parser with the file's content as input
            print("Parsing Succeeded: JSON Syntax OK") # Executed if no error has been raised
        except LexerError as error:
            print('Parsing Failed: LexerError around character no. {} (\"{}\")'
                  .format(error.args[0].lexpos, error.args[0].value[0]))
        except ParserError as error:
            if error.args[0]: # Check that ParserError is not due to reaching end-of-file.
                print('Parsing Failed: ParserError around character no. {} (\"{}\")'
                      .format(error.args[0].lexpos, error.args[0].value))
            else:
                print('Parsing Failed: ParserError at EOF')
    else:
        print("MISSING ARGUMENT: please add the RELATIVE path of the file to be tested.")
        print("Example: python3 app.py file_path.text")

if __name__ == "__main__":
    main()
