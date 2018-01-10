from steppyr import StepperController
from steppyr.profiles.accel import AccelProfile
from steppyr.drivers.a4988 import A4988Driver

class BarrieDriver():
    def __init__(self):
        self.driver = StepperController(profile=AccelProfile(), driver=A4988Driver(dir_pin=1, step_pin=2, enable_pin=3, ms1_pin=4, ms2_pin=5, ms3_pin=6))

    def test(self):
        self.driver.move(400)
        self.driver.run_until_done()
