class Other(object):
    def implicit(self):
        print("Parent implicit()")
    def altered(self):
        print("Parent altered()")
    def override(self):
        print("Parent override()")

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()
    def altered(self):
        print("Child altered()")
    def override(self):
        print("Child before Other override()")
        self.other.override()
        print("Child after Other override()")

son = Child()

son.implicit()
son.override()
son.altered()