from hashlib import md5
import os
from tempfile import gettempdir
from typing import BinaryIO, List
from simplecrypt import decrypt, DecryptionException


class KBP:
    _file: BinaryIO
    _plugins: List[bytes]
    _krom_id: List[str]
    _key: str
    _decoded: bytes

    def __init__(self, file: str, krom_id: List[str]) -> None:
        """KromBlastPlugins File Decoder"""
        self._plugins = []
        self._file = open(file, "rb")
        self._krom_id = krom_id
        self._key = bytes(md5(str(self._krom_id).encode("utf-8")).hexdigest(), "utf-8")
        try:
            self._decoded = decrypt(self._key, self._file.read())
        except DecryptionException:
            raise Exception("Invalid KromBlastPlugin file.".format(file))
        for plugin in self._decoded.split(b"\n" + bytes(self._key) + b"\n"):
            self._plugins.append(plugin)
        del self._plugins[0]
    
    def plugin_length(self) -> int:
        """Return the length of the plugins."""
        return len(self._plugins)
    
    def plugin_to_path(self, plugin_key: int) -> str:
        """Return the path of a plugin."""
        open(os.path.join(gettempdir(), "kbp"), "wb").write(self._plugins[plugin_key])
        return os.path.join(gettempdir(), "kbp")