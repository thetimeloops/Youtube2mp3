import youtube_dl

print(r'''

                                                                         
 __ __  _____  _____  _____  _____  _____  _____  ___  _____  _____  ___ 
|  |  ||     ||  |  ||_   _||  |  || __  ||   __||_  ||     ||  _  ||_  |
|_   _||  |  ||  |  |  | |  |  |  || __ -||   __||  _|| | | ||   __||_  |
  |_|  |_____||_____|  |_|  |_____||_____||_____||___||_|_|_||__|   |___|
                                                                         
                ------------------------------------------------------
                |    [+] Converts Youtube video to mp3 format [+]    |
             
                |    [+] Fast downloading (Threads included) [+]     |
                ------------------------------------------------------
                
                
''')


class MP3:
    def __init__(self):
        self.you=youtube_dl.YoutubeDL(self.getOptions())

    def hook(self,d):
        if  d['status'] == 'finished':
            print('''
            
                    DONE DOWNLOADING..
                    CONVERTING TO MP3 FORMAT NOW!

            ''')

    
    def getOptions(self):
        return{
            'format':'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192',
            }],
            'progress_hooks':[self.hook],
        }
    
    def startDownload(self,url):
        self.you.download([url]);

downloader=MP3()
url=input("Enter youtube url (USE HTTPS) ?>> ")
downloader.startDownload(url)