#Program to calculate switching functions for PLUMED CMAP, using the function provided by PLUMED v 1.3.
#Output is intended for QUANTUM ESPRESSO version 5.3.0
# By Francisco Carrascoza
# August 8th, 2020


import os


a1 = input("\nAtom1: ")
a2 = input("\nAtom2: ")
rab = float( input("\nInput distance (in A -> Borh): "))

n=6
m=12
w_ab = 1
rab =  rab / 0.529177
 
def Reference_Dab(a1,a2):
	nco = ('NCO')
	h = set('H')
	

	if (a1 == 'N' or a1 == 'C' or a1 == 'O') and (a2 == 'N' or a2 == 'C' or a2 == 'O'):

		r0ab = 3.40151 # = 1.8 A
		cab =  3.40152
	elif ( a1 == 'N' or a1 == 'C' or a1 == 'O') and a2 == 'H':
		r0ab= 2.83459 # 1.5 A
		cab = 2.83460
	elif (a2 == 'N' or a2 == 'C' or a2 == 'O') and a1 == 'H':
		r0ab= 2.83459 # 1.5 A
		cab = 2.83460
	elif a1 == 'H' and a2 == 'H':
		r0ab = 2.64562 # 1.5 A
		cab =  2.64563
	else:
		print("\nError: non of the given atoms is the list.")


	return(r0ab,cab)

def factor(rab, r0ab):
	f1 = (rab/r0ab)**n
	f2 = (rab/r0ab)**m
	f1 = 1 - f1
	f2 = 1 - f2
	f = f1/f2
	print("\nFactor: {}".format(f))
	return (f)

def Dab(a1,a2,rab):

	r0ab,cab = Reference_Dab(a1,a2)
	f = factor(rab,r0ab)
	theta = cab - rab
	d_ab = theta * w_ab * f
	return (d_ab)

d_ab = Dab(a1,a2,rab)

print("\n{:5f}".format(d_ab))

