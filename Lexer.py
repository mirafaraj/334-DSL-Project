import re #Python's regular expression engine (the heart of the lexer)
from collections import namedtuple #creates a lightweight object for tokens

Token = namedtuple("Token", ["type", "value", "line", "column"])
TOKEN_SPECIFICATION = [
    # Keywords
    ("KEYWORD", r"\b(agent|tool|task|action|system|run|if|for|in|string|int|bool|list)\b"),

    #Literals
    ("NUM", r"\b(0|[1-9][0-9]*)\b"),
    ("STRING_LITERAL", r'"([^"\\]|\\.)*"'),#[^...]->match anything but what's after ^, so " and \ are not allowed bec " would end 
                                           #the string early while \ alone at the end is problematic
    ("BOOL_LITERAL", r"\b(true|false)\b"),
    
    #Identifiers
    ("ID", r"\b[a-zA-Z_][a-zA-Z_0-9]*"),

    #Return Arrow
    ("ARROW", r"->"),

    #Operators
    ("OPERATORS", r"\+|-|==|<=|>=|<|>|=|\*|/"),

    #Delimiters
    ("DELIMITER", r"\(|\)|\{|\}|\[|\]|,|\.|:"),

    #Comments
    ("COMMENT", r"//.*|#.*"),

    #Whitespace
    ("WHITESPACE", r"[ \t\r\n]+"),

    #any other character
    ("MISMATCH", r".")
]

token_regex = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECIFICATION))

def tokenize(code):
    tokens = [] #initialize token array
    line_num = 1 #tracks which line we're currently at
    line_start = 0 #tells me at which character position my current line begins at since the source code given is one single long string


    #finditer():
    # starts at position 0
    # applies the regex
    # finds a match
    # advances the input pointer
    # repeats until EOF

    for match in token_regex.finditer(code): #iterates over every token match from left to right
        # lastgroup What kind of token is this? example: "KEYWORD"
        # group()   What text was matched? ex: "agent"
        # start()   Where did it occur?(which column in the line?)
        kind = match.lastgroup
        value = match.group() 
        column = match.start() - line_start + 1 #match.start() gives the absolute character position in the whole string, so subtracting line_start 
                                                #gives you the offset from the beginning of the current line. The +1 makes it 1-indexed.

        #print (kind, value, column)  # Debug print to trace tokenization

        #SKIP ANY EMPTY LINES OR COMMENTED ONES
        if kind == "WHITESPACE":
            if "\n" in value:
                line_num += value.count("\n")
                line_start = match.end()
            continue

        if kind == "COMMENT":
            continue #since our comments' regex doesn't involve having more than one line commmented in one single comment

        #display an error if nothing matched.
        if kind == "MISMATCH":
            raise SyntaxError(
                f"Unexpected character {value!r} at line {line_num}, column {column}"
            )

        if kind == "KEYWORD":
            token_kind = value
        elif kind == "ARROW":
            token_kind = "->"
        elif kind == "OPERATORS":
            token_kind = value
        elif kind == "DELIMITER":
            token_kind = value
        else:
            token_kind = kind

        #else: add the token to the tokens array if it did match and we reached this part of the code
        tokens.append(Token(token_kind, value, line_num, column))

    #Add end marker token for the LL(1) parser
    tokens.append(Token("$", "$", line_num, 1))

    return tokens
