#!/usr/bin/env python3

def nl_to_string(n,l,elec):	
	l_dict = {0:'s',1:'p',2:'d',3:'f'}
	return str(n)+l_dict[l]+str(elec)

def print_string(entry_list):

	conf_strings = []
	for entry in entry_list:
		string = nl_to_string(entry['n'],entry['l'],entry['elec'])
		conf_strings.append(string)

	print('.'.join(conf_strings))

def get_combs(nl):

	combs = []
	for n in range(1,nl+1):
		l = nl - n
		if l < n:
			combs.append((n,l))

	return combs

def get_entries(N):

	entries = []

	nl = 1
	while N > 0:
		
		combs = get_combs(nl)
		for comb in combs:
			n = comb[0]
			l = comb[1]
			elec = 4*l + 2

			if elec <= N:
				N -= elec
			elif elec > N:
				elec = N
				N = 0

			entries.append({'n':n,'l':l,'elec':elec})
			if N == 0:
				break
		nl += 1

	return entries

if __name__ == '__main__':

	N = int(input('Give me the atomic number! '))

	conf_entries = get_entries(N)
	print_string(conf_entries)
		
