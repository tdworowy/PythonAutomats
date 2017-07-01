import os

from Skype.SkypeBot.SkypeBot import SkypeBot
from Utils.decorators import logExeption


@logExeption
def main(login, password):

     autentycation = [login,password]
     message = SkypeBot()
     message.loginFacebook(autentycation)
     message.select("Echo")
     message.select("A smiechom i szopom nie było konca")
     message.sendMessageToSelected("Szczęsliwego Nowego roku !! [Auto]")



if __name__ == '__main__':

   f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
   main(f.readline().strip(), f.readline().strip())
   main()
