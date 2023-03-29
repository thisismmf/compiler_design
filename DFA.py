from enum import Enum


class Transition():
    def __init__(self, fromState: 'State', toState: 'State', regex: str):
        self.fromState = fromState
        self.toState = toState
        self.regex = regex


class State():
    def __init__(self, number: int, isFinal: bool, name: str = None):
        self.number = number
        self.isFinal = isFinal
        self.allStates = []
        self.allTransitions = []
        self.name = name
        # for a given regex check that it is available in inputs of one state transactions or not

    def add_new_transition(self, transition: Transition):
        self.allTransitions.append()


class DFA():
    def __init__(self, firstState: State):
        self.firstState = firstState
        self.allStates = {}

    def add_new_state(self, number, isFinal, name):
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


