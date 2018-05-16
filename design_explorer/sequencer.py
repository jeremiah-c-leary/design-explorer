
import graph

def get_participant_subnodes(lNodes):
    lBoxes = None
    for oNode in lNodes: 
        if oNode.subNode:
            if lBoxes:
                if not oNode.subNode in lBoxes:
                    lBoxes.append(oNode.subNode)
            else:
                lBoxes = [oNode.subNode]
           
    return lBoxes

def get_participants(oTrace, oNodeList, lEdges):

    lParticipants = []
    for oEdge in lEdges:
        oSourceNode = oNodeList.get_node(oEdge.source)
        oTargetNode = oNodeList.get_node(oEdge.target)
        if not oSourceNode in lParticipants:
            lParticipants.append(oSourceNode)
        if not oTargetNode in lParticipants:
            lParticipants.append(oTargetNode)
    return lParticipants


def create_plantuml_sequence_diagram(oTrace, oNodeList):

    lDiagram = ['@startuml']
    lDiagram.append('')

    lEdges = oTrace.get_expanded_path()

    lParticipants = get_participants(oTrace, oNodeList, lEdges) 

    lBoxes = get_participant_subnodes(lParticipants)

    dBoxes = {}
    if lBoxes:
        for sBox in lBoxes:
            dBoxes[sBox] = []

        for oParticipant in lParticipants:
            if oParticipant.subNode:
                dBoxes[oParticipant.subNode].append(oParticipant.name)

    lUsedNodes = []
    for oParticipant in lParticipants:
        if not oParticipant.name in lUsedNodes:
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

    for oEdge in lEdges:
        lDiagram.append(' '.join([oEdge.source, '->', oEdge.target, ':', oEdge.name]))

    lDiagram.append('')
    lDiagram.append('@enduml')
    return lDiagram
