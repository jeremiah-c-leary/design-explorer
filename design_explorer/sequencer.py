
import graph

def create_plantuml_sequence_diagram(oTrace):

    lDiagram = ['@startuml']
    lDiagram.append('')

    for oEdge in oTrace.get_expanded_path():
        lDiagram.append(' '.join([oEdge.source, '->', oEdge.target, ':', oEdge.name]))

    lDiagram.append('')
    lDiagram.append('@enduml')
    return lDiagram
