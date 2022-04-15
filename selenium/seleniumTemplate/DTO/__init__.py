from datetime import datetime
class baseDTO:
    def __init__(self):
        VERSION=1
        self.create_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.update_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.__version__ = VERSION

