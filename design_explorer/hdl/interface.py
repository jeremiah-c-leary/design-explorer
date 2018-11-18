
class create():
    '''
    Creates an object with a given instance name.
    '''

    def __init__(self, name):
        self.name = name
        self.description = None
        self.source_ports = None
        self.sink_ports = None

    def add_source_port(self, oPort):
        try:
            self.source_ports.append(oPort)
        except:
            self.source_ports = []
            self.source_ports.append(oPort)

    def add_sink_port(self, oPort):
        try:
            self.sink_ports.append(oPort)
        except:
            self.sink_ports = []
            self.sink_ports.append(oPort)
