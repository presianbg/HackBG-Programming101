#!/usr/bin/python3
from songs_class import Songs
from playlist_class import Playlist, NoMoreSongsInPlaylist
from musiccrawler_class import MusicCrawler
import readline
import shlex
from subprocess import Popen, PIPE

print('Welcome to WaaDaaFaak Python Player')
print('To get help, enter `help`.')
plist = None
p = None

while True:
    cmd, *args = shlex.split(input('Ener Command> '))

    if cmd == 'exit':
        if p:
            p.kill()
        break

    elif cmd == 'help':
        print('load "playlist_path/name.json"  : Loading Playlist from File')
        print('generate "dir_path/name"        : Generating playlist from all mp3, ogg or flac files in this dir')
        print('playlist                        : Displaying current playlist')
        print('play <number>                   : Playing the song with this number in the playlist')
        print('stop                            : stops playing current song')
        print('next                            : playing next song')

    elif cmd == 'load':
        if args:
            if plist:
                quest = input('There is {} loaded, do you want to overwrite it? Y/N> '.format(plist.name))
                if quest == "Y":
                    plist = Playlist.load(args[0])
                    print ("{} loaded".format(plist.name))
                else:
                    print ("Playlist Not Changed")
            else:
                plist = Playlist.load(args[0])
                print ("{} loaded".format(plist.name))
        else:
            print ('No Playlist Selected')

    elif cmd == 'generate':
        if args:
            if plist:
                quest = input('There is {} loaded, do you want to overwrite it? Y/N> '.format(plist.name))
                if quest == "Y":
                    crawler = MusicCrawler(args[0])
                    plist = crawler.generate_playlist()
                    print ("{} generated".format(plist.name))
                else:
                    print ("Playlist Not Changed")
            else:
                crawler = MusicCrawler(args[0])
                plist = crawler.generate_playlist()
                print ("{} generated".format(plist.name))
        else:
            print ('No Playlist Selected')

    elif cmd == "playlist":
        if plist:
            plist.pprint_playlist()
        else:
            print ("No playlist to display")

    elif cmd == 'play':
        if args:
            if p:
                p.kill()
            p = Popen(["mpg123", '-C', plist.rocklist[int(args[0])-1].songpath], stdout=PIPE, stderr=PIPE)
            print ("Playing - {}".format(plist.rocklist[int(args[0])-1].title))
            plist.song_number = int(args[0])
        else:
            print ('No song Selected')

    elif cmd == 'stop':
        p.kill()

    elif cmd == 'next':
        if p:
            p.kill()
        try:
            nsong = plist.next_song()
            p = Popen(["mpg123", '-C', nsong.songpath], stdout=PIPE, stderr=PIPE)
            print ("Playing - {}".format(nsong.title))
        except NoMoreSongsInPlaylist:
            print ("No more Songs in Playlist")

    else:
        print('Unknown command: {}'.format(cmd))
