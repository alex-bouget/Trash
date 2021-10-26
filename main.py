from Utopia.StartLib import log_setup, folder_setup
import logging
import sys
from Utopia import Utopia
from Utopia import Lang

file, principal_server, battle_server, folder, lang, client_path = sys.argv


if __name__ == "__main__":
    version = "2.5.28.S"
    log_setup(folder_setup(folder).get_folder("log"))
    logging.debug("Summary of starting:" +
                  "\n" + " " * 34 + "File: " + file +
                  "\n" + " " * 34 + "Data_folder: " + folder +
                  "\n" + " " * 34 + "Principal Server: " + principal_server +
                  "\n" + " " * 34 + "Battle_Server: " + battle_server +
                  "\n" + " " * 34 + "Version: " + version +
                  "\n" + " " * 34 + "Language: " + lang +
                  "\n" + " " * 34 + "Client: " + client_path
                  )
    Lang.lang = lang

    Utopia_class = Utopia(principal_server, battle_server, folder, version, lang, client_path)
    Utopia_class.mainloop()
    Utopia_class.update_idletasks()
    Utopia_class.quit()
