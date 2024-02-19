import random

types = {
    "fire": ["water", "wind"],
    "water": ["earth"],
    "earth": ["fire", "wind"],
    "wind": ["water"],
}

class pokemon:
    def __init__(self, name,level,strength,speed,type):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.type = type
        self.life = 120

class player:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons


p1= player('player1', [pokemon('charmar1', 1, 3, 5, 'water'),pokemon('charmander1', 5, 3, 5, 'fire'), pokemon('squirtle1', 5, 10, 3, 'water'), pokemon('bulbasaur1', 5, 10, 2, 'earth'), pokemon('pidgey1', 5, 10, 5, 'wind')])
p2= player('player2', [pokemon('charmar1', 1, 3, 5, 'water'),pokemon('bulbasaur2', 1, 1, 1, 'earth'), pokemon('pidgey2', 5, 10, 5, 'wind'), pokemon('charmander2', 5, 10, 5, 'fire'), pokemon('squirtle2', 5, 10, 4, 'water')])

# for p1 we have to choose a pokemon randomly

#p1 chooses a pokemon
p1Choice= random.choice(p1.pokemons)
#p2 chooses a pokemon
p2Choice= random.choice(p2.pokemons)

#to determine who will start firs we implement the given equasion
firstplayer = p1 if p1Choice.speed+random.randint(1,20) > p2Choice.speed+random.randint(1,20) else p2
secondplayer = p1 if firstplayer == p2 else p2
if firstplayer == p2:
    p1Choice, p2Choice = p2Choice, p1Choice
while(len(firstplayer.pokemons)>0 and len(secondplayer.pokemons)>0):
    #first player attacks second player
    damage = p1Choice.strength
    if p1Choice.type in types[p2Choice.type]:
        damage+=random.randint(1,20)
    p2Choice.life -= damage
    if p2Choice.life<=0:
        secondplayer.pokemons.remove(p2Choice)
        print(p2Choice.name, 'has fainted.')
        if len(secondplayer.pokemons)==0:
            break
        p2Choice= random.choice(secondplayer.pokemons)
        print(p2Choice.name, 'has joined the fight')

    print(p1Choice.name, 'attacks', p2Choice.name, '. deals', p1Choice.strength, 'damage',p2Choice.name, 'now has', p2Choice.life, 'amount of life after the attack')

    #second player attacks first player
    damage = p2Choice.strength
    if p2Choice.type in types[p1Choice.type]:
        damage+=random.randint(1,20)
    p1Choice.life -= damage
    if p1Choice.life<=0:
        firstplayer.pokemons.remove(p1Choice)
        print(p1Choice.name, 'has fainted.')
        if len(firstplayer.pokemons)==0:
            break
        p1Choice= random.choice(firstplayer.pokemons)
        print(p1Choice.name, 'has joined the fight') 
    print(p2Choice.name, 'attacks', p1Choice.name, '. deals', p2Choice.strength, 'damage',p1Choice.name, 'now has', p1Choice.life, 'amount of life after the attack')   
#to determine the winner we check who has pokemons alive
winnerName = p1.name if len(p1.pokemons)>0 else p2.name
loserName = p1.name if winnerName == p2.name else p2.name
print('The winner is:', winnerName,'\nThe loser is:', loserName)



