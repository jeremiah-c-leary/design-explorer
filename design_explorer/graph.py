
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


class edge():

    def __init__(self, source=None, target=None, name=None):
        self.source = source
        self.target = target
        self.name = name


class trace():

    def __init__(self):
        self.path = None

    def add_to_path(self, oEdge):
        try:
            self.path.append(oEdge)
        except AttributeError:
            self.path = [oEdge]

    def get_expanded_path(self):
        lExpandedPath = None
        for oPath in self.path:
            if isinstance(oPath, edge):
                try:
                    lExpandedPath.append(oPath)
                except AttributeError:
                    lExpandedPath = [oPath]
            elif isinstance(oPath, trace):
                lTracePath = oPath.get_expanded_path()
                try:
                    lExpandedPath.extend(lTracePath)
                except AttributeError:
                    lExpandedPath = lTracePath

        return lExpandedPath
