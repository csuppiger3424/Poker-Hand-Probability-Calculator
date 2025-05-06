import math
from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from classes.table import Table
from classes.hand import Hand
from classes.simulation import Simulation

def calculate_confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for a given dataset.
    Args:
        data (list of float): The dataset (e.g., win percentages).
        confidence (float): The confidence level (default is 0.95).
    Returns:
        tuple: (mean, lower_bound, upper_bound)
    """
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    standard_deviation = math.sqrt(variance)
    margin_of_error = 1.96 * (standard_deviation / math.sqrt(len(data)))  # 1.96 for 95% confidence
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return mean, lower_bound, upper_bound

def main():
    """
    Main function to run multiple poker game simulations and calculate a confidence interval.
    """
    # player_num = 7
    # num_games = 10000
    # num_simulations = 10  # Number of simulations to run
    # player_cards = [Card("Club", 5), Card("Club", 7)]  # Example player cards
    # table_cards = [Card("Heart", 2), Card("Spade", 3), Card("Club", 6), Card("Diamond", 6)]  # Example table cards
    # # table_cards = []
    # win_percentages = []

    # for i in range(num_simulations):
    #     sim = Simulation(num_games, player_num, table_cards, player_cards)
    #     sim.run()
    #     win_percentages.append(sim.player1_win_percentage)
    #     print(f"Simulation {i + 1}: Player 1 win percentage = {sim.player1_win_percentage:.2f}%")

    # # Calculate confidence interval
    # mean, lower_bound, upper_bound = calculate_confidence_interval(win_percentages)
    # print(f"\nPlayer 1 win percentage over {num_simulations} simulations:")
    # print(f"Mean: {mean:.2f}%")
    # print(f"95% Confidence Interval: [{lower_bound:.2f}%, {upper_bound:.2f}%]")
    hand1 = Hand([Card("Heart", 5), Card("Heart", 6), Card("Diamond", 5), Card("Diamond", 6), Card("Diamond", 10), Card("Club", 5), Card("Club", 6)])
    hand2 = Hand([Card("Heart", 6), Card("Spade", 4), Card("Diamond", 5), Card("Diamond", 6), Card("Diamond", 10), Card("Club", 5), Card("Club", 6)])
    print(hand1.compare_full_house(hand2))
    print(hand1.has_two_pair())


if __name__ == "__main__":
    main()
