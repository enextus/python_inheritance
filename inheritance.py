class Base:
    def __init__(self):
        self.__x = 4
        self.y = 2

    def display(self):
        print(self.__x, self.y)


class Child(Base):
    def __init__(self):
        super().__init__()
        self.__x = 5
        self.y = 9

    def display_two(self):
        print(self.__x, self.y)


if __name__ == "__main__":
    print("File one executed when imported")
    obj = Child()
    obj.display()
    obj.display_two()
