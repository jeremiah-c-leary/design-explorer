
def append_to_list(lList, item):
    try:
        lList.append(item)
    except AttributeError:
        lList = [item]
    return lList


class base_list():

    def __init__(self):
        self.lItems = None

    def add_item(self, oItem):
        try:
            self.lItems.append(oItem)
        except AttributeError:
            self.lItems = [oItem]

    def get_item(self, sItemName):
        for oItem in self.lItems:
            if oItem.name == sItemName:
                return oItem
        return None


class node_list(base_list):

    def __init__(self):
        base_list.__init__(self)

    def get_subnodes_of_node(self, sSubNodeName):
        lNodes = None
        for oNode in self.lItems:
            if oNode.subNode == sSubNodeName:
                lNodes = append_to_list(lNodes, oNode)
        return lNodes


class node():

    def __init__(self, name=None, subNode=None):
        self.name = name
        self.subNode = subNode


class edge():

    def __init__(self, source=None, target=None, name=None, sInterface=None):
        self.source = source
        self.target = target
        self.name = name
        self.interface = sInterface


class edge_list(base_list):

    def __init__(self):
        base_list.__init__(self)

    def get_edges_of_node(self, sNodeName):
        lEdges = None
        for oEdge in self.lItems:
            if oEdge.source == sNodeName:
                lEdges = append_to_list(lEdges, oEdge)
        return lEdges


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
