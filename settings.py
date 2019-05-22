import json


class Settings(dict):
    """MDAOfabric's container for configuration

    Can be initialised from a dictionary a string or file containing a json-style option set.
    It inherits from dictionary and can be read and sliced as such (using settings['key']).
    """
# functions for instantiation
    def __init__(self, settings_dict):
        super(Settings, self).__init__(settings_dict)
        self.CreateTreeOfSettings()

    @classmethod
    def FromString(cls, settings_string):
        """Extends constructor to read from a json-string instead of a dict

        :param settings_string: string in json formatting containing the settings to read
        :return: None
        """
        return cls(json.loads(settings_string))

    @classmethod
    def FromFile(cls, path):
        """Extends constructor to read settings from a json file

        :param path: path to json file to read
        :return: None
        """
        file = open(path, 'r')
        settings_string = file.read()
        file.close()
        return cls.FromString(settings_string)

    def CreateTreeOfSettings(self):
        """Replaces dictionaries in the settings-tree by instances of the Settings-class.

        :return: None
        """
        for key in self:
            value = self[key]
            if isinstance(value, dict) and value:
                self[key] = Settings(value)


# public functions
    def ValidateAndAssignDefaults(self, defaults, reading_class = None):
        for key, val in self.items():

            # check if the current entry also exists in the defaults
            if key not in defaults.keys():
                err_msg = 'Unexpected key "' + key + '" is provided in the settings!'
                # adds name of invoking class to output if provided
                if reading_class:
                    err_msg += ' of class' + reading_class
                err_msg += ' (NOT in the defaults)'
                raise Exception(err_msg)

            # check if the type is the same in the defaults
            if not isinstance(self[key], type(defaults[key])):
                err_msg = 'Unexpected type used by key "' + key + '" in the settings!'
                # adds name of invoking class to output if provided
                if reading_class:
                    err_msg += ' of class' + reading_class
                err_msg += ' (it is "' + str(type(self[key]).__name__) + \
                           '" while the defaults use "' + str(type(defaults[key]).__name__) + '")'
                raise Exception(err_msg)

        # loop the defaults and add the missing entries
        for key_d, val_d in defaults.items():
            if key_d not in self:
                self[key_d] = val_d


