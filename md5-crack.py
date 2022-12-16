## MD5-CRACK es una pequeña herramienta para romper hashes MD5 mediante la especificacion de una wordlist 

from hashlib import md5
from os.path import exists 

## COLORS 
endColour=" \033[0m"
yellowColour="\33[1;33m"
redColour="\33[1;31m"
blueColour="\33[1;34m"
purpleColour="\33[1;35m"
greenColour="\33[1;32m"

def banner():
	print(f"""
   {redColour}MD5-CRACK{endColour}
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
""")

def carack_md5(hash, path_wordlist):
	breaked = False
	if not exists(path_wordlist):
		print( f"{redColour}[!]{endColour}Ruta no encontrada")
		exit(1)
	print( f"{greenColour}=[*]= {blueColour}REALIZANDO FUERZA BRUTA {greenColour}=[*]=")
	with open(path_wordlist, "r") as wordlist:
		for word in wordlist:
			if md5(word.rstrip().encode()).hexdigest() == hash:
				print( f"{redColour}[!]{endColour}Encontrado: {purpleColour}{word}{endColour}")
				breaked = True
				break
		if not breaked:
			print( f"{redColour}[!]{endColour}No Encontrado: {purpleColour}{hash}{endColour}")

if "__main__" == __name__:
	banner()
	hash = input("HASH MD5: ")
	path_wordlist = input("Ruta de Wordlist: ")
	carack_md5(hash, path_wordlist)