parsing_table = {
    # Program / Agent section
    ("Program", "agent"): ["AgentList", "System"],
    ("Program", "system"): ["AgentList", "System"],

    ("AgentList", "agent"): ["AgentDef", "AgentList"],
    ("AgentList", "system"): ["ε"],

    ("AgentDef", "agent"): ["agent", "ID", "{", "AgentStmtList", "}"],

    ("AgentStmtList", "tool"): ["InnerStmt", "AgentStmtList"],
    ("AgentStmtList", "task"): ["InnerStmt", "AgentStmtList"],
    ("AgentStmtList", "}"): ["ε"],

    ("InnerStmt", "tool"): ["ToolStmt"],
    ("InnerStmt", "task"): ["TaskStmt"],

    ("ToolStmt", "tool"): ["tool", "ID"],

    ("TaskStmt", "task"): [
        "task", "ID", "(", "ParamList", ")", "->", "Type", "ID", "{", "ActionStmtList", "}"
    ],

    # Parameters
    ("ParamList", "string"): ["Type", "ID", "ParamTail"],
    ("ParamList", "int"): ["Type", "ID", "ParamTail"],
    ("ParamList", "bool"): ["Type", "ID", "ParamTail"],
    ("ParamList", "list"): ["Type", "ID", "ParamTail"],
    ("ParamList", ")"): ["ε"],

    ("ParamTail", ","): [",", "Type", "ID", "ParamTail"],
    ("ParamTail", ")"): ["ε"],

    # Actions / arguments
    ("ActionStmtList", "action"): ["ActionStmt", "ActionStmtList"],
    ("ActionStmtList", "}"): ["ε"],

    ("ActionStmt", "action"): ["action", ":", "ID", "(", "ArgumentList", ")"],

    ("ArgumentList", "ID"): ["Exp", "ArgumentTail"],
    ("ArgumentList", "NUM"): ["Exp", "ArgumentTail"],
    ("ArgumentList", "STRING_LITERAL"): ["Exp", "ArgumentTail"],
    ("ArgumentList", "BOOL_LITERAL"): ["Exp", "ArgumentTail"],
    ("ArgumentList", "["): ["Exp", "ArgumentTail"],
    ("ArgumentList", "("): ["Exp", "ArgumentTail"],
    ("ArgumentList", ")"): ["ε"],

    ("ArgumentTail", ","): [",", "Exp", "ArgumentTail"],
    ("ArgumentTail", ")"): ["ε"],

    # System section
    ("System", "system"): ["system", "{", "SystemStmtList", "}"],

    ("SystemStmtList", "string"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "int"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "bool"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "list"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "ID"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "if"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "for"): ["SystemStmt", "SystemStmtList"],
    ("SystemStmtList", "}"): ["ε"],

    ("SystemStmt", "string"): ["Type", "ID", "=", "SystemStmt'"],
    ("SystemStmt", "int"): ["Type", "ID", "=", "SystemStmt'"],
    ("SystemStmt", "bool"): ["Type", "ID", "=", "SystemStmt'"],
    ("SystemStmt", "list"): ["Type", "ID", "=", "SystemStmt'"],
    ("SystemStmt", "ID"): ["AssignStmt"],
    ("SystemStmt", "if"): ["IfStmt"],
    ("SystemStmt", "for"): ["ForStmt"],

    ("SystemStmt'", "ID"): ["Exp"],
    ("SystemStmt'", "NUM"): ["Exp"],
    ("SystemStmt'", "STRING_LITERAL"): ["Exp"],
    ("SystemStmt'", "BOOL_LITERAL"): ["Exp"],
    ("SystemStmt'", "["): ["Exp"],
    ("SystemStmt'", "("): ["Exp"],
    ("SystemStmt'", "run"): ["run", "ID", ".", "ID", "(", "ArgumentList", ")"],

    ("AssignStmt", "ID"): ["ID", "=", "Exp"],

    ("IfStmt", "if"): ["if", "Condition", "{", "SystemStmtList", "}"],
    ("ForStmt", "for"): ["for", "ID", "in", "ID", "{", "SystemStmtList", "}"],

    # Type / condition / comparison
    ("Type", "string"): ["string"],
    ("Type", "int"): ["int"],
    ("Type", "bool"): ["bool"],
    ("Type", "list"): ["list"],

    ("Condition", "ID"): ["Exp", "CompOp", "Exp"],
    ("Condition", "NUM"): ["Exp", "CompOp", "Exp"],
    ("Condition", "STRING_LITERAL"): ["Exp", "CompOp", "Exp"],
    ("Condition", "BOOL_LITERAL"): ["Exp", "CompOp", "Exp"],
    ("Condition", "["): ["Exp", "CompOp", "Exp"],
    ("Condition", "("): ["Exp", "CompOp", "Exp"],

    ("CompOp", "<"): ["<"],
    ("CompOp", ">"): [">"],
    ("CompOp", "<="): ["<="],
    ("CompOp", ">="): [">="],
    ("CompOp", "=="): ["=="],

    # Expressions
    ("Exp", "ID"): ["Term", "Exp'"],
    ("Exp", "NUM"): ["Term", "Exp'"],
    ("Exp", "STRING_LITERAL"): ["Term", "Exp'"],
    ("Exp", "BOOL_LITERAL"): ["Term", "Exp'"],
    ("Exp", "["): ["Term", "Exp'"],
    ("Exp", "("): ["Term", "Exp'"],

    ("Exp'", "+"): ["+", "Term", "Exp'"],
    ("Exp'", "-"): ["-", "Term", "Exp'"],
    ("Exp'", ","): ["ε"],
    ("Exp'", ")"): ["ε"],
    ("Exp'", "string"): ["ε"],
    ("Exp'", "int"): ["ε"],
    ("Exp'", "bool"): ["ε"],
    ("Exp'", "list"): ["ε"],
    ("Exp'", "ID"): ["ε"],
    ("Exp'", "if"): ["ε"],
    ("Exp'", "for"): ["ε"],
    ("Exp'", "}"): ["ε"],
    ("Exp'", "<"): ["ε"],
    ("Exp'", ">"): ["ε"],
    ("Exp'", "<="): ["ε"],
    ("Exp'", ">="): ["ε"],
    ("Exp'", "=="): ["ε"],
    ("Exp'", "{"): ["ε"],
    ("Exp'", "]"): ["ε"],

    ("Term", "ID"): ["Factor", "Term'"],
    ("Term", "NUM"): ["Factor", "Term'"],
    ("Term", "STRING_LITERAL"): ["Factor", "Term'"],
    ("Term", "BOOL_LITERAL"): ["Factor", "Term'"],
    ("Term", "["): ["Factor", "Term'"],
    ("Term", "("): ["Factor", "Term'"],

    ("Term'", "*"): ["*", "Factor", "Term'"],
    ("Term'", "/"): ["/", "Factor", "Term'"],
    ("Term'", "+"): ["ε"],
    ("Term'", "-"): ["ε"],
    ("Term'", ","): ["ε"],
    ("Term'", ")"): ["ε"],
    ("Term'", "string"): ["ε"],
    ("Term'", "int"): ["ε"],
    ("Term'", "bool"): ["ε"],
    ("Term'", "list"): ["ε"],
    ("Term'", "ID"): ["ε"],
    ("Term'", "if"): ["ε"],
    ("Term'", "for"): ["ε"],
    ("Term'", "}"): ["ε"],
    ("Term'", "<"): ["ε"],
    ("Term'", ">"): ["ε"],
    ("Term'", "<="): ["ε"],
    ("Term'", ">="): ["ε"],
    ("Term'", "=="): ["ε"],
    ("Term'", "{"): ["ε"],
    ("Term'", "]"): ["ε"],

    ("Factor", "ID"): ["ID"],
    ("Factor", "NUM"): ["NUM"],
    ("Factor", "STRING_LITERAL"): ["STRING_LITERAL"],
    ("Factor", "BOOL_LITERAL"): ["BOOL_LITERAL"],
    ("Factor", "["): ["ListExp"],
    ("Factor", "("): ["(", "Exp", ")"],

    # Lists
    ("ListExp", "["): ["[", "ListList", "]"],

    ("ListList", "ID"): ["Exp", "ListTail"],
    ("ListList", "NUM"): ["Exp", "ListTail"],
    ("ListList", "STRING_LITERAL"): ["Exp", "ListTail"],
    ("ListList", "BOOL_LITERAL"): ["Exp", "ListTail"],
    ("ListList", "["): ["Exp", "ListTail"],
    ("ListList", "("): ["Exp", "ListTail"],
    ("ListList", "]"): ["ε"],

    ("ListTail", ","): [",", "Exp", "ListTail"],
    ("ListTail", "]"): ["ε"],
}