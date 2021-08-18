import time

import os
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# definir o caminho da pasta download da maquina
DOWNLOAD_FOLDER = str(Path.home() / 'Downloads')

destination_folder = {

    'AUDIO': ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc', '.msv', '.nmf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx', '.cda'],

    'IMAGES': [".jpeg", ".jpg", '.JPG', ".tiff", ".gif", ".bmp", ".png", ".PNG", ".bpg", ".svg", ".heif", ".psd", '.jfif'],

    'VIDEO': ['.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.nsv', '.roq', '.mxf', '.3g2', '.3gp', '.svi', '.m4v', '.mpg', '.mpeg', '.m2v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.amv', '.asf', '.viv', '.rmvb', '.rm', '.yuv', '.wmv', '.mov', '.qt', '.MTS', '.M2TS', '.TS', '.avi', 'gifv', '.gif', '.drc', '.ogv', '.vob', '.flv', '.mkv', '.webm'],
 
    'WORD': ['.doc', '.dot', '.wbk', '.docx', '.docm', '.dotx', '.dotm', '.docb',
             ],

    'TEXTO': ['.txt'],

    'PDF': ['.pdf'],

    'EXECEL': ['.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', 'xlw'],

    'PowerPoint': ['.ppt', '.pot', '.pps', '.pptx', '.pptm', '.potx', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm'],

    'Winrar': ['.ace', '.taz', '.tbz', '.uu', '.bz', '.jar', '.lha', '.rev', '.tbz2', '.tgz', '.uue', '.xxe', '.7z', '.arj', '.lzh', '.z', '.zip', '.bz2', '.cab', '.gz', '.tar', '.iso', '.rar', '.r00']



}


class Program(FileSystemEventHandler):

    # função que modifica arquivos ou pastas
    def on_modified(self, event):

        # listar ariquvos da pasta DOWNLOADS
        for filename in os.listdir(DOWNLOAD_FOLDER):
            cont = 0

            
            extension = os.path.splitext(
                DOWNLOAD_FOLDER + '/' + filename)[1]
            try:
                # determinar o destino do arquivo
                for c in destination_folder.items():
                    for i in destination_folder[c[0]]:
                        if i == extension:
                            new_path = os.path.join(DOWNLOAD_FOLDER, c[0])
                            path = c[0] + '/' + filename
                            new_file_path = os.path.join(DOWNLOAD_FOLDER, path)
                            # caminho de origem do arquivo
                            source_path = os.path.join(
                                DOWNLOAD_FOLDER, filename)
            except:
                extension = ''
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
                print(extension)
                print('Error')


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
