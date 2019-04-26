

def node_list(oSystem):

    lReturn = []
    lReturn.append('Id, Label')

    for oComponent in oSystem.components:
        lReturn.append(oComponent.name + ', ' + oComponent.name)

    return lReturn
