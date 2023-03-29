from scanner import Scanner
from DFA import DFA, TokenType, Transition
import re
from enum import Enum

# read input
input_file = open("input.txt", "r")
input_lines = input_file.readlines()
tokens_list = []
symbol_table_list = []
lexical_errors_list = []
# creating scanner
scanner = Scanner(input_text=input_lines)


# creating DFA


def create_dfa():
    dfa = DFA.add_new_state(1, False)

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


# opening output text files
symbol_table = set(symbol_table_list)
tokens_file = open("tokens.txt", "w")
symbol_table_file = open("symbol_table.txt", "w")
lexical_errors_file = open("lexical_errors.txt", "w")

# putting lists into text files
tokens_file.writelines(tokens_list)
symbol_table_file.writelines(symbol_table)
if len(lexical_errors_list) == 0:
    lexical_errors_list.append("there is no lexical error.")
lexical_errors_file.writelines(lexical_errors_list)

