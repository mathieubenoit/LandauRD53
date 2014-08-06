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



def GetLandauParameter(x,mass,Ep) : 


	landau = TF1("landau"," ROOT::Math::landau_pdf(x)",-100,100)
	landau.SetNpx(10000)



	histo = TH1D("%f"%x,"",5000,0,1000)

	l=-50

	for i in xrange(100000) : 
	
		E=LambdaInv(x,mass,Ep,l)
		histo.Fill(E,landau.Eval(l))
		l+=0.01

	#histo.Draw("goff")
	
	f1 =TF1("f1","[0]*TMath::Landau(x,[1],[2])",-100,100);
	f1.SetParameters(histo.GetMaximum(),histo.GetMean(),histo.GetRMS())

	histo.Fit(f1,"NR","",histo.GetMean()-5,histo.GetMean()+10)
	
	
	return f1.GetParameter(1),f1.GetParameter(2)
	
	
	
x=0.05*mm
mass=511*keV
Ep=5.6*GeV	

npoints = 60
gr_mean=TGraph(npoints)
gr_sigma=TGraph(npoints)
	
	
for i in range(npoints): 
	mean,sigma=GetLandauParameter(x+i*10*um,mass,Ep)
	gr_mean.SetPoint(i,(x+i*10*um)/um,mean)
	gr_sigma.SetPoint(i,(x+i*10*um)/um,sigma)
	
	
	
can1 = TCanvas()
gr_mean.Draw("a*")
gr_mean.GetXaxis().SetTitle("Thickness (#mum)")	
gr_mean.GetYaxis().SetTitle("Landau's most probable value (keV)")	

can2 = TCanvas()
gr_sigma.Draw("a*")	
gr_sigma.GetXaxis().SetTitle("Thickness (#mum)")	
gr_sigma.GetYaxis().SetTitle("#sigma(keV)")		
	
rootfile = TFile("LandauParameter_5.6GeV_Electron_Silicon.root" , "recreate")
gr_mean.Write()
gr_sigma.Write()
rootfile.Close()	
	
	
	
	
	
	
	
