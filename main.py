class Track:
    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} {self.duration}'

    def __repr__(self):
        return f'{self.name} {self.duration}'

    def show(self):
        print(f'{self.name} - {self.duration}')

class Album:
    def __init__(self, alb_name, gr_name):
        self.tracks = []
        self.alb_name = alb_name
        self.gr_name = gr_name

    def get_tracks(self):
        print(self.tracks)

    def add_tracks(self, track):
        self.tracks.append(track)

    def info(self):
        print(self.tracks)

        for track in self.tracks:
            info = f'тип - {type(track)}  что на печать выведет - {track}'
            print(info)
            return info

    def info_2(self):
        for track in self.tracks:
            print(f'название - {track.name}  продолжительность - {track.duration}')

    def info_3(self):
        for track in self.tracks:
            print(track)

    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration

        print(duration)
        return duration


tone = Track('Nm', 2)
ttwo = Track('BN', 3)
tthree = Track('FG', 5)

aone = Album('Gh', 'gd')
atwo = Album('gd', 'dgg')

aone.add_tracks(tone)
aone.add_tracks(ttwo)
aone.add_tracks(tthree)

atwo.add_tracks(tone)
atwo.add_tracks(ttwo)
atwo.add_tracks(tthree)

aone.get_duration()
print('')
aone.info()
print('')
aone.info_2()
print('')
aone.info_3()
