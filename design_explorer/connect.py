

class create():

    def __init__(self, sName, oSource, sSourceInterfaceName, oSink, sSinkInterfaceName):
        self.name = sName
        self.source = oSource
        self.source_interface = oSource.get_interface(sSourceInterfaceName)
        self.sink = oSink
        self.sink_interface = oSink.get_interface(sSinkInterfaceName)
