

def node_list(oSystem):

    lReturn = []
    lReturn.append('Id, Label')

    for oComponent in oSystem.components:
        lReturn.append(oComponent.name + ', ' + oComponent.name)

    return lReturn


def edge_list(oSystem):

    lReturn = []
    lReturn.append('Source,Target,Type')
    for oConnection in oSystem.connections:
        lReturn.append(oConnection.source.parent.name + ',' + oConnection.sink.parent.name + ',Directed')

    return lReturn
