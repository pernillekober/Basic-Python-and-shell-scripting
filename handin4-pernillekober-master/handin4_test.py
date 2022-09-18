import handin4 as h4

#Ex 2: call read_fasta on given input file
fasta_dict = h4.read_fasta("Ecoli.prot.fasta")
print(len(fasta_dict.keys()))

#Ex 4: 
yhcn = h4.find_prot(fasta_dict,"YHCN_ECOLI")

#Ex 5:
boom = h4.find_prot(fasta_dict, "BOOM_ECOLI")

# Ex 6:
matches = h4.find_prot2(fasta_dict, r'.{3}\_')
print(len(matches))