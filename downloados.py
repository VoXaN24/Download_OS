import wget
def main(): #Menu principal
	print("Bienvenue dans DownloadOS\n Merci d'écrire le chiffre correspondant a votre choix\n")
	os=["1- Windows","2- Linux","3- MacOS","4- MS-Dos","5- Quitter le programme"]
	for i in range(len(os)):
		print(os[i])
	choix=int(input("Votre choix ?\n"))
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
		main() #C'est pas dur pourtant

def windows():
	print("Quel version de windows souhaitez-vous ?")
	winver=["1- Windows 1.0","2- Windows 2.x","3- Windows 3.x","4- Windows 95","5- Windows 98","6- Windows 2000","7- Windows NT 3.x","8- Windows NT 4.0","9- Windows ME","10- Windows XP","11- Windows Serveur 2003","12- Windows Vista","13- Windows 7","14- Windows Serveur 2008","15- Windows 8","16- Windows Server 2012","17- Windows 8.1","18- Windows Serveur 2012 R2","19- Windows 10","20- Windows Serveur 2016","21- Windows Serveur 2019","22- Retourner au menu principal","23- Quitter le programme"]
	for i in range(len(winver)):
		print(winver[i])
	choix=int(input("Votre choix ?\n"))
	if choix==1:
		windows1() # Widnows 1.0 -> Ok
	if choix==2:
		windows2() # Windows 2.x -> Ok
	if choix==3:
		windows3() # Windows 3.x -> Ok
	if choix==4:
		windows95() # Windows 95 -> Ok
	if choix==5:
		windows98() #Windows 98 -> Ok
	if choix==6:
		windows2k() #Windows 2000 -> Ok
	if choix==7:
		windowsnt3() #Windows NT 3.x -> OK
	if choix==8:
		windowsnt4() #Windows NT 4.x -> OK
	if choix==9:
		windowsme() # Windows ME -> Ok
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
		windows81() #Windows 8.1 -> Ok
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
	print("Choix de version\n")
	ver=["1- Windows 2.03","2- Windows 2.10/286","3- Windows 2.11/286 (3.5)","4- Windows 2.11 (5.25"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url=[0,'https://www.dropbox.com/s/6ua3948mtqy0s3c/Win2.03.zip?dl=1','https://www.dropbox.com/s/tml2c2taehan7gd/Win_2.10_286.zip?dl=1','https://www.dropbox.com/s/vg1of0pjgu1mhds/Win_2.11_286_35.zip?dl=1','https://www.dropbox.com/s/kap5fg79lsa01w2/Win2.11_286_525.zip?dl=1']
	name=[0,'Win2.03.zip','Win_2.10_286.zip','Win_2.11_286_35.zip','Win2.11_286_525.zip']
	if choix <= len(ver)-1 and choix != 0:
		dl(url[choix],name[choix])
		windows()
	else:
		windows2()
def windows3(): #Windows 3.x
	print("Choix de version\n")
	ver=["1- Windows 3.0a","2- Windows 3.1 (3.5)","3- Windows 3.1 (5.25)","4- Windows 3.1 for Workstation","5- Windows 3.11","6- Windows 3.11 for Workstation"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url=[0,'https://www.dropbox.com/s/jzv4uo24m1ca6qd/Win3.0a.zip?dl=1','https://www.dropbox.com/s/jy56hfp5gwgw6ht/Win3.1_35.zip?dl=1','https://www.dropbox.com/s/ai11n4x7drz9gj0/Win3.1_525.zip?dl=1','https://www.dropbox.com/s/x9rsag2zp05rjwi/Win3.1_workstation.zip?dl=1','https://www.dropbox.com/s/b2wjra9yse8qrcz/Win3.11.zip?dl=1','https://www.dropbox.com/s/xqys6qbksvxsy2e/Win3.11_workstation.zip?dl=1']
	name=[0,'Win3.0a.zip','Win3.1_35.zip','Win3.1_525.zip','Win3.1_workstation.zip','Win3.11.zip','Win3.11_workstation.zip']
	if choix <= len(ver)-1 and choix != 0:
		dl(url[choix],name[choix])
		windows()
	else:
		windows3()
def windows95(): #Windows 95
	print("Choix de version\n")
	ver=["1- Windows 95 RTM (Disquette)","2- Windows 95 RTM","3- Windows 95 OSR 1","4- Windows 95 OSR 2","5- Windows 95 OSR 2.1","6- Windows 95 OSR 2.5"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url=[0,'https://www.dropbox.com/s/vlcxi2uuqr84331/Win95Floppy.zip?dl=1','https://www.dropbox.com/s/xue2u98suw3osgd/Win95.zip?dl=1','https://www.dropbox.com/s/i59js5htmq64oy8/Win95OSR1.zip?dl=1','https://www.dropbox.com/s/1hru7q9uemt814q/Win95OSR2.zip?dl=1','https://www.dropbox.com/s/w73w3rftftogld9/Win95OSR2.1.zip?dl=1','https://www.dropbox.com/s/lzueklsi923yn19/Win95OSR2.5.zip?dl=1']
	name=[0,'Win95Floppy.zip','Win95.zip','Win95OSR1.zip','Win95OSR2.zip','Win95OSR2.1.zip','Win95OSR2.5.zip']
	if choix <= len(ver)-1 and choix != 0:
		dl(url[choix],name[choix])
		windows()
	else:
		windows95()

def windowsme(): #Windows ME
	dl('https://www.dropbox.com/s/72es4jknmljyjql/WinMe.zip?dl=1','WinMe.zip')
	windows()

def windows81(): #Windows 8.1
	print("Choix de version\n")
	ver=["1- Windows 8.1 32 Bits","2- Windows 8.1 64 Bits"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url=[0,'https://www.dropbox.com/s/8q9af9u9gm6qd5h/Win8.1_x86.zip?dl=1','https://www.dropbox.com/s/5kzqj5m3fkzrmjb/Win8.1_x64.zip?dl=1']
	name=[0,'Win8.1_x86.zip','Win8.1_x64.zip']
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else:
		windows81()

def windows98(): # Windows 98
	ver=["1- Windows 98 (Disquette de démarrage)","2- Windows 98 FE","3- Windows 98 FE (Disquette)","4- Windows 98 FE vers SE","5- Windows 98 SE","6- Windows 98 SE (Microsoft Select)"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url=[0,'https://www.dropbox.com/s/9dz2bmu5g7rjnx4/BootFloppyWin98.zip?dl=1','https://www.dropbox.com/s/oadmdoeh2sbihv8/Win98FE.zip?dl=1','https://www.dropbox.com/s/35weam9voxcqcy5/Win98_Floppy.zip?dl=1','https://www.dropbox.com/s/ps3znujq8vf6u6x/Win98FEtoSE.zip?dl=1','https://www.dropbox.com/s/qgtfkp6bhq2sx5i/Win98SE.zip?dl=1','https://www.dropbox.com/s/w7e94wc5fac6nk2/Win98SE_MS_Select.zip?dl=1']
	name=[0,'BootFloppyWin98.zip','Win98FE.zip','Win98_Floppy.zip','Win98FEtoSE.zip','Win98SE.zip','Win98SE_MS_Select.zip']
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else :
		windows98()

def windows2k(): # Windows 2000
	ver=["1- Windows 2000 Professionel","2- Windows 2000 Server","3- Windows 2000 Professionel (Microsoft Select)"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url[0,'https://www.dropbox.com/s/1vhjaalcnyv7puy/Win2kPro.zip?dl=1','https://www.dropbox.com/s/zblg08ouixo2ccx/Win2kServeur.zip?dl=1','https://www.dropbox.com/s/gc22xuue1ia682w/Win2kPro_MS_Select.zip?dl=1']
	name[0,'Win2kPro.zip','Win2kServeur.zip','Win2kPro_MS_Select.zip']
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else:
		windows2k()

def windowsnt3(): #Windows NT 3.x
	ver=["1- Windows NT 3.1 Workstation","2- Windows NT 3.1 Workstation (Disquettes)","3- Windows NT 3.5 Workstation","4- Windows NT 3.5 Serveur (Disquette)","5- Windows NT 3.51 Serveur","6- Windows NT 3.51 Serveur (Disquette)","7- Windows NT 3.51 Workstation","8- Windows NT 3.51 Workstation (Disquette)"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url[0,'https://www.dropbox.com/s/vb1k1pd5a4gx6vf/WinNT3.1Work.zip?dl=1','https://www.dropbox.com/s/7vfmu94y1yuj7fo/WinNT3.1WorkFloppy.zip?dl=1','https://www.dropbox.com/s/jf3ojlfdxbmnnek/WinNT3.5.zip?dl=1','https://www.dropbox.com/s/s0l1x9dovmmz2wo/WinNT3.5ServFloppy.zip?dl=1','https://www.dropbox.com/s/ans6hrk3uywe0ir/WinNT3.51Serv.zip?dl=1','https://www.dropbox.com/s/easj1oi5o30yfhi/WinNT3.51ServFloppy.zip?dl=1','https://www.dropbox.com/s/rszna9hi1akoffj/WinNT3.51Work.zip?dl=1','https://www.dropbox.com/s/opmb41eitn40a4d/WinNT3.51WorkFloppy.zip?dl=1']
	name[0,'WinNT3.1Work.zip','WinNT3.1WorkFloppy','WinNT3.5.zip','WinNT3.5ServFloppy.zip','WinNT3.51Serv.zip','WinNT3.51ServFloppy.zip','WinNT3.51Work.zip','WinNT3.51WorkFloppy.zip']
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else:
		windowsnt3()

def windowsnt4(): #Windows NT4.0
	ver=["1- Windows NT 4.0 Serveur",'2- Windows NT 4.0 Serveur Back Office 2.5',"3- Windows NT 4.0 Serveur Entreprise Edition","4- Windows NT 4.0 Terminal Serveur","5- Windows NT 4.0 Workstation"]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url[0,'https://www.dropbox.com/s/8udbpydfanv43i0/WinNT4.0Serv.zip?dl=1','https://www.dropbox.com/s/frj3ei5lvimbn5b/WinNT4.0Serv_Back_Office_2.5.zip?dl=1','https://www.dropbox.com/s/1hpx3jeas42lpl1/WinNT4.0Serv_Entreprise_Edition.zip?dl=1','https://www.dropbox.com/s/llqt5s41xgsrkz8/WinNT4.0Term_Serv.zip?dl=1','https://www.dropbox.com/s/un6xnf3niy3hocx/WinNT4.0Work.zip?dl=1']
	name[0,'WinNT4.0Serv.zip','WinNT4.0Serv_Back_Office_2.5.zip','WinNT4.0Serv_Entreprise_Edition.zip','WinNT4.0Term_Serv.zip','WinNT4.0Work.zip']
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else:
		windowsnt4()

def windowsxp():
	ver=["1- Windows XP Home/Famille","2- Windows XP Media Center","3- Windows XP Professionel","4- Windows XP Starter","5- Windows XP Tablet PC","6- Windows POSReady 2009"]
	
	for i in range(len(ver)):
		print(ver[i])
	ch=int(input("Votre choix ?\n"))
	if ch==1:
		winxphome()
	else:
		windowsxp()

def winxphome():
	ver=["1- Windows XP Home N","2- Windows XP Home N SP2","3- Windows XP Home N SP3","4- Windows XP Home RTM","5- Windows XP Home SP1","6- Windows XP Home SP2","7- Windows XP Home SP3"]
	url=[0,'https://www.dropbox.com/s/9a79i6rzb8yw2t3/WinXP_Home_N_SP0.zip?dl=1','https://www.dropbox.com/s/uubff062srqr7up/WinXP_Home_N_SP2.zip?dl=1','https://www.dropbox.com/s/r3loerq4odvuz9t/WinXP_Home_N_SP3.zip?dl=1','https://www.dropbox.com/s/739amnqspx9a3gd/WinXP_Home_SP0.zip?dl=1','https://www.dropbox.com/s/9qxc4etvva6cnpn/WinXP_Home_SP1.zip?dl=1','https://www.dropbox.com/s/gmq6ltwn1t4q674/WinXP_Home_SP2.zip?dl=1','https://www.dropbox.com/s/pk3fr6hduxn8g8t/WinXP_Home_SP3.zip?dl=1']
	name=[0,'WinXP_Home_N_SP0.zip','WinXP_Home_N_SP2.zip','WinXP_Home_N_SP3.zip','WinXP_Home_SP0.zip','WinXP_Home_SP1.zip','WinXP_Home_SP2.zip','WinXP_Home_SP3.zip']
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		windows()
	else:
		winxphome()

def dl(url,filename):
	print("Démarrage du téléchargement")
	wget.download(url,filename)
	print("Téléchargement terminé, le fichier se trouve dans le même dossier que le script")

def template():
	ver=[]
	for i in range(len(ver)):
		print(ver[i])
	choix=int(input("Votre choix ?\n"))
	url[0,1]
	name[0,1]
	if choix <= len(ver) - 1 and choix != 0:
		dl(url[choix], name[choix])
		var()
	else:
		precedentvar()

main()