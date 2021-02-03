import wget
def main():
	print("Bienvenue dans DownloadOS\n Merci d'écrire le chiffre correspondant a votre choix\n")
	os=["1- Windows","2- Linux","3- MacOS","4- MS-Dos","5- Quitter le programme"]
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
	if choix==5:
		exit()
	else:
		main()

def windows():
	print("Quel version de windows souhaitez-vous ?")
	winver=["1- Windows 1.0","2- Windows 2.x","3- Windows 3.x","4- Windows 95","5- Windows 98","6- Windows 2000","7- Windows NT 3.x","8- Windows NT 4.0","9- Windows ME","10- Windows XP","11- Windows Serveur 2003","12- Windows Vista","13- Windows 7","14- Windows Serveur 2008","15- Windows 8","16- Windows Server 2012","17- Windows 8.1","18- Windows Serveur 2012 R2","19- Windows 10","20- Windows Serveur 2016","21- Windows Serveur 2019","22- Retourner au menu principal","23- Quitter le programme"]
	for i in range(len(winver)):
		print(winver[i])
	choix=int(input("Votre choix ?"))
	if choix==1:
		windows1()
	if choix==2:
		windows2()
	if choix==3:
		windows3()
	if choix==4:
		windows95()
	if choix==5:
		windows98()
	if choix==6:
		windows2k()
	if choix==7:
		windowsnt3()
	if choix==8:
		windowsnt4()
	if choix==9:
		windowsme()
	if choix==10:
		windowsxp()
	if choix==11:
		windowssrv2k3()
	if choix==12:
		windowsvista()
	if choix==13:
		windows7()
	if choix==14:
		windowssrv2k8()
	if choix==15:
		windows8()
	if choix==16:
		windowssrv2k12()
	if choix==17:
		windows81()
	if choix==18:
		windowssrv2k12r2()
	if choix==19:
		windows10()
	if choix==20:
		windowssrv2k16()
	if choix==21:
		windowssrv2k19()
	if choix==22:
		main()
	if choix==23:
		exit()
	else:
		windows()

def windows1(): #Windows 1.0
	print("Démarrage du téléchargement")
	url='https://www.dropbox.com/s/9wkr5lrgvjqmupb/Win1.03.zip?dl=1'
	wget.download(url,'Win1.03.zip')
	print("Téléchargement terminé, le fichier se trouve dans le même dossier que le script")
	windows()

def template(): #Template quand il n'y a que 1 fichier
	print("Démarrage du téléchargement")
	url=''
	wget.download(url,'filename')
	print("Téléchargement terminé, le fichier se trouve dans le même dossier que le script")
main()