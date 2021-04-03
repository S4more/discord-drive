import youtube_dl
class VideoDownloader():

    def download(self, link: str, title: str) -> str:
        '''
        Downloads a video and returns the extension of the downloaded video.
        '''
        ydl_opts = {'noplaylist': True, 'outtmpl': f"./imgs/{title}.%(ext)s"}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link)
            try:
                return info['ext']
            except KeyError: # It could be facebook
                return info['entries'][0]['ext']


if __name__ == '__main__':
    vd = VideoDownloader()
    print(vd.download("https://www.facebook.com/groups/1573953756236079/permalink/1585387575092697/", "aha"))
