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
        # print(f"all states : {self.dfa.allStates}")
        keyword_name = "ID"
        current_state = self.dfa.firstState
        # print(f"first_state.state_transitions : {current_state.state_transitions}")
        # print(f"first_state: {current_state}")

        # for self.scanning_char, character in enumerate(self.input_text):
        for i in range(self.starting_char, len(self.input_text)):
            self.scanning_char = i
            character = self.input_text[i]
            if character == "\n":
                self.change_scanning_line()
            next_state = None
            no_transition = True
            for transition in current_state.state_transitions:
                # print(f"transition state : {transition.toState}")

                if re.match(transition.regex, character):
                    no_transition = False
                    next_state = transition.toState
                    current_state = next_state
                    break
            if not no_transition:
                continue
            if next_state == None:
                if current_state.isFinal:
                    token_string = self.input_text[self.starting_char:self.scanning_char]
                    if current_state.name == "ID":
                        if token_string in keywords:
                            keyword_name = "KEYWORD"
                    else:
                        keyword_name = current_state.name
                    self.starting_char = self.scanning_char + 1
                    return keyword_name, token_string
            else:
                return "", ""

    def change_scanning_line(self):
        self.scanning_line += 1

    def is_arrived_eof(self):
        if self.scanning_char < len(self.input_text):
            return True
        return False


keywords = ["if", " else", "void", "int", "repeat", "until", "break", "return"]
