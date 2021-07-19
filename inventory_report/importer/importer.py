from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(data):
        pass
