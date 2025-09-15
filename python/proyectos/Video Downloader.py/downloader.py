from pytubefix import YouTube
from pytubefix.cli import on_progress

def Download(link):
    yt= YouTube(link,on_complete_callback=on_progress)
    stream = yt.streams.filter(res="720p", progressive=True,file_extension="mp4").first()
    
    if stream is None:
        stream=yt.streams.filter(progressive=True).get_highest_resolution()
        
    try :
        print(f"Descargando: {yt.title} en {stream.resolution}")
        stream.download()
        print("Descarga completada")

    except:
        return "Hubo un error al descargar"
    
