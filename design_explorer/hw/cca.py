from design_explorer import system

def create(name):

    return cca(name)


class cca(system.create):
    '''
    Creates a CCA object with a given instance name.
    '''

    def __init__(self, name):
        system.create.__init__(self, name)
