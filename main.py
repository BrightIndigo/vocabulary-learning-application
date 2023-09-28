import random

# Słowniczek z zestawem słówek do nauki
slowniczek = {
    'kelnerka': 'die Kellnerin',
    'kosmetyczka': 'die Kosmetikerin',
    'dyrektorka': 'die Direktorin',
    'kucharka': 'die Köchin',
    'lekarka': 'die Ärztin',
    'przedszkolanka': 'die Kindergärtnerin',
    'opiekunka do dzieci': 'die Babysitter',
    'sekretarka': 'die Sekretärin',
    'tancerka': 'die Tänzerin',
    'architekt': 'der Architekt',
    'astronom': 'der Astronom',
    'autor': 'der Autor',
    'barman': 'der Barkellner',
    'bibliotekarz': 'der Bibliothekar',
    'chemik': 'der Chemiker',
    'chirurg': 'der Chirurg',
    'drukarz': 'der Buchdrucker',
    'dyrektor': 'der Chef/Direktor',
    'dziennikarz': 'der Journalist',
    'ekonomista': 'der Ökonomist',
    'fizyk': 'der Physiker',
    'fotograf': 'der Fotograf',
    'historyk': 'der Historiker',
    'informatyk': 'der Informatiker',
    'inspektor': 'der Inspektor',
    'kierowca': 'der Fahrer',
    'kosmonauta': 'der Kosmonaut',
    'ksiądz': 'der Priester',
    'makler': 'der Makler',
    'pilot': 'der Pilot'
}

def nauka_slownictwa(slowniczek):
    points = 0
    bledy = 0
    slowa = list(slowniczek.keys())
    random.shuffle(slowa)

    for slowo in slowa:
        tlumaczenie = input(f"Jakie jest tłumaczenie słowa '{slowo}'? Niemieckie litery: ä, Ä, ö, ü, β, Ö: ")

        if tlumaczenie.lower() == slowniczek[slowo].lower():
            points += 1
            print(f"Poprawna odpowiedź! Masz teraz {points} punktów!")
        else:
            bledy += 1
            print(f"Niepoprawna odpowiedź. Poprawne tłumaczenie to: {slowniczek[slowo]}, masz {bledy} błędów!")

if __name__ == "__main__":
    nauka_slownictwa(slowniczek)
