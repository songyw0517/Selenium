from datetime import datetime


class baseDTO:
    def __init__(self):
        VERSION=1
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        self.__version__ = VERSION

class spotDTO(baseDTO):
    def __init__(self, name=None, address=None):
        super().__init__()
        self.name = name
        self.address = address