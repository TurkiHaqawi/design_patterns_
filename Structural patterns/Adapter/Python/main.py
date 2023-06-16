

# Adaptee (Old components/system)
class MediaPlayer:
    def play_audio(slef, filename):
        # Implementation
        print(f"Playing audi with old way, {filename}")


# Adapter Class
class AdapterMediaPlayer(MediaPlayer):
    def __init__(self, intstance_of_new_player): 
        self.intstance_of_new_player = intstance_of_new_player

    def play_audio_(self, filename):
        file_type = self.get_file_type(filename)
        self.intstance_of_new_player.play(filename, file_type)

    def get_file_type(self, filename):
        file_extention = filename.split(".")[-1]
        if file_extention == "mp3":
            return "MP3"
        elif file_extention == "wav":
            return "WAV"
        else: 
            return "Unknown file type"


# Target Interface (New components/system)
class NewAudioPlayer:
    def play(self, filename, file_type):
        # Implementation
        print(f"Playing audio with new way, {filename} and type is {file_type}")


# Old Client
# audio_one = MediaPlayer()
# audio_one.play_audio("turki.mp3")


# New Client
# audio_two = NewAudioPlayer()
# audio_two.play("turki", "mp3")


# Client with Adapter way
audio = NewAudioPlayer()

adapter = AdapterMediaPlayer(audio)

adapter.play_audio_("turki.mp3")