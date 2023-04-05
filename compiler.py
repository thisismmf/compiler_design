from scanner import Scanner
from DFA import DFA, TokenType, Transition
import re
from enum import Enum

# read input
input_file = open("input.txt", "r")
input_lines_string = input_file.read()
tokens_list = [[]]
symbol_table_list = ["if", " else", "void", "int", "repeat", "until", "break", "return"]
lexical_errors_list = []


# creating DFA


def create_dfa():
    dfa = DFA()
    dfa.add_new_state(1, False)
    dfa.add_new_state(2, False)
    dfa.add_new_state(3, False)
    dfa.add_new_state(4, False)
    dfa.add_new_state(5, True, "COMMENT")
    dfa.add_new_state(6, True, "NUM")
    dfa.add_new_state(7, True, "ID")
    dfa.add_new_state(8, True, "WHITESPACE")
    dfa.add_new_state(9, True, "SYMBOL")
    dfa.add_new_state(10, False)

    dfa.add_new_transition(1, 2, r'/')
    dfa.add_new_transition(2, 3, r'\*')
    dfa.add_new_transition(3, 4, r'\*')
    dfa.add_new_transition(3, 3, r'^\*')
    dfa.add_new_transition(4, 3, r'^\*/')
    dfa.add_new_transition(4, 5, r'/')
    dfa.add_new_transition(4, 4, r'\*')
    dfa.add_new_transition(1, 7, r'[a-zA-Z]')
    dfa.add_new_transition(7, 7, r'[a-zA-Z0-9]')
    dfa.add_new_transition(1, 6, r'[0-9]')
    dfa.add_new_transition(6, 6, r'[0-9]')
    dfa.add_new_transition(1, 8, r'\s')
    dfa.add_new_transition(1, 10, r'=')
    dfa.add_new_transition(10, 9, r'=')
    dfa.add_new_transition(1, 9, r'[\;\:,\[\]\{\}\(\)\+\-\*\<]')
    return dfa


# creating scanner
scanner = Scanner(input_text=input_lines_string, dfa=create_dfa())

# opening output text files
symbol_table = set(symbol_table_list)
tokens_file = open("tokens.txt", "w")
symbol_table_file = open("symbol_table.txt", "w")
lexical_errors_file = open("lexical_errors.txt", "w")
# reading whole text file for scanner
while scanner.is_arrived_eof():
    token_type, token_string = scanner.get_next_token()
    if token_string == None and token_type == None:
        if len(tokens_list) != scanner.scanning_line:
            tokens_list.append([])
        tokens_list[scanner.scanning_line - 1].append((token_type, token_string))
        symbol_table_list.append(token_string)
symbol_table_list = list(set(symbol_table_list))
# putting lists into text files
tokens_file.writelines(tokens_list)
symbol_table_file.writelines(symbol_table_list)
symbol_table_file.writelines(symbol_table)
if len(lexical_errors_list) == 0:
    lexical_errors_list.append("there is no lexical error.")
lexical_errors_file.writelines(lexical_errors_list)
input_file.close()
tokens_file.close()
symbol_table_file.close()
lexical_errors_file.close()
