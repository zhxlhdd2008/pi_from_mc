import random

ofile = 'pi.dat'
fo = file(ofile,'w')

num_pi    = 0.0

nparticle = 1000000
i_cicle   = 0
i_square  = 0
for i in range(nparticle):
  i_square+=1
  random_number1 = random.random()
  random_number2 = random.random()
  if random_number1**2+random_number2**2<1.0:
    i_cicle+=1
  num_pi = float(i_cicle)/float(i_square)*4.0
  print i_square, num_pi
  fo.write('%8i ' %i_square)
  fo.write('%25.15g ' %num_pi)
  fo.write('\n')
fo.close()
