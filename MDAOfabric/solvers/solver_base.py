from abc import ABC, abstractmethod
import MDAOfabric

class SolverBase(ABC):
    """Abstract base class for all solvers

    """
    def __init__(self, settings):
        self.settings = settings
        self.settings.ValidateAndAssignDefaults(self.GetDefaultSettings())

    @abstractmethod
    def GetDefaultSettings(self):
        """Provides default settings

        Must be implemented by every solver to provide the default settings for validation and assignment
        :return: MDAOfabric.Settings object containing the expected defaults
        """
        pass

    @abstractmethod
    def Initialize(self):
        """Initialize computation of results

        Must be implemented to trigger all actions needed by the solver to enable results-computation afterwards
        :return: None
        """
        pass

    @abstractmethod
    def Run(self):
        """Compute all results

        Must be implemented to trigger all computations of results
        :return: None
        """
        pass

    @abstractmethod
    def Finalize(self):
        """Finalize outputs and cleanup

        Must be implemented to trigger all final results writing and memory deallocation
        :return: None
        """
        pass

    def RunFullSequence(self):
        """Run all from input files to results written

        This is only intended to be run by the user
        :return: None
        """
        self.Initialize()
        self.Run()
        self.Finalize()
