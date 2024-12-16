#!/usr/bin/python3

class ManagementTree:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + ' (' + self.designation + ')'
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation
        tabs = ' ' * self.get_level() * 3
        prefix = tabs + '|__' if self.parent else ''
        print(prefix+value)
        # my original solution
        # if property_name == 'name':
        #     print(prefix + self.name)
        # if property_name == 'designation':
        #     print(prefix + self.designation)
        # if property_name == 'both':
        #     print(prefix + self.name + ' ' + '(' + self.designation + ')')
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_management_tree():
    # Builds the management tree
    root = ManagementTree('Nilupul', 'CEO')

    cto = ManagementTree('Chinmay', 'CTO')
    infra_head = ManagementTree('Vishwa', 'Infrastructure Head')
    infra_head.add_child(ManagementTree('Dhaval', 'Cloud Manager'))
    infra_head.add_child(ManagementTree('Abhijit', 'App Manager'))
    app_head = ManagementTree('Aamir', 'Application Head')
    cto.add_child(infra_head)
    cto.add_child(app_head)

    hr_head = ManagementTree('Gels', 'HR Head')
    hr_head.add_child(ManagementTree('Peter', 'Recruitment Manager'))
    hr_head.add_child(ManagementTree('Waqas', 'Policy Manager'))

    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy