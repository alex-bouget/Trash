from Utopia.StartLib import log_setup, folder_setup
import logging
import sys
from Utopia import Utopia
"""
# battle_server = "http://utopia-card.000webhostapp.com/Utopia-Serv/"
# principal_server = "http://gigly.mygamesonline.org/API/"
battle_server = "http://localhost/Utopia-Server/Battle/"
principal_server = "http://localhost/Utopia-Server/Principal/"
folder = "Data"
"""

file, principal_server, battle_server, folder = sys.argv


if __name__ == "__main__":
    version = "2.2.21.S"
    log_setup(folder_setup(folder).get_folder("log"))
    logging.debug("Summary of starting:\n" + " "*34 + "File: " + file +
                  "\n" + " "*34 + "Data_folder: " + folder +
                  "\n" + " "*34 + "Principal Server: " + principal_server +
                  "\n" + " "*34 + "Battle_Server: " + battle_server +
                  "\n" + " "*34 + "Version: " + version)

    Utopia_class = Utopia(principal_server, battle_server, folder, version)
    Utopia_class.mainloop()
    Utopia_class.update_idletasks()
    Utopia_class.quit()
