import random
from player import Player
class Game:
    def __init__(self, place_names,weapons,players_number):
        self.place_names = place_names
        self.weapons = weapons
        self.players_number = players_number
        self.players = []
    
    def init_players(self,players_number):
        for i in range(players_number):

            tmp_player = Player("player"+str(i))

            state=self.visit_place(tmp_player)
            if state != "success":
                return state+" in init_players"
            
            state=self.make_favorite_weapons(tmp_player)
            if state != "success":
                return state+" in init_players"
            
            self.players.append(tmp_player)
        state=self.make_assassin()
        if state != "success":
            return state+" in init_players"
        return "success"
    
    def visit_place(self,player):
        if type(player) != Player:
            return "type error: player must be a Player"
        
        for r in range(random.randint(1,3)):
            place = self.place_names[random.randint(0,len(self.place_names)-1)]
            player.add_visited_place(place)

        return "success"
    
    def make_favorite_weapons(self,player):
        if type(player) != Player:
            return "type error: player must be a Player"
        
        for r in range(random.randint(1,3)):
            weapon = self.weapons[random.randint(0,len(self.weapons)-1)]
            player.add_favorite_weapon(weapon)

        return "success"
    
    def make_assassin(self):
        if len(self.players) == 0:
            return "error: no players"
        self.players[random.randint(0,len(self.players)-1)].set_inocent(0)
        return "success"
    
    def commit_murder(self,assassin,weapon):
        if type(assassin) != Player:
            return "type error: assassin must be a Player"
        if assassin.get_inocent==1:
            return "value error: you are innocent"
        if type(weapon) != str:
            return "type error: weapon must be a string"
        if weapon not in assassin.get_favorite_weapons:
            return "value error: you don't have this weapon"
        
        #randomly kill a player this method allows suicide
        self.players.remove(random.randint(self.players_number-1))
        
        self.murder_place=random.choice(assassin.get_visited_places)
        self.murder_weapon=random.choice(assassin.add_favorite_weapon)

        return "success"
        
    def accuse_player(self,player):
        if type(player) !=  Player:
            return "type error: player must be a Player"
        if player not in self.players:
            return "value error: this player is not playing"
        if player == self.round_assassin:
            return "assassin down"
        return "assassin free"
    
    def check_end_game(self):
        if len(self.players)==1 and self.players[0].get_inocent()==0:
            return "END: lose"
        for player in self.players:
            if player.get_inocent()==0:
                return "running..."
        return "END: win"
    
    
        
        