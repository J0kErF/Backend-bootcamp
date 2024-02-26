class Item:
    def __init__(self, ID, weight):
        self.ID = "Item"+ID
        self.weight = weight
    def __str__(self) -> str:
        return self.ID + " " + str(self.weight)
class Brand(Item):
    def __init__(self, ID, weight, brand):
        super().__init__("Brand"+ID, weight)
        self.brand = brand
    def __str__(self) -> str:
        return super().__str__() + " " + self.brand

class Laptop(Brand):
    def __init__(self, ID, weight, brand,processor, ram, storage,graphics):
        super().__init__("Laptop"+ID, weight, brand)
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics
    def __str__(self) -> str:
        return super().__str__() + " " + self.processor + " " + self.ram + " " + self.storage + " " + self.graphics

class Smartphone(Brand):
    def __init__(self, ID, weight, brand, operating_system,storage,display,camera,materials):
        super().__init__("Smartphone"+ID, weight, brand)
        self.operating_system = operating_system
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials
    def __str__(self) -> str:
        mat=""
        for i in self.materials:
            mat+=i+" "
        return super().__str__() + " " + self.operating_system + " " + self.storage + " " + self.display + " " + self.camera + " " + mat

class Campus(Brand):
    def __init__(self, ID, weight, brand,accuracy,materials,price):
        super().__init__("Campus"+ID, weight, brand)
        self.accuracy = accuracy
        self.materials = materials
        self.price = price
    def __str__(self) -> str:
        mat=""
        for i in self.materials:
            mat+=i+" "
        return super().__str__() + " " + self.accuracy + " " + mat + " " + str(self.price)
class Smartwatch(Brand):
    def __init__(self, ID, weight, brand,display,battery_life,fittness_features,connectivity):
        super().__init__("Smartwatch"+ID, weight, brand)
        self.display = display
        self.battery_life = battery_life
        self.fittness_features = fittness_features
        self.connectivity = connectivity
    def __str__(self) -> str:
        return super().__str__() + " " + self.display + " " + self.battery_life + " " + self.fittness_features + " " + self.connectivity

class Sneakers(Brand):
    def __init__(self, ID, weight, brand,new,bought_from):
        super().__init__("Sneakers"+ID, weight, brand)
        self.new = new
        self.bought_from = bought_from
    def __str__(self) -> str:
        return super().__str__() + " " + str(self.new) + " " + self.bought_from

class Sunglasses(Item):
    def __init__(self, ID, weight, have_case,color,origin):
        super().__init__("Sunglasses"+ID, weight)
        self.have_case = have_case
        self.color = color
        self.origin = origin
    def __str__(self) -> str:
        return super().__str__() + " " + str(self.have_case) + " " + self.color + " " + self.origin

class Passport(Item):
    def __init__(self, ID, weight,color,cost,bought_from):
        super().__init__("Passport"+ID, weight)
        self.color = color
        self.cost = cost
        self.bought_from = bought_from
    def __str__(self) -> str:
        return super().__str__() + " " + self.color + " " + str(self.cost) + " " + self.bought_from

class UniversalCharger(Brand):
    def __init__(self, ID,brand, weight,color,price,size):
        super().__init__("UniversalCharger"+ID, weight, brand)
        self.color = color
        self.price = price
        self.size = size
    def __str__(self) -> str:
        return super().__str__()+" "+self.color+" "+str(self.price)+" "+str(self.size)
# foreach type of Item I have created a separate class.

class bag():
    id=0
    def __init__(self, max_weight,max_items,items = []):
        self.max_weight = max_weight
        self.max_items = max_items
        self.items = items
        self.current_weight = 0
        self.current_items = 0
    def add_item(self, item):
        if self.current_weight + item.weight <= self.max_weight and self.current_items < self.max_items:
            self.items.append(item)
            self.current_weight += item.weight
            self.current_items += 1
            self.id+=1
        else:
            print("Bag is full")
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.current_weight -= item.weight
            self.current_items -= 1
        else:
            print("Item not in the bag")
    def print_items(self):
        for item in self.items:
            print(item)
    def print_by_category(self):
        self.items.sort(key=lambda x: x.ID)
        for item in self.items:
            print(item)
    def print_category(self, category):
        for item in self.items:
            if isinstance(item, category):
                print(item)

sp1=Smartphone("1", 0, "Apple", "IOS", "128 GB", "AMOLED", "Dual Lens", ["lithium", "plastic"])

lp1=Laptop("1", 60, "Dell", "Intel i7", "16 GB", "512 GB SSD", "NVIDIA GeForce4")

c1=Campus("1", 4, "Samsung", "High", ["iron","plastic"], 50)


sw1=Smartwatch("1", 44, "Samsung", "Touchscreen", "3 days", "Heart Rate Monitor", "Bluetooth")

sn1=Sneakers("1", 14, "New Balance", False, "Spain")

sg1=Sunglasses("1", 10, True, "Black", "Italy")

p1=Passport("1", 1, "Blue", 50, "USA")

uc1=UniversalCharger("1", "Lenovo", 12, "Black", 50, "Medium")

b1=bag(80, 6)

b1.add_item(sp1)
b1.add_item(lp1)
b1.add_item(c1)
b1.add_item(sw1)
b1.add_item(sn1)
b1.add_item(sg1)
b1.add_item(p1)

b1.print_items()
