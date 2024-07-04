

def taux_impot(somme):
	if somme < 11295:
		new_somme=somme
		print(f"Vôtre revenu  net est donc de:{new_somme} ")
		print(f"Vôtre pourcentage d'imposition est de: {int((1-(new_somme/somme))*100)} %")
	elif (somme > 11295) and  (somme <28797):
		retenu=(somme-11295)*0.89
		new_somme=11295+retenu
		print(f"Vôtre revenu net est donc de: {new_somme}")
		print(f"Vôtre pourcentage d'imposition est de: {int((1-(new_somme/somme))*100)} %")
	elif somme > 28797 and somme < 82341:
		retenu=(somme-11295-(28797-11295))*0.70
		new_somme=11295+((28797-11295)*0.89)+retenu
		print(f"Vôtre revenu net est donc de: {new_somme}")
		print(f"Vôtre pourcentage d'imposition est de: {int((1-(new_somme/somme))*100)} %")
	elif somme > 82341 and somme <177106:
		retenu=(somme-11295-(28797-11295)-(82341-28797))*0.59
		new_somme=11295+((28797-11295)*0.89)+((82341-28797)*0.70)+retenu 
		print(f"Vôtre revenu net est donc de: {new_somme}")
		print(f"Vôtre pourcentage d'imposition est de: {int((1-(new_somme/somme))*100)} %")
	elif somme > 177106:
		retenu=(somme-11295-(28797-11295)-(82341-28797)-(177106-82341))*0.55
		new_somme=11295+((28797-11295)*0.89)+((82341-28797)*0.70)+((177106-82341)*0.59)+retenu
		print(f"Vôtre revenu net est donc de: {new_somme}")
		print(f"Vôtre pourcentage d'imposition est de: {int((1-(new_somme/somme))*100)} %")
		
impôt=float(input("Quel est la somme: "))		
taux_impot(impôt)
