class Song(object):

#instance function
    def __init__(self,papa):
        self.lyrics = papa #instance attribute
# class function
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
jumla = ["Today is my birthday","She has my birthday"]

happy_bday = Song(jumla)

bulls_on_parade = Song(["WOOOOOEW","JIOJIOJIO","PIOPIOPIOP"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
