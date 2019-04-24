
class create():

    def __init__(self, name, source, sink, automap=True):
        self.name = name 
        self.source = source
        self.sink = sink
        self.map = self._initial_map(automap)

    def _initial_map(self, automap):
        if automap:
            myMap = {}
            try:
                for i in range (0, len(self.source.ports)):
                    myMap[self.source.ports[i].name] = self.sink.ports[i].name
                return myMap
            except TypeError:
                return None
        else:
            return None

    def map_port(self, source, sink):
        try:
            self.map[source] = sink
        except TypeError:
            self.map = {}
            self.map[source] = sink
