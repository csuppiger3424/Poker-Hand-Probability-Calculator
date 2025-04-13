class Hand:
    def __init__(self, hand):
        if not isinstance(hand, list):
            raise TypeError("Hand must be a list of cards")
        if len(hand) > 7:
            raise ValueError("A hand cannot contain more than 7 cards")
        self.cards_list = hand

    def __str__(self):
        return ', '.join(str(card) for card in self.cards_list) if self.cards_list else "Empty Hand"
    
    def __len__(self):
        return len(self.cards_list)
    
    def reset_hand(self):
        """
        Reset the hand by clearing all cards.
        """
        self.cards_list = []
    
    def has_royal_flush(self):
        if len(self.cards_list) < 5:
            return False
        royal_numbers = {10, 11, 12, 13, 14}
        suit_groups = {}

        for card in self.cards_list:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = set()
            suit_groups[card.suit].add(card.number)
        
        for suit, numbers in suit_groups.items():
            if royal_numbers.issubset(numbers):
                return True
        return False
    
    def has_straight_flush(self):
        if len(self.cards_list) < 5:
            return False
        suit_groups = {}
        for card in self.cards_list:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = set()
            suit_groups[card.suit].add(card.number)
        
        for suit, numbers in suit_groups.items():
            sorted_numbers = sorted(numbers)
            if len(sorted_numbers) >= 5:
                for i in range(len(sorted_numbers) - 4):
                    if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                        return True
        return False

    def has_four_of_a_kind(self):
        if len(self.cards_list) < 4:
            return False
        number_groups = {}
        for card in self.cards_list:
            number_groups[card.number] = number_groups.get(card.number, 0) + 1
        
        for count in number_groups.values():
            if count == 4:
                return True
        return False

    def has_full_house(self):
        if len(self.cards_list) < 5:
            return False
        number_groups = {}
        for card in self.cards_list:
            number_groups[card.number] = number_groups.get(card.number, 0) + 1
        
        has_three_of_a_kind = False
        has_pair = False
        
        for count in number_groups.values():
            if count == 3:
                has_three_of_a_kind = True
            elif count == 2:
                has_pair = True
        
        return has_three_of_a_kind and has_pair

    def has_flush(self):
        if len(self.cards_list) < 5:
            return False
        suit_groups = {}
        for card in self.cards_list:
            suit_groups[card.suit] = suit_groups.get(card.suit, 0) + 1
        
        for count in suit_groups.values():
            if count >= 5:
                return True
        return False

    def has_straight(self):
        if len(self.cards_list) < 5:
            return False
        numbers = set(card.number for card in self.cards_list)
        if 14 in numbers:
            numbers.add(1)

        sorted_numbers = sorted(numbers)
        for i in range(len(sorted_numbers) - 4):
            if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                return True

        return False

    def has_three_of_a_kind(self):
        if len(self.cards_list) < 3:
            return False
        number_groups = {}
        for card in self.cards_list:
            number_groups[card.number] = number_groups.get(card.number, 0) + 1
        
        for count in number_groups.values():
            if count == 3:
                return True
        return False

    def has_two_pair(self):
        if len(self.cards_list) < 4:
            return False
        number_groups = {}
        for card in self.cards_list:
            number_groups[card.number] = number_groups.get(card.number, 0) + 1
        
        pair_count = 0
        
        for count in number_groups.values():
            if count == 2:
                pair_count += 1
        
        return pair_count >= 2

    def has_one_pair(self):
        if len(self.cards_list) < 2:
            return False
        number_groups = {}
        for card in self.cards_list:
            number_groups[card.number] = number_groups.get(card.number, 0) + 1
        
        for count in number_groups.values():
            if count == 2:
                return True
        return False

    def has_high_card(self):
        return len(self.cards_list) > 0  # If no other hand is found, it is a high card hand.

    def get_hand_type(self):
        if self.has_royal_flush():
            return "Royal Flush"
        elif self.has_straight_flush():
            return "Straight Flush"
        elif self.has_four_of_a_kind():
            return "Four of a Kind"
        elif self.has_full_house():
            return "Full House"
        elif self.has_flush():
            return "Flush"
        elif self.has_straight():
            return "Straight"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_two_pair():
            return "Two Pair"
        elif self.has_one_pair():
            return "One Pair"
        else:
            return "High Card"

    def add_card(self, card):
        """Add a card to the hand."""
        if len(self.cards_list) >= 7:
            raise ValueError("A hand cannot contain more than 7 cards")
        self.cards_list.append(card)

    def compare_with(self, other_hand):
        """
        Compare this hand with another hand.
        Returns:
            1 if self is stronger,
            -1 if other_hand is stronger,
            0 if both hands are equal.
        """
        hand_rankings = [
            "Royal Flush",
            "Straight Flush",
            "Four of a Kind",
            "Full House",
            "Flush",
            "Straight",
            "Three of a Kind",
            "Two Pair",
            "One Pair",
            "High Card"
        ]

        self_hand_type = self.get_hand_type()
        other_hand_type = other_hand.get_hand_type()

        if hand_rankings.index(self_hand_type) < hand_rankings.index(other_hand_type):
            return 1
        elif hand_rankings.index(self_hand_type) > hand_rankings.index(other_hand_type):
            return -1
        else:
            # If hand types are the same, compare based on specific hand rules
            if self_hand_type == "Four of a Kind":
                return self.compare_four_of_a_kind(other_hand)
            elif self_hand_type == "Flush":
                return self.compare_flush(other_hand)
            elif self_hand_type == "Straight":
                return self.compare_straight(other_hand)
            elif self_hand_type == "Three of a Kind":
                return self.compare_three_of_a_kind(other_hand)
            elif self_hand_type == "Two Pair":
                return self.compare_two_pair(other_hand)
            elif self_hand_type == "One Pair":
                return self.compare_one_pair(other_hand)
            else:
                return self.compare_high_card(other_hand)

    def compare_four_of_a_kind(self, other_hand):
        """
        Compare two hands with Four of a Kind.
        """
        def get_four_of_a_kind_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 4:
                    return number
            return 0

        self_value = get_four_of_a_kind_value(self)
        other_value = get_four_of_a_kind_value(other_hand)

        if self_value > other_value:
            return 1
        elif self_value < other_value:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_flush(self, other_hand):
        """
        Compare two hands with a Flush.
        """
        self_numbers = sorted([card.number for card in self.cards_list], reverse=True)
        other_numbers = sorted([card.number for card in other_hand.cards_list], reverse=True)

        for self_num, other_num in zip(self_numbers, other_numbers):
            if self_num > other_num:
                return 1
            elif self_num < other_num:
                return -1
        return 0
    
    def compare_full_house(self, other_hand):
        """
        Compare two hands with a Full House.
        """
        def get_full_house_values(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            three_of_a_kind = max([number for number, count in number_groups.items() if count == 3], default=0)
            pair = max([number for number, count in number_groups.items() if count == 2], default=0)
            return three_of_a_kind, pair

        self_three, self_pair = get_full_house_values(self)
        other_three, other_pair = get_full_house_values(other_hand)

        if self_three > other_three:
            return 1
        elif self_three < other_three:
            return -1
        elif self_pair > other_pair:
            return 1
        elif self_pair < other_pair:
            return -1
        else:
            return 0

    def compare_straight(self, other_hand):
        """
        Compare two hands with a Straight.
        """
        def get_straight_high_card(hand):
            numbers = set(card.number for card in hand.cards_list)
            if 14 in numbers:
                numbers.add(1)
            sorted_numbers = sorted(numbers)
            for i in range(len(sorted_numbers) - 4):
                if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                    return sorted_numbers[i + 4]
            return 0

        self_high_card = get_straight_high_card(self)
        other_high_card = get_straight_high_card(other_hand)

        if self_high_card > other_high_card:
            return 1
        elif self_high_card < other_high_card:
            return -1
        else:
            return 0

    def compare_three_of_a_kind(self, other_hand):
        """
        Compare two hands with Three of a Kind.
        """
        def get_three_of_a_kind_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 3:
                    return number
            return 0

        self_value = get_three_of_a_kind_value(self)
        other_value = get_three_of_a_kind_value(other_hand)

        if self_value > other_value:
            return 1
        elif self_value < other_value:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_two_pair(self, other_hand):
        """
        Compare two hands with Two Pair.
        """
        def get_pairs(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            pairs = sorted([number for number, count in number_groups.items() if count == 2], reverse=True)
            return pairs

        self_pairs = get_pairs(self)
        other_pairs = get_pairs(other_hand)

        for self_pair, other_pair in zip(self_pairs, other_pairs):
            if self_pair > other_pair:
                return 1
            elif self_pair < other_pair:
                return -1

        return self.compare_high_card(other_hand)

    def compare_one_pair(self, other_hand):
        """
        Compare two hands with One Pair.
        """
        def get_pair_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 2:
                    return number
            return 0

        self_value = get_pair_value(self)
        other_value = get_pair_value(other_hand)

        if self_value > other_value:
            return 1
        elif self_value < other_value:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_high_card(self, other_hand):
        """
        Compare two hands with High Card.
        """
        self_numbers = sorted([card.number for card in self.cards_list], reverse=True)
        other_numbers = sorted([card.number for card in other_hand.cards_list], reverse=True)

        for self_num, other_num in zip(self_numbers, other_numbers):
            if self_num > other_num:
                return 1
            elif self_num < other_num:
                return -1
        return 0

