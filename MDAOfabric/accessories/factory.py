import MDAOfabric


class Factory:

    def GetPiece(self, type_string, settings):
        class_ = self.GetClass(type_string)
        return class_(settings)

    def GetClass(self, type_string):
        return getattr(MDAOfabric, type_string)


factory = Factory()
