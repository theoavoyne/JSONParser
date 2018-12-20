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

# --> Defining regular expression rules ---

# ==> Convert JSON objects into corresponding Python3 objects
# ==> JSON specs: http://www.json.org/

t_ignore = ' \t\n'
t_COMMA = r','
t_COLON = r':'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'

def t_STRING(t):
  r'"(([^"\\])|(\\["\\\/bfnrt])|(\\u[0-9a-f]{4}))*"'
  t.value = t.value[1:-1] # Remove quotation marks
  return t

def t_NUMBER(t):
  r'\-?(0|([1-9][0-9]*))(\.[0-9]*)?([eE][\+\-]?[0-9]*)?'
  try: t.value = int(t.value)
  except: t.value = float(t.value)
  return t

def t_TRUE(t):
  r'true'
  t.value = True
  return t

def t_FALSE(t):
  r'false'
  t.value = False
  return t

def t_NULL(t):
  r'null'
  t.value = None
  return t

# -----------------------------------------

# Error rule for lexing errors
def t_error(t):
  # The lexer stops executing and raise a LexerError
  raise LexerError(t)
