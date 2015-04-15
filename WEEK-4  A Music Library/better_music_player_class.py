#!/usr/bin/python3
from playlist_class import Playlist, NoMoreSongsInPlaylist, NoSuchPlaylist
from musiccrawler_class import MusicCrawler
import readline
from subprocess import Popen, PIPE


class MusicPlayer():

    def __init__(self):
        print('Welcome to WaaDaaFaak Python Player')
        print('To get help, enter `help`.')
        self.plist = None
        self.psong = None

    def create_help(self):
        help = ["Here is the list of commands:",
                "",
                "load <playlist_path/name.json>     : Loading Playlist from File",
                "generate <dir_path/name>           : Generating playlist from all mp3, ogg or flac files in this dir",
                "playlist                           : Displaying current playlist",
                "play <number>                      : Playing the song with this number in the playlist",
                "stop                               : stops playing current song",
                "next                               : playing next song"]
        return "\n".join(help)

    def trigger_unknown_command(self):
        unknown_command = ["Error: Unknown command!",
                           "Why don't you type help,",
                           "to see a list of commands."]

        return "\n".join(unknown_command)

    def exit_mplayer(self):
        if self.psong:
            self.psong.kill()

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def check_path(self, command):
        if len(command) > 1:
            path = command[1]

            if len(command) > 2:
                partial_path = []
                for i in range(1, len(command)):
                    partial_path.append(command[i])
                path = " ".join(partial_path)
            if path:
                return path

        print ("No path given! Using ~/Music instead")
        path = None
        return path

    def check_playlist(self):
        if self.plist:
            return True
        return False

    def quest(self):
        quest = input('There is {} loaded, do you want to overwrite it? [Y/N]> '.format(self.plist.name))
        if quest == "Y":
            return True
        elif quest == "N":
            return False

    def load_playlist(self, path):
        if self.check_playlist():
            if self.quest():
                try:
                    self.plist = Playlist.load(path)
                    print ("{} loaded".format(self.plist.name))
                except NoSuchPlaylist:
                    print ("Err: NoSuchPlaylist")
            else:
                print ("Playlist not changed".format(self.plist.name))
        else:
            try:
                self.plist = Playlist.load(path)
                print ("{} loaded".format(self.plist.name))
            except NoSuchPlaylist:
                print ("Err: NoSuchPlaylist")

    def generate_playlist(self, path):
        if self.check_playlist():
            if self.quest():
                self.make_playlist(path)
            else:
                print ("Playlist not changed".format(self.plist.name))
        else:
            self.make_playlist(path)

    def set_pl_param(self, param):
        if param == "True":
            param = True
        else:
            param = False
        return param

    def make_playlist(self, path):
        shuff = input('Shuffle? [True or False] ?> ')
        shuff = self.set_pl_param(shuff)
        repp = input('Repeat? [True or False] ?> ')
        repp = self.set_pl_param(repp)
        plname = input('Name of the playlist?> ')
        if path:
            crawler = MusicCrawler(path)
        elif not path:
            crawler = MusicCrawler()
        self.plist = crawler.generate_playlist(plname, repp, shuff)
        print ("{} generated".format(self.plist.name))

    def show_playlist(self):
        self.plist.pprint_playlist()

    def check_song_num(self, command):
        if len(command) > 1:
            song = int(command[1])

            if song:
                return song
        else:
            return 1

    def play_song(self, song):
        if not self.plist:
            print ("No songs to play")
        elif song > len(self.plist.rocklist):
            print ("Song Number is not in Playlist")
        else:
            self.stop_playing()
            player = self.check_player(self.plist.rocklist[song-1].songpath)
            self.psong = Popen([player, self.plist.rocklist[song-1].songpath], stdout=PIPE, stderr=PIPE)
            print ("Playing - {}".format(self.plist.rocklist[song-1].title))
            self.plist.song_number = song

    def play_next(self):
        self.stop_playing()
        try:
            nsong = self.plist.next_song()
            player = self.check_player(nsong.songpath)
            self.psong = Popen([player, nsong.songpath], stdout=PIPE, stderr=PIPE)
            print ("Playing - {}".format(nsong.title))
        except NoMoreSongsInPlaylist:
            print ("No more Songs in Playlist")

    def check_player(self, song_p):
        if song_p.endswith('.mp3'):
            player = 'mpg123'
            return player
        if song_p.endswith('.ogg') or song_p.endswith('.flac'):
            player = 'ogg123'
            return player

    def save_playlist(self):
        if self.check_playlist():
            self.plist.save()
        print("Saved {}".format(self.plist.name))

    def stop_playing(self):
        if self.psong:
                self.psong.kill()
