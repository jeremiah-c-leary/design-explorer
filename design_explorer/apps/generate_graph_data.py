import design_explorer as de


def node_list(oSystem, iLevel=1):

    lReturn = []
    lReturn.append('Id, Label')

    lNodes = []
    de.utils.get_component_paths(oSystem, oSystem.instanceName, lNodes)

    # Filter nodes based on level
    lFilteredNodes = []
    for sNode in lNodes:
        if sNode.count('.') <= iLevel and sNode.count('.') > 0:
            lFilteredNodes.append(sNode)

    lFinalNodes = []
    for sNode in lFilteredNodes[::-1]:
        fFound = False
        for sFinalNode in lFinalNodes:
            if sFinalNode.count(sNode) > 0:
                fFound = True
        if not fFound:
            lFinalNodes.append(sNode)

    for sNode in lFinalNodes[::-1]:
        lReturn.append(sNode + ', ' + sNode.split('.')[-1])

    return lReturn


def edge_list(oSystem):

    lReturn = []
    lReturn.append('Source,Target,Type')
    for oConnection in oSystem.connections:
        lReturn.append(oConnection.source.parent.name + ',' + oConnection.sink.parent.name + ',Directed')

    return lReturn
