#multithreading - used to perform multiple tasks concurrently(multi-tasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                     threading.Thread(target=my_function)

import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")

def take_out_trash():
    time.sleep(2)
    print("You finish taking out trash")

def get_mail():
    time.sleep(4)
    print("You finish getting mail")

# by default these 3 calls happens in order in main thread, one after the other
# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog,args=("Simba"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


#if we don't join the threads, the below message gets printed first. then other chores complete
chore1.join()
chore2.join()
chore3.join() #now all the chores would be completed first , then the program will move forward
print("all chores are complete")