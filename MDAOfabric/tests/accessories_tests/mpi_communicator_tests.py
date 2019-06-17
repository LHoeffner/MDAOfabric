import unittest
import mpi4py.MPI as MPI

import MDAOfabric
from MDAOfabric import mpi_world as world

class MPICommunicatorTests(unittest.TestCase):
    #def setUp(self):

    def test_init(self):
        new_world = MDAOfabric.MPICommunicator(MPI.COMM_WORLD)

    def test_root(self):
        self.assertEqual(0, world.root)
        self.assertTrue(world.IsRoot())


if __name__ == '__main__':
    unittest.main()
