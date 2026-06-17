import abc

class IPackageSystem(abc.ABC):

    @abc.abstractmethod
    def install_package(self, package_id):
        pass
