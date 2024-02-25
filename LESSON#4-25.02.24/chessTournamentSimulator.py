import random

class Player:
    def __init__(self, name):
        self.name = name
        self.rating = random.randint(1500, 2000)
        self.orgRate=self.rating
        self.points = 0

class Round:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        player1winRatio = 0.4
        player1loseRatio = 0.4
        player1drawRatio = 0.2
        ratio = abs((self.player1.rating / self.player2.rating) -1)
        if self.player1.rating > self.player2.rating:
            player1winRatio=0.4+ratio
            player1loseRatio=0.4-ratio
        else:
            player1winRatio=0.4-ratio
            player1loseRatio=0.4+ratio
        result = random.choices(['win', 'lose', 'draw'], [player1winRatio, player1loseRatio, player1drawRatio])[0]
        print("result:",result)
        if result == 'win':
            self.player1.points += 1
        elif result == 'lose':
            self.player2.points += 1
        else:
            self.player1.points += 0.5
            self.player2.points += 0.5
        self.updateRating(result)
    def updateRating(self, result):
        k = 32
        expectedScore = 1 / (1 + 10 ** ((self.player2.rating - self.player1.rating) / 400))
        if result == 'win':
            self.player1.rating += k * (1 - expectedScore)
            self.player2.rating += k * (0 - expectedScore)
        elif result == 'lose':
            self.player1.rating += k * (0 - expectedScore)
            self.player2.rating += k * (1 - expectedScore)
class Tournament:
    def __init__(self, players):
        self.players = players
        self.rounds = []
    # I make it constant because I know that there will be 4 players in the tournament, I can make it more dynamic by adding a function to calculate the roundsIndex   
    roundsIndex=[[[0,1],[2,3]],[[0,2],[1,3]],[[0,3],[1,2]]]

    def playRound(self):
        for roundIndex in self.roundsIndex:
            print("playing round:",roundIndex)
            round = Round(self.players[roundIndex[0][0]], self.players[roundIndex[0][1]])
            round.play()
            print("round played between:",round.player1.name,"and",round.player2.name,"result:",round.player1.points,round.player2.points)
            self.rounds.append(round)
            round = Round(self.players[roundIndex[1][0]], self.players[roundIndex[1][1]])
            round.play()
            print("round played between:",round.player1.name,"and",round.player2.name,"result:",round.player1.points,round.player2.points)
            self.rounds.append(round)
            print("round",roundIndex,"played")

    def printResults(self):
        players=sorted(self.players, key=lambda x: x.points)
        print('Results:')
        for player in players:
            print(f'{player.name} - {player.points} points')

    def printRatings(self):
        players=sorted(self.players, key=lambda x: abs(x.rating- x.orgRate))
        print('Ratings:')
        for player in players:
            print(f'{player.name} - {player.rating}- {player.orgRate} points, change: {player.rating- player.orgRate} points')


players = [Player('Player1'), Player('Player2'), Player('Player3'), Player('Player4')]
tournament = Tournament(players)
tournament.playRound()
tournament.printResults()
tournament.printRatings()
