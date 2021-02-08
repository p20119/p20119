# 9.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε
# χαρακτήρα στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. Eμφανίστε τα στατιστικά εμφάνισης του κάθε
# γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει
# προς τα πάνω.
char_list = [char for char in open("two_cities_ascii.txt").read()]
plithos = []
arithmosxar = 0
# arxikopoio to plithos poy emfanizetai o kathe xarakthras
for i in range(256):
    plithos.append(0)
# metatrepw toys xarakthres se ascii
for i in range(len(char_list)):
    characnoasc = char_list[i]
    characasc = ord(characnoasc)
    # krataw toys ascii me mono arithmo
    if characasc % 2 == 1:
        plithos[characasc] = plithos[characasc] + 1
        arithmosxar = arithmosxar + 1
pososto = []
# arxikopoiw ta pososta twn ascii xarakthrwn
for i in range(256):
    pososto.append(0)
# briskw kai stroggylopoiw ta pososta twn monwn
for i in range(256):
    pososto[i] = (plithos[i] / arithmosxar) * 100
    if pososto[i] > int(pososto[i]):
        pososto[i] = int(pososto[i] + 1)
    else:
        pososto[i] = int(pososto[i])
kati = "*"
# ftiaxnw tis mpares
for i in range(1, 256, 2):
    print(chr(i), ":", kati * pososto[i])
