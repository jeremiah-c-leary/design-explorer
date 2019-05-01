import design_explorer as de



def node_list(oSystem, iLevel=1):

    lReturn = []
    lReturn.append('Id, Label')

    lNodes = de.apps.hierarchy.extract(oSystem)

    lFilteredNodes = de.apps.hierarchy.filter_upto_level(lNodes, iLevel)
    
    lFinalNodes = de.apps.hierarchy.extract_end_points(lFilteredNodes)

    for sNode in lFinalNodes:
        lReturn.append(sNode + ', ' + sNode.split('.')[-1])

    return lReturn


def edge_list(oSystem, iLevel=1):

    lReturn = []
    lReturn.append('Source,Target,Type')
    for oConnection in oSystem.connections:
        lReturn.append(oConnection.source.parent.name + ',' + oConnection.sink.parent.name + ',Directed')

    return lReturn
