def turn_to_angle(self, angle):
    pwnPercent = self.translate(angle, 0.0, 360, 5.0, 10)
    self.p.ChangeDutyCycle(pwnPercent)
    # time.sleep(0.5)
    return pwnPercent