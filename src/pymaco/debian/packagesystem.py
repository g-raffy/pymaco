import subprocess
from pymaco import IPackageSystem

class DebianPackageSystem(IPackageSystem):

    def __init__(self, machine_configurator):
        """
        :param MachineConfigurator machine_configurator:
        """
        self.machine_configurator = machine_configurator

    def install_package(self, package_id):
        subprocess.run(['sudo', 'apt_get', 'install', package_id])
        if package_id == 'playonlinux':
        
            # https://linuxconfig.org/how-to-fix-cannot-open-shared-object-file-libudev-so-0-error-on-ubuntu-18-04-bionic-beaver-linux
            # http://wiki.playonlinux.com/index.php/Troubleshooting_Common_Problems#libudev.so.0_.28libudev.29
            # libudev.so.0 (libudev)
            # err:module:load_builtin_dll failed to load .so lib for builtin L"winebus.sys": libudev.so.0: : cannot open shared object file: No such file or directory

            # Udev is a device manager for the Linux kernel (Wikipedia).
            # This software is not included anymore in Ubuntu from v18.04. 
            if self.machine_configurator.os_name == 'ubuntu':
                if self.machine_configurator.os_version == 18:
                    self.install_package('libudev-dev')
