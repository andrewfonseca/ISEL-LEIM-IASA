from random import choice
from random import random
from random import shuffle
from reinforcement_learning.action_selection.action_selection import ActionSelection


class GreedyActionSelection(ActionSelection):

    def __init__(self, learning_memory, actions, epsilon):
        self._learning_memory = learning_memory
        self._actions = actions
        self._epsilon = epsilon

    def select_action(self, state):
        if random() > self._epsilon:
            action = self.max_action(state)
        else:
            action = self.explore(state)

        return action

    def max_action(self, state):
        shuffle(self._actions)
        return max(self._actions, key=lambda action: self._learning_memory.acquire((state, action)))

    def explore(self, state):
        choice(self._actions)
