import json
from abc import ABC, abstractmethod

class Library(ABC):

    def __init__(self, Time: int, Update: bool, Days: int):
        
        self.Time = Time
        self.Update = Update
        self.Days = Days

    def __repr__(self) -> str:
        return f'<\'{self.__class__.__name__}\' Name: {self.name}, Time: {self.Time}, Update: {self.Update}, Days: {self.Days}>'

    @abstractmethod
    def AverageDay(self):
        return f' Average time in the game {self.Name}: {self.Time / self.Days}'

    @abstractmethod
    def CheckUpdate(self):
        if self.Update:
            return f'{self.Name}- Update required'
        else:
            return f'{self.Name}- Ready to launch'

class CounterStrike(Library):
    def __init__(self, Time: int, Update: bool, Days: int):
        self.name = "CSGO"
        super().__init__(Time, Update, Days)

    def AverageDay(self):
        return super().AverageDay()
    def CheckUpdate(self):
        return super().CheckUpdate()

class GrandTheftAuto5(Library):
    def __init__(self, Time: int, Update: bool, Days: int):
        self.name = "GTA5"
        super().__init__(Time, Update, Days)

    def AverageDay(self):
        return super().AverageDay()
    def CheckUpdate(self):
        return super().CheckUpdate()

class EuropaUniversalis4(Library):
    def __init__(self, Time: int, Update: bool, Days: int):
        self.name = "EU4"
        super().__init__(Time, Update, Days)

    def AverageDay(self):
        return super().AverageDay()
    def CheckUpdate(self):
        return super().CheckUpdate()

class Satisfactory(Library):
    def __init__(self, Time: int, Update: bool, Days: int):
        self.name = "Satis"
        super().__init__(Time, Update, Days)

    def AverageDay(self):
        return super().AverageDay()
    def CheckUpdate(self):
        return super().CheckUpdate()


class EliteDangerous(Library):
    def __init__(self, Time: int, Update: bool, Days: int):
        self.name = "Elite"
        super().__init__(Time, Update, Days)

    def AverageDay(self):
        return super().AverageDay()
    def CheckUpdate(self):
        return super().CheckUpdate()


def output(file_name, company):
    with open(file_name, "w") as the_file:
        the_file.write(company.to_json())   

def imput(file_name):
    with open("the_file.json", "r") as read_file:
        data = json.load(read_file)
    return data

def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))


CSGO = CounterStrike(1141,True,1611)
GTA5 = GrandTheftAuto5(866,False,1265)
EU4 = EuropaUniversalis4(526,False,1181)
Satis = Satisfactory(243,True,440)
Elite = EliteDangerous(80,True,896)

objects = [CSGO, GTA5, EU4, Satis, Elite, ]
data = {
        'library': [],
}
for obj in objects:
    data['library'].append(obj.__dict__)

write(data)
data.clear()
objects.clear()
data = read_from_json()

for obj in data['library']:
    if obj['name'] == "CSGO":
        obj = CounterStrike(obj['Time'], obj['Update'], obj['Days'])
    elif obj['name'] == "GTA5":
        obj = GrandTheftAuto5(obj['Time'], obj['Update'], obj['Days'])
    elif obj['name'] == "EU4":
        obj = EuropaUniversalis4(obj['Time'], obj['Update'], obj['Days'])
    elif obj['name'] == "Satis":
        obj = Satisfactory(obj['Time'], obj['Update'], obj['Days'])
    elif obj['name'] == "Elite":
        obj = EliteDangerous(obj['Time'], obj['Update'], obj['Days'])
    objects.append(obj)

with open(encoding='utf-8', file='Output.txt', mode='w') as file:
    for obj in objects:
        output = obj.__repr__() + "\n"
        file.write(output)
#сдана
