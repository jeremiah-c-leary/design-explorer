from design_explorer import utils
from design_explorer import port


class create():
    '''
    Creates an interface.
    An interface can exist on multiple parts.

    Source = Master drives
    Sink = Slave consumes
    '''

    def __init__(self, name):
        self.name = name
        self.ports = None
        self.source = False
        self.parent = None
        self.path = None

    def add_port(self, oPort):
        self.ports = utils.append_to_list(self.ports, oPort)

    def create_port(self, name, width=None, source='in', description=None):
        oPort = port.create(name, width, source, description)
        self.add_port(oPort)
        return oPort

    def get_number_ports(self):

        try:
            iNumberPorts = 0
            for oPort in self.ports:
                iNumberPorts += oPort.width
        except TypeError:
            iNumberPorts = 0

        return iNumberPorts
