class Person:
    name = ''
    count = 0

    def __init__(self, new_name):
        self.name = new_name
        print(self.name, 'has been constructed')

    def increment_count(self):
        self.count = self.count + 1


ebun = Person('Ebunoluwa')
ebun.increment_count()
ebun.increment_count()
ebun.increment_count()
print(ebun.count)

ibk = Person('Ibukun')
ibk.increment_count()
print(ibk.count)
