

class Node():
    def __init__(self, name):
        self.name= name
        self.children = []
        self.tree = ''

    def add_child(self, obj):
        self.children.append(obj)

    def get_tree(self, ancestor):
        # print("Ancestor is: " + ancestor)
        if ancestor != '':
            ancestor += f' > {self.name}'
        else:
            ancestor += self.name
        if len(self.children) == 0:
            print(ancestor)
        for node in self.children:
            # self.tree += f'{self.name} < {node.name}'
            node.get_tree(ancestor)
        # return self.tree



a = Node('A')
b = Node('B')
d = Node('D')
c = Node('C')
goal = Node('Goal')
e = Node('E')

b.add_child(c)
b.add_child(goal)

d.add_child(goal)

goal.add_child(e)

a.add_child(b)
a.add_child(d)
a.add_child(goal)

print(a.get_tree(''))