from mpi4py import MPI


class MPICommunicator(object):
    """Extension/Wrapper to the MPI.Comm class

    """
    def __init__(self, comm, root=0):
        self._comm: MPI.Comm = comm
        self._root = root

        # fixed properties stored for quick accessibility
        self._rank = comm.Get_rank()
        self._size = comm.Get_size()

    def IsRoot(self):
        return self._rank == self.root

    @property
    def root(self):
        return self._root

    @root.setter
    def SetRoot(self, root):
        if 0 <= root < self._size:
            self.root = root
        else:
            raise Exception('Trying to set MPI root outside of communicator.')


mpi_world = MPICommunicator(MPI.COMM_WORLD, 0)
