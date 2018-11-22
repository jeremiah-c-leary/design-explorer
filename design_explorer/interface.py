from design_explorer import utils


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.description = None
        self.ports = None
        self.port_types = None

    def _add_port(self, oPort, sPortType):
        self.ports = utils.append_to_list(self.ports, oPort)
        self.port_types = utils.append_to_list(self.port_types, sPortType)

    def add_source_port(self, oPort):
        self._add_port(oPort, 'Source')

    def add_sink_port(self, oPort):
        self._add_port(oPort, 'Sink')

    def extract_port_list(self, interface_type):
        lReturn = []
        lReturn.append('-- [I:' + self.name + ']')
        try:
            for iIndex, oPort in enumerate(self.ports):
                sPortType = self.port_types[iIndex]
                lReturn.append(extract_port(oPort, interface_type, sPortType))

        except TypeError:
            pass

        return lReturn


def extract_port(oPort, sInterface_type, sPortType):
    # Define source and sink port mapping
    dPortMap = {}
    dPortMap['Source'] = {}
    dPortMap['Source']['Source'] = 'out'
    dPortMap['Source']['Sink'] = 'in'
    dPortMap['Sink'] = {}
    dPortMap['Sink']['Source'] = 'in'
    dPortMap['Sink']['Sink'] = 'out'

    return oPort.name + ' : ' + dPortMap[sInterface_type][sPortType]
