

def append_to_list(lList, oItem):
    try:
        lList.append(oItem)
    except AttributeError:
        lList = [oItem]
    return lList


def write_to_file(sFileName, lList):
    with open (sFileName, 'w') as oFile:
        for sLine in lList:
            oFile.write(sLine + '\n')
    oFile.close()
