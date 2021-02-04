import wget
def main(): #Menu principal
	print("Bienvenue dans DownloadOS\n Merci d'écrire le chiffre correspondant a votre choix\n")
	os=["1- Windows","2- Linux","3- MacOS","4- MS-Dos","5- Quitter le programme"]
	for i in range(len(os)):
		print(os[i])
	choix=int(input("Votre choix ?"))
	if choix==1 :
		windows() #Windows
	if choix==2 :
		linux() #Linux
	if choix==3:
		macos() #MacOS
	if choix==4:
		msdos() #MS-Dos
	if choix==5:
		exit() #Bye bye
	else:
		main() #C'est pas du pourtant

def windows():
	print("Quel version de windows souhaitez-vous ?")
	winver=["1- Windows 1.0","2- Windows 2.x","3- Windows 3.x","4- Windows 95","5- Windows 98","6- Windows 2000","7- Windows NT 3.x","8- Windows NT 4.0","9- Windows ME","10- Windows XP","11- Windows Serveur 2003","12- Windows Vista","13- Windows 7","14- Windows Serveur 2008","15- Windows 8","16- Windows Server 2012","17- Windows 8.1","18- Windows Serveur 2012 R2","19- Windows 10","20- Windows Serveur 2016","21- Windows Serveur 2019","22- Retourner au menu principal","23- Quitter le programme"]
	for i in range(len(winver)):
		print(winver[i])
	choix=int(input("Votre choix ?"))
	if choix==1:
		windows1() # Widnows 1.0 -> Ok
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
	dl('https://www.dropbox.com/s/9wkr5lrgvjqmupb/Win1.03.zip?dl=1','Win1.03.zip')
	windows()

def windows2(): #Windows 2.x
	print("Choix de version")
	ver=["1- Windows 2.03","2- Windows 2.10/286","3- Windows 2.11/286 (3.5)","4- Windows 2.11 (5.25"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?"))
	if choix==1:
		dl('https://www.dropbox.com/s/6ua3948mtqy0s3c/Win2.03.zip?dl=1','Win2.03.zip')
		windows()
	if choix==2:
		dl('https://www.dropbox.com/s/tml2c2taehan7gd/Win_2.10_286.zip?dl=1','Win_2.10_286.zip')
		windows()
	if choix==3:
		dl('https://www.dropbox.com/s/vg1of0pjgu1mhds/Win_2.11_286_35.zip?dl=1','Win_2.11_286_35.zip')
		windows()
	if choix==4:
		dl('https://www.dropbox.com/s/kap5fg79lsa01w2/Win2.11_286_525.zip?dl=1','Win2.11_286_525.zip')
		windows()
	else:
		windows2()

def dl(url,filename):
	print("Démarrage du téléchargement")
	wget.download(url,filename)
	print("Téléchargement terminé, le fichier se trouve dans le même dossier que le script")
main()