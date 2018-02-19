import csv
import numpy as np
import math
from scipy import stats
from astropy.time import Time
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import ticker
import re
import datetime


#file = 'XRT_AMI_abs.csv'
BATfile= 'SWIFTJ1753.5-0127.lc.txt'
XRTfile= ['XRT_J1753fits_FTEST.txt','J1753fits_EVERYTHING.txt']
XRTfile=XRTfile[1]
RADIOfile= 'radio_data.dat'

xlim = [53500,57300]
#xlim = [56400,56900]
##### Read in the data #####

radio_data=[]
XRT_data=[]
BAT_data=[]


### Read data:

with open(RADIOfile, 'rb') as f:

    # Strip headers:
    header_line = f.readline()

   
    for row in f:
        row =  row.split()
        
        radio_data.append({'epoch':Time(float(row[0]),format='mjd').mjd,\
            '15GHz':(row[1]),\
            '15GHz_err':(row[2]),\
            '1.7GHz':(row[3]),\
            '1.7GHz_err':(row[4]),\
            '1.4GHz':(row[5]),\
            '1.4GHz_err':(row[6]),\
            '4.8GHz':(row[7]),\
            '4.8GHz_err':(row[8]),\
            '8.4GHz':(row[9]),\
            '8.4GHz_err':(row[10]),\
            '4.9GHz':(row[11]),\
            '4.9GHz_err':(row[12]),\
            '8.5GHz':(row[13]),\
            '8.5GHz_err':(row[14]),\
            })          



def bin_BAT(data,bin_size=5):

    # initially sort data into numpy array
    epoch,cts,err,binned_data = [],[],[],[]
    for i in data:
        epoch.append(i['BAT_epoch'])
        cts.append(i['BAT_rate'])
        err.append(i['BAT_err'])

    bins = np.linspace(min(epoch),max(epoch),len(epoch)/bin_size)

    binned_cts = stats.binned_statistic(epoch,cts,'mean',bins=bins)
    binned_err = stats.binned_statistic(epoch,err,'mean',bins=bins)
    

    
    for i in range(len(binned_cts[1][:-1])):
        binned_data.append({'BAT_epoch':Time(float(binned_cts[1][i]),format='mjd').mjd,\
            'BAT_rate':(float(binned_cts[0][i])),\
            'BAT_err':(float(binned_err[0][i])),\
            })    
    return binned_data
        

  
    
with open(BATfile, 'rb') as f:

    # Strip headers:
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
   
    for row in f:
    
        row =  row.split()
    
    
        BAT_data.append({'BAT_epoch':Time(float(row[0]),format='mjd').mjd,\
            'BAT_rate':(float(row[1])),\
            'BAT_err':(float(row[2])),\
            })     

    BAT_data = bin_BAT(BAT_data,5)


with open(XRTfile, 'rb') as f:

    # Strip headers:
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()
    header_line = f.readline()       
      
    for row in f:
    
        row =  row.split()
        
        XRT_data.append({'epoch':Time(float(row[0]),format='mjd').mjd,\
            'XRT_nH':(float(row[1])),\
            'XRT_nH_UL':(float(row[2])),\
            'XRT_nH_LL':(float(row[3])),\
            'XRT_kT':(float(row[4])),\
            'XRT_kT_UL':(float(row[5])),\
            'XRT_kT_LL':(float(row[6])),\
            'XRT_N_d':(float(row[7])),\
            'XRT_N_d_UL':(float(row[8])),\
            'XRT_N_d_LL':(float(row[9])),\
            'XRT_Gamma':(float(row[10])),\
            'XRT_Gamma_UL':(float(row[11])),\
            'XRT_Gamma_LL':(float(row[12])),\
            'XRT_N_Gamma':(float(row[13])),\
            'XRT_N_Gamma_UL':(float(row[14])),\
            'XRT_N_Gamma_LL':(float(row[15])),\
            'XRT_absflux':(float(row[16])),\
            'XRT_absflux_UL':(float(row[17])),\
            'XRT_absflux_LL':(float(row[18])),\
            'XRT_unabsflux':(float(row[19])),\
            'XRT_unabsflux_UL':(float(row[20])),\
            'XRT_unabsflux_LL':(float(row[21])),\
            'XRT_PLflux':(float(row[22])),\
            'XRT_PLflux_UL':(float(row[23])),\
            'XRT_PLflux_LL':(float(row[24])),\
            'XRT_chi2':(float(row[25])),\
            'XRT_dof':(float(row[26]))         
            })     

###############################################


def plot_BAT(data):

    epoch=[]
    BAT_rate=[]
    BAT_err=[]
    BAT_upper=[]
    
    # BAT 1 cts/cm^2 -> 0.16  BAT cts/dector -> 5.946E-08 erg /cm/cm/s unbs   
    BAT_to_flux = 5.946E-08 
    
    for i in data: 
    
       
        epoch.append(i['BAT_epoch']) 
    
        if float(i['BAT_rate'])>float(i['BAT_err']):
    
            BAT_rate.append(float(i['BAT_rate']) * BAT_to_flux )
            BAT_err.append(float(i['BAT_err']) * BAT_to_flux )
            BAT_upper.append(0)               
        else:
            BAT_rate.append(float(i['BAT_err']) * BAT_to_flux )
            BAT_err.append(float(i['BAT_err']) * BAT_to_flux /1.001)
            BAT_upper.append(1)   
        
    ax3 = plt.subplot(3, 1, 1)
    ax3.semilogy(epoch,BAT_rate,marker=',',ls='None',label='Swift-BAT (15-50 keV)',color='black')
    ax3.errorbar(epoch,BAT_rate,marker=',',yerr=BAT_err,ls='None',color='black',capsize=1, uplims=BAT_upper,elinewidth=0.5)
    ax3.legend(loc=1, ncol=4, numpoints=1,frameon=False,prop={'size':10.5})
    ax3.set_ylim(1e-11,1e-8)
    ax3.set_ylabel(r"Hard X-ray unabsorbed flux" "\n(erg cm$^{-2}$ s$^{-1}$)")
    ax3.set_xlim(xlim)


    ax4= ax3.twiny() 
    #t = Time(epoch, format='mjd', scale='utc')
    #ax4.semilogy(t.decimalyear,BAT_rate,marker=',',ls='None',label='Swift-BAT (15-50 keV)',color='grey')
    ax4.set_xticks([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])

    xlim_yr = Time(xlim, format='mjd', scale='utc').decimalyear
    ax4.set_xlim(xlim_yr)



 #   ax4= ax3.twiny() 
  #  t = Time(epoch, format='mjd', scale='utc')
  #  ax4.semilogy(t.decimalyear,BAT_rate,marker=',',ls='None',label='Swift-BAT (15-50 keV)',color='grey')
   # ax4.set_xticks([2005,2007,2009,2011,2013,2015])
 
 



     
    ax3.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
    


    ax3.axvline(x=57155, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='black',alpha=0.5)
    ax3.axvline(x=56461, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='red',alpha=0.5)




def plot_XRT(data):
    epoch=[]
    Xray=[]
    Xray_err=[]
    Xray_upper=[]
            
    for i in data:

        sigma=1
       
        try:         
            epoch.append(i['epoch'])

            if float(i['XRT_unabsflux'])>sigma*(float(i['XRT_unabsflux'])-float(i['XRT_unabsflux_LL'])):
  
                Xray.append(float(i['XRT_unabsflux_LL']))
                Xray_err.append(float(i['XRT_unabsflux'])-float(i['XRT_unabsflux_LL']))
                Xray_upper.append(0)               
            else:
                Xray.append(np.nan)
                Xray_err.append(sigma*(float(i['XRT_unabsflux'])-float(i['XRT_unabsflux_LL'])))
                Xray_upper.append(1)   

        except:
            Xray.append(np.nan)
            Xray_err.append(np.nan)
            Xray_upper.append(np.nan)
          

    ax2 = plt.subplot(3, 1, 2)                             
    ax2.semilogy(epoch,Xray,marker='.',markersize=2,ls='None',label='Swift-XRT (0.6-10 keV)',color='black')
    ax2.errorbar(epoch,Xray,yerr=Xray_err,ls='None',color='black',uplims=Xray_upper,capsize=2, elinewidth=1)
    ax2.legend(loc=1, ncol=2, numpoints=1,frameon=False,prop={'size':10.5})
            
    ax2.set_ylabel(r"Soft X-ray unabsorbed flux" "\n(erg cm$^{-2}$ s$^{-1}$)")
    ax2.set_ylim(1e-10,1e-7)     
    ax2.set_yticks([1e-10, 1e-10, 1e-9,1e-8])
    ax2.set_xlim(xlim)


    ax2.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off

    plt.axvline(x=57155, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='black',alpha=0.5)
    plt.axvline(x=56461, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='red',alpha=0.5)




def plot_radio(data,freq):
    epoch=[]
    radio=[]
    radio_err=[]
    radio_upper=[]

            
    for i in data:

        sigma=1
        # used for selecting time ranges to calculate the mean, std, var, etc.
        #if i['epoch'] < 53660: continue
        #if i['epoch'] > 57041: continue
            
        try:
            epoch.append(i['epoch'])
            
            if float(i[freq])>sigma*float(i[freq+'_err']):
                radio.append(float(i[freq]))
                radio_err.append(float(i[freq+'_err']))
                radio_upper.append(0)
            else:
                radio.append(float(i[freq+'_err']))
                radio_err.append(float(i[freq+'_err'])/2.5)
                radio_upper.append(1)    
        except:
            radio.append(np.nan)
            radio_err.append(np.nan)
            radio_upper.append(np.nan)                 
     
          
    if freq == '15GHz':
        freq_label='AMI-LA (15 GHz)'
        color = 'black'               
    if freq == '1.4GHz':
        freq_label='VLA (1.4 GHz)'
        color = 'orange' 
    if freq == '1.7GHz':
        freq_label='MERLIN (1.7 GHz)'
        color = 'blue'         
    if freq == '4.8GHz':
        freq_label='VLA (4.8 GHz)'
        color = 'purple'    
    if freq == '8.4GHz':
        freq_label='VLA (8.4 GHz)'
        color = 'green'    
    if freq == '4.9GHz':
        freq_label='WSRT (4.9 GHz)'
        color = 'yellow'
    if freq == '8.5GHz':
        freq_label='WSRT (8.5 GHz)'
        color = 'grey'       
    if freq == '8.4GHz' and data[0]['epoch']==57155.:
        freq_label='JVLA (8.5 GHz)'
        color = 'red'     
    """
    if freq == 'Deep_VLA':
        freq_label='8.5 GHz'
        color = 'cyan'     
    """    
    
    
    epoch_dection,radio_dection,radio_err_dection,\
    epoch_nondection,radio_nondection,radio_err_nondection=[],[],[],[],[],[]
    for i in range(len(radio_upper)):

        if radio_upper[i] == 0:
            # radio detection
            epoch_dection.append(epoch[i])
            radio_dection.append(radio[i])
            radio_err_dection.append(radio_err[i])
    
        if radio_upper[i] == 1:
            # radio detection
            epoch_nondection.append(epoch[i])
            radio_nondection.append(radio[i])
            radio_err_nondection.append(radio_err[i])
    
    
       
    ax1 = plt.subplot(3, 1, 3)      
      
                               
    ax1.semilogy(epoch_dection,radio_dection,marker='.',ls='None',markersize=5,label=freq_label,color=color)
    ax1.errorbar(epoch_dection,radio_dection,yerr=radio_err_dection,ls='None',color=color,uplims=0,capsize=3, elinewidth=0.5)

    ax1.semilogy(epoch_nondection,radio_nondection,marker='o',ls='None',markerfacecolor='None',markersize=5,label=None,markeredgecolor=color,alpha=0.5)
    ax1.errorbar(epoch_nondection,radio_nondection,yerr=radio_err_nondection,ls='None',color=color,uplims=1,capsize=2, elinewidth=0.5,alpha=0.5)

 
    ax1.legend(loc=1, ncol=4, numpoints=1,frameon=False,prop={'size':10.5})
    ax1.set_ylim([1e-5,1e-2])
    ax1.set_yticks([1e-5, 1e-4, 1e-3])

    ax1.set_xlabel(r'Epoch (MJD)')  
    ax1.set_ylabel('Radio flux density\n(Jy)')

    ax1.set_xlim(xlim)
    
    plt.axvline(x=57155, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='black',alpha=0.5)
    plt.axvline(x=56461, ymin=0, ymax = 1, linewidth=0.5, linestyle='--', color='red',alpha=0.5)

    return (radio_dection+radio_nondection)

###############################################
    


def plot_lightcurve(radio_data,XRT_data,BAT_data):

    fig = plt.figure(figsize=(12,9))  
    
 
    
    deep_VLA = [{'epoch':57155.,'epoch2':57155.,'8.4GHz':0e-6,'8.4GHz_err':21e-6,'XRT_flux':1.36e-9,'XRT_flux_err':1.50e-9,'separation':0.0}]

    all_radio=[]

    all_radio.extend(plot_radio(radio_data,'1.4GHz'))
    all_radio.extend(plot_radio(radio_data,'4.8GHz'))
    all_radio.extend(plot_radio(radio_data,'8.4GHz'))
    all_radio.extend(plot_radio(radio_data,'1.7GHz'))
    all_radio.extend(plot_radio(radio_data,'4.9GHz'))
    all_radio.extend(plot_radio(radio_data,'8.5GHz'))
    all_radio.extend(plot_radio(radio_data,'15GHz'))
    all_radio.extend(plot_radio(deep_VLA,'8.4GHz'))

    
    # remove NaNs
    ta= []
    for i in range(len(all_radio)):
        if math.isnan(all_radio[i]) == True:
            continue
        ta.append(all_radio[i])
    all_radio = ta   
  
    
    print ('\nThe Mean, Var and STD:',np.mean(all_radio),np.var(all_radio),np.std(all_radio))
    print ('The noise corrected RMS:',np.sqrt(np.var(all_radio)-(50e-6)**2),'\n')
    
    plot_XRT(XRT_data)
    #plot_XRT_NGamma(XRT_data)
    plot_BAT(BAT_data)
    

    fig.subplots_adjust(hspace=0, wspace=0)
    plt.savefig('SwiftJ1753_lightcurve_publish.png')
    plt.savefig('SwiftJ1753_lightcurve_publish.eps')


    


for i in range(len(XRT_data)): XRT_data[i]['XRT_unabsflux'] = 10**(XRT_data[i]['XRT_unabsflux'])
for i in range(len(XRT_data)): XRT_data[i]['XRT_unabsflux_UL'] = 10**(XRT_data[i]['XRT_unabsflux_UL'])
for i in range(len(XRT_data)): XRT_data[i]['XRT_unabsflux_LL'] = 10**(XRT_data[i]['XRT_unabsflux_LL'])
for i in range(len(XRT_data)): XRT_data[i]['XRT_absflux'] = 10**(XRT_data[i]['XRT_absflux'])
for i in range(len(XRT_data)): XRT_data[i]['XRT_absflux_UL'] = 10**(XRT_data[i]['XRT_absflux_UL'])
for i in range(len(XRT_data)): XRT_data[i]['XRT_absflux_LL'] = 10**(XRT_data[i]['XRT_absflux_LL'])



    
plot_lightcurve(radio_data,XRT_data,BAT_data)
plt.show()