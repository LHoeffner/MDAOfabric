import MDAOfabric
from .solver_base import SolverBase


class EmptySolver(SolverBase):
    """An empty standalone-solver for testing purposes

    Raises exceptions when one of the methods is called, except for GetDefaultSettings()
    """

    def GetDefaultSettings(self):
        default_settings = ('''{
                    "surface_opt"       : "empty_sth",
                    "example_block"     : {
                        "comment"       : "empty comment here",
                        "solver_type"   : "empty_sub_solver",
                        "start_time"    : 0.0,
                        "deeper_level"  : {
                            "some_lowerlevel_key"   : 43,
                            "comment"               : "also in empty lower level"
                        }
                    }
                }''')
        return MDAOfabric.Settings.FromString(default_settings)

    def Initialize(self):
        raise Exception('Initialize() of the EmptySolver called.')

    def Run(self):
        raise Exception('Run() of the EmptySolver called.')

    def Finalize(self):
        raise Exception('Finalize() of the EmptySolver called.')
