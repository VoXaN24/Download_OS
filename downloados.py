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