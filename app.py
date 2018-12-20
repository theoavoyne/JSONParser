import ply.lex as lex
import ply.yacc as yacc
import sys
import pickle

from lexer import *
from parser import *

lexer = lex.lex() # Build the lexer
parser = yacc.yacc() # Build the parser

print_dict = True # Enable to print the resulting python dict()

def main():
  if len(sys.argv) == 2:
    file = open(sys.argv[1]).read()

    # ----- Try to parse the file -----

    try:
      # Run the parser. If no error is raised, the JSON object is
      # converted to a python dict(), and saved as result
      result = parser.parse(file)
      print("Parsing Succeeded: JSON Syntax OK")
      print("The corresponding python dict() has been saved in dict.pickle")

      # Print the resulting python dict() to the terminal
      # It can be enabled / disabled at line 11
      if print_dict: print(result)

      # The python dict() is serialized and written in dict.pickle
      pickling_on = open("dict.pickle","wb")
      pickle.dump(result, pickling_on)
      pickling_on.close()

    # ------ Handle exceptions --------

    except LexerError as error:
      # If this error is raised, it means that the lexer failed to tokenize
      # the input JSON file. The file is not correctly formatted
      print('Parsing Failed: LexerError around character no. {} (\"{}\")'
            .format(error.args[0].lexpos, error.args[0].value[0]))

    except ParserError as error:
      # If this error is raised, it means that parsing failed due
      # to an incorrect syntax. Check specs at www.json.org
      if error.args[0]:
        # If ParserError is not due to reaching end-of-file.
        print('Parsing Failed: ParserError around character no. {} (\"{}\")'
              .format(error.args[0].lexpos, error.args[0].value))
      else:
        print('Parsing Failed: ParserError at EOF')

  # ------- Argument missing --------

  else:
    print("MISSING OR INVALID ARGUMENTS: please add the RELATIVE path of the file to be tested.")
    print("Example: python3 app.py file_path.text")

if __name__ == "__main__":
  main()
