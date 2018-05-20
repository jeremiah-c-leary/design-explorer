
class node():

    def __init__(self, name=None, subNode=None):
        self.name = name
        self.subNode = subNode


class node_list():

    def __init__(self):
        self.nodes = None

    def add_node(self, oNode):
        try:
            self.nodes.append(oNode)
        except AttributeError:
            self.nodes = [oNode]

    def get_node(self, sNodeName):
        for oNode in self.nodes:
            if oNode.name == sNodeName:
                return oNode
        return None


class edge():

    def __init__(self, source=None, target=None, name=None):
        self.source = source
        self.target = target
        self.name = name


class edge_list():

    def __init__(self):
        self.edges = None

    def add_edge(self, oEdge):
        try:
            self.edges.append(oEdge)
        except AttributeError:
            self.edges = [oEdge]

    def get_edge(self, sEdgeName):
        for oEdge in self.edges:
            if oEdge.name == sEdgeName:
                return oEdge
        return None


class trace():

    def __init__(self, sName):
        self.name = sName
        self.path = None

    def add_to_path(self, oEdge):
        try:
            self.path.append(oEdge)
        except AttributeError:
            self.path = [oEdge]

    def get_expanded_path(self):

        lExpandedPath = []

        for oPath in self.path:
            if isinstance(oPath, edge):
                lExpandedPath.append(oPath)
            elif isinstance(oPath, trace):
                lTracePath = oPath.get_expanded_path()
                lExpandedPath.extend(lTracePath)

        return lExpandedPath


class trace_list():

    def __init__(self):
        self.traces = None

    def add_trace(self, oTrace):
        try:
            self.traces.append(oTrace)
        except AttributeError:
            self.traces = [oTrace]

    def get_trace(self, sTraceName):
        for oTrace in self.traces:
            if oTrace.name == sTraceName:
                return oTrace
        return None
