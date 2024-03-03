class Robot:
    def __init__(self,name,id,battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type

class Pet(Robot):
    def __init__(self,main_material,price,cost_to_fix_per_day,name,id,battery_type,animal_type):
        super().__init__(name,id,battery_type)
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.animal_type = animal_type

class Employee(Robot):
    def __init__(self,daily_salary,name,id,battery_type):
        super().__init__(name,id,battery_type)
        self.daily_salary = daily_salary


class Store:
    def __init__(self,employees=[],pets={},balance=0):
        self.employees = employees
        self.pets = pets
        self.balance = balance
    
    def add_employee(self,employee):
        ### is there a way to make sure that the employee is realy an employee? same for other initiliazations
        if employee not in self.employees:
            self.employees.append(employee)
            print("Employee",employee.name,"added successfully")
        else:
            print("Employee already exists")
    def remove_employee(self,employee):
        ### good input handleing! same for all below
        if employee in self.employees:
            self.employees.remove(employee)
            print("Employee",employee.name,"removed successfully")
        else:
            print("Employee does not exist")
    
    def add_pet(self,pet,status):
        if status not in self.pets:
            self.pets[status] = []
        if pet not in self.pets[status]:
            self.pets[status].append(pet)
            print("Pet",pet.name,"added successfully")
        else:
            print("Pet already exists")

    def remove_pet(self,pet,status):
        if status in self.pets and pet in self.pets[status]:
            self.pets[status].remove(pet)
            print("Pet",pet.name,"removed successfully")
        else:
            print("Pet does not exist")
    def find_pet_status(self,pet):
        for status in self.pets:
            if pet in self.pets[status]:
                return status
        return "Pet does not exist"
    def update_pet_status(self,pet,status):
        old_status = self.find_pet_status(pet)
        if old_status == "Pet does not exist":
            print("Pet does not exist")
        elif old_status == status:
            print("Pet already has the same status")
        else:
            self.pets[old_status].remove(pet)
            self.add_pet(pet,status)
            print("Pet status updated successfully")
    def sell_pet(self,pet):
        status = self.find_pet_status(pet)
        if status == "Pet does not exist":
            print("Pet does not exist")
        elif status == "sold":
            print("Pet already sold")
        else:
            self.update_pet_status(pet,"sold")
            self.balance += pet.price
            print("Pet sold successfully")
    def fix_pet(self,pet):
        status = self.find_pet_status(pet)
        if status == "Pet does not exist":
            print("Pet does not exist")
        elif status == "sold":
            print("Pet already sold")
        elif status == "repair":
            print("Pet already being fixed")
        elif status == "broken":
            if len(self.pets["repair"])>len(self.employees):
                print("Not enough employees to fix pet")
            else:
                self.update_pet_status(pet,"repair")
                print("Pet sent for repair")
    def day_gone(self):
        for pet in self.pets["repair"]:
            self.balance -= pet.cost_to_fix_per_day
            self.update_pet_status(pet,"for sale")
        for employee in self.employees:
            self.balance -= employee.daily_salary
        self.pets["repair"] = []
        print("Day gone")

    def __str__(self):
        return "Store with "+str(len(self.employees))+" employees and "+str(len(self.pets["for_sale"])+len(self.pets["sold"])+len(self.pets["repair"]))+" pets"

    def print_all_in_repair(self):
        for pet in self.pets["repair"]:
            print(pet.name)
    def print_all_employees_salary(self):
        for employee in self.employees:
            print(employee.name,employee.daily_salary)
    def print_balance(self):
        print(self.balance)
    def print_employee_id(self,id):
        for employee in self.employees:
            if employee.id == id:
                print(employee.id,employee.name,employee.battery_type,employee.daily_salary)
                return
    def print_pet_id(self,id):
        for status in self.pets:
            for pet in self.pets[status]:
                if pet.id == id:
                    print(pet.id,pet.name,pet.battery_type,pet.price,pet.cost_to_fix_per_day,pet.animal_type)
                    return
    def print_sale_pets_in_range(self,low,high):
        for pet in self.pets["for sale"]:
            if(pet.price>=low and pet.price<=high):
                print(pet.name,pet.price)

# Create a store
store = Store()

### dry + hardcoding. please make dynamic

# Create employees
employee1 = Employee(100,"John",1,"AA")
employee2 = Employee(200,"Mike",2,"BB")
employee3 = Employee(300,"Alice",3,"CC")

# Add employees to the store
store.add_employee(employee1)
store.add_employee(employee2)
store.add_employee(employee3)

# Create pets
pet1 = Pet("metal",100,10,"dog",1,"AA","dog")
pet2 = Pet("plastic",200,20,"cat",2,"BB","cat")
pet3 = Pet("wood",300,30,"parrot",3,"CC","bird")
pet4 = Pet("metal",400,40,"hamster",4,"DD","hamster")
pet5 = Pet("plastic",500,50,"rabbit",5,"EE","rabbit")

# Add pets to the store
store.add_pet(pet1,"repair")
store.add_pet(pet2,"for sale")
store.add_pet(pet3,"broken")
store.add_pet(pet4,"sold")
store.add_pet(pet5,"broken")

# Print all pets in repair
store.print_all_in_repair()

# Print all employees salary
store.print_all_employees_salary()

# Print balance
store.print_balance()

# Print employee with id 2
store.print_employee_id(2)

# Day gone
store.day_gone()

# Print balance
store.print_balance()
