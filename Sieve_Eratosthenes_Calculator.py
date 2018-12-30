import __builtin__ as bi
def doprimes(decimal_value):
 #Primes from Range {All O/E}
 # n1 list
 bi.n1 = []
 bi.alltriggers = []
 bi.eventriggers = []
 bi.oddtriggers = []
 nlen = decimal_value
 # populate column n1
 population = 0
 for x in range(0,nlen+1):
  bi.n1.append(population)
  population += 1
 for tp in bi.n1:
  if tp < bi.n1[-1]:
   bi.alltriggers.append(tp**2)
   if tp**2 % 2 == 0:
    bi.eventriggers.append(tp**2)
   else:
    bi.oddtriggers.append(tp**2)
  else:
   break
 bi.allprimeslist = {}
 bi.evenprimeslist = {}
 bi.oddprimeslist = {}
 for r in xrange(len(bi.n1)):
  bi.allprimeslist[r] = {}
  bi.allprimeslist[r][bi.n1[r]] = []
  bi.evenprimeslist[r] = {}
  bi.evenprimeslist[r][bi.n1[r]] = []
  bi.oddprimeslist[r] = {}
  bi.oddprimeslist[r][bi.n1[r]] = []
  val = bi.n1[r]
  c = 1
  for s in xrange(1,val+1):
   if c >= val+1:
    c = 1
    break
   else:
    mal = val % c
    if mal == 0:
     bi.allprimeslist[r][bi.n1[r]].append(c)
     c2o = c % 2
     if c2o == 0:
      bi.evenprimeslist[r][bi.n1[r]].append(c)
     else:
      bi.oddprimeslist[r][bi.n1[r]].append(c)
   c+=1


doprimes(60000)

bi.allprimeslist
bi.evenprimeslist
bi.oddprimeslist
bi.alltriggers
bi.eventriggers
bi.oddtriggers
