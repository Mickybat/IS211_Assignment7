import random


def throw_die(sides=6):
#Commented out random.seed(0), so game plays regurlaly, but used it for testing.
    #random.seed(0)
    return random.randint(1, sides)


def number_players():
    num_players = 0

    while num_players <= 1:
        try:
            num_players = int(input("How many players want to play?"))
            if num_players <= 1:
                print("Number of players must be more than 1 ")
        except ValueError:
            print("Please enter a number greater than 1")

    return num_players

class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def play(self):
        """Represents a player's turn"""
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h':
            die = throw_die()
            print(self.name + " Rolled a " + str(die))
            if die == 1:
                break
            turn_total += die
            print(
                f"{self.name} Turn Total = {turn_total}, "
                f"{self.name} Total = {self.total}, "
                f"Possible {self.name} Total = {self.total + turn_total}"
            )
            # Noticed that the code was making me input 'h' on the next player's turn, so it can show a winner
            #so, I automated an 'h' input after turn_total reaches 100
            if self.total + turn_total >= 100:
                roll_hold = "h"
                break

            roll_hold = input("Roll(r) or Hold(h)?").lower()

        if roll_hold == 'h':
            self.total += turn_total

        print(f"{self.name} Total = {self.total}")


class Game:
    def __init__(self, players):
        self.players = players
        self.winner = None

    def check_winner(self):

        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

    def play_game(self):
        currentPlayerPosition = 0
        current_player = self.players[currentPlayerPosition]

        while not self.check_winner():

            current_player.play()

            if currentPlayerPosition == len(self.players) - 1:
                currentPlayerPosition = 0
                current_player = self.players[currentPlayerPosition]
            else:
                currentPlayerPosition = currentPlayerPosition + 1
                current_player = self.players[currentPlayerPosition]

        print(self.winner.name + " wins")


if __name__ == "__main__":
    playersCount = number_players()
    players = []

    for count in range(1, playersCount + 1):
        players.append(Player("P" + str(count)))

    pig_game = Game(players)
    pig_game.play_game()

