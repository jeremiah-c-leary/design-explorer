import design_explorer as de


def node_list(oSystem, iLevel=1):

    lReturn = []
    lReturn.append('Id,Label,Type,Level')

    lNodes = de.apps.hierarchy.extract(oSystem)

    lFilteredNodes = de.apps.hierarchy.filter_upto_level(lNodes, iLevel)

    lFinalNodes = de.apps.hierarchy.extract_end_points(lFilteredNodes)

    for sNode in lFinalNodes:
        oComponent = oSystem.get_component_named(de.utils.remove_first_element_from_path(sNode))
        sReturn = sNode + ','
        sReturn += sNode.split('.')[-1] + ','
        sReturn += oComponent.type + ','
        sReturn += de.utils.remove_last_element_from_path(sNode)
        lReturn.append(sReturn)

    return lReturn


def edge_list(oSystem, iLevel=1):

    lMap = de.apps.hierarchy.extract(oSystem)
    lFilteredMap = de.apps.hierarchy.filter_upto_level(lMap, iLevel)

    lEndPoints = de.apps.hierarchy.extract_end_points(lFilteredMap)
    lMidPoints = de.apps.hierarchy.extract_mid_points(lFilteredMap)

    de.apps.hierarchy.update_paths(oSystem)

    lConnections = de.apps.hierarchy.extract_connections(oSystem, lMidPoints)

    lReturn = []
    lReturn.append('Source,Target,Type')
    for oConnection in lConnections:
        for sSourcePoint in lEndPoints:
            for sSinkPoint in lEndPoints:
                if oConnection.source.path.find(sSourcePoint) > -1 and oConnection.sink.path.find(sSinkPoint) > -1:
                    sReturn = de.utils.trim_path_to_level(sSourcePoint, iLevel) + ','
                    sReturn += de.utils.trim_path_to_level(sSinkPoint, iLevel) + ','
                    sReturn += 'Directed'
                    lReturn.append(sReturn)

    return lReturn
