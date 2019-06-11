import unittest

import MDAOfabric
from MDAOfabric.tests import *

# set how much is output ('ERROR' will only print logs of error level and above)
MDAOfabric.log.SetConsoleLevel('ERROR')

# run all tests
if __name__ == '__main__':
    unittest.main()