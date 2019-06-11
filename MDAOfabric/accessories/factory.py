import MDAOfabric


class Factory:
    """generates instances or classes based on their name

    The object MDAOfabric.factory is only searching the MDAOfabric namespace (uppermost level).
    """
    def GetPiece(self, type_string, settings):
        """Get an MDAOfabric of the specified type

        :param type_string: string naming class of the desired obj
        :param settings: MDAOfabric.Settings which are passed on to the initializer
        :return: newly created object of named class
        """
        class_x = self.GetClass(type_string)
        obj_x = class_x(settings)
        return obj_x

    @staticmethod
    def GetClass(type_string):
        """resolves class name to reference

        :param type_string: string naming desired class
        :return: reference to named class
        """
        return getattr(MDAOfabric, type_string)


factory = Factory()
