class Hand:
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        return ', '.join(str(card) for card in self.hand)    
    
    def hasRoyalFlush(self):
        royalNumbers = {10, 11, 12, 13, 14}
        suit_groups = {}

        for card in self.hand:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = set()
            suit_groups[card.suit].add(card.number)
        
        for suit, numbers in suit_groups.items():
            if royalNumbers.issubset(numbers):
                return True
        return False
    
    def hasStraightFlush(self):
        suit_groups = {}
        for card in self.hand:
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

    def hasFourOfAKind(self):
        number_groups = {}
        for card in self.hand:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 4:
                return True
        return False

    def hasFullHouse(self):
        number_groups = {}
        for card in self.hand:
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

    def hasFlush(self):
        suit_groups = {}
        for card in self.hand:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = 0
            suit_groups[card.suit] += 1
        
        for count in suit_groups.values():
            if count >= 5:
                return True
        return False

    def hasStraight(self):
        numbers = set(card.number for card in self.hand)
        if 14 in numbers:
            numbers.add(1)

        sorted_numbers = sorted(numbers)
        for i in range(len(sorted_numbers) - 4):
            if sorted_numbers[i + 4] - sorted_numbers[i] == 4:
                return True

        return False

    def hasThreeOfAKind(self):
        number_groups = {}
        for card in self.hand:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 3:
                return True
        return False

    def hasTwoPair(self):
        number_groups = {}
        for card in self.hand:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        pair_count = 0
        
        for count in number_groups.values():
            if count == 2:
                pair_count += 1
        
        return pair_count == 2

    def hasOnePair(self):
        number_groups = {}
        for card in self.hand:
            if card.number not in number_groups:
                number_groups[card.number] = 0
            number_groups[card.number] += 1
        
        for count in number_groups.values():
            if count == 2:
                return True
        return False

    def hasHighCard(self):
        return True # If no other hand is found, it is a high card hand.

    def getHandType(self):
        if self.hasRoyalFlush():
            return "Royal Flush"
        elif self.hasStraightFlush():
            return "Straight Flush"
        elif self.hasFourOfAKind():
            return "Four of a Kind"
        elif self.hasFullHouse():
            return "Full House"
        elif self.hasFlush():
            return "Flush"
        elif self.hasStraight():
            return "Straight"
        elif self.hasThreeOfAKind():
            return "Three of a Kind"
        elif self.hasTwoPair():
            return "Two Pair"
        elif self.hasOnePair():
            return "One Pair"
        else:
            return "High Card"
        
    def compareHands(self, other_hand):
        # Define hand ranks
        hand_types = {
            "Royal Flush": 10,
            "Straight Flush": 9,
            "Four of a Kind": 8,
            "Full House": 7,
            "Flush": 6,
            "Straight": 5,
            "Three of a Kind": 4,
            "Two Pair": 3,
            "One Pair": 2,
            "High Card": 1
        }

        # Get the hand types of both players
        self_hand_type = self.getHandType()
        other_hand_type = other_hand.getHandType()

        # Compare the hand types
        if hand_types[self_hand_type] > hand_types[other_hand_type]:
            return 1
        elif hand_types[self_hand_type] < hand_types[other_hand_type]:
            return -1

        # If hand types are the same, compare based on specific hand rankings
        if self_hand_type == "Straight" or other_hand_type == "Straight":
            return self.compareStraight(other_hand)

        # If not a straight, compare high cards
        return self.compareHighCards(other_hand)

    def compareStraight(self, other_hand):
        # Helper function to handle Ace as 1 in A-2-3-4-5 straight
        def adjust_for_ace(straight_cards):
            if 14 in straight_cards and 2 in straight_cards:
                straight_cards.remove(14)  # Remove Ace from the list
                straight_cards.add(1)  # Add Ace as 1 for A-2-3-4-5
            return sorted(straight_cards)

        # Get the card numbers of each hand
        self_numbers = set(card.number for card in self.hand)
        other_numbers = set(card.number for card in other_hand.hand)

        # Adjust for Ace in straight
        self_numbers = adjust_for_ace(self_numbers)
        other_numbers = adjust_for_ace(other_numbers)

        # Compare the highest card in the straight
        if max(self_numbers) > max(other_numbers):
            return 1
        elif max(self_numbers) < max(other_numbers):
            return -1
        return 0  # If they have the same high card in the straight

    def compareHighCards(self, other_hand):
        def get_card_value(card):
            # Handle Ace as 1 in case of A-2-3-4-5 straight
            if card.number == 14 and self.hasStraight() and 2 in [c.number for c in self.hand]:
                return 1
            return card.number

        # Sort both hands by card value, descending
        self_sorted = sorted(self.hand, key=get_card_value, reverse=True)
        other_sorted = sorted(other_hand.hand, key=get_card_value, reverse=True)

        # Compare the cards from highest to lowest
        for self_card, other_card in zip(self_sorted, other_sorted):
            if get_card_value(self_card) > get_card_value(other_card):
                return 1
            elif get_card_value(self_card) < get_card_value(other_card):
                return -1
        return 0  # If all cards are the same


    def __str__(self):
        return ', '.join(str(card) for card in self.hand)    
