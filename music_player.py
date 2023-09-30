import pygame
import os

# Initialize pygame
pygame.mixer.init()

# Function to play a song
def play_music(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to pause playback
def pause_music():
    pygame.mixer.music.pause()

# Function to resume playback
def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop playback
def stop_music():
    pygame.mixer.music.stop()

# Function to set the volume
def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Function to list available songs
def list_songs(directory):
    songs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):  # You can add more supported formats
                songs.append(os.path.join(root, file))
    return songs

if __name__ == "__main__":
    music_directory = "D:/QEDGE/HTML TUTORIALS/Musicplayer"  # Change this to your music directory
    songs = list_songs(music_directory)

    if not songs:
        print("No songs found in the specified directory.")
    else:
        print("Available songs:")
        for i, song in enumerate(songs):
            print(f"{i + 1}. {os.path.basename(song)}")

        while True:
            choice = input("Enter the song number you want to play (q to quit): ")

            if choice.lower() == "q":
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(songs):
                    selected_song = songs[choice - 1]
                    play_music(selected_song)
                    print(f"Now playing: {os.path.basename(selected_song)}")

                    while True:
                        action = input("Enter action (play/pause/resume/volume/stop/q): ")

                        if action.lower() == "play":
                            unpause_music()
                        elif action.lower() == "pause":
                            pause_music()
                        elif action.lower() == "resume":
                            unpause_music()
                        elif action.lower() == "stop":
                            stop_music()
                            break
                        elif action.lower() == "q":
                            stop_music()
                            break
                        elif action.lower() == "volume":
                            try:
                                volume = float(input("Enter volume level (0 to 1): "))
                                if 0 <= volume <= 1:
                                    set_volume(volume)
                                else:
                                    print("Invalid volume level. Please enter a value between 0 and 1.")
                            except ValueError:
                                print("Invalid input. Please enter a valid volume level.")
                        else:
                            print("Invalid action. Please enter a valid action.")
                else:
                    print("Invalid song number. Please choose a valid song.")
            except ValueError:
                print("Invalid input. Please enter a valid song number.")
