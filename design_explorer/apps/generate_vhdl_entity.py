
def generate_vhdl_entity(oHdlComponent):

    lReturn = []

    lReturn.append('entity ' + oHdlComponent.name.upper() + ' is')
    lReturn.append('  port (')
    if not oHdlComponent.interfaces is None:
        for oInterface in oHdlComponent.interfaces:
            lReturn.append('    -- [I:' + oInterface.name + ']')
            if not oInterface.ports is None:
                for oPort in oInterface.ports:
                    sReturn = '    ' + oPort.name + ' : ' + oPort.direction + ' '
                    if oPort.width == 1:
                        sReturn += 'std_logic; '
                    else:
                        sReturn += 'std_logic_vector(' + str(oPort.width - 1) + ' downto 0); '
                    if oPort.description is None:
                        sReturn += '-- ::WARNING:: Missing description'
                    else:
                        sReturn += '-- ' + oPort.description
                    lReturn.append(sReturn)
            lReturn.append('')
        lReturn.pop()
    lReturn.append('  );')
    lReturn.append('end entity ' + oHdlComponent.name.upper() + ';')

    return lReturn
