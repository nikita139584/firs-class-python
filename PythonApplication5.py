class Alphabet:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show_a(self):
        print(self.a)

    def show_b(self):
        print(self.b)

    def show_c(self):
        print(self.c)

    def show_all(self):
        print(self.a, self.b, self.c)


world1 = Alphabet("abc","defg","hijk")
world2 = Alphabet("lmn","op","qrst")
world3 = Alphabet("uvw","x","yz")

world1.show_all()
world2.show_all()
world3.show_all()