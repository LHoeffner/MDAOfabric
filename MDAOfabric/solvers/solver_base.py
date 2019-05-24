from abc import ABC, abstractmethod
import MDAOfabric

class SolverBase(ABC):
    def __init__(self, settings):
        self.settings = settings

    @abstractmethod
    def GetDefaultSettings(self):
        pass

    @abstractmethod
    def Initialize(self):
        pass

    @abstractmethod
    def Run(self):
        pass

    @abstractmethod
    def Finalize(self):
        pass

    def RunFullSequence(self):
        self.settings.ValidateAndAssignDefaults(self.GetDefaultSettings())
        self.Initialize()
        self.Run()
        self.Finalize()
