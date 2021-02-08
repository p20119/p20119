# 12.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε
# χαρακτήρα του στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες είναι αυτοί των οποίων το άθροισμα
# είναι 128. Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.
# kanei to diavasma toy arxeioy
char_list = [char for char in open("two_cities_ascii.txt").read()]
# ftiaxnw pinakes gia metatropi se ascii kai meta gia na ginei katoptriko
asciim = []
katoptr = []
asciimf = []
# epanalipsi oso ypaxoyn xarakthres
for i in range(len(char_list)):
    # metatropi se ascii
    characnoasc = char_list[i]
    asciim = ord(characnoasc)
    # euresh toy katoptrikou
    katoptr = 255 - asciim
    # metatropi ksana se xarakthres kai dhmioyrgw thn lista poy tha emfanisw anapoda
    asciim = chr(katoptr)
    asciimf.append(asciim)
asciimf.reverse()
print(asciimf)
