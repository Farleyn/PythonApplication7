print("Tere! Olen sinu uus sõber - Python!")

nimi = input("Mis on sinu nimi? ")

if nimi:
    print(f"{nimi}, oi kui ilus nimi!")

question = input(f"{nimi}, kas leian sinu kehamassiindeksi? 0 - ei, 1 - jah => ")

if question == "0":
    print("Ok, head aega!")
elif question == "1":
    try:
        pikkus_cm = float(input("Sisesta oma pikkus sentimeetrites (nt 175): "))

        if pikkus_cm <= 0:
            print("Pikkus ei saa olla 0 või negatiivne")
        elif pikkus_cm < 100 or pikkus_cm > 250:
            print("Vale pikkus")
        else:
            pikkus = pikkus_cm / 100
            mass = float(input("Sisesta oma kehakaal kilogrammides (nt 70): "))

            if mass <= 0:
                print("Kehakaal ei saa olla 0 või negatiivne")
            elif mass < 30 or mass > 300:
                print("Vale kehakaal")
            else:
                kehamassiindeks = mass / (pikkus ** 2)
                print(f"Sinu kehamassiindeks on: {kehamassiindeks:.2f}")

    except ValueError:
        print("Vale sisend")
else:
    print("Vale valik")
