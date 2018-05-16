import os

import unittest
from design_explorer import sequencer
from design_explorer import graph


class testSequencer(unittest.TestCase):

    def test_get_participant_subnodes(self):
        lNodes = []
        lNodes.append(graph.node('N1'))
        lNodes.append(graph.node('N2', 'F1'))
        lNodes.append(graph.node('N3', 'F1'))
        lNodes.append(graph.node('N4'))
        lNodes.append(graph.node('N5', 'F2'))
        lNodes.append(graph.node('N6', 'F2'))
        lNodes.append(graph.node('N7'))
        self.assertEqual(sequencer.get_participant_subnodes(lNodes), ['F1', 'F2'])

    def test_edge_only_diagram_creation(self):
        oNodeList = graph.node_list()
        oNodeList.add_node(graph.node('N1'))
        oNodeList.add_node(graph.node('N2'))
        oNodeList.add_node(graph.node('N3'))
        oNodeList.add_node(graph.node('N4'))
        oNodeList.add_node(graph.node('N5'))
        oNodeList.add_node(graph.node('N6'))
        oTrace = graph.trace()
        oTrace.add_to_path(graph.edge('N1', 'N2', 'E1'))
        oTrace.add_to_path(graph.edge('N2', 'N3', 'E2'))
        oTrace.add_to_path(graph.edge('N3', 'N4', 'E3'))
        oTrace.add_to_path(graph.edge('N4', 'N5', 'E4'))
        oTrace.add_to_path(graph.edge('N5', 'N6', 'E5'))

        dExpected = ['@startuml']
        dExpected.append('')
        dExpected.append('participant N1')
        dExpected.append('participant N2')
        dExpected.append('participant N3')
        dExpected.append('participant N4')
        dExpected.append('participant N5')
        dExpected.append('participant N6')
        dExpected.append('')
        dExpected.append('N1 -> N2 : E1')
        dExpected.append('N2 -> N3 : E2')
        dExpected.append('N3 -> N4 : E3')
        dExpected.append('N4 -> N5 : E4')
        dExpected.append('N5 -> N6 : E5')
        dExpected.append('')
        dExpected.append('@enduml')

        self.assertEqual(dExpected, sequencer.create_plantuml_sequence_diagram(oTrace, oNodeList))
        

    def test_edge_and_trace_diagram_creation(self):
        oNodeList = graph.node_list()
        oNodeList.add_node(graph.node('N1'))
        oNodeList.add_node(graph.node('N2'))
        oNodeList.add_node(graph.node('N3'))
        oNodeList.add_node(graph.node('N4'))
        oNodeList.add_node(graph.node('N5'))
        oNodeList.add_node(graph.node('N6'))
        oTrace = graph.trace()
        oTrace.add_to_path(graph.edge('N1', 'N2', 'E1'))
        oTrace.add_to_path(graph.edge('N2', 'N3', 'E2'))
        oTrace1 = graph.trace()
        oTrace1.add_to_path(oTrace)
        oTrace1.add_to_path(graph.edge('N3', 'N4', 'E3'))
        oTrace1.add_to_path(graph.edge('N4', 'N5', 'E4'))
        oTrace1.add_to_path(graph.edge('N5', 'N6', 'E5'))

        dExpected = ['@startuml']
        dExpected.append('')
        dExpected.append('participant N1')
        dExpected.append('participant N2')
        dExpected.append('participant N3')
        dExpected.append('participant N4')
        dExpected.append('participant N5')
        dExpected.append('participant N6')
        dExpected.append('')
        dExpected.append('N1 -> N2 : E1')
        dExpected.append('N2 -> N3 : E2')
        dExpected.append('N3 -> N4 : E3')
        dExpected.append('N4 -> N5 : E4')
        dExpected.append('N5 -> N6 : E5')
        dExpected.append('')
        dExpected.append('@enduml')

        self.assertEqual(dExpected, sequencer.create_plantuml_sequence_diagram(oTrace1, oNodeList))
     
      
    def test_edge_and_trace_diagram_creation_with_boxes(self):
        oNodeList = graph.node_list()
        oNodeList.add_node(graph.node('N1'))
        oNodeList.add_node(graph.node('N2', 'F1'))
        oNodeList.add_node(graph.node('N3', 'F1'))
        oNodeList.add_node(graph.node('N4'))
        oNodeList.add_node(graph.node('N5', 'F2'))
        oNodeList.add_node(graph.node('N6', 'F2'))
        oNodeList.add_node(graph.node('N7'))
        oTrace = graph.trace()
        oTrace.add_to_path(graph.edge('N1', 'N2', 'E1'))
        oTrace.add_to_path(graph.edge('N2', 'N3', 'E2'))
        oTrace1 = graph.trace()
        oTrace1.add_to_path(oTrace)
        oTrace1.add_to_path(graph.edge('N3', 'N4', 'E3'))
        oTrace1.add_to_path(graph.edge('N4', 'N5', 'E4'))
        oTrace1.add_to_path(graph.edge('N5', 'N6', 'E5'))
        oTrace1.add_to_path(graph.edge('N6', 'N7', 'E6'))

        dExpected = ['@startuml']
        dExpected.append('')
        dExpected.append('participant N1')
        dExpected.append('box "F1"')
        dExpected.append('  participant N2')
        dExpected.append('  participant N3')
        dExpected.append('end box')
        dExpected.append('participant N4')
        dExpected.append('box "F2"')
        dExpected.append('  participant N5')
        dExpected.append('  participant N6')
        dExpected.append('end box')
        dExpected.append('participant N7')
        dExpected.append('')
        dExpected.append('N1 -> N2 : E1')
        dExpected.append('N2 -> N3 : E2')
        dExpected.append('N3 -> N4 : E3')
        dExpected.append('N4 -> N5 : E4')
        dExpected.append('N5 -> N6 : E5')
        dExpected.append('N6 -> N7 : E6')
        dExpected.append('')
        dExpected.append('@enduml')

        self.assertEqual(dExpected, sequencer.create_plantuml_sequence_diagram(oTrace1, oNodeList))

if __name__ == '__main__':
    unittest.main()
