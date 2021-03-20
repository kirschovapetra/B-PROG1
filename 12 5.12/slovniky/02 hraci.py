def nova_sezona(d,postupujuci):
    for i in range(2):
        minIndex = 0
        min_val = min(d.values())
        for i in d:
            if d[i] == min_val:
                minIndex = i
        del(d[minIndex])
 
    for i in postupujuci:
        d[i] = 0
    # Nastavime body vsetkym teamom na 0
    for team in d:
        d[team] = 0
    return d
 
vysledky={'Chelsea':93, 'Liverpool':76, 'Arsenal':75, 'Hull City':34,'Sunderland':24}
p=['Watford','Southampton']
print(nova_sezona(vysledky,p))
