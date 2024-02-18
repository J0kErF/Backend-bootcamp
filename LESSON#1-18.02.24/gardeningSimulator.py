class plant:
    sunlight = True
    waterAmount = 0
    wind = False
    snow = 0

    def __init__(self, waterAmount, sunlight, wind,snow):
        self.waterAmount = waterAmount
        self.sunlight = sunlight
        self.wind = wind
        self.snow = snow
    
plant1 = plant(5, True, False,12)
plant2 = plant(3, False, True,3)
plant3 = plant(7, True, True,11)
plants= [plant1, plant2, plant3]
#ask for the user to describe the weather today - sun or clouds, precipitation number, and wind or not.

sunlight = input('Is it sunny today? (yes/no): ')
precipitation = int(input('How much precipitation is there today? (0-10): '))
wind = input('Is it windy today? (yes/no): ')
snow = int(input('How much snow is there today? (0-10): '))

#for each condition - print what plant likes this condition.
for i in range(len(plants)):
    if plants[i].sunlight == True and sunlight == 'yes':
        print('Plant', i+1, 'likes the sunlight')
    
for i in range(len(plants)):
    if plants[i].waterAmount >= precipitation:
        print('Plant', i+1, 'likes the precipitation')
for i in range(len(plants)):
    if plants[i].wind == True and wind == 'yes':
        print('Plant', i+1, 'likes the wind')
for i in range(len(plants)):
    if plants[i].snow >= snow:
        print('Plant', i+1, 'is dead because of the snow')
