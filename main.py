from Utopia.lib.Log import log_setup
import logging
from Utopia import Utopia
from Utopia.lib.MM1_Lib.folders import SuperFolders

if __name__ == "__main__":
    version = "2.1.24.S"
    battle_server = "http://utopia-card.000webhostapp.com/Utopia-Serv/"
    file = SuperFolders()
    file.add_folder("Data", "Data")
    file.add_folder("p.load", "Data/p.load")
    file.add_folder("s.load", "Data/s.load")
    file.add_folder("log", "Data/log")
    log_setup(file.get_folder("log"))
    logging.debug("Summary of starting:\n" + " "*34 + "Data_folder: " + file.get_folder("Data") +
                  "\n" + " "*34 + "Principal Server: " + "None" + "\n" + " "*34 + "Battle_Server: "+battle_server +
                  "\n" + " "*34 + "Version: " + version)
    pil_logger = logging.getLogger('PIL')
    pil_logger.setLevel(logging.INFO)
    print("your PlayerId is a list of letters and numbers for the authentication")
    Utopia_class = Utopia(input("PlayerId: "), battle_server, version)
    Utopia_class.mainloop()
    Utopia_class.update_idletasks()
    Utopia_class.quit()
