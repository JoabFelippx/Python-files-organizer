import time

import os
from pathlib import Path
# import filetype
import mimetypes

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# definir o caminho da pasta download da maquina
DOWNLOAD_FOLDER = str(Path.home() / 'Downloads')

destination_folder = {

    'image': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_de_imagem'),
    'video': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_de_video'),
    'audio': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_de_audio'),
    'text': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_de_texto'),
    'pdf': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_pdf'),
    
    'vnd.openxmlformats-officedocument.spreadsheetml.sheet': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_excel'),
    'vnd.ms-excel': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_excel'),
    'vnd.openxmlformats-officedocument.spreadsheetml.template': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_excel'),


    
    'x-bittorrent': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_torrent'),
    'x-zip-compressed': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_winrar'),
    'x-msdownload': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_exe'),
    # 'vnd.openxmlformats-officedocument.presentationml.presentation': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_pptx'),
    'x-tar': os.path.join(DOWNLOAD_FOLDER, 'Arquivos_winrar'),

}


class Program(FileSystemEventHandler):

    # função que modifica arquivos ou pastas
    def on_modified(self, event):

        # listar ariquvos da pasta DOWNLOADS
        for filename in os.listdir(DOWNLOAD_FOLDER):
            cont = 0

            # caminho de origem do arquivo
            source_path = os.path.join(DOWNLOAD_FOLDER, filename)

            try:
                # pega mime do arquivo
                guess_type = mimetypes.guess_type(source_path)
                mimes = (guess_type[0].split('/')[0],
                         guess_type[0].split('/')[1])

                # definir o caminho de destino
                if mimes[0] != 'application':
                    new_path = destination_folder[mimes[0]]
                    new_file_path = os.path.join(new_path, filename)
                
                new_path = destination_folder[mimes[1]]
                new_file_path = os.path.join(new_path, filename)

            except:
                print(filename)
                print("no extension")

            try:
                # verificar se o caminho de destino existe
                if not os.path.exists(new_path):
                    # criar pasta de destino
                    os.mkdir(new_path)
                # examinar se existe arquivos de mesmo nome
                file_exist = os.path.isfile(new_file_path)
                while file_exist:

                    cont += 1

                    # numerar arquivo baseado na quantidade de arquivos com mesmo nome
                    new_filename = str(cont) + '-' + filename
                    new_file_path = os.path.join(
                        new_path, new_filename)
                    file_exist = os.path.isfile(new_file_path)
                    cont = cont

                # mover o arquivo para pasta de destino
                os.rename(source_path, new_file_path)

            except:
                print('there is no path to this extension')


event_handler = Program()

observer = Observer()
observer.schedule(event_handler, DOWNLOAD_FOLDER, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
