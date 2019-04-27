

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
