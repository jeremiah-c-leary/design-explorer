from design_explorer import utils


class create():
    '''
    Creates an HDL Subsystem object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.components = None
        self.connections = None

    def add_component(self, oComponent):
        self.components = utils.append_to_list(self.components, oComponent)

    def add_connection(self, oConnection):
        self.connections = utils.append_to_list(self.connections, oConnection)

    def extract_node_list(self):
        lReturn = ['Id,Label']
        for iIndex, oComponent in enumerate(self.components):
            lReturn.append(str(iIndex + 1) + ',' + oComponent.name)
        return lReturn
