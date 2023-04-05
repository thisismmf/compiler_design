import re


class Scanner:
    def __init__(self, dfa, input_text=None, ):
        self.scanning_line = 1
        self.scanning_char = 0
        self.starting_char = 0
        self.dfa = dfa
        self.input_text = input_text

    def panic_mode(self):
        pass

    def get_next_token(self):
        keyword_name = "ID"
        current_state = self.dfa.firstState
        next_state = None
        for self.scanning_char, character in enumerate(self.input_text):
            if character == "\n":
                self.change_scanning_line()
            for transition in current_state.state_transitions:
                if re.match(transition.regex, character):
                    next_state = transition.toState
            if next_state!= None:
                if next_state.isFinal:
                    token_string = self.input_text[self.starting_char:self.scanning_char + 1]
                    if next_state.name == "ID":
                        if token_string in keywords:
                            keyword_name = "KEYWORD"
                    else:
                        keyword_name = next_state.name
                    self.starting_char = self.scanning_char + 1
                    return keyword_name, token_string
            else:
                return "" , ""

    def change_scanning_line(self):
        self.scanning_line += 1

    def is_arrived_eof(self):
        if self.scanning_char < len(self.input_text):
            return True
        return False


keywords = ["if", " else", "void", "int", "repeat", "until", "break", "return"]
