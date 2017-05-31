class Hand:
    def __init__(self, stack = None):
        self.stack = stack
        if self.stack == None:
            self.stack = []
        
    def play_card(self, card):
        return self.stack.pop(card)

    def __repr__(self):
        return str(self.stack)

my_cards = [5, 8, 3]
my_hand = Hand(my_cards)
print(my_hand.stack)

playing = my_hand.play_card(1)
print(playing)
print(my_hand.stack)
print(my_hand)
    
