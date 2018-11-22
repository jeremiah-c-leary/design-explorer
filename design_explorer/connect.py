

class create():

    def __init__(self, sName):
        self.name = sName
        self.source = None
        self.source_interface = None
        self.sink = None
        self.sink_interface = None

    def add_source(self, oComponent, sInterfaceName):
        self.source = oComponent
        self.source_interface = oComponent.get_interface(sInterfaceName)

    def add_sink(self, oComponent, sInterfaceName):
        self.sink = oComponent
        self.sink_interface = oComponent.get_interface(sInterfaceName)
