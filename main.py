from pytube.exceptions import VideoUnavailable
import pytube
import sys


# run whenever chunk is downloaded, the stream, the data chunk, the bytes
def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write("\r[%s%s] %d%%" % ('=' * int(percentage_of_completion / 2),
    ' ' * (50 - int(percentage_of_completion / 2)), percentage_of_completion))
    sys.stdout.flush()


# run after video has been fully downloaded, the stream and the file path
def complete_func(stream, file_path):
    sys.stdout.write('\n')  # Finish progress bar row
    print("download completed")


# create object of YouTube class
def url_identifier(url_link):
    global yt
    yt = pytube.YouTube(
        url_link,
        # run whenever chunk is downloaded, the stream, the data chunk, the bytes
        on_progress_callback=progress_func,

        # run after video has been fully downloaded, the stream and the file path
        on_complete_callback=complete_func,

        # sign in account
        use_oauth=False,
        allow_oauth_cache=True)


# choosing resolution
def resolution_det():
    print(f"Downloading video: {yt.title}")
    if y == 1:
        yt.streams.get_highest_resolution().download()

    elif y == 2:
        yt.streams.get_lowest_resolution().download()


#  choosing Playlist or Single Video
while True:
    try:
        x = int(input("Which one will you download?/n 1- Single Video/n 2- Playlist/n Enter 1 or 2: "))
        if x == 1 or x == 2:
            break
        else:
            print("Error, try again")
    except:
        print("Error, try again.")

# choosing resolution
while True:
    try:
        y = int(input("In what resolution will you download??/n 1- Highest /n 2- Lowest/n Enter 1 or 2: "))
        if y == 1 or y == 2:
            break
        else:
            print("Error, try again")
    except:
        print("Error, try again.")


url = input("Enter video url: ")  # url request
path = ""  # address request
yt = pytube.YouTube("https://youtu.be/FXvtujVDXrQ?si=Q3ZMqlcpACQo8Dbb")

# download single video
if x == 1:
    while True:
        try:
            url_identifier(url)

        except:
            print("url error, try again")
            url = input("Enter video url: ")

        else:
            resolution_det()
            break

# download Playlist
else:
    p = pytube.Playlist(url)

    while True:
        try:
            for urls in p.video_urls:
                try:
                    url_identifier(urls)

                except VideoUnavailable:
                    print(f'Video {urls} is unavailable, skipping.')

                else:
                    resolution_det()
            break

        except:
            print("url error, try again")
            url = input("Enter video url: ")


"""
print(yt.title)  # başlık yazdırma
print(yt.streams)  # akışları görme
print(yt.captions)  # altyazılardaki diller
p = Playlist("playlist veya playlistteki video linki")  #work with playlist
s = Search('YouTube Rewind')  # search YouTube
len(s.results)  # Search results len
print(s.results) # search results
s.get_next_results()  # request append additional results to the .results attribute

streams.get_highest_resolution().download()
stream = yt.streams.get_by_itag(22) #  istediğin streami seçip kaydetmeni sağlıyor
stream.downland() #  istediğin streami indirmeni sağlıyor
"""

