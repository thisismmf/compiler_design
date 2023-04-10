from enum import Enum


class State:
    def __init__(self, number: int, isFinal: bool = None, name: str = None):
        self.number = number
        self.isFinal = isFinal
        self.state_transitions = []
        self.name = name
        # for a given regex check that it is available in inputs of one state transactions or not

    def __str__(self):
        return f"name : {self.name} , number : {self.number}"

    def add_new_transition(self, transition: 'Transition'):
        self.state_transitions.append(transition)


class Transition:
    def __init__(self, fromState: State, toState: State, regex: str):
        self.fromState = fromState
        self.toState = toState
        self.regex = regex


class DFA:
    def __init__(self, firstState: State):
        # self.firstState = State(1, False)
        self.firstState = firstState
        self.allStates = {1: self.firstState}



    def add_new_state(self, number: int = None, isFinal: bool = None, name: str = None):
        self.allStates[number] = State(number=number, isFinal=isFinal, name=name)

    def add_new_transition(self, fromState: int, toState: int, regex: str):
        print("new transition:")
        print("from state: " + str(fromState))
        print("to state: " + str(toState))
        self.allStates[fromState].add_new_transition(Transition(fromState=self.allStates[fromState], toState=self.allStates[toState], regex=regex))


class TokenType(Enum):
    NUM = 0
    ID = 1
    KEYWORD = 2
    SYMBOL = 3
    COMMENT = 4
    WHITESPACE = 5
