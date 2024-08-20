# example of function, just for demo purposes
import lib.audio.am1

def hello2(s: str):
    print(f'Hello2 {s} from {__file__}')

def hello_and_play(s: str, f: str):
    print(f'hello_and_play {s} from {__file__}')
    lib.audio.am1.play_audio(f)

