import MDAOfabric
from .solver_base import SolverBase


class EmptySolver(SolverBase):
    """An empty standalone-solver for testing purposes

    Raises exceptions when one of the methods is called, except for GetDefaultSettings()
    """
    def __init__(self, settings):
        super(EmptySolver, self).__init__(settings)
        MDAOfabric.log.warning('The EmptySolver got initialized.')

    def GetDefaultSettings(self):
        default_settings = ('''{
                    "type"              : "EmptySolver",
                    "name"              : "EmptySolver_unnamed",
                    "surface_opt"       : "empty_sth",
                    "example_block"     : {
                        "comment"       : "empty comment here",
                        "another_opt"   : "thing",
                        "start_time"    : 0.0
                    }
                }''')
        return MDAOfabric.Settings.FromString(default_settings)

    def Initialize(self):
        MDAOfabric.log.warning('Initialize() of the EmptySolver called.')

    def Run(self):
        MDAOfabric.log.warning('Run() of the EmptySolver called.')

    def Finalize(self):
        MDAOfabric.log.warning('Finalize() of the EmptySolver called.')
