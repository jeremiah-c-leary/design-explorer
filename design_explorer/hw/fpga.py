
from design_explorer import component
from design_explorer import utils


class create(component.create):
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name, instanceName=None):
        component.create.__init__(self, name, instanceName)
        self.hdl_blocks = None

    def add_hdl_block(self, oHdlBlock):
        self.hdl_blocks = utils.append_to_list(self.hdl_blocks, oHdlBlock)
