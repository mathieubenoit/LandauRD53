from ROOT import * 
from sympy import * 
from sympy.printing import print_ccode

eV=0.001
keV=1
MeV=1000
GeV=1000000

um=1e-4
mm=1e-1
cm=1.
m=100

mg=1
g=1000*mg

s=1

R = Rational
F = Float
I = Integer
Sy = symbols

eV=F(0.001)
keV=F(1)
MeV=F(1000)
GeV=F(1000000)

um=F(1e-4)
mm=F(1e-1)
cm=F(1.)
m=F(100)

mg=F(1)
g=F(1000*mg)

s=F(1)


#silicon properties
Z=F(14.)
A=F(28.)		
I=13.5*Z
rho = F(2.33*g/cm**3)

def BitCodeToLambda(b,xmin,xmax,nbits) : 

	
	dl = (xmax-xmin)/(2**nbits-1)
	return xmin + b*dl

def EtoBitCode(E,emin,emax,nbits) : 

	
	dl = (emax-emin)/(2.**nbits-1)
	return (E-emin)/dl
#	if(E<emax):
#		return int(TMath.Floor((E-emin)/dl)) 
#	elif(E<emin):
#		return 0
#	else:
#		return (2**nbits-1)


def LambdaInv(x,mass,Ep,Lambda) :
	
	Z=14.
	A=28.
	S= x*2.33*g/cm**3
	p = sqrt(Ep**2 - mass**2)		
	beta = p/Ep
	k=0.1
	#eps = (1.78/beta**2)*1e-2*keV*(x/um)
	
	eps = (0.1536/beta**2)*(Z/A)*S*keV
	
	I=13.5*Z
	epsmax=(2*511*keV*beta**2)/(1-beta**2)
	

	gamma = 1.0/sqrt(1-beta**2)				
	dE = eps*(Lambda) -1 +0.577 + eps*(log(eps)-log(I**2/(2*mass*(beta**2)*gamma**2))) 
	return dE


xmin = -5.
xmax = 500.

emin = Sy("Threshold")
emax = Sy("Overflow")

NBit = Sy("Nbit_ini")
NBitNew = Sy("Nbit_final")

nbin = 2**NBit



x=Sy("x")
mass =Sy("mass")
Ep=Sy("Ep")
b=Sy("bitcode")

#Lambda=BitCodeToLambda(b,xmin,xmax,NBit)
Lambda=Sy("Lambda")
E=LambdaInv(x,mass,Ep,Lambda)
new_bc=EtoBitCode(E,emin,emax,NBitNew)

print_ccode( new_bc)
