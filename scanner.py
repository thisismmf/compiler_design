import re


class Scanner:
    def __init__(self, dfa, input_text=None, ):
        self.scanning_line = 0
        self.scanning_char = 0
        self.dfa = dfa
        self.input_text = input_text

    def panic_mode(self):
        pass

    def get_next_token(self):
        current_state = self.dfa.firstState
        next_state = None
        for self.scanning_char, character in enumerate(self.input_text[self.scanning_line]):
            for transition in current_state.allTransitions:
                if re.match(transition.regex, character):
                    next_state = transition.toState
            if next_state.isFinal:
                return ()

    def change_scanning_line(self):
        self.scanning_line += 1


Keyword = ["if", " else", "void", "int", "repeat", "until", "break", "return"]
