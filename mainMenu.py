import pandas as pd

import addNewMusic
import addStyle
import filterStyle
import removeSongMain
import musicReview
import prevalenceMusic
import rankingPlaylist
import bestRankStyleMain
import playlistManual
import playlistRules
import playlistAddMusic
import visualization2
import userRankPlaylist

playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

main_menu = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\033[94m                       J U K E B O T I F Y      \033[0;0m
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        \033[1m MAIN MENU \033[0;0m
======================================================================
\033[1m┇ 1️⃣ \033[0;0m database management                                                 ┇
\033[1m┇ 2️⃣ \033[0;0m playlists management                                             ┇
\033[1m┇ 3️⃣ \033[0;0m quick play                                                       ┇
\033[1m┇ 0️⃣ \033[0;0m exit Jukebotify                                                  ┇
======================================================================
🎵  Please select the option by number 🎵 >>> """

submenu_1 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/\033[1mMANAGE DATABASE \033[0;0m
\033[1m 1 \033[0;0m check database
\033[1m 2 \033[0;0m add song to database
\033[1m 3 \033[0;0m delete song from database
\033[1m 4 \033[0;0m create new music style
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/\033[1mMANAGE PLAYLISTS \033[0;0m
\033[1m 1 \033[0;0m create random playlist
\033[1m 2 \033[0;0m create personalized a playlist
\033[1m 3 \033[0;0m edit a playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_1 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mRANDOM PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m start playback
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_2 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mPERSONALIZED PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m create another playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_3 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mEDIT PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m expand playlist
\033[1m 2 \033[0;0m add song to playlist
\033[1m 3 \033[0;0m remove song from playlist
\033[1m 4 \033[0;0m rate playlist
\033[1m 5 \033[0;0m pick another playlist
\033[1m 0 \033[0;0m back
 """

submenu_3 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu\033[1m/QUICK PLAY \033[0;0m
\033[1m 1 \033[0;0m play random song
\033[1m 2 \033[0;0m pick song
\033[1m 3 \033[0;0m check most popular songs in playlists
\033[1m 4 \033[0;0m check highest rated songs
\033[1m 0 \033[0;0m back
 (enter a number) => """

from colorama import Fore, Style

def welcome_message():
    print(Fore.WHITE)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                      ║")
    print(Fore.BLUE + Style.BRIGHT +"║                       J U K E B O T I F Y                            ║"+ Style.RESET_ALL)
    print("║                                                                      ║")
    print("║                🎶 Bringing Your Tunes to Life 🎶                     ║")
    print("║                                                                      ║")
    print("║  Hello there! Welcome to Jukebotify, your ultimate music companion.  ║")
    print("║                                                                      ║")
    print("║  Whether you're into pop, jazz, rock any other style...              ║")
    print("║  ... we've got you covered!                                          ║")
    print("║                                                                      ║")
    print("║  Explore a world of music management, automatic playlist generation, ║")
    print("║  and personalized playlists based on your tastes.                    ║")
    print("║  With Jukebotify, you're in control of your musical journey.         ║")
    print("║                                                                      ║")
    print("║  Get ready to dive into the rhythm and let Jukebotify curate the     ║")
    print("║  perfect playlists for every moment.                                 ║")
    print("║                                                                      ║")
    print("║  Let the music play!                                                 ║")
    print("║                                                                      ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)

# Chame a função para exibir a mensagem de boas-vindas
welcome_message()


def subMenu_1():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_1)
        match(second_input):
            case("1"):
                print(tableMusic_df.to_markdown(index=False))
            case("2"):
                addNewMusic.addMusic()
            case("3"):
                removeSongMain.removeSongDataBaseMenu()
            case("4"):
                addStyle.addStyle()
            case("0"):
                return
            case(_):
                subMenu_1()

def subMenu_2():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2)
        match(second_input):
            case("1"):
                subMenu_2_1()
            case("2"):
                subMenu_2_2()
            case("3"):
                subMenu_2_3()
            case("0"):
                return
            case(_):
                subMenu_2()


def subMenu_2_1():
    playlistRules.playlistRulesFun()
    # second_input = -1
    # while second_input != 0:
    #     playlistRules.playlistRulesFun()
    #     second_input = input(submenu_2_1)
    #     match(second_input):
    #         case("1"):
    #             subMenu_2_1()
    #         case("0"):
    #             return
    #         case(_):
    #             subMenu_2_1()

def subMenu_2_2():
    playlistManual.playlistManualFun()
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2_2)
        match(second_input):
            case("1"):
                subMenu_2_2()
            case("0"):
                return
            case(_):
                subMenu_2_2()

def subMenu_2_3():
    second_input = -1
    playlist_pick = playlistAddMusic.pickPlaylist(playlist_df)
    while second_input != 0:
        second_input = input(submenu_2_3 + "selected playlist[\033[1m" + playlist_pick + "\033[0;0m]\n" + " (enter a number) => ")
        match(second_input):
            case("1"):
                visualization2.view_playlist_songs(playlist_pick)
            case("2"):
                playlistAddMusic.addMusic(playlist_df, tableMusic_df, playlist_pick)
            case("3"):
                removeSongMain.removeSongPlaylist(tableMusic_df, playlist_df, playlist_pick)
            case("4"):
                userRankPlaylist.addRank(playlist_df, playlist_pick)
            case("5"):
                subMenu_2_3()
            case("0"):
                return
            case(_):
                subMenu_2_3()

def subMenu_3():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_3)
        match(second_input):
            case("1"):
                print("NOT ADDED YET") # RANDOM PLAYBACK
                return
            case("2"):
                print("NOT ADDED YET") # PICK PLAYLIST
                return
            case("3"):
                prevalenceMusic.songRecurrence()
            case("4"):
                bestRankStyleMain.rankByStyle()
            case("0"):
                return
            case(_):
                subMenu_3()

def mainMenu():
    first_input = -1
    while first_input != 0:
        first_input = input(main_menu)
        match(first_input):
            case("1"):
                subMenu_1()
            case("2"):
                subMenu_2()
            case("3"):
                subMenu_3()
            case("0"):
                return
            case(_):
                mainMenu()
mainMenu()
