class AudioPlayer:
    def play_audio(self):
        print("Playing audio...")

class VideoPlayer:
    def play_video(self):
        print("Playing video...")

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play(self):
        self.play_audio()
        self.play_video()
        print("Playing multimedia content...")
player = MultimediaPlayer()
player.play()