import sys
import numpy
from random import choice

aas = {}
aas[0] = {}
aas[0]['A'] = 0.15
aas[0]['B'] = 0.1
aas[0]['C'] = -0.15
aas[0]['D'] = 0.0
aas[0]['E'] = 0.2
aas[0]['F'] = -0.05
aas[0]['G'] = -0.4
aas[1] = {}
aas[1]['A'] = 0.3
aas[1]['B'] = 0.2
aas[1]['C'] = 0.03
aas[1]['D'] = -0.1
aas[1]['E'] = -0.25
aas[1]['F'] = -0.4
aas[1]['G'] = 0.0
aas[2] = {}
aas[2]['A'] = 0.0
aas[2]['B'] = -0.2
aas[2]['C'] = -0.5
aas[2]['D'] = -0.1
aas[2]['E'] = -0.05
aas[2]['F'] = -0.35
aas[2]['G'] = -0.3
aas[3] = {}
aas[3]['A'] = 0.3
aas[3]['B'] = 0.5
aas[3]['C'] = 0.0
aas[3]['D'] = -0.04
aas[3]['E'] = 0.1
aas[3]['F'] = -0.2
aas[3]['G'] = -0.15
aas[4] = {}
aas[4]['A'] = -0.1
aas[4]['B'] = 0.0
aas[4]['C'] = 0.25
aas[4]['D'] = -0.15
aas[4]['E'] = -0.2
aas[4]['F'] = 0.2
aas[4]['G'] = -0.35
aas[5] = {}
aas[5]['A'] = -0.4
aas[5]['B'] = 0.25
aas[5]['C'] = -0.45
aas[5]['D'] = -0.6
aas[5]['E'] = -0.3
aas[5]['F'] = 0.0
aas[5]['G'] = -0.35

num_seqs = int(sys.argv[1])

num_identity_features = int(sys.argv[2])

num_value_features = int(sys.argv[3])


sequences = []
scores = []
ones = []
outfile = open("fakefitnesses_long.txt", 'w')
for num in range(num_seqs):
	seq = ''
	score = 0.0
	for num in range(len(aas.keys())):
		aa = choice(list(aas[num].keys()))
		score += aas[num][aa]
		seq = seq + aa
	sequences.append(seq)
	scores.append(score)
	ones.append(1)
	outfile.write(str("name, %f, %f, %f, 1.0, 1.0, 1.0, 3.0, %s\n") %(score, numpy.random.rand()*0.4, numpy.random.rand()*0.2, seq))
outfile.close()



outfile = open("seq_list_long.txt", 'w')	
for seq in sequences:
	outfile.write(str("%s\n") % seq)
outfile.close()

outfile = open("fake_id_features.txt", 'w')

outfile.write(str("ID_feature = np.array(%s)\nmachine_learning.setIdentityFeature(ID_feature, 'ID')\n") %(str(ones)))

for num in range(num_identity_features):
	values = []
	for val in range(num_seqs):
		values.append(choice([0,1]))
	outfile.write(str("ID_feature%d = np.array(%s)\nmachine_learning.setIdentityFeature(ID_feature%d, 'ID%d', add_not_feature=True)\n") %(num,str(values),num,num))
outfile.close()



outfile = open("fake_value_features.txt", 'w')

outfile.write(str("true_feature = np.array(%s)\nmachine_learning.setValueFeature(true_feature, 'true')\n") %(str(scores)))

for num in range(num_value_features):
	values = []
	for val in range(num_seqs):
		values.append(numpy.random.rand()*2 - 1.0)
	outfile.write(str("val_feature%d = np.array(%s)\nmachine_learning.setValueFeature(val_feature%d, 'val%d')\n") %(num,str(values),num,num))
outfile.close()
	

