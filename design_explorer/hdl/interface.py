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

    def _add_port(self, oPort, sPort_type):
        self.ports = utils.append_to_list(self.ports, oPort)
        self.port_types = utils.append_to_list(self.port_types, sPort_type)

    def add_source_port(self, oPort):
        self._add_port(oPort, 'Source')

    def add_sink_port(self, oPort):
        self._add_port(oPort, 'Sink')

    def extract_port_list(self, interface_type):
        lReturn = []
        lReturn.append('--[I:' + self.name + ']')
        try:
            for iIndex, oPort in enumerate(self.ports):
                if interface_type == 'Source':
                    if self.port_types[iIndex] == 'Source':
                        lReturn.append(oPort.name + ' : out')
                    else:
                        lReturn.append(oPort.name + ' : in')
                if interface_type == 'Sink':
                    if self.port_types[iIndex] == 'Source':
                        lReturn.append(oPort.name + ' : in')
                    else:
                        lReturn.append(oPort.name + ' : out')
        except TypeError:
            pass

        return lReturn
