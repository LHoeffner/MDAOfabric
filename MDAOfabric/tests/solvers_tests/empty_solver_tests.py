import unittest
import MDAOfabric


class EmptySolverTests(unittest.TestCase):

    def setUp(self):
        self.settings_string = '''{
                    "surface_opt"       : "something",
                    "example_block"       : {
                        "comment"       : "some comment here",
                        "solver_type"   : "some_solver",
                        "start_time"    : 0.0,
                        "deeper_level"  : {
                            "some_lowerlevel_key"   : 43,
                            "comment"               : "also on lower level"
                        }
                    }
                }'''
        self.settings = MDAOfabric.Settings.FromString(self.settings_string)
        self.solver = MDAOfabric.EmptySolver(self.settings)

    def test_run_full_sequence(self):
        with self.assertRaises(Exception) as excep:
            self.solver.RunFullSequence()
        self.assertEqual(str(excep.exception), 'Initialize() of the EmptySolver called.')

    def test_initialize(self):
        with self.assertRaises(Exception) as excep:
            self.solver.Initialize()
        self.assertEqual(str(excep.exception), 'Initialize() of the EmptySolver called.')

    def test_run(self):
        with self.assertRaises(Exception) as excep:
            self.solver.Run()
        self.assertEqual(str(excep.exception), 'Run() of the EmptySolver called.')

    def test_finalize(self):
        with self.assertRaises(Exception) as excep:
            self.solver.Finalize()
        self.assertEqual(str(excep.exception), 'Finalize() of the EmptySolver called.')