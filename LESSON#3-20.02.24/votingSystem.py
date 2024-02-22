class Voter:
    def __init__(self, name, age,addr):
        self.name = name
        self.age = age
        self.addr = addr
        self.votes = {}
    def vote(self, candidate, position):
        if position in candidate.positions:
            if position not in self.votes:
                candidate.addVote(position)
                self.votes[position] = candidate

class Candidate:
    def __init__(self, name, positions={}):

        self.name = name
        self.positions = positions

    #this function allows us to know the number of votes this candidate has for a specific position fastly
    def addVote(self,position):
        if position in self.positions:
            self.positions[position] += 1
        else:
            self.positions[position] = 1
id=0

class Vote:
    def __init__(self, candidate, position):
        id+=1
        self.candidate = candidate
        self.position = position

position1 = "president"
position2 = "vice-president"
position3 = "secretary"

c1 = Candidate("John", {position1: 0, position2: 0, position3: 0})
c2 = Candidate("James", { position2: 0, position3: 0})
c3 = Candidate("Jill", {position1: 0, position2: 0})
c4 = Candidate("Jack", {position1: 0, position3: 0})

v1 = Voter("Voter1", 20, "address1")
v2 = Voter("Voter2", 20, "address2")
v3 = Voter("Voter3", 20, "address3")
v4 = Voter("Voter4", 20, "address4")
v5 = Voter("Voter5", 20, "address5")

v1.vote(c1, position1)
v1.vote(c2, position2)
v1.vote(c3, position3)

v2.vote(c2, position2)
v2.vote(c4, position3)
v2.vote(c3, position1)

v3.vote(c1, position1)
v3.vote(c2, position2)
v3.vote(c3, position3)

v4.vote(c1, position1)
v4.vote(c2, position2)
v4.vote(c3, position3)

v5.vote(c1, position1)
v5.vote(c2, position2)
v5.vote(c3, position3)

print(c1.name,c1.positions)
print(c2.name,c2.positions)
print(c3.name,c3.positions)
print(c4.name,c4.positions)

voters=[v1,v2,v3,v4,v5]
for voter in voters:
    print(voter.name)
    for position in voter.votes:
        print(position, voter.votes[position].name)
print(id)
