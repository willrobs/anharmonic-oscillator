
# coding: utf-8

# In[1]:

import numpy as np
import pandas
import sys

def bootstrap(spring_const,mass,la,lattice_spacing,num_config,num_lat_points,bootstrap_samples):
    mu=spring_const
    m=mass
    a=lattice_spacing
    niter=num_config
    points=num_lat_points
    smu=mu,
    sla=la,
    sm=m,
    sma=a,
    sniter=niter,
    spoints=points,
    smu=str(smu)
    sla=str(sla)
    sm=str(sm)
    sma=str(sma)
    sniter=str(sniter)
    spoints=str(spoints)
    name=smu+sla+sm+sma+sniter+spoints

    data=pandas.read_csv('2binned_data'+name+'.txt', delim_whitespace=True)
    datap=len(data.x2)
    ####first term
    energies_t1=[]
    sum2=0
    for p in range(bootstrap_samples):
        
        random_sample=np.random.choice(data.x2,datap)
        sum1=0
        for x in random_sample:
            
            sum1=sum1 + x
        
        energy=(mu**2)*(sum1/datap)
        energies_t1=np.append(energies_t1, energy)
        sum2=sum2+energy
        
    menergy_t1=sum2/bootstrap_samples
    
    sum1=0
    for q in energies_t1:
        sum1=sum1+(q-menergy_t1)**2
    
    std_t1=((1/bootstrap_samples)*sum1)**(0.5)
    
    ####second term
    energies_t2=[]
    sum2=0
    for p in range(bootstrap_samples):
        
        random_sample=np.random.choice(data.x4,datap)
        sum1=0
        for x in random_sample:
            
            sum1=sum1 + x
        
        energy=(3*la)*(sum1/datap)
        energies_t2=np.append(energies_t2, energy)
        sum2=sum2+energy
        
    menergy_t2=sum2/bootstrap_samples
    
    sum1=0
    for q in energies_t2:
        sum1=sum1+(q-menergy_t2)**2
    
    std_t2=((1/bootstrap_samples)*sum1)**(0.5)
    
    ###################
    menergy=menergy_t1 + menergy_t2
    std=std_t1 + std_t2
    print('Internal energy: ' ,menergy)
    print('error: ',std)
    
    g=open('info'+name+'.txt', 'a')
    g.write('col1' + '\t' + 'col2' + '\n')
    g.write(str(menergy) + '\t' + str(std) + '\n')
    g.close()
    
    
num_config=int(sys.argv[1])
num_lat_points=int(sys.argv[2])
a=float(sys.argv[3])
num_boot_samples=int(sys.argv[4])

mass=float(sys.argv[5])
mu=float(sys.argv[6])
la=float(sys.argv[7])

    
bootstrap(mu,mass,la,a,num_config,num_lat_points,num_boot_samples)

