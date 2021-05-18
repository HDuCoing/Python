class Cake:
    """data object for storing a cake
    """

    def __init__(self, pieces = []):
        self.pieces = pieces # stores pieces a integers indicating their size
        # min-max interval of pieces taken, "wraps around"
        self.taken_min = None # inclusive
        self.taken_max = None # exclusive

    def prev(self, index):
        """return index of piece before given index
        """
        return (index - 1) % len(self.pieces)

    def next(self, index):
        """return index of piece before given index
        """
        return (index + 1) % len(self.pieces)

    def is_empty(self):
        """check if all pieces have been taken
        """
        return self.taken_min == self.taken_max != None

    def is_whole(self):
        """check if no pieces have been taken
        """
        return self.taken_min == self.taken_max == None

    def is_taken(self, index):
        """check if piece has already been taken
        """
        if self.is_whole():
            return False
        if self.is_empty():
            return True
        if self.taken_min <= self.taken_max:
            return self.taken_min <= index < self.taken_max
        else: # taken interval wraps around 
            return self.taken_min <= index or index < self.taken_max

    def can_take_piece(self, index):
        """check whether user is allowed to pick piece at given index - for checking user picks
        """
        if self.is_empty():
            return False
        return self.is_whole() or index in [self.prev(self.taken_min), self.taken_max] 

    def take_piece(self, index):
        """mark piece at given index as taken and return its size
        """
        if self.is_empty():
            raise Exception('cannot take piece from empty cake')

        # special case: cake is whole
        if self.is_whole():
            self.taken_min = index
            self.taken_max = (index + 1) % len(self.pieces)
        elif index == self.taken_max:
            self.taken_max = self.next(self.taken_max)
        elif index == self.prev(self.taken_min):
            self.taken_min = self.prev(self.taken_min)
        else:
            raise Exception('invalid piece', str(index))

        return self.pieces[index]
