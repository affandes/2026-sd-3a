class TreeNode:
    def __init__(self, data):
        self._data = data
        self.children = []

    def get_children(self):
        print("Get Children... ok")
        # Cari posisi 0
        id_nol = self._data.state.index(0)
        print("Posisi 0 ada di indeks ", id_nol)
        if id_nol == 0:
            c = []
            c.append(self.move_right())
            c.append(self.move_down())
            return c
        elif id_nol == 1:
            c = []
            c.append(self.move_left())
            c.append(self.move_right())
            c.append(self.move_down())
            return c
        elif id_nol == 2:
            c = []
            c.append(self.move_left())
            c.append(self.move_down())
            return c
        elif id_nol == 3:
            c = []
            c.append(self.move_up())
            c.append(self.move_right())
            c.append(self.move_down())
            return c
        elif id_nol == 4:
            c = []
            c.append(self.move_up())
            c.append(self.move_left())
            c.append(self.move_right())
            c.append(self.move_down())
            return c
        elif id_nol == 5:
            c = []
            c.append(self.move_up())
            c.append(self.move_left())
            c.append(self.move_down())
            return c
        elif id_nol == 6:
            c = []
            c.append(self.move_up())
            c.append(self.move_right())
            return c
        elif id_nol == 7:
            c = []
            c.append(self.move_up())
            c.append(self.move_left())
            c.append(self.move_right())
            return c
        elif id_nol == 8:
            c = []
            c.append(self.move_up())
            c.append(self.move_left())
            return c
        
