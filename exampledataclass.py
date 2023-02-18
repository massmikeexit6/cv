from dataclasses import dataclass, field


@dataclass(order=True , frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False) # repr=False so sort_index doesn't show on line 25
    name: str
    job: str
    age: int
    strength: int=100
    def __post_init__(self):
        #self.sort_index = self.strength
        object.__setattr__(self, 'sort_index', self.strength)
    def __str__(self):
        return f'{self.name}, {self.job}, ({self.age})'

    # def __init__(self, name, job, age):
    #     self.name = name
    #     self.job = job
    #     self.age = age


person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(id(person2))
print(id(person3))
print(person1)

print(person1> person2)

'''
With dataclass you see the data and line 24(print(person3 == person2)) is True


#'Projects\\pythonProject\\WEb Developement\\HTML Personal Site\\exampledataclass.py' 
2393356132048
2393364812496
Person(name='Geralt', job='Witcher', age=30)
True

without dataclass you need to add the __init__ and self.info in the the class description and line 24 will be false line
 21 will print that person1 is an object instead of seeing the data. 
 2136508448208
2136508448272
<__main__.Person object at 0x000001F171D3BD10>
False

 
'''
