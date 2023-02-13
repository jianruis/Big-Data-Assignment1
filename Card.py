import random
# Rank dictionary, used to compare the rank of cards
rank_dict={'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'X':10, 'J':11, 'Q':12, 'K':13}
class Card:
    """
    Card class, used to represent a card.
    The suit of the card can be 'S', 'H', 'D', 'C', which means Spade, Heart, Diamond and Club.
    The rank of the card can be 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K',
    which means Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
    The used flag is used to indicate whether the card has been used.
    """
    def __init__(self, suit, rank):
        """
        Constructor, init the suit and rank of the card, and set the used flag to False
        """
        self.suit = suit
        self.rank = rank
        self.used = False
    def __str__(self):
        """
        method to print the card
        """
        return self.suit + self.rank
    
    # Override the __repr__ method, so that we can print the card directly
    def __repr__(self):
        return self.suit + self.rank
    # Override the __gt__ method, so that we can compare the rank of two cards
    def __gt__(self, other):
        if(self.rank == other.rank):
            # If the rank of two cards are the same, compare the suit
            return self.suit > other.suit
        else:
            return rank_dict[self.rank] > rank_dict[other.rank]
    
    def __lt__(self, other):
        if(self.rank == other.rank):
            # If the rank of two cards are the same, compare the suit
            return self.suit < other.suit
        else:
            return rank_dict[self.rank] < rank_dict[other.rank]
class Player:
    """
    Player class, used to represent a player.
    The cards attribute is a list of cards that the player has.
    The name attribute is the name of the player.
    The score attribute is the score of the player.
    """

    def __init__(self, cards, name):
        """
        Constructor, init the cards, name and score of the player.
        """
        self.cards = cards
        self.name = name
        self.score = 0

class Game:
    """
    Game class, used to represent the game.
    """
    def __init__(self):
        cards=[]
        # Generate 52 cards
        for suit in ['S', 'H', 'D', 'C']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']:
                cards.append(Card(suit, rank))
        # Shuffle the cards, and divide them into 4 players
        random.shuffle(cards)
        self.players = [Player(cards[0:13],'player1'), Player(cards[13:26],'player2'),
                         Player(cards[26:39],'player2'), Player(cards[39:52],'player4')]

    def move(self, player):
        """
        The move method, used to get the card that the player chooses.
        """
        # Get the unused cards of the player
        unused_cards = [card for card in player.cards if not card.used]
        print("Your cards are: %s" % unused_cards)
        while True:
            # Get the card that the player chooses
            choose = input("Choose a card: ")
            for card in unused_cards:
                if(str(card) == choose[0:2]):
                    # If the card is unused, set the used flag to True and return the card
                    card.used = True
                    return card
            else:
                print("You can't choose this card")

    def get_winner(self):
        """
        The get_winner method, used to get the winner of the game.
        """
        # 
        winner = None
        for player in self.players:
            if(winner == None or player.score > winner.score):
                winner = player
        return winner

    def round(self):
        """
        The round method, used to play a round of the game.
        """
        best_card = None
        best_card_player = None
        for player in self.players:
            print("It's %s's turn, now your score is %d." %(player.name, player.score))
            # Get the card that the player chooses
            card=self.move(player)
            # compare the card with the best card of this round
            if(best_card == None or card > best_card):
                best_card = card
                best_card_player = player
        # Print the best card of this round
        print("The best card is %s from %s" %(best_card, best_card_player.name))
        best_card_player.score += 1

    def start(self):
        print("Welcome to the game of 13 cards!")
        print("Each player will get 13 cards, they will be diplayed as 'S2', 'H3' and so on.")
        print("Where S means Spade, H means Heart, D means Diamond and C means Club.")
        print("The rank of cards are: A, 2, 3, 4, 5, 6, 7, 8, 9, X, J, Q, K.")
        print("At each round, you will choose a card to play, the one with the highest rank wins and gets 1 point.")
        print("If there are two cards with the same rank, the one with the highest suit wins.")
        print("The game will start now!")
        for i in range(13):
            print("========================Round %d========================" % (i+1))
            # The best card of this round, and the player who plays the best card
            self.round()
        print("The winner of the is %s" % self.get_winner().name)     

def main():
    # Create a game object and start the game
    game = Game()
    game.start()

if __name__ == '__main__':
    main()