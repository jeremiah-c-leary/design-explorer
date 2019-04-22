from design_explorer import utils


class create():
    '''
    Creates a system object with a given instance name.
    This is the base object of design explorer.

    A system can contain other systems by using the add_components method. 
    '''

    def __init__(self, name):
        self.name = name
        self.components = None
        self.connections = None

    def add_component(self, oItem):
        self.components = utils.append_to_list(self.components, oItem)

    def add_connection(self, oConnection):
        self.connections = utils.append_to_list(self.connections, oConnection)

