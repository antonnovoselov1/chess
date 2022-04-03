class Accountant:
    def __init__(self):

    def give_sallary(self, worker):
        self.worker = worker


class Pupa(Accountant):
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2

    def do_work(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2


class Lupa(Accountant):
    def __init__(self):



