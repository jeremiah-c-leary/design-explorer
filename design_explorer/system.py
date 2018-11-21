from design_explorer import utils


class create():
    '''
    Creates an HDL Subsystem object with a given instance name.
    '''

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.subblocks = None

    def add_subblock(self, oSubblock):
        self.subblocks = utils.append_to_list(self.subblocks, oSubblock)
