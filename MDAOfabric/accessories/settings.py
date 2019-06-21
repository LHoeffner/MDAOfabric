import json


class Settings(dict):
    """MDAOfabric's container for configuration and settings

    Can be initialised from a dictionary (less efficient with large depth) a string or file containing a json-style option set.
    It inherits from dictionary and can be read and sliced as such (using settings['key']).
    """
# functions for instantiation
    def __init__(self, settings_dict, check_subdicts=True):
        super(Settings, self).__init__(settings_dict)
        if check_subdicts:
            self.CreateTreeOfSettings()

    @classmethod
    def FromString(cls, settings_string):
        """Extends constructor to read from a json-string instead of a dict

        :param settings_string: string in json formatting containing the settings to read
        :return: None
        """
        return cls(json.loads(settings_string, object_pairs_hook=Settings), check_subdicts=False)

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
            if isinstance(value, dict) and not isinstance(value, Settings) and value:
                self[key] = Settings(value)

# public functions
    def ValidateAndAssignDefaults(self, defaults, branch_key = None, recursive = True):
        """Compares this settings to the provided defaults

        :param defaults: default settings to validate against (of Settings type)
        :param branch_key: optional string naming the caller class for more useful exceptions
        :param recursive: boolean causing the validation to continue through all levels of the settings-tree
        :return: None
        """
        for key, val in self.items():

            # check if the current entry also exists in the defaults
            if key not in defaults.keys():
                err_msg = 'Unexpected key "' + key + '" is provided in the settings!'
                # adds name of invoking class to output if provided
                if branch_key:
                    err_msg += ' (in settings branch "' + branch_key + '")'
                err_msg += ' (NOT in the defaults)'
                raise Exception(err_msg)

            # check if the type is the same in the defaults (for mandatory settings)
            if isinstance(defaults[key], str) and '<mandatory_' in defaults[key]:
                default_type = defaults[key].split('_')[1].split('>')[0]
                if str(type(val).__name__) != default_type:
                    err_msg = 'Unexpected type used by key "' + key + '" in the settings!'
                    # adds name of invoking class to output if provided
                    if branch_key:
                        err_msg += ' (in settings branch "' + branch_key + '")'
                    err_msg += ' (it is "' + str(type(val).__name__) + \
                               '" while the defaults use "' + default_type + '")'
                    raise Exception(err_msg)

            # check if the type is the same in the defaults (for optional settings)
            elif not isinstance(val, type(defaults[key])):
                err_msg = 'Unexpected type used by key "' + key + '" in the settings!'
                # adds name of invoking class to output if provided
                if branch_key:
                    err_msg += ' (in settings branch "' + branch_key + '")'
                err_msg += ' (it is "' + str(type(val).__name__) + \
                           '" while the defaults use "' + str(type(defaults[key]).__name__) + '")'
                raise Exception(err_msg)

            # recursively continue for lower level options if option is set and non-empty subbranch is found
            if recursive and isinstance(val, Settings) and defaults[key]:
                val.ValidateAndAssignDefaults(defaults[key], key, True)

        # loop the defaults and add the missing entries
        for key_d, val_d in defaults.items():
            if key_d not in self:
                # raise Error if mandatory setting is missing
                if isinstance(val_d, str) and '<mandatory_' in val_d:
                    err_msg = 'Missing mandatory key "' + key_d + '" in the settings!'
                    # adds name of invoking class to output if provided
                    if branch_key:
                        err_msg += ' (in settings branch "' + branch_key + '")'
                    raise Exception(err_msg)
                # set default if optional
                else:
                    self[key_d] = val_d


