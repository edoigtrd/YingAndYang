import os

import pygame

from config import config


class sound:
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)
        self.name = path.split('/')[-1].split('.')[0]

    def play(self):
        self.sound.play()


class music:
    def __init__(self, path):
        self.path = path
        self.music = pygame.mixer.music.load(path)
        self.name = path.split('/')[-1].split('.')[0]

    def play(self):
        pygame.mixer.music.play()

    def loop(self):
        pygame.mixer.music.play(-1)


class audio_collection:
    def __init__(self):
        self.sounds = []
        self.music = []
        self.names = []
        self.macros = {}

    def __getitem__(self, name):
        if name in self.macros.keys():
            name = self.macros[name]
        for i in self.sounds:
            if i.name == name:
                return i
        for i in self.music:
            if i.name == name:
                return i
        raise KeyError(name)

    def append(self, audio, type="sound"):
        if type == "sound":
            self.sounds.append(audio)
        elif type == "music":
            self.music.append(audio)
        else:
            raise TypeError(f"Type must be 'sound' or 'music', not {type}")
        self.names.append(audio.name)

    def play(self, name, loop=False):
        if config.muted:
            return
        if not name in self.names:
            return
        for i in self.sounds:
            if i.name == name:
                i.play()
                return
        for i in self.music:
            if i.name == name:
                if loop:
                    i.loop()
                else:
                    i.play()
                return


pygame.mixer.init()

audios = audio_collection()

for i in os.listdir('sound/sounds'):
    if i.endswith('.mp3'):
        print(f"Loading sound: {i}")
        audios.append(sound('sound/sounds/' + i))

for i in os.listdir('sound/music'):
    if i.endswith('.mp3'):
        print(f"Loading music: {i}")
        audios.append(music('sound/music/' + i), type="music")
