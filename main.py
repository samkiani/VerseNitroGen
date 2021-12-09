import requests 
import os
import random
import string
import keep_alive 

class VerseGen:
	
	BOLD = '\033[1m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	print(f"""██╗░░░██╗███████╗██████╗░░██████╗███████╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝""")
	print(BOLD + UNDERLINE + "\nVerse Nitro Generator" + END)
	
	print("\nCreated by DraKenCodeZ")
	num = int(input("\nHow many codes you want to generate and check : "))
	
	valid = 0
	invalid = 0

	for i in range(num):
		code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
		nitrocode = f"\n https://discord.gift/{code}"
		
		url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
		response = requests.get(url)		
		
		
		if response.status_code == 200:
			print(f"Valid | {nitrocode}\nVerseGenerator - {valid} Valid | {invalid} Invalid")
			valid +=1
			f = open("NitroCodes/valid.txt","a")		
			f.write(nitrocode)
			f.close()
		else:
			invalid += 1
			print(f"Invalid | {nitrocode}\nVerseGenerator - {valid} Valid | {invalid} Invalid")
			f = open("NitroCodes/invalid.txt","a")
			f.write(nitrocode)
			f.close
			
	print(f"""
──────────────────────────
Valid - {valid}
Invalid - {invalid}""")		

keep_alive.keep_alive()
