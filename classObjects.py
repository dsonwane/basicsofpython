class Dog:
    val = "mammal"
    animal = "dog"

    def demo(self):
        print("I'm a", self.val)
        print("I'm a", self.animal)

obj = Dog()

print(obj.val)
obj.demo()