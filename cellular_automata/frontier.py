class frontier:
    def __init__(self, frontier):
        if frontier == "0":
            self.is_on = self.open_0
        elif frontier == "1":
            self.is_on = self.open_1
        elif frontier == "r":
            self.is_on = self.reflex
        elif frontier == "c":
            self.is_on = self.circular

    def open_0(self, m, r, c):
        return 0

    def open_1(self, m, r, c):
        return 1

    def reflex(self, m, r, c):
        i = r
        j = c
        if r < 0 or r >= m.shape[0]:
            i = abs(r + 1) if r < 0 else m.shape[0] - (r - m.shape[0] + 1)
        if c < 0 or c >= m.shape[1]:
            j = abs(c + 1) if c < 0 else m.shape[1] - (c - m.shape[1] + 1)
        return m[i, j]

    def circular(self, m, r, c):
        return m[r % m.shape[0], c % m.shape[1]]
