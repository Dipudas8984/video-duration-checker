import os, sys
import itertools
import threading
import time


def get_length(list):
    total_sec = 0
    for i in list:
        video = VideoFileClip(i)
        video_duration = int(video.duration)
        total_sec += video_duration
    return total_sec



def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

t = threading.Thread(target=animate)


#long process here

argv_list = sys.argv

if __name__ == '__main__':
    if len(argv_list) > 1:
        argv_list.pop(0)
        list = argv_list
    else:
        list = [i for i in os.listdir() if '.mp4' in i]
        if len(list) == 0:
            print('No Suppported Video Files here')
            exit()
    t.start()
    from moviepy.editor import VideoFileClip
    hour , mins, secs = convert(get_length(list))
    done = True
    print(f'Total Duration: {hour}:{mins}:{secs}')

