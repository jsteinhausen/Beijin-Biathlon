
class Circle:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Target:
    inv=False
    def __init__(self, height, width, tolerance, circle_low_X, circle_low_Y, circle_high_X, circle_high_Y):
        self.height = height

        self.width = width

        self.tolerance = tolerance
        # Circles are created with the corresponding class
        self.circle_low = Circle(circle_low_X, circle_low_Y)
        self.circle_high = Circle(circle_high_X, circle_high_Y)

    def test_cord(self, min, max, cord):
        if (min <= cord <= max):
            return True
        else:
            return False

    def test_object(self, min_X, max_X, min_Y, max_Y, test_circle):
        if self.test_cord(min_X, max_X, test_circle.x) and self.test_cord(min_Y, max_Y, test_circle.y):
            return True
        else:
            return False

    def test_target(self, low_min_X, low_max_X, low_min_Y, low_max_Y, high_min_X, high_max_X, high_min_Y, high_max_Y,test_circles):
        if self.test_object(low_min_X, low_max_X, low_min_Y, low_max_Y,test_circles[0]):
            if self.test_object(high_min_X, high_max_X, high_min_Y, high_max_Y,test_circles[1]):
                return True
        else:
            return False

    def is_this_targent(self, test_circles):

        low_min_X = self.circle_low.x * (1 - self.tolerance)
        low_max_X = self.circle_low.x * (1 + self.tolerance)
        low_min_Y = self.height - self.circle_low.y * (1 + self.tolerance)
        low_max_Y = self.height - self.circle_low.y * (1 - self.tolerance)
        high_min_X = self.circle_high.x * (1 - self.tolerance)
        high_max_X = self.circle_high.x * (1 + self.tolerance)
        high_min_Y = self.height - self.circle_high.y * (1 + self.tolerance)
        high_max_Y = self.height - self.circle_high.y * (1 - self.tolerance)
        inv_high_min_Y = high_min_Y #self.circle_high.y * (1 - self.tolerance)
        inv_high_max_Y = high_max_Y #self.circle_high.y * (1 + self.tolerance)
        inv_low_min_X = self.width - self.circle_low.x * (1 + self.tolerance)
        inv_low_max_X = self.width - self.circle_low.x * (1 - self.tolerance)
        inv_low_min_Y = low_min_Y  # self.circle_low.y * (1 - self.tolerance)
        inv_low_max_Y = low_max_Y # self.circle_low.y * (1 + self.tolerance)
        inv_high_min_X = self.width - self.circle_high.x * (1 + self.tolerance)
        inv_high_max_X = self.width - self.circle_high.x * (1 - self.tolerance)

        if (
        self.test_target(low_min_X, low_max_X, low_min_Y, low_max_Y, high_min_X, high_max_X, high_min_Y, high_max_Y,test_circles)):
            return True, False

        elif (
        self.test_target(inv_low_min_X, inv_low_max_X, inv_low_min_Y, inv_low_max_Y, inv_high_min_X, inv_high_max_X,
                         inv_high_min_Y, inv_high_max_Y,test_circles)):
            return True, True
        else:
            return False, False

    def get_inv_target(self):
        self.inv=True
        inv_target=Target(self.height,self.width,self.tolerance,self.height-self.circle_low.x,self.width-self.circle_low.y,self.width-self.circle_high.x,self.height-self.circle_high.y)
        return inv_target

