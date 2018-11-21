from design_explorer import system


class create(system.create):
    '''
    Creates a CCA object with a given instance name.
    '''

    def __init__(self, name):
        system.create.__init__(self, name)
