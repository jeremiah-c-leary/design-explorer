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

    def add_component(self, oComponent):
        self.components = utils.append_to_list(self.components, oComponent)

    def add_connection(self, oConnection):
        self.connections = utils.append_to_list(self.connections, oConnection)

    def extract_node_list(self):
        lReturn = ['Id,Label']
        for oComponent in self.components:
            lReturn.append(oComponent.name + ',' + oComponent.name)
        return lReturn

    def extract_edge_list(self):
        lReturn = ['Source,Target,Type,Kind,Id,Label,timeset,Weight']
        for iIndex, oConnection in enumerate(self.connections):
            lReturn.append(oConnection.source.name + ',' +
                           oConnection.sink.name + ',Directed,,' +
                           str(iIndex) + ',' +
                           oConnection.name + ',,1')
        return lReturn
