class Parent(object):
    def implicit(self):
        print("Parent implicit()")
    def altered(self):
        print("Parent altered()")
    def override(self):
        print("Parent override()")

class Child(Parent):
    def altered(self):
        print("Child before Parent altered()")
        super(Child, self).altered()
        print("Child after Parent altered()")
    def override(self):
        print("Child override()")

dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.altered()
child.altered()

dad.override()
child.override()