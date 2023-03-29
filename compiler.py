from scanner import Scanner

# read input
input_file = open("input.txt", "r")
input_lines = input_file.readlines()
tokens_list = []
symbol_table_list = []
lexical_errors_list = []
scanner = Scanner
for input_line in input_lines:
    for character in input_line:
        token = Scanner.get_next_token(character)
        tokens_list.append(token)
        lexical_errors_list.append(Scanner.panic_mode())
        symbol_table_list.append(token[1])

# opening output text files
symbol_table = set(symbol_table_list)
tokens_file = open("tokens.txt", "w")
symbol_table_file = open("symbol_table.txt", "w")
lexical_errors_file = open("lexical_errors.txt", "w")

# putting lists into text files
tokens_file.writelines(tokens_list)
tokens_file.writelines(symbol_table)
if len(lexical_errors_list) == 0:
    lexical_errors_list.append("there is no lexical error.")
tokens_file.writelines(lexical_errors_list)
