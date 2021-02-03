import wget
def main():
	print("Bienvenue dans DownloadOS\n Merci d'écrire le chiffre correspondant a votre choix\n")
	os=["1- Windows","2- Linux","3- MacOS","4- MS-Dos"]
	for i in range(len(os)):
		print(os[i])
	choix=int(input("Votre choix ?"))
	if choix==1 :
		windows()
	if choix==2 :
		linux()
	if choix==3:
		macos()
	if choix==4:
		msdos()
	else:
		main()

def windows():
	print("Quel version de windows souhaitez-vous ?")
	winver=["1- Windows 1.0","2- Windows 2.x","3- Windows 3.x","4- Windows 95","5- Windows 98","6- Windows 2000","7- Windows NT 3.x","8- Windows NT 4.0","9- Windows ME","10- Windows XP","11- Windows Serveur 2003","12- Windows Vista","13- Windows 7","14- Windows Serveur 2008","15- Windows 8","16- Windows Server 2012","17- Windows 8.1","18- Windows Serveur 2012 R2","19- Windows 10","20- Windows Serveur 2016","21- Windows Serveur 2019"]
	for i in range(len(winver)):
		print(winver[i])
	choix=int(input("Votre choix ?"))
	if choix==1:
		windows1()

def windows1():
	print("Démarrage du téléchargement")
	url='https://www.dropbox.com/s/9wkr5lrgvjqmupb/Win1.03.zip?dl=1'
	wget.download(url,'Win1.03.zip')
	print("téléchargement terminé, merci de retirer le ?dl=1 & la fin du fichier afin d'avoir un fichier fonctionnel")

def template():
	print("Démarrage du téléchargement")
	url=''
	wget.download(url,'filename')
	print("téléchargement terminé, merci de retirer le ?dl=1 & la fin du fichier afin d'avoir un fichier fonctionnel")
main()