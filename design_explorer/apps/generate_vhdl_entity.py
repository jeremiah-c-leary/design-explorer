
def generate_vhdl_entity(oHdlComponent):

    lReturn = []

    add_entity_header(lReturn, oHdlComponent)
    if not oHdlComponent.interfaces is None:
        for oInterface in oHdlComponent.interfaces:
            lReturn.append('    -- [I:' + oInterface.name + ']')
            add_ports(lReturn, oInterface)
            lReturn.append('')
        lReturn.pop()
    add_end_entity(lReturn, oHdlComponent)

    return lReturn


def add_ports(lReturn, oInterface):
    if not oInterface.ports is None:
        for oPort in oInterface.ports:
            sReturn = '    ' + oPort.name + ' : ' + oPort.direction + ' '
            sReturn += add_port_type(oPort)
            sReturn += add_port_description(oPort)
            lReturn.append(sReturn)


def add_port_type(oPort):
    if oPort.width == 1:
        return 'std_logic; '
    else:
        return 'std_logic_vector(' + str(oPort.width - 1) + ' downto 0); '


def add_port_description(oPort):
    if oPort.description is None:
        return '-- ::WARNING:: Missing description'
    else:
        return '-- ' + oPort.description


def add_entity_header(lReturn, oHdlComponent):
    lReturn.append('entity ' + oHdlComponent.name.upper() + ' is')
    lReturn.append('  port (')


def add_end_entity(lReturn, oHdlComponent):
    lReturn.append('  );')
    lReturn.append('end entity ' + oHdlComponent.name.upper() + ';')
