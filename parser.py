# Defining an exception to handle parsing errors
class ParserError(Exception): pass

# --- Defining grammar rules ---

# The docstrings contain context-free grammar specifications

def p_object(p):
    """object : LBRACKET members RBRACKET
              | LBRACKET RBRACKET"""

def p_members(p):
    """members : pair
               | pair COMMA members"""

def p_pair(p):
    """pair : STRING COLON value"""

def p_array(p):
    """array : LSQBRACKET RSQBRACKET
             | LSQBRACKET elements RSQBRACKET"""

def p_elements(p):
    """elements : value
                | value COMMA elements"""

def p_value(p):
    """value : STRING
             | NUMBER
             | object
             | array
             | TRUE
             | FALSE
             | NULL"""

# ------------------------------

# Error rule for parsing errors
def p_error(p):
  # The parser stops executing and raise a ParserError
    raise ParserError(p)


