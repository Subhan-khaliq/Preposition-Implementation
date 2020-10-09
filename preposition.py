def converse(s):
    a=s.find(">")
    if s[0]=="~":
        return (s[a+1: ]+"->"+s[0:2])
    if "~" in s[a:]:
        return (s[a+1: ]+"->"+s[0:1])
    else:
        return (s[a+1: ]+"->"+s[0])

def inverse(d):
    a=d.find(">")
    if "~" not in d[:d.find("-"):] and "~" not in d[a:]:
        return "~"+d[:d.find("-"):]+"->"+"~"+d[a+1:]
    if "~" in d[:d.find("-")] and "~" in d[a:]:
        return d[1:d.find("-")]+"->"+d[a+2:]
    if "~" not in d[:d.find("-"):] and "~" in d[a:]:
        return "~" +d[:d.find("-"):]+"->" +d[a+2]
    else:
        return d[1:d.find("-")]+"->"+"~"+d[a+1:]



def contrapositive(t):
    a=t.find(">")
    if "~" in t[:t.find("-"):] and "~" in t[a:]:
        return t[a+2:]+"->"+t[1:t.find("-"):]
    if "~" not in t[:t.find("-"):] and "~" not in t[a:]:
        return "~" + t[a+1:]+"->"+"~"+t[:t.find("-"):]
    if "~" not in t[:t.find("-"):] and "~" in t[a:]:
        return t[a+2:]+"->"+"~"+t[:t.find("-"):]
    else:
        return "~"+t[a+1:]+"->"+t[1:t.find("-"):]



def preposition(x,y):
    if y=="implication":
        print("Implication : ",x)
        print("Converse : ",converse(x))
        print("Inverse : ",inverse(x))
        print("Contrapositive : ",contrapositive(x))
    elif y=="inverse":
        d=inverse(x)
        print("Implication : ",d)
        print("Converse : ",converse(d))
        print("Inverse : ",inverse(d))
        print("Contrapositive : ",contrapositive(d))
    elif y=="converse":
        c=converse(x)
        print("Implication : ",c)
        print("Converse : ",converse(c))
        print("Inverse : ",inverse(c))
        print("Contrapositive : ",contrapositive(c))
    elif y=="contrapositive":
        e=contrapositive(x)
        print("Implication : ",e)
        print("Converse : ",converse(e))
        print("Inverse : ",inverse(e))
        print("Contrapositive : ",contrapositive(e))


preposition("~p->q","implication")
print('\n')
preposition("~p->q","inverse")
print('\n')
preposition("~p->q","converse")
print('\n')
preposition("~p->q","contrapositive")