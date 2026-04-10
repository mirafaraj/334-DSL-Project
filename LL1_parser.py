# Import the parsing table from the separate file
from Parsing_table import parsing_table


class LL1Parser:
    def __init__(self):
        # Store the LL(1) parsing table
        self.parsing_table = parsing_table

        # Define the start symbol of the grammar
        self.start_symbol = "Program"

        # Set of all non-terminals in the grammar
        # Used to distinguish between terminals and non-terminals
        self.non_terminals = {
            "Program", "AgentList", "AgentDef", "AgentStmtList", "InnerStmt",
            "ToolStmt", "TaskStmt", "ParamList", "ParamTail",
            "ActionStmtList", "ActionStmt", "ArgumentList", "ArgumentTail",
            "System", "SystemStmtList", "SystemStmt", "SystemStmt'",
            "AssignStmt", "IfStmt", "ForStmt", "Type", "Condition",
            "CompOp", "Exp", "Exp'", "Term", "Term'", "Factor",
            "ListExp", "ListList", "ListTail"
        }

    def parse(self, tokens):
        # Initialize the stack with end marker and start symbol
        stack = ["$", self.start_symbol]

        # Index to track current token in input
        index = 0

        # Parsing loop
        while True:
            # Get top of the stack
            top = stack[-1]

            # Get current token from input
            current = tokens[index]

            # Lookahead is the token type (used for table lookup)
            lookahead = current.type

            # =========================
            # ACCEPT CONDITION
            # =========================
            # If both stack and input reach end marker, parsing is successful
            if top == "$" and lookahead == "$":
                return True, "Parsing completed successfully."

            # =========================
            # TERMINAL CASE
            # =========================
            # If top of stack is a terminal
            if top not in self.non_terminals:

                # If it matches the current token → consume it
                if top == lookahead:
                    stack.pop()       # Remove terminal from stack
                    index += 1        # Move to next input token

                # Otherwise → syntax error
                else:
                    return False, (
                        f"Syntax error at line {current.line}, column {current.column}: "
                        f"expected '{top}', found '{lookahead}'"
                    )

            # =========================
            # NON-TERMINAL CASE
            # =========================
            else:
                # Form key using (non-terminal, lookahead)
                key = (top, lookahead)

                # If no rule exists in parsing table → error
                if key not in self.parsing_table:
                    return False, (
                        f"Syntax error at line {current.line}, column {current.column}: "
                        f"no rule for '{top}' with lookahead '{lookahead}'"
                    )

                # Get the production rule from the table
                production = self.parsing_table[key]

                # Remove the non-terminal from stack
                stack.pop()

                # If production is not epsilon, push RHS onto stack
                # Reverse order is used because stack is LIFO
                if production != ["ε"]:
                    for symbol in reversed(production):
                        stack.append(symbol)