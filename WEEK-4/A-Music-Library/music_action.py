#!/usr/bin/python3
from better_music_player_class import MusicPlayer


def main():
    mp = MusicPlayer()

    while True:
        command = mp.parse_command(input("Enter command>"))

        if mp.is_command(command, "help"):
            print(mp.create_help())

        elif mp.is_command(command, "playlist"):
            if mp.check_playlist():
                mp.show_playlist()
            else:
                print ("No playlist to display")

        elif mp.is_command(command, "load"):
            pt = mp.check_path(command)
            if pt:
                mp.load_playlist(pt)

        elif mp.is_command(command, "generate"):
            pt = mp.check_path(command)
            mp.generate_playlist(pt)

        elif mp.is_command(command, "play"):
            sn = mp.check_song_num(command)
            if sn:
                mp.play_song(sn)

        elif mp.is_command(command, "next"):
                mp.play_next()

        elif mp.is_command(command, "stop"):
                mp.stop_playing()

        elif mp.is_command(command, "save"):
            mp.save_playlist()

        elif mp.is_command(command, "exit"):
            mp.stop_playing()
            break

        else:
            print(mp.trigger_unknown_command())

if __name__ == '__main__':
    main()
