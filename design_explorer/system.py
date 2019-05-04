from design_explorer import utils


class create():
    '''
    Creates a system object with a given instance name.
    This is the base object of design explorer.

    A system can contain other systems by using the add_components method.
    '''

    def __init__(self, name):
        self.name = name
        self.instanceName = name
        self.components = None
        self.connections = None
        self.type = 'system'

    def add_component(self, oItem):
        self.components = utils.append_to_list(self.components, oItem)
        return oItem

    def add_connection(self, oConnection):
        self.connections = utils.append_to_list(self.connections, oConnection)

    def get_component_named(self, sPath, sFullPath=None):
        if sFullPath is None:
            sFullPath = sPath
        lPath = sPath.split('.')
        sComponentName = lPath[0]
        lComponentPath = lPath[1:]
        for oComponent in self.components:
            if oComponent.instanceName == sComponentName:
                if len(lPath) == 1:
                    return oComponent
                else:
                    return oComponent.get_component_named('.'.join(lComponentPath), sFullPath)
        if len(lPath) == 1:
            raise ValueError('Component named ' + sFullPath + ' could not be found in system ' + self.name)
