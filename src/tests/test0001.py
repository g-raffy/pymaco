from pymaco import MachineConfigurator
from modules.ageofempiresgold import AgeOfEmpiresGold
def configure_graffyws2():

    configurator = MachineConfigurator()
    configurator.add_config(AgeOfEmpiresGold(iso_file_location='/home/graffy/soft/iso/Microsoft-AgeOfEmpiresGoldEdition.iso'))
    configurator.configure()

configure_graffyws2()
