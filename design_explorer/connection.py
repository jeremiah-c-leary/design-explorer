
import design_explorer as de


class create():

    def __init__(self, name, oSystem, source, sink, automap=True):
        self.name = name
        self.parent = oSystem
        self.source = self._find_interface(source, oSystem.name)
        self.sink = self._find_interface(sink, oSystem.name)
        self.map = self._initial_map(automap)

    def _initial_map(self, automap):
        if automap:
            return automap_ports(self)
        else:
            return None

    def map_port(self, source, sink):
        try:
            self.map[source] = sink
        except TypeError:
            self.map = {}
            self.map[source] = sink

    def _find_interface(self, sString, sSystemName):
        oComponent = self.parent.get_component_named(de.utils.remove_interface_from_path(sString))
        oInterface = oComponent.get_interface_named(de.utils.extract_interface_from_path(sString))
        return oInterface


def automap_ports(self):
    myMap = {}
    try:
        for i in range(0, len(self.source.ports)):
            myMap[self.source.ports[i].name] = self.sink.ports[i].name
        return myMap
    except TypeError:
        return None
