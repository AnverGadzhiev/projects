from car import *

def main():
    lada = Bucket(False, True, True, False)
    # lada.pr()
    print(lada.get_state())
    lada.repair(1, 4)
    print(lada.get_state(), lada.get_garage_state())
    del lada

if __name__ == '__main__':
    main()