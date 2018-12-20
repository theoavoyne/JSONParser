# Defining an exception to handle parsing errors
class ParserError(Exception): pass

# ==> Defining the context-free grammar specifications

def p_object(p):
  """object : LBRACKET members RBRACKET
            | LBRACKET RBRACKET"""
  p[0] = {}
  if len(p) == 4:
    for item in p[2]:
      p[0][item[0]] = item[1]

def p_members(p):
  """members : pair
             | pair COMMA members"""
  p[0] = [p[1]]
  if len(p) == 4:
    for item in p[3]:
      p[0].append(item)

def p_pair(p):
  """pair : STRING COLON value"""
  p[0] = [p[1], p[3]]

def p_array(p):
  """array : LSQBRACKET RSQBRACKET
           | LSQBRACKET elements RSQBRACKET"""
  p[0] = []
  if len(p) == 4:
    for item in p[2]:
      p[0].append(item)

def p_elements(p):
  """elements : value
              | value COMMA elements"""
  p[0] = [p[1]]
  if len(p) == 4:
    for item in p[3]:
      p[0].append(item)

def p_value(p):
  """value : STRING
           | NUMBER
           | object
           | array
           | TRUE
           | FALSE
           | NULL"""
  p[0] = p[1]

# Error rule for parsing errors
def p_error(p):
  # The parser stops executing and raise a ParserError
  raise ParserError(p)


