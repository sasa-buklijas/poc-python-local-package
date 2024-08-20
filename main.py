import lib.m1
#import lib.m2

def main():
    print('MAIN -- start')

    #lib.m2.hello2('top level main')
    #hello1('top level main')
    #hello3('top level main')

    lib.m1.call_hello2_from_m1()

    print('MAIN -- end')

if __name__ == "__main__":
    main()
