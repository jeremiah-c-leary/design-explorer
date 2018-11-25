
import copy
from design_explorer import utils


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.interfaces = None
        self.interface_types = None

    def _add_interface(self, oInterface, sInterfaceType, sInterfaceName=None):
        if sInterfaceName:
            oInterface.name = sInterfaceName
        self.interfaces = utils.append_to_list(self.interfaces, oInterface)
        self.interface_types = utils.append_to_list(self.interface_types, sInterfaceType)

    def add_source_interface(self, oInterface, sInterfaceName=None):
        self._add_interface(copy.deepcopy(oInterface), 'Source', sInterfaceName)

    def add_sink_interface(self, oInterface, sInterfaceName=None):
        self._add_interface(copy.deepcopy(oInterface), 'Sink', sInterfaceName)

    def get_interface(self, sInterfaceName):
        for oInterface in self.interfaces:
            if sInterfaceName == oInterface.name:
                return oInterface
