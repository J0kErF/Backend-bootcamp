class Player:
    def __init__(self,name,inocent=1,visitedPlaces=[],favoriteWeapons=[]):
        self.name = name
        self.inocent = inocent
        self.visitedPlaces = visitedPlaces
        self.favoriteWeapons = favoriteWeapons

    def get_visited_places(self):
        return self.visitedPlaces.copy()
    def get_favorite_weapons(self):
        return self.favoriteWeapons.copy()
    def get_inocent(self):
        return self.inocent
    def get_name(self):
        return self.name
    
    def set_visited_places(self,visitedPlaces):
        if type(visitedPlaces) != list:
            return "type error: visitedPlaces must be a list"
        self.visitedPlaces = visitedPlaces
        return "success"
    
    def set_favorite_weapons(self,favoriteWeapons):
        if type(favoriteWeapons) != list:
            return "type error: favoriteWeapons must be a list"
        self.favoriteWeapons = favoriteWeapons
        return "success"
    
    def set_inocent(self,inocent):
        if type(inocent) != int:
            return "type error: inocent must be an integer"
        if inocent < 0 or inocent > 1:
            return "value error: inocent must be 0 or 1"
        self.inocent = inocent
        return "success"
    
    def set_name(self,name):
        if type(name) != str:
            return "type error: name must be a string"
        if len(name) == 0:
            return "value error: name must not be empty"
        self.name = name

    
    def add_visited_place(self,place):
        if type(place) != str:
            return "type error: place must be a string"
        self.visitedPlaces.append(place)
        return "success"
    
    def add_favorite_weapon(self,weapon):
        if type(weapon) != str:
            return "type error: weapon must be a string"
        self.favoriteWeapons.append(weapon)
        return "success"
    
    def remove_visited_place(self,place):
        if type(place) != str:
            return "type error: place must be a string"
        if place not in self.visitedPlaces:
            return "value error: place not in visitedPlaces"
        self.visitedPlaces.remove(place)
        return "success"
    
    def remove_favorite_weapon(self,weapon):
        if type(weapon) != str:
            return "type error: weapon must be a string"
        if weapon not in self.favoriteWeapons:
            return "value error: weapon not in favoriteWeapons"
        self.favoriteWeapons.remove(weapon)
        return "success"
    
    
        