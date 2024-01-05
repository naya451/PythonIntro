

class Shared:
    local = 0
    live = 0
    objs = 0
    total = 0
    def __init__(self):
        Shared.live += 1
        Shared.objs += 1
    def __del__(self):
        Shared.live -= 1
    def __str__(self):
        return '|'+ str(Shared.objs) + '/' + str(Shared.live) + '/' + str(Shared.total) + '/' + str(self.local) + '|'
    def __invert__(self):
        self.local += 1
        Shared.total += 1
        return self.local
