import abc

class ConfModule(abc.ABC):

    @abc.abstractmethod
    def get_dependencies(self):
        pass