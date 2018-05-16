import os

import unittest
from design_explorer import sequencer
from design_explorer import graph


class testSequencer(unittest.TestCase):

    def test_edge_only_diagram_creation(self):
        oTrace = graph.trace()
        oTrace.add_to_path(graph.edge('N1', 'N2', 'E1'))
        oTrace.add_to_path(graph.edge('N2', 'N3', 'E2'))
        oTrace.add_to_path(graph.edge('N3', 'N4', 'E3'))
        oTrace.add_to_path(graph.edge('N4', 'N5', 'E4'))
        oTrace.add_to_path(graph.edge('N5', 'N6', 'E5'))

        dExpected = ['@startuml']
        dExpected.append('')
        dExpected.append('N1 -> N2 : E1')
        dExpected.append('N2 -> N3 : E2')
        dExpected.append('N3 -> N4 : E3')
        dExpected.append('N4 -> N5 : E4')
        dExpected.append('N5 -> N6 : E5')
        dExpected.append('')
        dExpected.append('@enduml')

        self.assertEqual(dExpected, sequencer.create_plantuml_sequence_diagram(oTrace))
        

    def test_edge_and_trace_diagram_creation(self):
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
        dExpected.append('N1 -> N2 : E1')
        dExpected.append('N2 -> N3 : E2')
        dExpected.append('N3 -> N4 : E3')
        dExpected.append('N4 -> N5 : E4')
        dExpected.append('N5 -> N6 : E5')
        dExpected.append('')
        dExpected.append('@enduml')

        self.assertEqual(dExpected, sequencer.create_plantuml_sequence_diagram(oTrace1))
     
      
if __name__ == '__main__':
    unittest.main()
