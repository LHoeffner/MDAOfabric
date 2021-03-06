import unittest

import MDAOfabric


class GenericIteratingBundleSolverTests(unittest.TestCase):

    def setUp(self):
        self.settings_string = '''{ 
                    "no_iterations" : 3,
                    "stack"         : { 
                        "1st empty solver":   { 
                            "type"              : "EmptySolver",
                            "surface_opt"       : "something",
                            "example_block"     : {
                                "comment"       : "some comment here",
                                "another_opt"   : "thing",
                                "start_time"    : 0.0
                            }
                        },
                        "2nd empty solver":   { 
                            "type"              : "EmptySolver",
                            "surface_opt"       : "something",
                            "example_block"     : {
                                "comment"       : "some comment here",
                                "another_opt"   : "thing",
                                "start_time"    : 0.0
                            }
                        },
                        "3rd empty solver":   { 
                            "type"              : "EmptySolver",
                            "surface_opt"       : "something",
                            "example_block"     : {
                                "comment"       : "some comment here",
                                "another_opt"   : "thing",
                                "start_time"    : 0.0
                            }
                        }
                    }
                }'''
        self.settings = MDAOfabric.Settings.FromString(self.settings_string)

    def test_initialize(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            solver = MDAOfabric.GenericIteratingBundleSolver(self.settings)
            solver.Initialize()
            self.assertEqual(msg.output, ['WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:Initialize() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Initialize() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Initialize() of the EmptySolver called.'])

    def test_run(self):
        with self.assertLogs(MDAOfabric.log, 'WARNING') as msg:
            solver = MDAOfabric.GenericIteratingBundleSolver(self.settings)
            solver.Run()
            self.assertEqual(msg.output, ['WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:The EmptySolver got initialized.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.',
                                          'WARNING:MDAOlogger:Run() of the EmptySolver called.'])


if __name__ == '__main__':
    unittest.main()
