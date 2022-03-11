from tkinter import messagebox, filedialog
from copiar import CopiarOrigemDestino
from copiar import CopiarOrigemDestino

def continuarSelecao():
    return messagebox.askyesno(title='Adicionar linha', message='Gostaria de adicionar um par Origem/Destino?')

def CriarOrigemDestino(nomeArquivo):
    with open(nomeArquivo, 'w') as dircsv:
        dircsv.write('origem,destino\n')

        while continuarSelecao():
            origem = filedialog.askdirectory()
            destino = filedialog.askdirectory()
            dircsv.write(f'{origem},{destino}\n')
            # continuar = messagebox.askyesno(title='Adicionar linha', message='Gostaria de adicionar novamente um par Origem/Destino?')
if __name__ == '__main__':
    arquivo = 'C:\\Users\\fabio\\OneDrive\\Área de Trabalho\\Backup\\diretorio.csv'
    CriarOrigemDestino(arquivo)
    CopiarOrigemDestino(arquivo)