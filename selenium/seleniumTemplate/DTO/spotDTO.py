from DTO.__init__ import baseDTO
class spotDTO(baseDTO):
    def __init__(self, name=None, address=None):
        super().__init__()
        self.name = name
        self.address = address