import unittest
import MDAOfabric


class TestSettingsClass(unittest.TestCase):

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
        settings = MDAOfabric.Settings.FromFile('test_files/smallest.json')
        self.assertEqual(self.small_reference_dict, settings)

    def test_validation(self):
        settings = MDAOfabric.Settings(self.small_reference_dict)
        defaults = MDAOfabric.Settings(self.small_reference_dict)

        # exception should be raised if same key uses different type
        settings['surface_opt'] = 1
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

        # exception should be raised if key missing in defaults
        del defaults['surface_opt']
        with self.assertRaises(Exception):
            settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')

    def test_default_assign(self):
        settings = MDAOfabric.Settings(self.small_reference_dict)
        defaults = MDAOfabric.Settings(self.small_reference_dict)
        del settings['surface_opt']
        settings.ValidateAndAssignDefaults(defaults, 'TestSettingsClass')
        self.assertEqual(self.small_reference_dict, settings)


if __name__ == '__main__':
    unittest.main()