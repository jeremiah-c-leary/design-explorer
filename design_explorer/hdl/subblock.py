
from design_explorer import utils


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, instance_name):
        self.interfaces = None
        self.interface_types = None
        self.instance_name = instance_name

    def _add_interface(self, oInterface, sInterfaceType):
        self.interfaces = utils.append_to_list(self.interfaces, oInterface)
        self.interface_types = utils.append_to_list(self.interface_types, sInterfaceType)

    def add_source_interface(self, oInterface):
        self._add_interface(oInterface, 'Source')

    def add_sink_interface(self, oInterface):
        self._add_interface(oInterface, 'Sink')

    def _extract_interface(self, oInterface, sInterfaceType):
        for sLine in oInterface.extract_port_list(sInterfaceType):
            return '    ' + sLine

    def create_entity(self):
        lReturn = []
        lReturn.append('entity ' + self.instance_name.upper() + ' is')
        lReturn.append('  port map (')
        for iIndex, oInterface in enumerate(self.interfaces):
            lReturn.append(self._extract_interface(oInterface, self.interface_types[iIndex]))
            lReturn.append('')
        lReturn.append('  )')
        lReturn.append('end entity ' + self.instance_name.upper() + ';')

        return lReturn
