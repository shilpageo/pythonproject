#duck typing means dynamic typing

class Swift:
    def start(self):
        print("swift car starts")

    def accelarate(self):
        print("swift car accelarating functionality")

    def breaks(self):
        print("swift car break method")

    def stop(self):
        print("swift car stopping")


class Seltos:
    def start(self):
        print("seltos car starts")

    def accelarate(self):
        print("seltos car accelarating functionality")

    def breaks(self):
        print("seltos car break method")

    def stop(self):
        print("seltos car stopping")

class Person:
    def drive(self,car):
        car.start()
        car.accelarate()
        car.breaks()
        car.stop()
p=Person()
sel=Swift()
p.drive(sel)
