import sys
from Lexer import tokenize 
from LL1_parser import LL1Parser 


def main():
    # Check the command line input
    # The program expects exactly one argument: the source file
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    # Get the filename from command-line arguments
    filename = sys.argv[1]

    try:
        # Open and read the file contents
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read() # Store the source code in the variable "code"
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)

    
    try:
        # Convert source code into a list of tokens
        tokens = tokenize(code)
    except SyntaxError as e:
        # If lexer encounters invalid characters, report error
        print("Lexical error:", e)
        sys.exit(1)

    # Create an instance of the LL(1) parser
    parser = LL1Parser()

    # Parse the token list
    success, message = parser.parse(tokens)

    if success:
        # If parsing succeeds, print success message
        print(message)
    else:
        # If parsing fails, print error message
        print(message)
        sys.exit(1)


if __name__ == "__main__":
    main()

# Every python file has a built-in variable called __name__ and it depends on how the file is being used. 
# Initially, __name__ is "__main__" by defualt. 
# If you're tryign to run the program form the file itself then __name__=="__main__"
# But if you import this file to another one then __name__=filename now so it's !="__main__"
# So main won't run here on its own if u try to run the program, unless u run the lexer file directly form the prompt
