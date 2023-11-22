class Person:
    """Описание класса"""

    birth_year = ''

    def __init__(self, age, male):
        self.age = age
        self.male = male

    def pr(self):
        """информация о человеке"""
        print("человек " + str(self.age) + " лет " + self.male)

    def birthYear(self):
        self.birth_year = 2023 - self.age
        print("год рождения", self.birth_year)


Person1 = Person(18, "мужчина")
Person1.pr()
Person1.birthYear()


Person2 = Person(20, "женщина")
Person2.pr()
Person2.birthYear()


class Child(Person):

    def __init__(self, age, male, color):
        super().__init__(age,male)
        self.color = color

    def GetColor(self):
        return self.color


Child1 = Child(20, "женщина2", "red")
Child1.pr()
print("color: " + Child1.GetColor())