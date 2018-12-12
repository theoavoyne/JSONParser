# Defining an exception to handle lexing errors
class LexerError(Exception): pass

# List of token names
tokens = [
    'STRING',
    'NUMBER',
    'COMMA',
    'COLON',
    'TRUE',
    'FALSE',
    'NULL',
    'LBRACKET',
    'RBRACKET',
    'LSQBRACKET',
    'RSQBRACKET'
    ]

# Regular expression rules for tokens
# JSON specifications found on http://www.json.org/
t_ignore = ' \t\n'
t_STRING = r'"(([^"\\])|(\\["\\\/bfnrt])|(\\u[0-9a-f]{4}))*"'
t_NUMBER = r'\-?(0|([1-9][0-9]*))(\.[0-9]*)?([eE][\+\-]?[0-9]*)?'
t_COMMA = r','
t_COLON = r':'
t_TRUE = r'true'
t_FALSE = r'false'
t_NULL = r'null'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'

# Error rule for lexing errors
def t_error(t):
  # The lexer stops executing and raise a LexerError
    raise LexerError(t)
