import time

import os
from pathlib import Path
import filetype

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# definir o caminho da pasta download da maquina
DOWNLOAD_FOLDER = str(Path.home() / "Downloads")


class Program(FileSystemEventHandler):

    # função que modifica arquivos ou pastas
    def on_modified(self, event):

        # listar ariquvos da pasta DOWNLOAD
        for filename in os.listdir(DOWNLOAD_FOLDER):

            file_path = os.path.join(DOWNLOAD_FOLDER, filename)

            try:
                # pegar a extensão do arquivo
                kind = filetype.guess(file_path)
                file_extension = kind.extension
                print(file_extension, kind.mime, file_path)
            except:
                print("no extension")

        