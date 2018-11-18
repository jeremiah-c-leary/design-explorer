
class create():
    '''
    Creates an HDL Subsystem object with a given instance name.
    '''

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.subblocks = None


    def add_subblock(self, oSubblock):
        try:
            self.subblocks.append(oSubblock)
        except:
            self.subblocks = []
            self.subblocks.append(oSubblock)
