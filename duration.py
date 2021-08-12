import os, sys


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
    
    from moviepy.editor import VideoFileClip


    hour , mins, secs = convert(get_length(list))
    print(f'Total Duration: {hour}:{mins}:{secs}')

