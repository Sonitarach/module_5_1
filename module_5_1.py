class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        floor_ = 0
        self.new_floor = new_floor

        if self.new_floor > self.numbers_of_floors or self.new_floor < 1:
                print("Такого этажа не существует")
        else:
            for floor_ in range(new_floor):
                print(floor_ + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)