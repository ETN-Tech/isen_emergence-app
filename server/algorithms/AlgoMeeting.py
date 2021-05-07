
#This algorithms create the meeting for all godfather and laureates according to the 6 laureates each godfathers selected previously.
#Each godfather will be associated with 4 laureates in a correct order 
# Each laureates won't have two meetings at the same time.



# input file example (stringify json):
# "{\"Parrain 1\": [\"Laureat 4\", \"Laureat 21\", \"Laureat 34\", \"Laureat 17\", \"Laureat 24\", \"Laureat 27\"], \"Parrain 2\": [\"Laureat 16\", \"Laureat 4\", \"Laureat 7\", \"Laureat 18\", \"Laureat 30\", \"Laureat 22\"], \"Parrain 3\": [\"Laureat 17\", \"Laureat 23\", \"Laureat 19\", \"Laureat 10\", \"Laureat 6\", \"Laureat 30\"], \"Parrain 4\": [\"Laureat 37\", \"Laureat 14\", \"Laureat 28\", \"Laureat 29\", \"Laureat 20\", \"Laureat 3\"], \"Parrain 5\": [\"Laureat 18\", \"Laureat 5\", \"Laureat 33\", \"Laureat 12\", \"Laureat 29\", \"Laureat 21\"], \"Parrain 6\": [\"Laureat 29\", \"Laureat 9\", \"Laureat 17\", \"Laureat 28\", \"Laureat 34\", \"Laureat 33\"], \"Parrain 7\": [\"Laureat 24\", \"Laureat 40\", \"Laureat 28\", \"Laureat 13\", \"Laureat 8\", \"Laureat 37\"], \"Parrain 8\": [\"Laureat 14\", \"Laureat 1\", \"Laureat 33\", \"Laureat 3\", \"Laureat 4\", \"Laureat 15\"], \"Parrain 9\": [\"Laureat 32\", \"Laureat 28\", \"Laureat 14\", \"Laureat 25\", \"Laureat 11\", \"Laureat 26\"], \"Parrain 10\": [\"Laureat 38\", \"Laureat 21\", \"Laureat 17\", \"Laureat 4\", \"Laureat 12\", \"Laureat 3\"], \"Parrain 11\": [\"Laureat 11\", \"Laureat 32\", \"Laureat 38\", \"Laureat 23\", \"Laureat 30\", \"Laureat 40\"], \"Parrain 12\": [\"Laureat 16\", \"Laureat 39\", \"Laureat 36\", \"Laureat 33\", \"Laureat 13\", \"Laureat 4\"], \"Parrain 13\": [\"Laureat 2\", \"Laureat 14\", \"Laureat 10\", \"Laureat 11\", \"Laureat 12\", \"Laureat 33\"], \"Parrain 14\": [\"Laureat 5\", \"Laureat 1\", \"Laureat 8\", \"Laureat 7\", \"Laureat 17\", \"Laureat 32\"], \"Parrain 15\": [\"Laureat 20\", \"Laureat 7\", \"Laureat 8\", \"Laureat 34\", \"Laureat 30\", \"Laureat 29\"], \"Parrain 16\": [\"Laureat 25\", \"Laureat 21\", \"Laureat 17\", \"Laureat 18\", \"Laureat 36\", \"Laureat 27\"], \"Parrain 17\": [\"Laureat 6\", \"Laureat 16\", \"Laureat 32\", \"Laureat 13\", \"Laureat 27\", \"Laureat 29\"], \"Parrain 18\": [\"Laureat 24\", \"Laureat 12\", \"Laureat 33\", \"Laureat 27\", \"Laureat 32\", \"Laureat 17\"], \"Parrain 19\": [\"Laureat 4\", \"Laureat 15\", \"Laureat 7\", \"Laureat 20\", \"Laureat 8\", \"Laureat 23\"], \"Parrain 20\": [\"Laureat 11\", \"Laureat 29\", \"Laureat 31\", \"Laureat 39\", \"Laureat 27\", \"Laureat 38\"], \"Parrain 21\": [\"Laureat 5\", \"Laureat 7\", \"Laureat 31\", \"Laureat 35\", \"Laureat 10\", \"Laureat 9\"], \"Parrain 22\": [\"Laureat 36\", \"Laureat 33\", \"Laureat 23\", \"Laureat 37\", \"Laureat 13\", \"Laureat 32\"], \"Parrain 23\": [\"Laureat 1\", \"Laureat 13\", \"Laureat 26\", \"Laureat 22\", \"Laureat 20\", \"Laureat 17\"], \"Parrain 24\": [\"Laureat 3\", \"Laureat 1\", \"Laureat 16\", \"Laureat 28\", \"Laureat 30\", \"Laureat 2\"], \"Parrain 25\": [\"Laureat 29\", \"Laureat 36\", \"Laureat 9\", \"Laureat 1\", \"Laureat 33\", \"Laureat 8\"], \"Parrain 26\": [\"Laureat 20\", \"Laureat 32\", \"Laureat 18\", \"Laureat 13\", \"Laureat 23\", \"Laureat 29\"], \"Parrain 27\": [\"Laureat 7\", \"Laureat 34\", \"Laureat 14\", \"Laureat 12\", \"Laureat 20\", \"Laureat 28\"], \"Parrain 28\": [\"Laureat 26\", \"Laureat 21\", \"Laureat 11\", \"Laureat 23\", \"Laureat 6\", \"Laureat 15\"], \"Parrain 29\": [\"Laureat 40\", \"Laureat 15\", \"Laureat 22\", \"Laureat 18\", \"Laureat 6\", \"Laureat 38\"], \"Parrain 30\": [\"Laureat 21\", \"Laureat 7\", \"Laureat 13\", \"Laureat 10\", \"Laureat 30\", \"Laureat 23\"], \"Parrain 31\": [\"Laureat 20\", \"Laureat 32\", \"Laureat 1\", \"Laureat 15\", \"Laureat 21\", \"Laureat 33\"], \"Parrain 32\": [\"Laureat 32\", \"Laureat 11\", \"Laureat 31\", \"Laureat 34\", \"Laureat 30\", \"Laureat 37\"], \"Parrain 33\": [\"Laureat 15\", \"Laureat 29\", \"Laureat 9\", \"Laureat 40\", \"Laureat 5\", \"Laureat 6\"], \"Parrain 34\": [\"Laureat 34\", \"Laureat 15\", \"Laureat 6\", \"Laureat 1\", \"Laureat 18\", \"Laureat 23\"], \"Parrain 35\": [\"Laureat 21\", \"Laureat 29\", \"Laureat 19\", \"Laureat 31\", \"Laureat 30\", \"Laureat 12\"], \"Parrain 36\": [\"Laureat 18\", \"Laureat 1\", \"Laureat 9\", \"Laureat 24\", \"Laureat 14\", \"Laureat 29\"], \"Parrain 37\": [\"Laureat 37\", \"Laureat 36\", \"Laureat 14\", \"Laureat 1\", \"Laureat 7\", \"Laureat 24\"], \"Parrain 38\": [\"Laureat 35\", \"Laureat 17\", \"Laureat 5\", \"Laureat 30\", \"Laureat 34\", \"Laureat 20\"], \"Parrain 39\": [\"Laureat 15\", \"Laureat 26\", \"Laureat 33\", \"Laureat 7\", \"Laureat 20\", \"Laureat 13\"], \"Parrain 40\": [\"Laureat 25\", \"Laureat 14\", \"Laureat 13\", \"Laureat 3\", \"Laureat 24\", \"Laureat 40\"]}" 

#  Output with those data :
# {"Parrain 1": ["Laureat 4", "Laureat 19", "Laureat 2", "Laureat 27"], "Parrain 2": ["Laureat 22", "Laureat 4", "Laureat 16", "Laureat 18"], "Parrain 3": ["Laureat 30", "Laureat 10", "Laureat 19", "Laureat 17"], "Parrain 4": ["Laureat 36", "Laureat 14", "Laureat 3", "Laureat 37"], "Parrain 5": ["Laureat 21", "Laureat 33", "Laureat 12", "Laureat 5"], "Parrain 6": ["Laureat 28", "Laureat 22", "Laureat 9", "Laureat 33"], "Parrain 7": ["Laureat 25", "Laureat 24", "Laureat 40", "Laureat 8"], "Parrain 8": ["Laureat 3", "Laureat 1", "Laureat 15", "Laureat 39"], "Parrain 9": ["Laureat 14", "Laureat 25", "Laureat 26", "Laureat 28"], "Parrain 10": ["Laureat 38", "Laureat 21", "Laureat 4", "Laureat 12"], "Parrain 11": ["Laureat 23", "Laureat 30", "Laureat 38", "Laureat 40"], "Parrain 12": ["Laureat 16", "Laureat 39", "Laureat 33", "Laureat 13"], "Parrain 13": ["Laureat 10", "Laureat 12", "Laureat 11", "Laureat 2"], "Parrain 14": ["Laureat 32", "Laureat 5", "Laureat 17", "Laureat 7"], "Parrain 15": ["Laureat 8", "Laureat 35", "Laureat 29", "Laureat 11"], "Parrain 16": ["Laureat 27", "Laureat 18", "Laureat 25", "Laureat 21"], "Parrain 17": ["Laureat 29", "Laureat 27", "Laureat 6", "Laureat 16"], "Parrain 18": ["Laureat 24", "Laureat 2", "Laureat 27", "Laureat 32"], "Parrain 19": ["Laureat 7", "Laureat 15", "Laureat 8", "Laureat 4"], "Parrain 20": ["Laureat 11", "Laureat 31", "Laureat 39", "Laureat 38"], "Parrain 21": ["Laureat 31", "Laureat 7", "Laureat 35", "Laureat 10"], "Parrain 22": ["Laureat 39", "Laureat 32", "Laureat 37", "Laureat 36"], "Parrain 23": ["Laureat 17", "Laureat 26", "Laureat 13", "Laureat 22"], "Parrain 24": ["Laureat 2", "Laureat 16", "Laureat 28", "Laureat 3"], "Parrain 25": ["Laureat 33", "Laureat 8", "Laureat 1", "Laureat 9"], "Parrain 26": ["Laureat 13", "Laureat 20", "Laureat 23", "Laureat 29"], "Parrain 27": ["Laureat 34", "Laureat 28", "Laureat 36", "Laureat 20"], "Parrain 28": ["Laureat 26", "Laureat 6", "Laureat 21", "Laureat 23"], "Parrain 29": ["Laureat 18", "Laureat 38", "Laureat 22", "Laureat 15"], "Parrain 30": ["Laureat 19", "Laureat 11", "Laureat 10", "Laureat 30"], "Parrain 31": ["Laureat 20", "Laureat 36", "Laureat 32", "Laureat 1"], "Parrain 32": ["Laureat 37", "Laureat 34", "Laureat 30", "Laureat 31"], "Parrain 33": ["Laureat 9", "Laureat 40", "Laureat 5", "Laureat 6"], "Parrain 34": ["Laureat 6", "Laureat 23", "Laureat 18", "Laureat 34"], "Parrain 35": ["Laureat 12", "Laureat 29", "Laureat 31", "Laureat 19"], "Parrain 36": ["Laureat 35", "Laureat 9", "Laureat 24", "Laureat 14"], "Parrain 37": ["Laureat 1", "Laureat 37", "Laureat 7", "Laureat 24"], "Parrain 38": ["Laureat 5", "Laureat 17", "Laureat 34", "Laureat 35"], "Parrain 39": ["Laureat 15", "Laureat 13", "Laureat 20", "Laureat 26"], "Parrain 40": ["Laureat 40", "Laureat 3", "Laureat 14", "Laureat 25"]}


# Output : json file {"Parrain" : ["Meeting1","Meeting2","Meeting3","Meeting4"], ...}

# Errors : - error : there are two godfather's choice similar. ! GodFather : #Parrain#
# 			!! One of the godfather choose two times the same laureate !!

# 		   - error : couldn't find a result with this data 
# 			
# 			!! Maybe the number of godfather and laureates are not the same ? !!

# Average satisfaction rate : 91% !! Test with random choice for all the godfathers !!
# Here it means that 91% of the meetings were requested by the godfather



import sys
import random
from ortools.sat.python import cp_model
import json

#######################################
# fichier json
# with open('choixparrain.json') as json_data:
#    choixparrain = json.load(json_data)
# print(choixparrain)

# Choix random

# Lparrain=['Parrain 1', 'Parrain 2', 'Parrain 3', 'Parrain 4', 'Parrain 5', 'Parrain 6', 'Parrain 7', 'Parrain 8', 'Parrain 9', 'Parrain 10', 'Parrain 11', 'Parrain 12', 'Parrain 13', 'Parrain 14', 'Parrain 15', 'Parrain 16', 'Parrain 17', 'Parrain 18', 'Parrain 19', 'Parrain 20', 'Parrain 21', 'Parrain 22', 'Parrain 23', 'Parrain 24', 'Parrain 25', 'Parrain 26', 'Parrain 27', 'Parrain 28', 'Parrain 29', 'Parrain 30', 'Parrain 31', 'Parrain 32', 'Parrain 33', 'Parrain 34', 'Parrain 35', 'Parrain 36', 'Parrain 37', 'Parrain 38', 'Parrain 39', 'Parrain 40']
# Llaureat=['Laureat 1', 'Laureat 2', 'Laureat 3', 'Laureat 4', 'Laureat 5', 'Laureat 6', 'Laureat 7', 'Laureat 8', 'Laureat 9', 'Laureat 10', 'Laureat 11', 'Laureat 12', 'Laureat 13', 'Laureat 14', 'Laureat 15', 'Laureat 16', 'Laureat 17', 'Laureat 18', 'Laureat 19', 'Laureat 20', 'Laureat 21', 'Laureat 22', 'Laureat 23', 'Laureat 24', 'Laureat 25', 'Laureat 26', 'Laureat 27', 'Laureat 28', 'Laureat 29', 'Laureat 30', 'Laureat 31', 'Laureat 32', 'Laureat 33', 'Laureat 34', 'Laureat 35', 'Laureat 36', 'Laureat 37', 'Laureat 38', 'Laureat 39', 'Laureat 40']

# dictchoix={p:[] for p in Lparrain}
# for i in dictchoix.items():
#    correct=False
#    while correct==False:
#        correct=True
#        rdm=random.sample(Llaureat, 6)
#        for j in rdm:
#            if rdm.count(j)!=1:
#                correct=False
# print(rdm)
#    for a in rdm:
#        i[1].append(a)
# print(dictchoix)
# print(sys.argv[1])
a = sys.argv[1]
choixparrain = json.loads(a)
# print(type(choixparrain))
# choixparrain=dictchoix

Llaureat = []
for j in choixparrain.items():
    for l in j[1]:
        if l not in Llaureat:
            Llaureat.append(l)
# print(Llaureat)
#######################################


b = True
while b == True:
    b = False
    err = False

    nomlaureat = []
    for i in choixparrain.items():
        for a in i[1]:
            if a not in nomlaureat:
                nomlaureat.append(a)

    laureatchoisipar = {k: [] for k in nomlaureat}

    for i in choixparrain.items():
        for j in i[1]:
            laureatchoisipar[j].append(i[0])

    # print(laureatchoisipar)
    Meeting = {k: [] for k in choixparrain}
    # print(Meeting)
    for i in laureatchoisipar.items():
        if len(i[1]) <= 4:
            for j in i[1]:
                if len(Meeting[j]) < 4:
                    Meeting[j].append(i[0])

    # print(Meeting)

    Lbannedparrain = []
    for a in laureatchoisipar.items():
        for m in Meeting.items():
            if len(m[1]) > 4:
                print("error : already more than 4 meeting for a godfather")
            if len(m[1]) == 4:
                Lbannedparrain.append(m[0])

        if len(a[1]) > 4:
            L = []
            for j in a[1]:
                if j not in Lbannedparrain:
                    L.append(j)
            if len(L) <= 4:
                b = L
            else:
                b = random.sample(L, 4)
            for p in b:
                Meeting[p].append(a[0])

    # print(Meeting)
    cpt1 = 0
    cpt2 = 0
    for a in Meeting.items():
        cpt2 += 4
        cpt1 += len(a[1])

    # if cpt1/cpt2<0.88:
    # print("attention taux de satisfaction inférieur à 0.88")
    # err=True

    # print(Meeting)
    Lrandomparrain = []
    for i in Meeting.items():
        if len(i[1]) < 4:
            for j in range(4 - len(i[1])):
                Lrandomparrain.append(i[0])

    # print(Lrandomparrain, len(Lrandomparrain))

    cptmeetinglaureat = {k: 0 for k in Llaureat}
    for i in Meeting.items():
        for j in i[1]:
            cptmeetinglaureat[j] += 1
    # print(cptmeetinglaureat)
    Lrandomlaureat = []
    for i in cptmeetinglaureat.items():
        if i[1] < 4:
            for j in range(4 - i[1]):
                Lrandomlaureat.append(i[0])
    # print(Lrandomlaureat, len(Lrandomlaureat))

    Lduorandom = []
    while len(Lrandomparrain) != 2:
        a = random.choice(Lrandomlaureat)
        b = random.choice(Lrandomparrain)
        # print(a,b)
        if (a, b) not in Lduorandom:
            Meeting[b].append(a)

            Lduorandom.append((a, b))
            # print(a,b)
            Lrandomlaureat.remove(a)
            Lrandomparrain.remove(b)
            # print(Lrandomlaureat)
            # print(Lrandomparrain)
    Lerror = []
    for i in range(2):
        Lerror.append((Lrandomparrain[i], Lrandomlaureat[i]))
    Lerror.append((Lrandomparrain[0], Lrandomlaureat[1]))
    Lerror.append((Lrandomparrain[1], Lrandomlaureat[0]))

    duoerror = 0
    for i in Lerror:
        if i in Lduorandom:
            duoerror = i
            Lerror.remove(i)
    if duoerror == 0:
        cpt = 0
        while cpt < 2:
            cpt += 1
            a = random.choice(Lrandomlaureat)
            b = random.choice(Lrandomparrain)
            # print(a,b)
            if (a, b) not in Lduorandom:
                Meeting[b].append(a)
                Lduorandom.append((a, b))
                # print(a,b)
                Lrandomlaureat.remove(a)
                Lrandomparrain.remove(b)
                # print(Lrandomlaureat)
                # print(Lrandomparrain)
    else:
        for j in Lerror:
            if j[0] != duoerror[0] and j[1] != duoerror[1]:
                Lerror.remove(j)
        for j in Lerror:
            Meeting[j[0]].append(j[1])
    for a in Meeting.items():
        if len(a[1]) != 4:
            # print("error : more than 4 meetings for a godfather")
            err = True

        for l in a[1]:
            if a[1].count(l) > 1:
                # print("error : doublon de meeting")
                err = True
        if len(a[1]) < 4:
            # print("error : less than 4 meetings for a godfather")
            err = True

    if err == True:
        b = True
    else:
        # print("Taux de satisfaction des parrains : ",cpt1/cpt2)

        y = json.dumps(Meeting)

dictchoix = Meeting
nbrGodFather = 8
nbrLaureate = nbrGodFather
nbrLaureat = 8
nbrMeeting = 4
dictmeeting = {}
dictresult = {p: [0, 0, 0, 0] for p in dictchoix}

nomlaureat = []
for i in dictchoix.items():
    for a in i[1]:
        nomlaureat.append(a)

dictlaureat = {k: [] for k in nomlaureat}
for i in dictchoix.items():
    for a in i[1]:
        dictlaureat[a].append(i[0])
model = cp_model.CpModel()

for i in dictchoix.items():
    p = i[0]
    for l in i[1]:
        for m in range(nbrMeeting):
            dictmeeting[(p, l, m)] = model.NewBoolVar('meeting_p%sl%sm%i' % (p, l, m))
# print(model)
# print(dictmeeting)

for i in dictchoix.items():
    p = i[0]
    for m in range(nbrMeeting):
        model.Add(sum(dictmeeting[(p, l, m)] for l in i[1]) == 1)

# print(model)

for m in range(nbrMeeting):
    for l in nomlaureat:
        model.Add(sum(dictmeeting[(p, l, m)] for p in dictlaureat[l]) == 1)

# print(model)

for i in dictchoix.items():
    p = i[0]
    for l in i[1]:
        model.Add(sum(dictmeeting[(p, l, m)] for m in range(0, 4)) == 1)

solver = cp_model.CpSolver()

solver.parameters.max_time_in_seconds = 10.0

status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    for i in dictchoix.items():
        p = i[0]

        for l in i[1]:
            for m in range(0, 4):

                if (solver.Value(dictmeeting[(str(p), l, m)]) != 0):
                    dictresult[p][m] = l

else:
    print("error")

f = json.dumps(dictresult)
print(f)
