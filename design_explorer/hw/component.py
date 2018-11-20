
from design_explorer import utils


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.interfaces = None
        self.interface_types = None

    def _add_interface(self, oInterface, sInterfaceType):
        self.interfaces = utils.append_to_list(self.interfaces, oInterface)
        self.interface_types = utils.append_to_list(self.interface_types, sInterfaceType)

    def add_source_interface(self, oInterface):
        self._add_interface(oInterface, 'Source')

    def add_sink_interface(self, oInterface):
        self._add_interface(oInterface, 'Sink')
