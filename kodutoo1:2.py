# Funktsioon kehamassiindeksi (KMI) arvutamiseks
def arvuta_kmi(kaal, pikkus):
    kmi = kaal / (pikkus ** 2)
    return kmi

# Funktsioon KMI tulemuse hindamiseks
def hinda_kmi(kmi):
    if kmi < 18.5:
        return "Alakaal"
    elif 18.5 <= kmi < 24.9:
        return "Normaalkaal"
    elif 25 <= kmi < 29.9:
        return "Ülekaal"
    else:
        return "Rasvumine"

# Tsükkel, et kasutaja saaks teha mitu arvutust
while True:
    # Küsime kasutajalt sisendit
    kaal = float(input("Sisesta oma kaal kilogrammides: "))
    pikkus = float(input("Sisesta oma pikkus meetrites: "))

    # Arvutame KMI ja hindame tulemust
    kmi = arvuta_kmi(kaal, pikkus)
    tulemus = hinda_kmi(kmi)

    # Kuvame tulemuse
    print(f"Sinu kehamassiindeks on: {kmi:.2f}")
    print(f"See tähendab: {tulemus}")
    
    # Küsime, kas kasutaja soovib teha uue arvutuse
    uus_arvutus = input("Kas soovid teha uue arvutuse? (jah/ei): ").lower()
    
    if uus_arvutus != "jah":
        print("Programmi lõpetamine.")
        break  # Lõpetab tsükli, kui vastus ei ole 'jah'
