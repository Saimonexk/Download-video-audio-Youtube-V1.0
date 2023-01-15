# Download de vídeos e audios do Youtube - Versão 1.0
'''funciona, mas tem 3 problema(s):
- não será feito o download se tiver um video ou audio com o mesmo nome do local onde você escolheu
para fazer o download
- tem que dar ALT + TAB para ver a janela do explorador de arquivos e assim poder
 escolher onde se deseja fazer o download
- Mesmo apertando em "candelar" no explorador de arquivos, o download continua sendo feito'''
from pytube import YouTube
from tkinter import filedialog
from os import rename, path
yt = YouTube(str(input('Cole aqui a url de um vídeo do Youtube aqui: ')))
mp4ou3 = input('Deseja baixar o vídeo ou apenas o audio desse vídeo ? ')
if 'video' in mp4ou3:
    print('Se o explorador de arquivos não abriu, dê ALT + TAB')
    local = filedialog.askdirectory()
    mp4 = yt.streams.get_highest_resolution().download(local)
    print('O download do video de {} foi realizado com êxito.'.format(yt.title))
elif 'audio' in mp4ou3:
    print('Se o explorador de arquivos não abriu, dê ALT + TAB')
    local = filedialog.askdirectory()
    mp3 = yt.streams.filter(only_audio=True).first()
    arquivo_mp3 = mp3.download(output_path=local)
    base, ext = path.splitext(arquivo_mp3)
    novo_arquivo = base + '.mp3'
    rename(arquivo_mp3, novo_arquivo)
    print('O download do audio de {} foi realizado com êxito.'.format(yt.title))
else:
    print('Você não digitou nem audio nem vídeo, execute o código novamente')
