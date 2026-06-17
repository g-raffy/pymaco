from pymaco.debian.packagesystem import DebianPackageSystem

class MachineConfigurator(object):

    def __init__(self):
        self.package_system = DebianPackageSystem(self)
    
    def install_package(self, package_id):
        """
        :param str package_id:
        """
        self.package_system.install_package(package_id)
        