# 1.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον
# αντίστοιχο πίνακα. check Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει στην τύχη τις μισές με
# μονάδες (στρογγυλοποίηση προς τα πάνω). Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια,
# κάθετα, και διαγώνια. Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο
# των τετράδων.
import random

# ftiaxno to tetragwno
inp = input("dwse diastasi tetragwnou")
megethos = int(inp)
# elegxw an einai dynaton na sxhmatistoyn 4ades alliws einai anoysio
while megethos < 4:
    inp = input("dwse diastasi tetragwnou")
    megethos = int(inp)
# o arithmos olwn twn thesewn
theseis = megethos * megethos
mo = 0
#oi 100 epanalhpseis
for q in range (100):
    # ftiaxnw mia lista me oles tis theseis gia na kano to gemisma
    oles = []
    for i in range(theseis):
        oles.append(0)
    # brisko tis misestheseis
    half = theseis / 2
    halfint = int(half)
    # stroggylopoiw pros ta panw
    if half > halfint:
        half = halfint + 1
    misa = int(half)
    # kano ta misa ena kai meta ta anakateuw
    for i in range(misa):
        oles[i] = 1
    random.shuffle(oles)
    print(oles)
    # xwrizw tis listes se mikroteres megethous poy tha symbolizoyn mia seira
    seires = []
    k = 0
    j = megethos
    for l in range(megethos):
        slicee = (oles[k:j])
        seires.append(slicee)
        j = j + megethos
        k = k + megethos
    print(seires)
    score = 0
    # sygkinw orizontia se kathe lista
    for list in seires:
        for a in range(megethos - 3):
            if list[a] == 1 and list[a + 1] == 1 and list[a + 2] == 1 and list[a + 3] == 1:
                score = score + 1
    # sygkrinw katheta
    for b in range(megethos - 3):
        for c in range(megethos):
            if (seires[b][c] == 1) and (seires[b + 1][c] == 1) and (seires[b + 2][c] == 1) and (seires[b + 3][c] == 1):
                score = score + 1
    # sygkrinw diagwnia
    for d in range(megethos - 3):
        for e in range(megethos - 3):
            if (seires[d][e] == 1) and (seires[d + 1][e + 1] == 1) and (seires[d + 2][e + 2] == 1) and (
                    seires[d + 3][e + 3] == 1):
                score = score + 1
    for f in range(megethos - 3):
        for g in range(3, megethos):
            if (seires[f][g] == 1) and (seires[f + 1][g - 1] == 1) and (seires[f + 2][g - 2] == 1) and (
                    seires[f + 3][g - 3] == 1):
                score = score + 1
    # emfanizw to apotelesma
    print(score)
    mo = mo + score
    # reset to random
    import random
tel = mo / 100
print("O mesos oros twn tetradwn :",tel)