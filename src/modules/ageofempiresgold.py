from pymaco import ConfModule

class AgeOfEmpiresGold(ConfModule):

    def install(self, machine_configurator, install_disk_location):
        """
        :param MachineConfigurator machine_configurator
        :param DiskLocation install_disk_location: 
        """

        machine_configurator.install_package('playonlinux')

        # managed to get age of empires working on ubuntu 18 with 
        # - installed playonlinux
        # - mount iso on /home/graffy/cdrom
        #    mount -t iso9660 -o loop ./soft/iso/Microsoft-AgeOfEmpiresGoldEdition.iso ./cdrom
        # - from playonlinux :
        #   - install games/age of empires gold edition
        #       - select /home/graffy/cdrom as source
        #       - the age of empires install screen displays
        #       - problem 1: the age of empires install screen complains with a popup that says that this game only supports win95, win98 or winnt 4.
        #       - this is because the wine virtual machine it created by  ($HOME/PlayOnLinux/wineprefix/AgeOfEmpiresI) was in win7. (this can be seen when configuring wineprefix for $HOME/PlayOnLinux/wineprefix/AgeOfEmpiresI from playonlinux)
        #       - here's the script that playonlinux probably used (I found it on https://www.playonlinux.com/en/app-922-Age_Of_Empires_I__Gold_Edition.html)
                    # #!/bin/bash
     
                    # # CHANGELOG
                    # # [?] (2014)
                    # #   First script.
                    # # [Dadu042] (2019-11-05)
                    # #   Wine 1.7.22 -> 2.22 (this sould debug some user cases).
                     
                    # [ "$PLAYONLINUX" = "" ] && exit 0
                    # source "$PLAYONLINUX/lib/sources"
                     
                    # TITLE="Age Of Empires I - Gold Edition"
                    # PREFIX="AgeOfEmpiresI"
                     
                    # POL_SetupWindow_Init
                    # POL_Debug_Init
                    # POL_SetupWindow_presentation "$TITLE" "Microsoft" "" "Tinou" "$PREFIX"
                    # POL_SetupWindow_cdrom
                     
                    # SETUPFILE="AOESETUP.EXE"
                    # [ -e "$CDROM/AOEINST.EXE" ] && SETUPFILE="AOEINST.EXE"
                     
                    # POL_SetupWindow_check_cdrom "$SETUPFILE"
                     
                    # POL_Wine_SelectPrefix "$PREFIX"
                    # POL_Wine_PrefixCreate "2.22"
                     
                    # POL_Wine --ignore-errors "$CDROM/$SETUPFILE"
                    # POL_Wine_WaitExit
                     
                    # cd "$WINEPREFIX/drive_c/windows/system32"
                    # POL_Download "$SITE/divers/dplaydlls-win98se.tar.bz2" "2cc36b915b901e7656ad3b533f83aa7d"
                    # #tar -xvf dplaydlls-win98se.tar.bz2
                     
                    # #POL_Wine_OverrideDLL native,builtin dplayx dpnet dpnhpast dpwsockx
                     
                    # POL_Shortcut "EMPIRES.EXE" "Age Of Empire I"
                    # POL_Shortcut "EMPIRESX.EXE" "Age Of Empire I - Extension"
                     
                    # POL_SetupWindow_Close
                    # exit 0

        #       - the script doesn't specify a windows version, so it was using win7 !!! I think this can be fixed by adding 'Set_OS "win7"' after POL_Wine_PrefixCreate "2.22" but I didn't manage to go as far when using a local script than when using the online official script. I think it can be done though
        #       - anyway, the first install attempt created $HOME/PlayOnLinux/wineprefix/AgeOfEmpiresI with the os win7. We need to change that for win95. This can be when configuring wineprefix $HOME/PlayOnLinux/wineprefix/AgeOfEmpiresI from within playonlinux.
        #       - once this wineprefix hass the right os, we can try to install age of empires again, but this time but reusing the disk image instead of creating a new one. This way, I managed have age of empires's installer to complete (full install). So this fixed problem 1. Hovever, the re is now problem 2: when I try to run the game, the game complains that it doesn't find the cd. This was solved by finding a nocd patch /home/graffy/soft/iso/rdt-aoegldcs, which contains EMPIRES.EXE and EMPIRESX.EXE (rise of rome) that need to be copied over .PlayOnLinux/wineprefix/AgeOfEmpiresI/drive_c/Program\ Files/Microsoft\ Games/Age\ of\ Empires/EMPIRES.EXE and .PlayOnLinux/wineprefix/AgeOfEmpiresI/drive_c/Program\ Files/Microsoft\ Games/Age\ of\ Empires/EMPIRESX.EXE
        #       - then it worked (I need to check but the iso might not be necessary with these exe)
        