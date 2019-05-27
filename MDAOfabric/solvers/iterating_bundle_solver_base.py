from abc import abstractmethod

import MDAOfabric
from .bundle_solver_base import BundleSolverBase


class IteratingBundleSolverBase(BundleSolverBase):
    """Abstract class for iterations containing multiple solvers

    """
    def __init__(self, settings):
        super(IteratingBundleSolverBase, self).__init__(settings)
        self.no_iterations = settings['no_iterations']

    @abstractmethod
    def GetDefaultSettings(self):
        pass

    def Run(self):
        """Run the stack for n iterations

        :return: None
        """
        for i in range(self.no_iterations):
            super(IteratingBundleSolverBase, self).Run()
