def check_salute(couloir):
    if not isinstance(couloir, str) or not couloir:
        return 0

    salutations = 0
    officiers_gauche = 0

    for char in couloir:
        if char == '>':
            officiers_gauche += 1  # Un officier se dirige vers la droite
        elif char == '<':
            salutations += officiers_gauche  # Saluer chaque officier déjà compté se dirigeant vers la gauche
       
    return salutations
  # Exemples de tests
print(check_salute("-->>----<<--"))  # Attendu: 4
print(check_salute("--->--->----->--"))  # Attendu: 0
print(check_salute("---<---->-->----<<-->"))  # Attendu: 4
