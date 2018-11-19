

def append_to_list(lList, oItem):
    try:
        lList.append(oItem)
    except AttributeError:
        lList = [oItem]
    return lList
