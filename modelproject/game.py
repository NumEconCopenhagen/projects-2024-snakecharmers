# Here we define the game
import random


class game:
    def __init__(self, value_of_resource=2, cost_of_fight=3):

        # NOTE to self cost has to be greater than the
        # value of the resource

        self.V = value_of_resource
        self.C = cost_of_fight
        self.strategies = ["Dove", "Hawk"]

        # Define the payoff matrix using the strategies and their interactions
        self.payoff_matrix = {
            ('Hawk', 'Hawk'): (self.V / 2 - self.C / 2, self.V / 2 - self.C / 2),
            ('Hawk', 'Dove'): (self.V, 0),
            ('Dove', 'Hawk'): (0, self.V),
            ('Dove', 'Dove'): (self.V / 2, self.V / 2)
        }

    def simulate_interaction(self, strategy1, strategy2):
        """
        Simulates an interaction between two strategies and returns their payoffs.
        """
        return self.payoff_matrix[(strategy1, strategy2)]

    def random_strategy(self, dove = 0.5):
        """
        Returns a randomly selected strategy from the available strategies.
        """
        return random.choices(self.strategies, [dove, 1-dove], k=1)[0]
