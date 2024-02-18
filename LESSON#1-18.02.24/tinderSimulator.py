class person:
    def __init__(self, name,gender, age, profession,favoriteTvShow,favoriteFood):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self.favoriteTvShow = favoriteTvShow
        self.favoriteFood = favoriteFood
    def __eq__(self,other):
        count=0
        if abs(self.age - other.age) <= 10:
            count+=1
        if self.profession == other.profession:
            count+=1
        if self.favoriteTvShow == other.favoriteTvShow:
            count+=1
        if self.favoriteFood == other.favoriteFood:
            count+=1
        if count>=2:
            return True
        else:
            return False
        

person1 = person('alex','m', 25, 'engineer','friends','pizza')
person2 = person('bob','m', 30, 'teacher','simpsons','pasta')
person3 = person('marian','f', 35, 'doctor','friends','burger')
person4 = person('jane','f', 40, 'teacher','simpsons','pasta')


people= [person1, person2, person3, person4]
while(True):
    name= input('Enter your name:')
    gender= input('Enter your gender (m/f):')
    age= int(input('Enter your age:'))
    profession= input('Enter your profession:')
    favoriteTvShow= input('Enter your favorite TV show:')
    favoriteFood= input('Enter your favorite food:')

    person0 = person(name,gender, age, profession,favoriteTvShow,favoriteFood)
    matched=0
    for person1 in people:
        if person1 == person0:
            print(person0.name, 'is a match with', person1.name)
            matched=1
            
    if matched==0:
        print(person0.name, 'is not a match with anyone')
    else:
        break
