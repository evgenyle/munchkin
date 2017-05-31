import random

class Deck:
    '''
    класс "Карточная колода"
    '''
        
    def __init__(self, cards):
        self.cards = cards
        self.playing = []#карты в игре
        self.played = []#карты сыгранные
        print("Opening new deck")

    def shuffl(self):
        #перемешать колоду
        print("Shuffling deck")
        return random.shuffle(self.cards)

    def draw(self):
        #тянуть карту
        self.playing.append(self.cards[0])
        print(self.playing)
        return self.cards.pop(0)

    def draw_low(self):
        #тянуть нижнюю
        self.playing.append(self.cards[-1])
        return self.cards.pop(-1)

    def show(self):
        print(self.cards)

    def show_playing(self):
        print(self.playing)

    def show_played(self):
        print(self.played)
        

my_deck = Deck([1, 2, 3, 4, 5])
print(my_deck.cards)
print(my_deck.playing)
print(my_deck.played)

my_deck.shuffl()
my_deck.show()
print(my_deck.draw())
print(my_deck.draw_low())

my_deck.show_playing()
my_deck.show_played()


