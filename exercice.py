import random

def get_first_part_of_name(name):
	liste = name.split("-")
	return f"Bonjour, {liste[0].title()}"

def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd’hui, j’ai vu un {random.choice(animals)} s’emparer d’un panier {random.choice(adjectives)} plein de {random.choice(fruits)}."

def encrypt(text, shift):
	string= ""
	for i in text:
		if 65 <= ord(i) <=90 or 97 <= ord(i) <= 122:
			lettre = chr(ord(i)+shift)
			if (65 <= ord(i) <=90 and ord(i)+shift > 90) or (97 <= ord(i) <= 122 and ord(i)+shift > 122):
				lettre = chr(ord(i)+shift-26)
			string += lettre.upper()
		else:
			string += i
	return string

def decrypt(encrypted_text, shift):
	string= ""
	for i in encrypted_text:
		if 65 <= ord(i) <=90 or 97 <= ord(i) <= 122:
			lettre = chr(ord(i)-shift)
			if (65 <= ord(i) <=90 and ord(i)-shift < 65) or (97 <= ord(i) <= 122 and ord(i)-shift < 97):
				lettre = chr(ord(i)-shift+26)
			string += lettre
		else:
			string += i
	return string


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
