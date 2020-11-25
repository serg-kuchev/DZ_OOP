class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'Название трека {self.name} его продолжительность {self.duration}'

    # def show(self):
    #     print(f'{self.name} - {self.duration}')

    def __lt__(self, other):
        if not isinstance(other, Track):
            print('Сравнить нельзя')
        return self.duration < other.duration


class Album:
    def __init__(self, alb_name, gr_name):
        self.tracks = []
        self.alb_name = alb_name
        self.gr_name = gr_name

    def get_tracks(self):
        print(self.tracks)

    def add_tracks(self, track):
        self.tracks.append(track)

    def __str__(self):
        return f'Имя группы {self.gr_name} \n' \
               f'Название альбома {self.alb_name} \n' \
               f'Треки: {self.tracks}'
        # for track in self.tracks:
        #     print(f'название - {track.name}  продолжительность - {track.duration}')
        # # for track in self.tracks:
        #     return f'{track.name} {track.duration} мин'



    def info_2(self):
        for track in self.tracks:
            print(f'название - {track.name}  продолжительность - {track.duration}')

    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration
        return duration


tone = Track('Nm', 5)
ttwo = Track('BN', 7)
tthree = Track('FG', 5)

aone = Album('Gh', 'gd')
atwo = Album('gd', 'dgg')

aone.add_tracks(tone)
aone.add_tracks(ttwo)
aone.add_tracks(tthree)

atwo.add_tracks(tone)
atwo.add_tracks(ttwo)
atwo.add_tracks(tthree)

# aone.get_duration()
# print(tone)
# print('')
# aone.info_2()
# print('')
# print(tone > ttwo)
print(aone)