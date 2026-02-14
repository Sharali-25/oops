class Dog:
    species="canis lupus"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        print("name",self.name)
        print("age",self.age)
        print("species",Dog.species)
dog1 = Dog("golden retriever",10)
dog2 = Dog("husky",12)
dog1.display_details()
dog2.display_details()