class Hand:
    def __init__(self, hand):
        if not isinstance(hand, list):
            raise TypeError("Hand must be a list of cards")
        if len(hand) < 2:
            raise ValueError("A hand must contain at least 2 cards")
        if len(hand) > 7:
            raise ValueError("A hand cannot contain more than 7 cards")
        self.cards_list = hand

    def __str__(self):
        return ', '.join(str(card) for card in self.cards_list)
    
    def __len__(self):
        return len(self.cards_list)
    
    def has_royal_flush(self):
        royalNumbers = {10, 11, 12, 13, 14}
        suit_groups = {}

        for card in self.cards_list:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = set()
            suit_groups[card.suit].add(card.number)
        
        for suit, numbers in suit_groups.items():
            if royalNumbers.issubset(numbers):
                return True
        return False
    
    def has_straight_flush(self):
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
        number_groups = {}
        for card in self.cards_list:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 4:
                return True
        return False

    def has_full_house(self):
        number_groups = {}
        for card in self.cards_list:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        hasThreeOfAKind = False
        hasPair = False
        
        for count in number_groups.values():
            if count == 3:
                hasThreeOfAKind = True
            elif count == 2:
                hasPair = True
        
        return hasThreeOfAKind and hasPair

    def has_flush(self):
        suit_groups = {}
        for card in self.cards_list:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = 0
            suit_groups[card.suit] += 1
        
        for count in suit_groups.values():
            if count >= 5:
                return True
        return False

    def has_straight(self):
        numbers = set(card.number for card in self.cards_list)
        if 14 in numbers:
            numbers.add(1)

        sorted_numbers = sorted(numbers)
        for i in range(len(sorted_numbers) - 4):
            if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                return True

        return False

    def has_three_of_a_kind(self):
        number_groups = {}
        for card in self.cards_list:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 3:
                return True
        return False

    def has_two_pair(self):
        number_groups = {}
        for card in self.cards_list:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        pair_count = 0
        
        for count in number_groups.values():
            if count == 2:
                pair_count += 1
        
        return pair_count == 2

    def has_one_pair(self):
        number_groups = {}
        for card in self.cards_list:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 2:
                return True
        return False

    def has_high_card(self):
        return True # If no other hand is found, it is a high card hand.

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

    def compare_high_card(self, other_hand):
        sorted_self = sorted([card.number for card in self.cards_list], reverse=True)
        sorted_other = sorted([card.number for card in other_hand.cards_list], reverse=True)

        for card1, card2 in zip(sorted_self, sorted_other):
            if card1 > card2:
                return 1
            elif card1 < card2:
                return -1
        return 0

    def compare_one_pair(self, other_hand):
        def get_pair_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 2:
                    return number
            return 0

        pair_self = get_pair_value(self)
        pair_other = get_pair_value(other_hand)

        if pair_self > pair_other:
            return 1
        elif pair_self < pair_other:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_two_pair(self, other_hand):
        def get_pairs(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            pairs = [number for number, count in number_groups.items() if count == 2]
            return sorted(pairs, reverse=True)

        pairs_self = get_pairs(self)
        pairs_other = get_pairs(other_hand)

        for pair1, pair2 in zip(pairs_self, pairs_other):
            if pair1 > pair2:
                return 1
            elif pair1 < pair2:
                return -1

        return self.compare_high_card(other_hand)

    def compare_three_of_a_kind(self, other_hand):
        def get_three_of_a_kind_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 3:
                    return number
            return 0

        three_self = get_three_of_a_kind_value(self)
        three_other = get_three_of_a_kind_value(other_hand)

        if three_self > three_other:
            return 1
        elif three_self < three_other:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_straight(self, other_hand):
        def get_straight_high_card(hand):
            numbers = set(card.number for card in hand.cards_list)
            if 14 in numbers:
                numbers.add(1)
            sorted_numbers = sorted(numbers)
            for i in range(len(sorted_numbers) - 4):
                if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                    return sorted_numbers[i + 4]
            return 0

        high_self = get_straight_high_card(self)
        high_other = get_straight_high_card(other_hand)

        if high_self > high_other:
            return 1
        elif high_self < high_other:
            return -1
        else:
            return 0  # Tie

    def compare_flush(self, other_hand):
        sorted_self = sorted([card.number for card in self.cards_list], reverse=True)
        sorted_other = sorted([card.number for card in other_hand.cards_list], reverse=True)

        for card1, card2 in zip(sorted_self, sorted_other):
            if card1 > card2:
                return 1
            elif card1 < card2:
                return -1
        return 0  # Tie

    def compare_full_house(self, other_hand):
        def get_full_house_values(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            three = max([number for number, count in number_groups.items() if count == 3], default=0)
            pair = max([number for number, count in number_groups.items() if count == 2], default=0)
            return three, pair

        three_self, pair_self = get_full_house_values(self)
        three_other, pair_other = get_full_house_values(other_hand)

        if three_self > three_other:
            return 1
        elif three_self < three_other:
            return -1
        elif pair_self > pair_other:
            return 1
        elif pair_self < pair_other:
            return -1
        else:
            return 0  # Tie

    def compare_four_of_a_kind(self, other_hand):
        def get_four_of_a_kind_value(hand):
            number_groups = {}
            for card in hand.cards_list:
                number_groups[card.number] = number_groups.get(card.number, 0) + 1
            for number, count in number_groups.items():
                if count == 4:
                    return number
            return 0

        four_self = get_four_of_a_kind_value(self)
        four_other = get_four_of_a_kind_value(other_hand)

        if four_self > four_other:
            return 1
        elif four_self < four_other:
            return -1
        else:
            return self.compare_high_card(other_hand)

    def compare_straight_flush(self, other_hand):
        return self.compare_straight(other_hand)

    def compare_royal_flush(self, other_hand):
        return 0

    def compare_with(self, other_hand):
        hand_rankings = [
            "High Card", "One Pair", "Two Pair", "Three of a Kind",
            "Straight", "Flush", "Full House", "Four of a Kind",
            "Straight Flush", "Royal Flush"
        ]

        self_rank = hand_rankings.index(self.get_hand_type())
        other_rank = hand_rankings.index(other_hand.get_hand_type())

        if self_rank > other_rank:
            return 1
        elif self_rank < other_rank:
            return -1
        else:
            comparison_methods = {
                "High Card": self.compare_high_card,
                "One Pair": self.compare_one_pair,
                "Two Pair": self.compare_two_pair,
                "Three of a Kind": self.compare_three_of_a_kind,
                "Straight": self.compare_straight,
                "Flush": self.compare_flush,
                "Full House": self.compare_full_house,
                "Four of a Kind": self.compare_four_of_a_kind,
                "Straight Flush": self.compare_straight_flush,
                "Royal Flush": self.compare_royal_flush
            }
            return comparison_methods[hand_rankings[self_rank]](other_hand)