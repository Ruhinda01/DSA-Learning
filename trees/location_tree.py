#!/usr/bin/python3

class LocationTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        # sets the parent of the child to self(the parent)
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, level):
        if self.get_level() > level:
            return
        tabs = ' ' * self.get_level() * 3
        prefix = tabs + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = LocationTree('Global')

    india = LocationTree('India')
    ind_city = LocationTree('Gujarat')
    ind_city.add_child(LocationTree('Ahmedabad'))
    ind_city.add_child(LocationTree('Baroda'))
    ind_town = LocationTree('Karnataka')
    ind_town.add_child(LocationTree('Bengaluru'))
    ind_town.add_child(LocationTree('Mysore'))    
    india.add_child(ind_city)
    india.add_child(ind_town)

    usa = LocationTree('USA')
    east = LocationTree('New Jersey')
    east.add_child(LocationTree('Princeton'))
    east.add_child(LocationTree('Trenton'))
    west = LocationTree('California')
    west.add_child(LocationTree('San Francisco'))
    west.add_child(LocationTree('Mountain View'))
    west.add_child(LocationTree('Palo Alto'))
    usa.add_child(east)
    usa.add_child(west)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(4)
