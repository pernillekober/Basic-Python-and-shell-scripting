# Ex 1
wget http://wouterboomsma.github.io/ppds2020/data/british-english
wget http://wouterboomsma.github.io/ppds2020/data/british-english-subset

# Ex 2
diff british-english british-english-subset | cut -b 3 | uniq |sed '1d'

# Ex 3
grep -v '^[XYZ]' british-english > british-english-subset2