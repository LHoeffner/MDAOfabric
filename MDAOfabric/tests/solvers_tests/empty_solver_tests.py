import unittest

import MDAOfabric


class EmptySolverTests(unittest.TestCase):

    def setUp(self):
        self.settings_string = '''{
                    "surface_opt"       : "something",
                    "example_block"       : {
                        "comment"       : "some comment here",
                        "another_opt"   : "thing",
                        "start_time"    : 0.0
                    }
                }'''
        self.settings = MDAOfabric.Settings.FromString(self.settings_string)
        self.solver = MDAOfabric.EmptySolver(self.settings)

    def test_run_full_sequence(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            self.solver.RunFullSequence()
            self.assertEqual('WARNING:MDAOlogger:Initialize() of the EmptySolver called.', msg.output[0])
            self.assertEqual('WARNING:MDAOlogger:Run() of the EmptySolver called.', msg.output[1])
            self.assertEqual('WARNING:MDAOlogger:Finalize() of the EmptySolver called.', msg.output[2])

    def test_initialize(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            self.solver.Initialize()
            self.assertEqual('WARNING:MDAOlogger:Initialize() of the EmptySolver called.', msg.output[0])

    def test_run(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            self.solver.Run()
            self.assertEqual('WARNING:MDAOlogger:Run() of the EmptySolver called.', msg.output[0])

    def test_finalize(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            self.solver.Finalize()
            self.assertEqual('WARNING:MDAOlogger:Finalize() of the EmptySolver called.', msg.output[0])


if __name__ == '__main__':
    unittest.main()
