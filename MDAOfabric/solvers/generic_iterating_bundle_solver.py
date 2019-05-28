import MDAOfabric
from .iterating_bundle_solver_base import IteratingBundleSolverBase


class GenericIteratingBundleSolver(IteratingBundleSolverBase):
    """Solver class for iterations containing multiple solvers which are chosen via the settings file

    """
    def __init__(self, settings):
        super(GenericIteratingBundleSolver, self).__init__(settings)

        # create stack of solvers and IO
        for piece_name, piece_settings in self.settings['stack'].items():
            if 'name' not in piece_settings:
                piece_settings['name'] = piece_name

            piece = MDAOfabric.factory.GetPiece(piece_settings['type'], piece_settings)
            self.stack.append(piece)

    def GetDefaultSettings(self):
        defaults = MDAOfabric.Settings.FromString('''{
            "type"          : "GenericIteratingBundleSolver",
            "name"          : "GenericIteratingBundleSolver_unnamed",
            "no_iterations" : 5
        }''')
        defaults['stack'] = MDAOfabric.Settings.FromString('{}')
        return defaults
