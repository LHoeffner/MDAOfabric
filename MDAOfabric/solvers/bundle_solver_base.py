from abc import abstractmethod

import MDAOfabric
from .solver_base import SolverBase


class BundleSolverBase(SolverBase):
    """Abstract class for solvers bundling other solvers

    This class is meant to be implemented as a container bundling a number of IO and solver components
    so they can be treated as one solver for creating components or black boxing
    """
    def __init__(self, settings):
        super(BundleSolverBase, self).__init__(settings)
        self.stack = []

    @abstractmethod
    def GetDefaultSettings(self):
        pass

    def Initialize(self):
        """Initializes all pieces in the stack in order

        :return: None
        """
        for piece in self.stack:
            piece.Initialize()

    def Run(self):
        """Runs all pieces in the stack in order

        :return: None
        """
        for piece in self.stack:
            piece.Run()

    def Finalize(self):
        """Finalizes all pieces in the stack in order

        :return: None
        """
        for piece in self.stack:
            piece.Finalize()
