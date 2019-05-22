from abc import ABC, abstractmethod
import MDAOfabric

class SolverBase(ABC):
    def __init__(self, custom_settings):
        # validate settings against defaults
        self.settings = custom_settings
        self.settings.ValidateAndAssignDefaults(self.GetDefaultSettings())

    def GetDefaultSettings(self):
        default_settings = MDAOfabric.Settings('''{
        }''')
        return MDAOfabric.Settings.FromString(default_settings)

    @abstractmethod
    def Initialize(self):
        pass

    @abstractmethod
    def Run(self):
        pass

    @abstractmethod
    def Finalize(self):
        pass
