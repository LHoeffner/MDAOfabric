import unittest

import MDAOfabric


class GenericIteratingBundleSolverTests(unittest.TestCase):

    def setUp(self):
        self.settings_string = '''{ 
                    "no_iterations" : 7,
                    "stack"         : { 
                        "first empty solver":   { 
                            "type"              : "EmptySolver",
                            "surface_opt"       : "something",
                            "example_block"     : {
                                "comment"       : "some comment here",
                                "solver_type"   : "some_solver",
                                "start_time"    : 0.0
                            }
                        }
                    }
                }'''
        self.settings = MDAOfabric.Settings.FromString(self.settings_string)

    def test_initialize(self):
        solver = MDAOfabric.GenericIteratingBundleSolver(self.settings)
