#######JOINT FIELD PLOTS WITH INTENSITIES###################

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



f54=open('fields54_4.dat','r')
c54=open('circuit54_4.dat','r')
f55=open('fields55_5.dat','r')
c55=open('circuit55_5.dat','r')
f56=open('fields56_4.dat','r')
c56=open('circuit56_4.dat','r')
f57=open('fields57_0.dat','r')
c57=open('circuit57_0.dat','r')
f58=open('fields58_2.dat','r')
c58=open('circuit58_2.dat','r')
dataf54=np.loadtxt(f54)
datac54=np.loadtxt(c54)
dataf55=np.loadtxt(f55)
datac55=np.loadtxt(c55)
dataf56=np.loadtxt(f56)
datac56=np.loadtxt(c56)
dataf57=np.loadtxt(f57)
datac57=np.loadtxt(c57)
dataf58=np.loadtxt(f58)
datac58=np.loadtxt(c58)

I54=datac54[:,5]
I55=datac55[:,5]
I56=datac56[:,5]
I57=datac57[:,5]
I58=datac58[:,5]



# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
fig = plt.figure(figsize = (8,10))
#fig.text(0.5, 0.04, c, ha='center',fontsize=16)
#fig.text(0.0, 0.5, '$dU/dt$', va='center', rotation='vertical',fontsize=16)
# set height ratios for sublots
gs = gridspec.GridSpec(10, 1) 

# the fisrt subplot
ax0 = plt.subplot(gs[0])
# log scale for axis Y of the first subplot
divider0 = make_axes_locatable(ax0)
cax0 = divider0.append_axes("right", size="3%", pad=0.4)
cax0.axis('off')
line0, = ax0.plot(datac54[:,0], datac54[:,1], color='r')

#the second subplot
# shared axis X
ax1 = plt.subplot(gs[1], sharex = ax0)
#line1,= ax1.plot(data1[:,0],data1[:,1])
pos=ax1.imshow(dataf54.T, interpolation='nearest', aspect='auto',cmap='viridis')
divider1 = make_axes_locatable(ax1)
cax = divider1.append_axes("right", size="3%", pad=0.4 )
cbar1=plt.colorbar(pos, cax=cax, orientation='vertical')
#plt.colorbar(pos)

#line1, = ax1.imshow(data.T, interpolation='nearest', aspect='auto',cmap='viridis')
plt.setp(ax0.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax1.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)

# put lened on first subplot
#ax0.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='lower left')
#ax0.set_xlim([0,30000])
#ax0.set_ylim([6,12.5])
#ax1.set_xlim([0,30000])
#ax1.set_ylim([222,50])

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near





ax2 = plt.subplot(gs[2],sharex=ax1)
# log scale for axis Y of the first subplot
divider2 = make_axes_locatable(ax2)
cax0 = divider2.append_axes("right", size="3%", pad=0.4)
cax0.axis('off')
line2, = ax2.plot(datac55[:,0], datac55[:,1], color='r')

ax3 = plt.subplot(gs[3], sharex = ax2)
#line1,= ax1.plot(data1[:,0],data1[:,1])
pos=ax3.imshow(dataf55.T, interpolation='nearest', aspect='auto',cmap='viridis')
divider3 = make_axes_locatable(ax3)
cax = divider3.append_axes("right", size="3%", pad=0.4 )
cbar3=plt.colorbar(pos, cax=cax, orientation='vertical')
#plt.colorbar(pos)

#line1, = ax1.imshow(data.T, interpolation='nearest', aspect='auto',cmap='viridis')
plt.setp(ax1.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax2.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)




ax4 = plt.subplot(gs[4],sharex=ax3)
# log scale for axis Y of the first subplot
divider4 = make_axes_locatable(ax4)
cax0 = divider4.append_axes("right", size="3%", pad=0.4)
cax0.axis('off')
line4, = ax4.plot(datac56[:,0], datac56[:,1], color='r')

ax5 = plt.subplot(gs[5], sharex = ax4)
#line1,= ax1.plot(data1[:,0],data1[:,1])
pos=ax5.imshow(dataf56.T, interpolation='nearest', aspect='auto',cmap='viridis')
divider5 = make_axes_locatable(ax5)
cax = divider5.append_axes("right", size="3%", pad=0.4 )
cbar5=plt.colorbar(pos, cax=cax, orientation='vertical')
#plt.colorbar(pos)

#line1, = ax1.imshow(data.T, interpolation='nearest', aspect='auto',cmap='viridis')
plt.setp(ax2.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax2.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)






ax6 = plt.subplot(gs[6],sharex=ax5)
# log scale for axis Y of the first subplot
divider6 = make_axes_locatable(ax6)
cax0 = divider6.append_axes("right", size="3%", pad=0.4)
cax0.axis('off')
line6, = ax6.plot(datac57[:,0], datac57[:,1], color='r')

ax7 = plt.subplot(gs[7], sharex = ax6)
#line1,= ax1.plot(data1[:,0],data1[:,1])
pos=ax7.imshow(dataf57.T, interpolation='nearest', aspect='auto',cmap='viridis')
divider7 = make_axes_locatable(ax7)
cax = divider7.append_axes("right", size="3%", pad=0.4 )
cbar7=plt.colorbar(pos, cax=cax, orientation='vertical')
#plt.colorbar(pos)

#line1, = ax1.imshow(data.T, interpolation='nearest', aspect='auto',cmap='viridis')
plt.setp(ax1.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax2.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)






ax8 = plt.subplot(gs[8],sharex=ax7)
# log scale for axis Y of the first subplot
divider8 = make_axes_locatable(ax8)
cax0 = divider8.append_axes("right", size="3%", pad=0.4)
cax0.axis('off')
line8, = ax8.plot(datac58[:,0], datac58[:,1], color='r')

ax9 = plt.subplot(gs[9], sharex = ax8)
#line1,= ax1.plot(data1[:,0],data1[:,1])
pos=ax9.imshow(dataf58.T, interpolation='nearest', aspect='auto',cmap='viridis')
divider9 = make_axes_locatable(ax9)
cax = divider9.append_axes("right", size="3%", pad=0.4 )
cbar9=plt.colorbar(pos, cax=cax, orientation='vertical')
#plt.colorbar(pos)
cbar9.set_label('Mod. Bias ($mV$)',fontsize=12)

#line1, = ax1.imshow(data.T, interpolation='nearest', aspect='auto',cmap='viridis')
plt.setp(ax1.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax2.yaxis.get_major_ticks()
yticks[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)
cbar9.set_ticks([0.02,0.04,0.06])
cbar9.set_ticklabels(['10','35','60'])
#cbar9.setp(ax9.get_xticklabels(), fontsize=12)
cbar7.set_ticks([0.02,0.04,0.06])
cbar7.set_ticklabels(['10','35','60'])
cbar5.set_ticks([0.02,0.04,0.06])
cbar5.set_ticklabels(['10','35','60'])
cbar3.set_ticks([0.02,0.04,0.06])
cbar3.set_ticklabels(['10','35','60'])
cbar1.set_ticks([0.02,0.04,0.06])
cbar1.set_ticklabels(['10','35','60'])




ax0.set_xlim([0,20000])
ax0.set_ylim([8,16])
ax2.set_ylim([8,16])
ax4.set_ylim([8,16])
ax6.set_ylim([8,16])
ax8.set_ylim([8,16])


plt.setp(ax0.get_xticklabels(), visible=False)
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax7.get_xticklabels(), visible=False)
plt.setp(ax8.get_xticklabels(), visible=False)



#cbaxes = inset_axes(ax1, width="30%", height="3%", loc=3)

plt.setp(ax0.get_yticklabels(), fontsize=14)
plt.setp(ax1.get_yticklabels(), fontsize=14)
plt.setp(ax2.get_yticklabels(), fontsize=14)
plt.setp(ax3.get_yticklabels(), fontsize=14)
plt.setp(ax4.get_yticklabels(), fontsize=14)
plt.setp(ax5.get_yticklabels(), fontsize=14)
plt.setp(ax6.get_yticklabels(), fontsize=14)
plt.setp(ax7.get_yticklabels(), fontsize=14)
plt.setp(ax8.get_yticklabels(), fontsize=14)
plt.setp(ax9.get_yticklabels(), fontsize=14)
plt.setp(ax9.get_xticklabels(), fontsize=20)

#fig.text(0.0, 0.5, '$dU/dt$', va='center', rotation='vertical',fontsize=16)
#xticks=(np.arange(0,20000,2000), ('0', '2', '4', '6', '8','10','12','14','16','18'))
ax9.set_xticks([0,2000,4000,6000,8000,10000,12000,14000,16000,18000,20000])
ax9.set_xticklabels(['0','2','4','6','8','10','12','14','16','18','20'])

ax0.set_ylabel('$U_{qcl}$ ($V$)',fontsize=14,color="r")
ax3.set_ylabel('Mod. Indx', fontsize=14)
#fig.text(0.0, 0.5, 'Module Index', va='center', rotation='vertical',fontsize=18)
ax9.set_xlabel('Time ($ns$)', fontsize=20)

#ax0.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='upper left')
#ax2.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='upper left')
#ax4.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='lower left')
#ax6.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='lower left')
#ax8.legend((line0, line1), ('$56.90$ $V$', '$56.95$ $V$'), loc='lower left')

ax0.annotate("a) Region I - $705.82$ A/cm$^2$ - $54.4$ V", xy=(0.1, 0.7), xycoords="axes fraction",fontsize=12)
ax2.annotate("b) Region II - $712.50$ A/cm$^2$ - $55.5$ V", xy=(0.1, 0.7), xycoords="axes fraction",fontsize=12)
ax4.annotate("c) Region III - $722.86$ A/cm$^2$ - $56.4$ V", xy=(0.1, 0.7), xycoords="axes fraction",fontsize=12)
ax6.annotate("d) Region IV - $734.95$ A/cm$^2$ - $57.0$ V", xy=(0.1, 0.7), xycoords="axes fraction",fontsize=12)
ax8.annotate("e) Region V - $760.0$ A/cm$^2$ - $58.2$ V", xy=(0.1, 0.7), xycoords="axes fraction",fontsize=12)



################################Intensity plots##########################################


ax00=ax0.twinx()
ax22=ax2.twinx()
ax44=ax4.twinx()
ax66=ax6.twinx()
ax88=ax8.twinx()


divider00 = make_axes_locatable(ax00)
cax00 = divider00.append_axes("right", size="3%", pad=0.4)
cax00.axis('off')
divider22 = make_axes_locatable(ax22)
cax22 = divider22.append_axes("right", size="3%", pad=0.4)
cax22.axis('off')
divider44 = make_axes_locatable(ax44)
cax44 = divider44.append_axes("right", size="3%", pad=0.4)
cax44.axis('off')
divider66 = make_axes_locatable(ax66)
cax66 = divider66.append_axes("right", size="3%", pad=0.4)
cax66.axis('off')
divider88 = make_axes_locatable(ax88)
cax88 = divider88.append_axes("right", size="3%", pad=0.4)
cax88.axis('off')


plt.setp(ax00.get_xticklabels(), visible=False)
plt.setp(ax22.get_xticklabels(), visible=False)
plt.setp(ax44.get_xticklabels(), visible=False)
plt.setp(ax66.get_xticklabels(), visible=False)
plt.setp(ax88.get_xticklabels(), visible=False)
plt.setp(ax00.get_yticklabels(), visible=False)
plt.setp(ax22.get_yticklabels(), visible=False)
plt.setp(ax44.get_yticklabels(), visible=False)
plt.setp(ax66.get_yticklabels(), visible=False)
plt.setp(ax88.get_yticklabels(), visible=False)


ax00.plot(datac54[:,0],I54*1e5, label="Intensity (a.u.)")
ax22.plot(datac55[:,0],I55*1e5)
ax44.plot(datac56[:,0],I56*1e5)
ax66.plot(datac57[:,0],I57*1e5)
ax88.plot(datac58[:,0],I58*1e5)
ax00.set_xlim([0,20000])
ax22.set_xlim([0,20000])
ax44.set_xlim([0,20000])
ax66.set_xlim([0,20000])
ax88.set_xlim([0,20000])
ax00.legend(loc="upper right")
plt.show()
