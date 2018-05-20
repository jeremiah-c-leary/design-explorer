
import graph


def get_participant_subnodes(lNodes):

    lBoxes = []
    for oNode in lNodes:
        if oNode.subNode:
            if oNode.subNode not in lBoxes:
                lBoxes.append(oNode.subNode)

    return lBoxes


def get_participants(oTrace, oNodeList, lEdges):

    lParticipants = []
    for oEdge in lEdges:
        oSourceNode = oNodeList.get_node(oEdge.source)
        oTargetNode = oNodeList.get_node(oEdge.target)
        if oSourceNode not in lParticipants:
            lParticipants.append(oSourceNode)
        if oTargetNode not in lParticipants:
            lParticipants.append(oTargetNode)
    return lParticipants


def build_participant_section(lBoxes, lParticipants):

    lDiagram = []
    dBoxes = {}
    if lBoxes:
        for sBox in lBoxes:
            dBoxes[sBox] = []

        for oParticipant in lParticipants:
            if oParticipant.subNode:
                dBoxes[oParticipant.subNode].append(oParticipant.name)

    lUsedNodes = []
    for oParticipant in lParticipants:
        if oParticipant.name not in lUsedNodes:
            if not oParticipant.subNode:
                lDiagram.append(' '.join(['participant', oParticipant.name]))
                lUsedNodes.append(oParticipant.name)
            else:
                lDiagram.append('box "' + oParticipant.subNode + '"')
                for sNodeName in dBoxes[oParticipant.subNode]:
                    lDiagram.append('  ' + ' '.join(['participant', sNodeName]))
                    lUsedNodes.append(sNodeName)
                lDiagram.append('end box')

    lDiagram.append('')
    return lDiagram


def build_sequence_section(lEdges):

    lDiagram = []
    for oEdge in lEdges:
        lDiagram.append(' '.join([oEdge.source, '->', oEdge.target, ':', oEdge.name]))
    return lDiagram


def create_plantuml_sequence_diagram(oTrace, oNodeList):

    lDiagram = ['@startuml']
    lDiagram.append('')

    lEdges = oTrace.get_expanded_path()

    lParticipants = get_participants(oTrace, oNodeList, lEdges)

    lBoxes = get_participant_subnodes(lParticipants)

    lDiagram.extend(build_participant_section(lBoxes, lParticipants))

    lDiagram.extend(build_sequence_section(lEdges))

    lDiagram.append('')
    lDiagram.append('@enduml')
    return lDiagram
