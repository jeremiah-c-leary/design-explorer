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
        return oItem

    def add_connection(self, oConnection):
        self.connections = utils.append_to_list(self.connections, oConnection)

    def get_component_named(self, sString):
        for oComponent in self.components:
            if oComponent.instanceName == sString:
                return oComponent
        raise ValueError('Component named ' + sString + ' could not be found in system ' + self.name)
