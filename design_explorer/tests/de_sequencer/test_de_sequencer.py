
import os
import unittest

sTestDirPath = os.path.dirname(__file__)

with open (os.path.join(sTestDirPath,'t1_expected_output.uml')) as oFile:
    lT1_expected_output = oFile.readlines()

with open (os.path.join(sTestDirPath,'t2_expected_output.uml')) as oFile:
    lT2_expected_output = oFile.readlines()


class testDeSequencer(unittest.TestCase):

    def test_trace_T1(self):
        if os.path.isfile(os.path.join(sTestDirPath,'t1_actual_output.uml')):
            os.remove(os.path.join(sTestDirPath,'t1_actual_output.uml'))
        os.system('python ' + sTestDirPath + '/../../../bin/' + 'de_sequencer -tf ' + sTestDirPath + '/example.json -tn T1 -uf ' + sTestDirPath + '/t1_actual_output.uml')
        with open (os.path.join(sTestDirPath,'t1_actual_output.uml')) as oFile:
            lT1_actual_output = oFile.readlines()
        self.assertEqual(lT1_expected_output, lT1_actual_output)

    def test_trace_T2(self):
        if os.path.isfile(os.path.join(sTestDirPath,'t2_actual_output.uml')):
            os.remove(os.path.join(sTestDirPath,'t2_actual_output.uml'))
        os.system('python ' + sTestDirPath + '/../../../bin/' + 'de_sequencer -tf ' + sTestDirPath + '/example.json -tn T2 -uf ' + sTestDirPath + '/t2_actual_output.uml')
        with open (os.path.join(sTestDirPath,'t2_actual_output.uml')) as oFile:
            lT2_actual_output = oFile.readlines()
        self.assertEqual(lT2_expected_output, lT2_actual_output)


if __name__ == '__main__':
    unittest.main()
