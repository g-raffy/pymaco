from pymaco import ConfModule

class Ur1Vpn(ConfModule):

    def get_dependencies(self):
        return ['openvpn']

    def install(self, machine_configurator):
        """
        :param MachineConfigurator machine_configurator
        """
        # put the launcher in a location that allows the user to add it as favourites (https://askubuntu.com/questions/1026528/adding-custom-programs-to-favourites-of-ubuntu-dock)
        # graffy@graffy-ws2:~$ cat ~/.local/share/applications/firefox-sslsrv.desktop 
        # #!/usr/bin/env xdg-open
        # [Desktop Entry]
        # Version=1.0
        # Type=Application
        # Terminal=false
        # Icon[fr_FR]=firefox
        # Name[fr_FR]=Firefox sslsrv
        # Comment[fr_FR]=Firefox sslsrv
        # Name=Firefox sslsrv
        # Comment=Firefox sslsrv
        # Icon=firefox
        
        

