class Scanner:
    def __init__(self, dfa, input_text=None, ):
        self.scanning_line = 0
        self.dfa = dfa
        self.input_text = input_text

    def panic_mode(self):
        pass

    def get_next_token(self):
        pass

    def change_scanning_line(self):
        self.scanning_line += 1
