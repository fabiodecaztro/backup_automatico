import os
import shutil
from csv import DictReader
from pathlib import PurePath

def CopiarOrigemDestino(nomeArquivo):
    with open(nomeArquivo) as meuCsv:
        reader = DictReader(meuCsv)
        for linha in reader:
            origin = linha['origem']
            destiny = linha['destino']
            if os.path.exists(destiny):
                nome = PurePath(origin).name
                destiny = os.path.join(destiny, nome)

            shutil.copytree(origin, destiny)
            print(linha['origem'])
            print(linha['destino'])
            print('*'*60)


if __name__ == "__main__":
    CopiarOrigemDestino('C:\\Users\\fabio\\OneDrive\\Área de Trabalho\\Backup\\diretorio.csv')