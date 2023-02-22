class ConfigJsonError(Exception):
    """Appen when the config.ini value is not json serializable"""
    pass

class ModeError(Exception):
    """Appen when the mode of file is not valid"""
    pass

class InvalidWindowParameter(Exception):
    """Appen when a window parameter does not exist"""
    pass

class SubPluginException(Exception):
    """Appen when a subplugin is detected (not implemented)"""
    pass