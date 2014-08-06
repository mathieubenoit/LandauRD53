#include "TMath.h"
#include "TRandom3.h"



double MyFormula(double Lambda,int Nbit_final,double Ep ,double mass , double x,double Threshold ,double Overflow ){
	

	
	return (pow(2.0, Nbit_final) - 1)*(178.944*pow(Ep, 2)*Lambda*x/(pow(Ep, 2) - pow(mass, 2)) + 178.944*pow(Ep, 2)*x*(log(178.944*pow(Ep, 2)*x/(pow(Ep, 2) - pow(mass,
	2))) - log(17860.5*pow(Ep, 2)*(1 - (pow(Ep, 2) - pow(mass, 2))/pow(Ep, 2))/(mass*(pow(Ep, 2) - pow(mass, 2)))))/(pow(Ep, 2) - pow(mass, 2)) - Threshold -
	0.423)/(Overflow - Threshold);
	
	}



int GetABitcode(){
	
	
	int Nbit_final = 4;
	double Ep = 5600000 ;
	double mass = 511;
	double x = 100e-4;
	double Threshold = 5;
	double Overflow = 50;
	
	
	int bc = MyFormula(gRandom->Landau(),Nbit_final,Ep,mass,x,Threshold,Overflow);
	
	if(bc<0){
		return -1;
		}
	else {
	
		return bc;
	};
	
	
}
