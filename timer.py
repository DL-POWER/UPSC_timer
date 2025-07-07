import time
import playsound3 as playsound
import os
file  = "piep-33489.mp3"
mid_tune_file = "700-hz-beeps-86815.mp3"



num_second = 60
tune_length = 14
mid_tune_length = 4
offset = 2

extra_time_in_minute = 0.5
extra_time_in_minute_15 = 1
extra_time_in_minute_20 = 1
min_10_marks = 7+extra_time_in_minute
min_15_marks = 11+extra_time_in_minute
min_20_marks = 15+extra_time_in_minute


num_10_marks = int(input("num_10_marks: "))
num_15_marks = int(input("num_15_marks: "))
num_20_marks = int(input("num_20_marks: "))

# variables to edit
# num_10_marks = 1
# num_15_marks = 1
# num_second = 40
# min_10_marks = 1
# min_15_marks = 1
#


def countdown_timer(seconds):
    seconds-=tune_length
    seconds-=mid_tune_length
    seconds-=offset
    mid = seconds/2
    while seconds > 0:
        # if(seconds<60):
        print('Update %d' % seconds,end='          \r')
            # print('', end=f'\rUpdate {seconds}')
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
        if(seconds==mid):
            playsound.playsound(mid_tune_file,True)
    playsound.playsound(file, True)
    print("**********************Time's up!********************")


# # Example usage:
# seconds = int(input("Enter the number of seconds for the timer: "))
# countdown_timer(seconds)


# os.system("xset dpms force off")
for i in range(num_10_marks):
    print("Q",i+1)
    countdown_timer(min_10_marks*num_second)


for i in range(num_15_marks):
    print("Q",11+i)
    countdown_timer(min_15_marks*num_second)


for i in range(num_20_marks):
    print("Q",11+i)
    countdown_timer(min_20_marks*num_second)

# countdown_timer(16)



# vlc.MediaPlayer(file).play