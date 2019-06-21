import unittest
import os
import MDAOfabric

# makes file import independent from exec directory
small_settings_path = os.path.join(os.path.dirname(__file__), '../test_files/smallest.json')


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.small_reference_dict = {'surface_opt': 'something',
                                     'example_block': {'comment': 'some comment here',
                                                       'solver_type': 'some_solver',
                                                       'start_time': 0.0,
                                                       'deeper_level': {'some_lowerlevel_key': 43,
                                                                        'comment': 'also on lower level'}}}
        self.small_reference_string = '''{
            "surface_opt"       : "something",
            "example_block"       : {
                "comment"       : "some comment here",
                "solver_type"   : "some_solver",
                "start_time"    : 0.0,
                "deeper_level"  : {
                    "some_lowerlevel_key"   : 43,
                    "comment"               : "also on lower level"
                }
            }
        }'''

    def test_string_init(self):
        settings = MDAOfabric.Settings.FromString(self.small_reference_string)
        # creation of settings as subclass of dict
        self.assertEqual(self.small_reference_dict, settings)
        # sub-tree should also be equal
        self.assertEqual(self.small_reference_dict['example_block']['comment'], settings['example_block']['comment'])

    def test_create_tree_of_settings(self):
        settings = MDAOfabric.Settings.FromString(self.small_reference_string)
        # all sub-trees should be of Settings-type (not dict)
        self.assertIsInstance(settings['example_block'], MDAOfabric.Settings)

    def test_file_init(self):
        settings = MDAOfabric.Settings.FromFile(small_settings_path)
        self.assertEqual(self.small_reference_dict, settings)

    def test_validation(self):
        settings = MDAOfabric.Settings.FromString(self.small_reference_string)
        defaults = MDAOfabric.Settings.FromString(self.small_reference_string)

        # exception should be raised if same key uses different type
        settings['surface_opt'] = 1
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

        # exception should be raised if key missing in the defaults
        del defaults['surface_opt']
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

        # also in case the key is missing in a subtree of the defaults
        del defaults['example_block']['deeper_level']['some_lowerlevel_key']
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

    def test_default_assign(self):
        settings = MDAOfabric.Settings.FromString(self.small_reference_string)
        defaults = MDAOfabric.Settings.FromString(self.small_reference_string)

        # deleted setting should be restored from defaults
        del settings['surface_opt']
        settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')
        self.assertEqual(self.small_reference_dict, settings)

        # also in a subtree
        del settings['example_block']['deeper_level']['some_lowerlevel_key']
        settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')
        self.assertEqual(self.small_reference_dict, settings)

    def test_mandatory_settings(self):
        settings = MDAOfabric.Settings.FromString(self.small_reference_string)
        defaults = MDAOfabric.Settings.FromString(self.small_reference_string)

        # should raise error if mandatory setting is missing
        defaults['something_needed'] = '<mandatory_int>'
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

        # also if the settings has the wrong type
        settings['something_needed'] = 'still no integer'
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

        # but not if the setting is set correctly
        settings['something_needed'] = 3
        settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')


if __name__ == '__main__':
    unittest.main()
