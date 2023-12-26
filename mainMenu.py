import addNewMusic_possible_fix
import addStyle
import filterStyle
import removeSongMain
import musicReview
import prevalenceMusic
import rankingPlaylist
import bestRankStyleMain
import playlistManual_possible_fix

main_menu = """
\033[1m 1 \033[0;0m manage database
\033[1m 2 \033[0;0m generate random playlist
\033[1m 3 \033[0;0m create personalized playlist
\033[1m 4 \033[0;0m create playlist by filters
\033[1m 5 \033[0;0m quick play
\033[1m 0 \033[0;0m exit
 =>"""

submenu_1 = """
\033[1m 1 \033[0;0m add new song
\033[1m 2 \033[0;0m delete song
\033[1m 3 \033[0;0m create new music style
\033[1m 4 \033[0;0m the most popular songs in playlists
\033[1m 5 \033[0;0m highest rated songs
\033[1m 0 \033[0;0m exit
 => """

submenu_2 = """
\033[1m 1 \033[0;0m show songs per style
\033[1m 2 \033[0;0m expand playlist info
\033[1m 3 \033[0;0m play
\033[1m 0 \033[0;0m back
 => """

submenu_3 = """
\033[1m 1 \033[0;0m apply filters
\033[1m 2 \033[0;0m rate song
\033[1m 3 \033[0;0m add song to playlist
\033[1m 0 \033[0;0m back
 => """

submenu_4 = """
\033[1m 1 \033[0;0m create playlist
\033[1m 2 \033[0;0m show playlist rankings
\033[1m 3 \033[0;0m show playlists by style
\033[1m 0 \033[0;0m back
 => """

submenu_5 = """
\033[1m 1 \033[0;0m random
\033[1m 2 \033[0;0m pick playlist
\033[1m 0 \033[0;0m back
 => """

welcome_message = "WELCOME TO JUKEBOTIFY!"
print("\n",welcome_message.center(40, "#"))

def subMenu_1():
    second_input = -1
    while second_input != 0:
        second_input = input(print(submenu_1))
        match(second_input):
            case("1"):
                addNewMusic_possible_fix.addMusic()
            case("2"):
                removeSongMain.removeSongFun()
            case("3"):
                addStyle.addStyle()
            case("4"):
                prevalenceMusic.songRecurrence()
            case("5"):
                bestRankStyleMain.rankByStyle()
            case("0"):
                return
            case(_):
                subMenu_1()

def subMenu_2():
    second_input = -1
    while second_input != 0:
        second_input = input(print(submenu_2))
        match(second_input):
            case("1"):
                print(filterStyle.applyFilters(["style", "band", "year"], "data/tableMusic.csv"))
            case("2"):
                print("case 2")
            case("0"):
                return
            case(_):
                subMenu_2()

def subMenu_3():
    second_input = -1
    while second_input != 0:
        second_input = input(print(submenu_3))
        playlistManual_possible_fix.playlistManualFun()
        match(second_input):
            case("1"):

                print("NOT ADDED YET") # APPLY FILTERS
                return
            case("2"):
                musicReview.song_rating()
                return
            case("3"):
                addNewMusic_possible_fix.addMusic()
                return
            case("4"):
                print("NOT ADDED YET") # START PLAYING PLAYLIST
                return
            case("0"):
                return
            case(_):
                subMenu_3()

def subMenu_4():
    second_input = -1
    while second_input != 0:
        second_input = input(print(submenu_4))
        match(second_input):
            case("1"):
                print("NOT ADDED YET") # CREATE PLAYLIST BY FILTERS
                return
            case("2"):
                rankingPlaylist.playlistsRanking()
                return
            case("3"):
                print("NOT ADDED YET") # SHOW PLAYLISTS BY STYLE
                return
            case("0"):
                return
            case(_):
                subMenu_4()

def subMenu_5():
    second_input = -1
    while second_input != 0:
        second_input = input(print(submenu_5))
        match(second_input):
            case("1"):
                print("NOT ADDED YET") # RANDOM PLAYBACK
                return
            case("2"):
                print("NOT ADDED YET") # PICK PLAYLIST
                return
            case("0"):
                return
            case(_):
                subMenu_5()

def mainMenu():
    first_input = -1
    while first_input != 0:
        first_input = input(print(main_menu))
        match(first_input):
            case("1"):
                subMenu_1()
            case("2"):
                subMenu_2()
            case("3"):
                subMenu_3()
            case("4"):
                subMenu_4()
            case("5"):
                subMenu_5()
            case("0"):
                return
            case(_):
                mainMenu()
mainMenu()
