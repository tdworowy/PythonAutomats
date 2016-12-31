import os

from SongOfTheDay.songOfTheDay import songOfTheDay


def main(login, password):
    try:
        autentycation = [login,password]
        message = songOfTheDay()
        message.login(autentycation)

        message.select("Echo")
        message.select("A smiechom i szopom nie było konca")
        message.sendMessageToSelected("Szczęsliwego Nowego roku !! [Auto]")
    except Exception  as err:
        print(err)

    finally:
        quit()



if __name__ == '__main__':

   f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
   main(f.readline().strip(), f.readline().strip())
   main()
