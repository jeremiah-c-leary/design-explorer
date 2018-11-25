
from design_explorer import component
from design_explorer import utils


class create(component.create):
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        component.create.__init__(self, name)
        self.hdl_blocks = None

    def add_hdl_block(self, oHdlBlock):
        self.hdl_blocks = utils.append_to_list(self.hdl_blocks, oHdlBlock)

    def create_entity(self):
        lReturn = []
        lReturn.append('entity ' + self.name.upper() + ' is')
        lReturn.append('  port map (')
        for iIndex, oInterface in enumerate(self.interfaces):
            sInterfaceType = self.interface_types[iIndex]
            lReturn.append(extract_interface(oInterface, sInterfaceType))
            lReturn.append('')
        lReturn.append('  )')
        lReturn.append('end entity ' + self.name.upper() + ';')

        return lReturn


def extract_interface(oInterface, sInterfaceType):
    for sLine in oInterface.extract_port_list(sInterfaceType):
        return '    ' + sLine
