# Import required modules
import sys
from Lexer import tokenize        # Function to convert input code into tokens
from LL1_parser import LL1Parser # LL(1) parser class


def main():
    # =========================
    # CHECK COMMAND-LINE INPUT
    # =========================
    # The program expects exactly one argument: the source file
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    # Get the filename from command-line arguments
    filename = sys.argv[1]

    # =========================
    # READ SOURCE FILE
    # =========================
    try:
        # Open and read the file contents
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        # Handle case where file does not exist
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)

    # =========================
    # LEXICAL ANALYSIS
    # =========================
    try:
        # Convert source code into a list of tokens
        tokens = tokenize(code)
    except SyntaxError as e:
        # If lexer encounters invalid characters, report error
        print("Lexical error:", e)
        sys.exit(1)

    # =========================
    # PARSING PHASE
    # =========================
    # Create an instance of the LL(1) parser
    parser = LL1Parser()

    # Parse the token list
    success, message = parser.parse(tokens)

    # =========================
    # OUTPUT RESULT
    # =========================
    if success:
        # If parsing succeeds, print success message
        print(message)
    else:
        # If parsing fails, print error message
        print(message)
        sys.exit(1)


# =========================
# ENTRY POINT
# =========================
# Ensures the program runs only when executed directly
if __name__ == "__main__":
    main()