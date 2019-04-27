
class create():
    '''
    Creates a port with the given
    '''

    def __init__(self, name, width=None, direction='in', description=None):
        self.name = name
        self.width = width
        self.direction = validate_direction(direction)
        self.description = description


def validate_direction(sString):
    if sString not in ['in', 'out', 'inout']:
        raise ValueError('Only in, out, or inout are valid port directions.')
    return sString
