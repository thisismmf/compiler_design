from scanner.scanner import Scanner
from scanner.DFA import DFA, TokenType, Transition, State
import re
from enum import Enum

# read input
input_file = open("input.txt", "r")
input_lines_string = input_file.read()
tokens_list = [[]]
symbol_table_list = ["break", "else", "if", "int", "repeat", "return", "until", "void", ]
lexical_errors_list = {}
INVALID_INPUT = r'[^a-zA-Z0-9;:,\[\]\(\)\{\}\+\-<=\*/\s]'


# creating DFA


def create_dfa():
    firstState = State(1, False)
    dfa = DFA(firstState)
    # dfa.add_new_state(1, False)
    dfa.add_new_state(2, True, False, "Error", "Invalid input")
    dfa.add_new_state(3, False, False)
    dfa.add_new_state(4, False, False)
    dfa.add_new_state(5, True, False, "COMMENT")
    dfa.add_new_state(6, True, False, "NUM")
    dfa.add_new_state(7, True, False, "ID")
    dfa.add_new_state(8, True, False, "WHITESPACE")
    dfa.add_new_state(9, True, False, "SYMBOL")
    dfa.add_new_state(10, True, False, "SYMBOL")
    dfa.add_new_state(11, True, False, "SYMBOL")
    dfa.add_new_state(12, True, True, "Error", "Unmatched comment")
    dfa.add_new_state(13, True, True, "Error", "Invalid number")
    dfa.add_new_state(14, True, True, "Error", "Invalid input")
    # dfa.add_new_state(15, True, True, "Error", "Invalid input")

    dfa.add_new_transition(1, 2, r'/')
    dfa.add_new_transition(2, 3, r'\*')
    dfa.add_new_transition(3, 4, r'\*')
    dfa.add_new_transition(3, 3, r'[^\*]')
    dfa.add_new_transition(4, 3, r'[^\*/]')
    dfa.add_new_transition(4, 5, r'/')
    dfa.add_new_transition(4, 4, r'\*')
    dfa.add_new_transition(1, 7, r'[a-zA-Z]')
    dfa.add_new_transition(7, 7, r'[a-zA-Z0-9]')
    dfa.add_new_transition(1, 6, r'[0-9]')
    dfa.add_new_transition(6, 6, r'[0-9]')
    dfa.add_new_transition(1, 8, r'\s')
    # dfa.add_new_transition(8, 8, r'\s')
    dfa.add_new_transition(1, 10, r'=')
    dfa.add_new_transition(10, 9, r'=')
    dfa.add_new_transition(1, 9, r'[\;\:,\[\]\{\}\(\)\+\-\<]')

    # Errors:
    # unmatched comment error:
    dfa.add_new_transition(1, 11, r'\*')
    dfa.add_new_transition(11, 12, r'/')  # state 12 has error massage

    # invalid number:
    dfa.add_new_transition(6, 13, r'([a-zA-Z]|[^a-zA-Z0-9;:,\[\]\(\)\{\}\+\-<=\*/\s])')
    # state 13 has error massage

    # invalid input:    state 14 has error massage
    dfa.add_new_transition(1, 14, INVALID_INPUT)
    dfa.add_new_transition(2, 14, INVALID_INPUT)
    dfa.add_new_transition(10, 14, INVALID_INPUT)
    dfa.add_new_transition(11, 14, INVALID_INPUT)
    dfa.add_new_transition(7, 14, INVALID_INPUT)

    return dfa


# creating scanner
scanner = Scanner(input_text=input_lines_string, dfa=create_dfa())

# opening output text files
tokens_file = open("tokens.txt", "w")
symbol_table_file = open("symbol_table.txt", "w")
lexical_errors_file = open("lexical_errors.txt", "w")
# reading whole text file for scanner
while not scanner.is_arrived_eof():
    lineNo, token_type, token_string, massage = scanner.get_next_token()
    # print(f"token_type, token_string = {(token_type, token_string)}")

    if len(tokens_list) != scanner.scanning_line:
        tokens_list.append([])
    if token_type not in ["WHITESPACE", "COMMENT", "Error"]:
        tokens_list[scanner.scanning_line - 1].append((token_type, token_string))
        if token_type == "ID" and token_string not in symbol_table_list:
            symbol_table_list.append(token_string)
    if token_type == "Error":
        if str(scanner.scanning_line) not in lexical_errors_list.keys():
            lexical_errors_list[str(scanner.scanning_line)] = ""
        lexical_errors_list[str(scanner.scanning_line)] += f"{(token_string, massage)} "
# symbol_table_list = list(set(symbol_table_list))
# putting lists into text files
for line, tokens in enumerate(tokens_list):
    if len(tokens) != 0:
        tokens_file.write(f"{line + 1}.   ")
        for token in tokens:
            tokens_file.write(" " + str(token))
        tokens_file.write("\n")

for line, symbol in enumerate(symbol_table_list):
    symbol_table_file.write(f"{line + 1}.\t")
    symbol_table_file.write(symbol + "\n")
if len(lexical_errors_list) == 0:
    lexical_errors_file.write("There is no lexical error.")
else:
    for key, value in lexical_errors_list.items():
        lexical_errors_file.write(f"{key}.\t{value}\n")
input_file.close()
tokens_file.close()
symbol_table_file.close()
lexical_errors_file.close()
