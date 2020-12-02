class RandomColours:

    def __init__(self, random, mote, time):
        self.random = random
        self.mote = mote
        self.time = time

    def displayColours(self):
        random_number = self.random.randint(0, 16777215)
        hex_number = str(hex(random_number))
        hex_number = '#' + hex_number[2:]
        print('A  Random Hex Color Code is :', hex_number)

        r, g, b = tuple(int(hex_number.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

        for channel in range(1, 5):
            for pixel in range(16):
                self.mote.set_pixel(channel, pixel, r, g, b)
        self.mote.show()
        self.time.sleep(1)
