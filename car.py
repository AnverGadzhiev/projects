from abc import ABC

class Car(ABC):  
    __garage = 0

    def __init__(self, wheels: tuple[bool, ...]):
        self.__wheels = list(wheels)
        self.__garage += 1

    def __del__(self):
        self.__garage -= 1
        del self
        
    def broke(self, numbers: int):
        if (x > 5 and x < 0 for x in numbers):
            for num in  numbers:
                self.__wheels[num] = False
    
    def repair(self, *numbers: int):
        if (x < 5 and x > 1 for x in numbers):
            for num in  numbers:
                self.__wheels[num - 1] = True
        else:
            raise Exception('hh') 
    
    def get_state(self):
        car_state = ''

        for i in range(4):
            state = 'unbroken' if self.__wheels[i] else 'broken'
            car_state += f'{i + 1} wheel is {state}\n'

        return car_state

    def get_garage_state(self):
        return self.__garage


class Bucket(Car):

    def __init__(self, *wheels:bool):
        if len(wheels) == 4:
            super(Bucket, self).__init__(wheels)
        else:
            raise Exception('Need 4 wheels')