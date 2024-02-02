# Usando AND as duas sentenças precisam ser verdadeiras

sa = 6000
status = "limpo"

if sa > 5000 and status == "limpo":
    print("Você pode financiar.")
else:
    print("Você não pode financiar.")

# Usando OR ele vai aceitar se apenas uma estiver correta
sa = 4000
status = "limpo"

if sa > 5000 or status == "limpo":
    print("Você pode financiar.")
else:
    print("Você não pode financiar.")