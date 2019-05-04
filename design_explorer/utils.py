

def append_to_list(lList, oItem):
    '''
    Appends an item to a list.
    If the list is None, then it will create the list with the given item.
    '''
    try:
        lList.append(oItem)
    except AttributeError:
        lList = [oItem]
    return lList


def write_to_file(sFileName, lList):
    '''
    Writes a list of strings to a file.
    '''
    with open(sFileName, 'w') as oFile:
        for sLine in lList:
            oFile.write(sLine + '\n')
    oFile.close()


def extract_interface_from_path(sPath):
    '''
    Returns the interface from a dot notation path.
    '''

    lPath = sPath.split('.')
    return lPath[-1]


def extract_component_from_path(sPath):
    '''
    Returns the last component from a dot notation path.
    '''

    lPath = sPath.split('.')
    return lPath[-2]


def remove_interface_from_path(sPath):
    '''
    Returns the entire path to a component
    '''

    lPath = sPath.split('.')
    return '.'.join(lPath[:-1])


def get_component_paths(oSystem, sPath, lPaths):
    try:
        lComponents = oSystem.components
    except:
        lPaths.append(sPath)
        return lPaths

    for oComponent in lComponents:
        if sPath not in lPaths:
            lPaths.append(sPath)
        get_component_paths(oComponent, sPath + '.' + oComponent.instanceName, lPaths)

    return lPaths


def split_path(sPath):
    return sPath.split('.')    


def trim_path_to_level(sPath, iLevel):
    lPath = split_path(sPath)
    return '.'.join(lPath[:iLevel + 1])


def remove_first_element_from_path(sPath):
    return '.'.join(split_path(sPath)[1:])
