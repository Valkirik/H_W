class Origin_song:
    def __init__(self, song, year, singer):
        self.song = song
        self.year = year
        self.singer = singer
    def __str__(self):
        return f"'{self.song}' {self.singer} ({self.year})"


song_1 = Origin_song("Dangerous", "1991", "Michael Jackson")
print(song_1)


class Genra:
    def __init__(self, genra):
        self.genra = genra

    def __str__(self):
        return f"{self.genra}"

g = Genra("Rock")
print(g)

class Music_group:
    def __init__(self, name_group):
        self.name_group = name_group

class Covers(Origin_song, Genra, Music_group):
    def __init__(self, song, year, singer, genra, name_group):
        Origin_song.__init__(self, song, year, singer)
        Genra.__init__(self, genra)
        Music_group.__init__(self, name_group)
    def __str__(self):
        return f"'{self.song}'. '{self.name_group}', singer - {self.singer} ({self.year})"

cover_1 = Covers("Creep", "2000", "Richard Cheese", "Launge", "Richard Cheese")
print(cover_1)



class Concerts(Covers, Genra, Music_group):
    def __init__(self, name_group, genra, date, city):
        Music_group.__init__(self, name_group)
        Genra.__init__(self, genra)
        self.city = city
        self.date = date

    def __str__(self):
        return f"'{self.name_group}'. Genra - {self.genra}. {self.city} ({self.date})"

concert_1 = Concerts("Queen", "Rock", "1986", "London")
print(concert_1)













