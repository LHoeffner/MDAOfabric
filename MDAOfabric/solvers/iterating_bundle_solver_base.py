import MDAOfabric
from .bundle_solver_base import BundleSolverBase


class IteratingBundleSolverBase(BundleSolverBase):

    def __init__(self, settings):
        super(IteratingBundleSolverBase, self).__init__(settings)
        self.no_iterations = settings['no_iterations']

    def GetDefaultSettings(self):
        default_settings = super(IteratingBundleSolverBase, self).GetDefaultSettings()
        default_settings['no_iterations'] = 10
        return default_settings

    def Run(self):
        for i in range(self.no_iterations):
            super(IteratingBundleSolverBase, self).Run()
