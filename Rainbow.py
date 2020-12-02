class Rainbow:

    def __init__(self, mote, time, hsv_to_rgb):
        self.mote = mote
        self.time = time
        self.hsv_to_rgb = hsv_to_rgb
        print('running rainbow effect')

    def rainbow(self):
        h = self.time.time() * 50
        for channel in range(4):
            for pixel in range(16):
                hue = (h + (channel * 64) + (pixel * 4)) % 360
                r, g, b = [int(c * 255) for c in self.hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
                self.mote.set_pixel(channel + 1, pixel, r, g, b)
        self.mote.show()
        self.time.sleep(0.01)
