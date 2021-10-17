#include "stm32f10x.h"
#include <math.h>



int main(){
	
//link lengths
double a1=2.0;
double a2=2.0;



double x=-2;
double y=2;


double phi1=0,phi2=0,phi3=0,T1=0,T2=0;
double r;

double pi=3.14;

	//initialize the clock for GPIOC, TIM4 and enable ALT function
	RCC->APB2ENR |=RCC_APB2ENR_IOPBEN | RCC_APB2ENR_AFIOEN;
	RCC->APB1ENR |=RCC_APB1ENR_TIM4EN;
	
	//configure pin9 on GPIOC as output ALT-PUSH/PULL @50MHZ
	GPIOB->CRH |= GPIO_CRH_MODE9_0 | GPIO_CRH_MODE9_1 | GPIO_CRH_CNF9_1;
	GPIOB->CRH &= ~(GPIO_CRH_CNF9_0);
	
	//TIMER


	TIM4->CCER |= TIM_CCER_CC4E;
	TIM4->CR1 |= TIM_CR1_ARPE;
	TIM4->CCMR2 |= TIM_CCMR2_OC4M_1 | TIM_CCMR2_OC4M_2 | TIM_CCMR2_OC4PE;
	
	TIM4->PSC=100;
	TIM4->ARR=2000;
	TIM4->CCR4 =0;
	
	TIM4->EGR |= TIM_EGR_UG;
	TIM4->CR1 |=TIM_CR1_CEN;
	
	
	while(1)
		
	{



    //IK
    r = sqrt(pow(x,2)+pow(y,2));

    if(x>=0 && y>=0)
		{
    
        phi1 = acos((pow(a1,2)+pow(r,2)-pow(a2,2))/(2*a1*r));
        phi2 = atan(y/(x+0.00001));
        phi3 = acos((pow(a1,2)+pow(a2,2)-pow(r,2))/(2*a1*a2));
		}

    if(x<0 && y>0)
		{
        phi1 = -acos((pow(a1,2)+pow(r,2)-pow(a2,2))/(2*a1*r));
        phi2 = pi/2-atan(y/(x+0.00001));
        phi3 = -acos((pow(a1,2)+pow(a2,2)-pow(r,2))/(2*a1*a2)); 
		}			


    //joint angles
    T1=phi1+phi2;
    T2=phi3-pi;
		TIM1->CCR4=50; //T-on
	}
	



	
	
	
	
}
