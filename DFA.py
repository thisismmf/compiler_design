from enum import Enum


class State:
    def __init__(self, number: int, isFinal: bool = None, name: str = None):
        self.number = number
        self.isFinal = isFinal
        self.state_transitions = []
        self.name = name
        # for a given regex check that it is available in inputs of one state transactions or not

    def add_new_transition(self, transition: 'Transition'):
        self.state_transitions.append(transition)


class Transition:
    def __init__(self, fromState: State, toState: State, regex: str):
        self.fromState = fromState
        self.toState = toState
        self.regex = regex


class DFA:
    def __init__(self):
        self.firstState = State(1, False)
        self.allStates = {}

    def add_new_state(self, number: int = None, isFinal: bool = None, name: str = None):
        self.allStates[number] = State(number=number, isFinal=isFinal, name=name)

    def add_new_transition(self, fromState: int, toState: int, regex: str):
        Transition(fromState=self.allStates[fromState], toState=self.allStates[toState], regex=regex)


class TokenType(Enum):
    NUM = 0
    ID = 1
    KEYWORD = 2
    SYMBOL = 3
    COMMENT = 4
    WHITESPACE = 5
