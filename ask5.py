# 5.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες
# τον αντίστοιχο πίνακα. Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις
# μισές με O (στρογγυλοποίηση προς τα πάνω). Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια,
# κάθετα, και διαγώνια. Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο
# όρο των τριάδων SOS.
import random

h = int(input('DWSE YPSOS'))
w = int(input('DWSE PLATOS'))
while True:
    if h < 3:
        h = int(input('KSANADWSE SWSTO YPSOS'))
    elif w < 3:
        w = int(input('KSANADWSE SWSTO PLATOS'))
    else:
        break
tableseats = h * w  # ola ta koytakia
tscore = 0
for c in range(100):
    my_list = []
    for i in range(tableseats):  # theto se kathe thesi to 0 gia na leitoyrgisei ws flag argotera
        my_list.append(0)
    fhalf = tableseats / 2  # ta misa koytakia
    half = int(fhalf)
    if half < fhalf:
        half = half + 1
    for i in range(tableseats):  # elegxei poy exei 0 kai to antikathista me 'O'
        if i < half:
            my_list[i] = 'S'
        else:
            my_list[i] = 'O'
    random.shuffle(my_list)
    score = 0
    # xwrizw tis listes se mikroteres megethous poy tha symbolizoyn mia seira
    seires = []
    k = 0
    j = w
    print(my_list)
    for l in range(h):
        slicee = (my_list[k:j])
        seires.append(slicee)
        j = j + w
        k = k + w
    print(seires)
    # orizontia sygkrisi
    for m in range(h):
        for n in range(w - 2):
            if (seires[m][n] == 'S') and (seires[m][n + 1] == 'O') and (seires[m][n + 2] == 'S'):
                score = score + 1
    print(score)
    # katheti sygkrisi
    for o in range(w):
        for p in range(h - 2):
            if (seires[p][o] == 'S') and (seires[p + 1][o] == 'O') and (seires[p + 2][o] == 'S'):
                score = score + 1
    print(score)
    # diagwnia sygkrisi
    for d in range(h - 2):
        for e in range(w - 2):
            if (seires[d][e] == 'S') and (seires[d + 1][e + 1] == 'O') and (seires[d + 2][e + 2] == 'S'):
                score = score + 1
    print(score)
    # diagwnia apo tin allh
    for f in range(h - 2):
        for g in range(2, w):
            if (seires[f][g] == 'S') and (seires[f + 1][g - 1] == 'O') and (seires[f + 2][g - 2] == 'S'):
                score = score + 1
    print(score)
    tscore = tscore + score
    import random
finalscore = tscore / 100
print("MESOS OROS TRIADWN:", finalscore)
