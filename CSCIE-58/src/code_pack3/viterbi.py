# viterbi.py
# Ashkan Bigdeli 
# Assignment  4/8/15
#
# This program will find the best possible path through a Hidden Markove Model
# using the veterbi algorithm and print a corresponding table as well as path. 
#
# !!!
# This program has been adapted and modified slightly from the example and explanations
# shown at http://en.wikipedia.org/wiki/Viterbi_algorithm
# Visit this url for the original source. 
# !!!
#
# Bugs: The forward algorithm does not work sadly, it simply sums everything
#        and all I am left with is repeated values. 
# Usage: Modify each of the instance variables, states, obs, start_p, trans_p
#        and emit_p to your given markov model and simply run viterbi.py

# array of states
states =('Fair', 'Bias')

# array of observed output
obs = ('H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T')

#starting probabilites for each state
start_p = { 'Fair' : 0.5, 'Bias' : 0.5 }

# dictionary of state transistion probablity 
trans_p = {
              'Fair' : {'Fair': 0.9, 'Bias': 0.1},
              'Bias' : {'Fair': 0.1, 'Bias': 0.9}
          }

# dictionary of emission probablities                        
emit_p = {
              'Fair' : {'H': 0.5, 'T': 0.5},
              'Bias' : {'H': 0.75, 'T': 0.25}
         }
             
             
def viterbi(obs, states, start_p, trans_p, emit_p):
    # array of dictionaries to store paths
    V = [{}]
    path = {}
 
    # multiply starting prob to emission prob
    # set path
    for i in states:
        V[0][i] = start_p[i] * emit_p[i][obs[0]]
        path[i] = [i]

 
    # Run Viterbi for each observation, add max to V array of dictionaries
    for j in range(1, len(obs)):
        #add path to array of dictionaries
        V.append({})
        newpath = {}
 
        #for each state, take the max of the that state transition OR emission probablity
        #for forward algorithm, comment out line 61, uncomment line 62-63
        for y in states:
            (prob, state) = max((V[j-1][y0] * trans_p[y0][y] * emit_p[y][obs[j]], y0) for y0 in states)
            prob = sum((V[j-1]['Fair'] * trans_p['Fair'][y] * emit_p[y][obs[j]]) for y in states)
            state = y
            V[j][y] = prob
            newpath[y] = path[state] + [y]
        # reset path
        path = newpath
    return V
 
# print table
def print_table(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        # print to 5 decimals including state
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)

V_table = viterbi(obs, states, start_p, trans_p, emit_p)
print_table(V_table)