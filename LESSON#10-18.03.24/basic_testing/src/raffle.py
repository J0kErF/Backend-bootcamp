from utils import *
class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.ticket_price = ticket_price
        self.total_earning = 0
        self.people = {}

    def add_person(self,name):
        if len(self.people)>=self.max_people:
            return "FAIL: you have reached the max number of people"
        self.people[name]=0
        return "SUCCESS"
    
    def buy_tickets(self,name,num_tickets):
        if name not in self.people:
            return "FAIL: this person is not participated."
        remaining_tickets= self.max_tickets-sum(self.people.values())
        if num_tickets >remaining_tickets:
            return "FAIL: there is no enough tickets"
        cost = num_tickets*self.ticket_price
        self.people[name]+=num_tickets
        self.total_earning+=cost
        return "SUCCESS"
    
    def select_winner(self):
        return pick_winner(self.people)