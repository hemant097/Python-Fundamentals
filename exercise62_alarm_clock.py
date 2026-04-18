import time, datetime, pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file="alarm_song.mp3"
    is_running = True

    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP ⏰⏰⏰⏰⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            #Keeps the program running until the audio file is playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)



if __name__=="__main__":
    wakeup_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(wakeup_time)
