#from lib.m2 import hello2
### why does it need lib ???
# from m2 import hello2
### need to have lib

#import lib.m2 # working
import m2

# example of function, just for demo purposes
def hello1(s: str):
    print(f'Hello1 "{s}" from: {__file__}')

def hello3(s: str):
    pass
    hello2(s)
    #m2.hello2(s)

def call_hello2_from_m1():
    import m2
    #lib.m2.hello2('call_hello2_from_m1')   # working
    m2.hello2('call_hello2_from_m1')


if __name__ == "__main__":
    import m2
    m2.hello2('call_hello2_from_m1')
