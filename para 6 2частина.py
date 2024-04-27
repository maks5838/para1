# class AudioPlayer:
#     def play_audio(self):
#         print("Playing audio...")
#
# class VideoPlayer:
#     def play_video(self):
#         print("Playing video...")
#
# class MultimediaPlayer(AudioPlayer, VideoPlayer):
#     def play(self):
#         self.play_audio()
#         self.play_video()
#         print("Playing multimedia content...")
# player = MultimediaPlayer()
# player.play()













class Engine:
    def start(self):
        print("Двигун запущено")

    def charge(self):
        pass


class ElectricVehicle:
    def start(self):
        pass

    def charge(self):
        print("Процес зарядки")


class HybridCar(Engine, ElectricVehicle):
    def drive(self):
        print("Гібридний автомобіль рухається")


car = HybridCar()
car.start()
car.charge()
car.drive()