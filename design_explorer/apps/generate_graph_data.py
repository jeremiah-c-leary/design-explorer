import design_explorer as de



def node_list(oSystem, iLevel=1):

    lReturn = []
    lReturn.append('Id,Label,Type,Level')

    lNodes = de.apps.hierarchy.extract(oSystem)

    lFilteredNodes = de.apps.hierarchy.filter_upto_level(lNodes, iLevel)
    
    lFinalNodes = de.apps.hierarchy.extract_end_points(lFilteredNodes)

    for sNode in lFinalNodes:
        oComponent = oSystem.get_component_named(de.utils.remove_first_element_from_path(sNode))
        lReturn.append(sNode + ',' + sNode.split('.')[-1] + ',' + oComponent.type + ',' + de.utils.remove_last_element_from_path(sNode))

    return lReturn


def edge_list(oSystem, iLevel=1):

    lMap = de.apps.hierarchy.extract(oSystem)
    lFilteredMap = de.apps.hierarchy.filter_upto_level(lMap, iLevel)

    lEndPoints = de.apps.hierarchy.extract_end_points(lFilteredMap)
    lMidPoints = de.apps.hierarchy.extract_mid_points(lFilteredMap)

    de.apps.hierarchy.update_paths(oSystem)

#    print lEndPoints
#    print lMidPoints

    lConnections = de.apps.hierarchy.extract_connections(oSystem, lMidPoints)

#    print lConnections

    lReturn = []
    lReturn.append('Source,Target,Type')
    for oConnection in lConnections:
        for sSourcePoint in lEndPoints:
            for sSinkPoint in lEndPoints:
#                print '[' + sSourcePoint + '][' + oConnection.source.path + '][' + sSinkPoint + '][' + oConnection.sink.path + ']'
                if oConnection.source.path.find(sSourcePoint) > -1 and oConnection.sink.path.find(sSinkPoint) > -1:
                    lReturn.append(de.utils.trim_path_to_level(sSourcePoint, iLevel) + ',' + de.utils.trim_path_to_level(sSinkPoint, iLevel) + ',Directed')

    return lReturn
