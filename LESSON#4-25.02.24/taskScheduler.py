class Task:
    def __init__(self,id, name,startHour,endHour,day,worker):
        self.id = id
        self.name = name
        self.startHour = startHour
        self.endHour = endHour
        self.day = day
        self.worker = worker

class Worker:
    def __init__(self, name,workingDays,startHour):
        self.name = name
        self.workingDays = workingDays
        self.startHour = startHour
        self.endHour = startHour+8
        self.calendar = [[None for i in range(8)] for j in range(7)]
    def assignTask(self,task):
        #check if the task day is in the working Days 
        #the working days = [0,1,1,1,1,1,0,0] this worker work from moday to thursday each index represent a day in the week
        print("Task:",task.id,"Day:",task.day,"workingDays:",self.workingDays[task.day-1])
        day=task.day-1
        if self.workingDays[task.day-1] ==0:
            print("Task:",task.id,"This is not a working day for you")
            return
        #check if the hours not in the range of the working hours
        if task.endHour< task.startHour or task.startHour < self.startHour or task.endHour>self.endHour:
            print("Task:",task.id,"the choosen hours is not on your working hours")
            return
        #check if the hours are already taken
        for i in range(task.startHour,task.endHour):
            if self.calendar[day][i-self.startHour] is not None:
                print("Task:",task.id,"the choosen hours are already taken")
                return
        #assign the task
        for i in range(task.startHour,task.endHour):
            self.calendar[day][i-self.startHour]=task
            
        task.worker=self
        print("Task:",task.id,"assigned succefuly to",self.name)
    def deassignTask(self,task):
        day=task.day-1
        for i in range(task.startHour,task.endHour):
            self.calendar[day][i-self.startHour]=None
        task.worker=None
        print("Task:",task.id,"deassigned succefuly from",self.name)
    def printCalendar(self):
        for i in range(7):
            print("Day:",i+1)
            for j in range(8):
                print(self.calendar[i][j].name if self.calendar[i][j] is not None else "None")
            print("\n")


worker1=Worker("worker1",[1,1,0,1,1,0,0],8)

tasks=[]

task1 = Task(1,"task1",8,10,1,None) 
task2 = Task(2,"task2",10,14,2,None)
task3 = Task(3,"task3",12,14,3,None)
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

worker1.assignTask(task1)
worker1.assignTask(task2)
worker1.assignTask(task3)

for task in tasks:
    print("Task:",task.id,task.worker.name if task.worker is not None else "None")
worker1.printCalendar()