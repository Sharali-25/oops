class  Myclass:
    
    privateVar:32
    def __privateMeth(self):
      print("Im inside of my class Myclass")
    def hello(self):
      print("Private variable value,",Myclass.__privateVar)
foo=Myclass()
foo.hello()
foo.__privateMeth