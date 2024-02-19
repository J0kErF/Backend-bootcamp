import random


materilas = ["carbonite", "durasteel", "quadranium"]#, "adamantium", "cortosis", "phrik", "beskar", "orichalc", "neuranium", "electrum", "alusteel", "duralloy", "ceramic", "plasteel", "transparisteel", "laminasteel", "transparasteel", "agrocite", "agrinium", "anbar"]

class delegation:
    def __init__(self, name, suggestions):
        self.name = name
        self.materials = [random.choice(materilas) for i in range(random.randint(2,3))]
        self.suggestions = suggestions

delegations = [delegation('delegation1',12), delegation('delegation2',7), delegation('delegation3',5), delegation('delegation4',4)]

# to maximize the successful convinced percentage we have to choose the delegation with the least amount of suggestions and the most amount of materials


wantedMaterials = {}
for i in range(len(delegations)):
    for material in delegations[i].materials:
        if wantedMaterials==None or material not in wantedMaterials.keys():
            wantedMaterials[material]=1
for i in wantedMaterials:
    print(i, wantedMaterials[i])

delegations.sort(key=lambda x: x.suggestions)

percentage=0
for d in delegations:
    for m in d.materials:
        if m in wantedMaterials.keys() and wantedMaterials[m]>0:
            wantedMaterials[m]-=1
            percentage+=1
            print(d.name, 'convinced with', m, 'material')
            break
print('the percentage of convinced delegations is', percentage/len(delegations)*100, '%')

