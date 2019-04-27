
from design_explorer import utils
from design_explorer import interface


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.interfaces = None
        self.datasheet = None

    def add_interface(self, oInterface):
        oInterface.parent = self
        self.interfaces = utils.append_to_list(self.interfaces, oInterface)

    def create_interface(self, name):
        oInterface = interface.create(name)
        self.add_interface(oInterface)
        return oInterface

    def get_interface_named(self, sInterfaceName):
        for oInterface in self.interfaces:
            if sInterfaceName == oInterface.name:
                return oInterface
        raise ValueError('Interface named ' + sInterfaceName + ' could not be found on component ' + self.name)
        return None
