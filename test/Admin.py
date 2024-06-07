# -*- coding: UTF-8 -*-
__author__ = "helios"

from pathlib import Path
from xy_configure.Pair.Section import Section


class Admin(Section):
    name: str | None = "Admin"

    host: str | None = "0.0.0.0"

    debug_port: int | None = 8403

    release_port: int | None = 8404

    logs_path: Path | None = None

    backup_path: Path | None = Path("../workspace/backup/admin/")

    def _load(self):
        ########## sync_data ##########

        self.name = self._sync_data("name", self.name)

        self.host = self._sync_data("host", self.host)

        self.debug_port = self._sync_data("debug_port", self.debug_port)

        self.release_port = self._sync_data("release_port", self.release_port)

        ########## fetch_path ##########

        self.backup_path = self._fetch_path("backup_path", self.backup_path)

        self.logs_path = self._fetch_path("logs_path", self.logs_path)
