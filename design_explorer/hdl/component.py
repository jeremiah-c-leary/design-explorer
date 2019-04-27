
from design_explorer import component


class create(component.create):
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        component.create.__init__(self, name)
