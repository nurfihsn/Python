import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nIs it all inside of my head?", 0.103),
        ("Maybe you still think I don't care", 0.083),
        ("But all I need is you", 0.130),
        ("Yeah, you know it's true, yeah, you know it's true", 0.096),
        ("Forget about where we are and let go", 0.128),
        ("We're so close", 0.143),
        ("If you don't know where to start, just hold on", 0.114),
        ("And don't run, no", 0.25),
        ("We're looking back, we messed around", 0.118),
        ("But that was then and this is now", 0.129),
        ("All we need's enough love to hold us",0.152),
        ("Where we are", 0.25)
    ]
    
    delays = [2.0, 5.0, 7.5, 10.0, 13.0, 16.0, 18.0, 20.5, 23.0, 26.0, 30.0, 34.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
