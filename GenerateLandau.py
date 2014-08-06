from ROOT import * 


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


def BitCodeToLambda(b,xmin,xmax,nbits) : 

	
	dl = (xmax-xmin)/(2**nbits-1)
	return xmin + b*dl

def EtoBitCode(E,emin,emax,nbits) : 

	
	dl = (emax-emin)/(2.**nbits-1)
	
	if(E<emax):
		return int(TMath.Floor((E-emin)/dl)) 
	elif(E<emin):
		return 0
	else:
		return (2**nbits-1)


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
	dE = eps*(Lambda) -1 +0.577 + eps*(log(eps)-log(I**2/(2*mass*(beta**2)*gamma**2))) +beta**2
	return dE
	

xmin = -5.
xmax = 500.


landau = TF1("landau"," ROOT::Math::landau_pdf(x)",-100,100)
landau.SetNpx(10000)

#landau.Draw("")



NBit = 16
nbin = 2**NBit
dx = (xmax-xmin)/nbin


emin = 5*keV
emax = 40*keV
dbit = (emax-emin)/(2**NBit -1)


NBitNew = 4
histo = TH1D("","",2**NBitNew,0,2**NBitNew)
histo2 = TH1D("","",100,0,50)


samplefile = open("Landau_Unitless_24bits.txt","w")



for i in xrange(nbin) : 
	x=BitCodeToLambda(i,xmin,xmax,NBit)
	E=LambdaInv(0.05*mm,511*keV,5.6*GeV,x)
	bc=EtoBitCode(E,emin,emax,NBitNew)
	histo.Fill(bc,landau.Eval(x))
	histo2.Fill(E,landau.Eval(x))
	samplefile.write("%i %f \n"%(i,landau.Eval(x)))
samplefile.close()	

histo2.DrawNormalized()




threshold = 3*keV
overflow = 25*keV
bitrange = overflow - threshold
dbit = bitrange/(2**NBit)


#for i in xrange(2**32) :

	






















