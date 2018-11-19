
from design_explorer import utils


class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, instance_name):
        self.source_interfaces = None
        self.sink_interfaces = None
        self.instance_name = instance_name

    def add_source_interface(self, oInterface):
        self.source_interfaces = utils.append_to_list(self.source_interfaces, oInterface)

    def add_sink_interface(self, oInterface):
        self.sink_interfaces = utils.append_to_list(self.sink_interfaces, oInterface)

    def create_entity(self):
        lReturn = []
        lReturn.append('entity ' + self.instance_name.upper() + ' is')
        lReturn.append('  port map (')
        for oInterface in self.sink_interfaces:
            for sLine in oInterface.extract_port_list('Sink'):
                lReturn.append('    ' + sLine)
            lReturn.append('')
        for oInterface in self.source_interfaces:
            for sLine in oInterface.extract_port_list('Source'):
                lReturn.append('    ' + sLine)
            lReturn.append('')
        lReturn.append('  )')
        lReturn.append('end entity ' + self.instance_name.upper() + ';')

        return lReturn
