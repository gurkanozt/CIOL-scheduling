import matplotlib.pyplot as plt
import matplotlib as mpl
import schedulingProblem as SP
import solution as SS
import numpy as np

class tranformation():
    def __init__(self,problem,solution):
        self.jobs = list()
        self.machineName=list()#machines name in the gantt chart
        self.startTime=list()#start time set
        self.finishTime=list()#finish time set
        self.names=list()#operation name set
        self.colors=list()#operation color
        preEndTime=0#finish time of previous operation in the permutation
        indexa=0
        for i in solution.solution:
            job = i[0]#assign job to job id
            op = i[1]#assign op to operation id
            mak = i[2]#assign mak to machine id
            machineEndTime = solution.machines[mak].mlft#find machine latest finish time
            startTime = max(preEndTime,machineEndTime)#define current job start time
            preEndTime = startTime+i[3]#calculate current job finish time
            solution.machines[mak].mlft=preEndTime#update current machine last finis time
            solution.jobs[job].operations[op].ost = startTime#assign operation start time to solution jobs set
            solution.jobs[job].operations[op].oft = preEndTime#assign operation finish time to solution jobs set
            #print "bitis", solution.machines[mak].id, "\t",job,"\t",op,"\t",startTime,"\t",solution.machines[mak].mlft
            self.machineName.append(mak)#add machine id to machinename set
            self.startTime.append(startTime)#add operation start time to startTime set
            self.finishTime.append(preEndTime)#add operation finish time to finishTime set
            self.names.append([mak, startTime, preEndTime, "O_"+str(job)+str(op)])#add operation name to names set

            if job%2 ==0:
                self.colors.append("red")
            else:
                self.colors.append("green")
            indexa=indexa+1
        print "aa"
        #plt.rc('grid', linestyle="-", color='gray')

        #plt.grid(True)

        fig = plt.figure(figsize=(10,10))
        k=0

        cmaps  = ["Blues", "Greens", "Reds", "Purples", "Oranges", "Greens", "autumn"]

        for j in solution.machines:
            ax = fig.add_axes([0.05, 0.1 + k*0.12 , 0.9, 0.1])
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
            k += 1

        maxft = 3* max(self.finishTime)
        minst = min(self.startTime)
        range = maxft-minst
        k=0
        for j in solution.jobs:
            cmap = plt.get_cmap(cmaps[k])
            for o in j.operations:
                mid = o.machine.id
                nost = ((o.ost-minst) / range)      #normalized operatio start time
                noft = ((o.oft-minst) /range)       #normalized operation finis time
                ax = fig.add_axes([0.05+nost, 0.1 + 0.01 + mid * 0.12 , 0.05+noft, 0.08])
                cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                            orientation='vertical')
                ax.xaxis.set_visible(False)
                ax.yaxis.set_visible(False)

            k +=1

        #plt.hlines(self.machineName, 0, max(self.finishTime), color="gray", lw=44)#define gantt chart interval

        #plt.hlines(self.machineName, self.startTime, self.finishTime, colors=self.colors, lw=40)#draw Gantt Chart
        #plt.margins(0.1)
        #font = {
        #'size'   : 10}

        #plt.rc('font', **font)
        #plt.ylabel("MACHINE",color='red')
        #plt.xlabel("TIME",color='red')
        #for i in self.names:
        #    plt.text(i[1], i[0], i[3])

        plt.show()







'''def create_date(minute):
    """Creates the date"""

    minute = dt.datetime.minute(minute,1)
    mdate = matplotlib.dates.date2num(minute)

    return mdate
# Data


def drawGanttChart(problem,solution):
    pos = arange(0.5,5.5,0.5)
    ylabels = []
    for i in problem.machines:
        ylabels.append(str("Machine"+str(i.id)))

    ylabels.append('Hardware Design & Review')
    ylabels.append('Hardware Construction')
    ylabels.append('Integrate and Test Laser Source')
    ylabels.append('Objective #1')
    ylabels.append('Objective #2')
    ylabels.append('Present at ASMS')
    ylabels.append('Present Data at Gordon Conference')
    ylabels.append('Manuscripts and Final Report')

    effort = []
    for i in problem.jobs:
        pass
    effort.append([0.2, 1.0])
    effort.append([0.2, 1.0])
    effort.append([0.2, 1.0])
    effort.append([0.3, 0.75])
    effort.append([0.25, 0.75])
    effort.append([0.3, 0.75])
    effort.append([0.5, 0.5])
    effort.append([0.7, 0.4])

    customDates = []
    for i in solution:
        job=i[0]
        op=i[1]
        mak=i[2]
        a=problem.jobs[job].operations[op].ost
        b=problem.jobs[job].operations[op].oft
        customDates.append([mak,a,b])


    customDates.append([create_date(5)],[create_date(6)])
    customDates.append([create_date(6),create_date(8),create_date(8)])
    customDates.append([create_date(7),create_date(9),create_date(9)])
    customDates.append([create_date(10),create_date(3),create_date(3)])
    customDates.append([create_date(2),create_date(6),create_date(6)])
    customDates.append([create_date(5),create_date(6),create_date(6)])
    customDates.append([create_date(6),create_date(7),create_date(7)])
    customDates.append([create_date(4),create_date(8),create_date(8)])

    task_dates = list()
    for i,task in enumerate(ylabels):
            task_dates.append(customDates[i])
        # task_dates['Climatology'] = [create_date(5,2014),create_date(6,2014),create_date(10,2013)]
        # task_dates['Structure'] = [create_date(10,2013),create_date(3,2014),create_date(5,2014)]
        # task_dates['Impacts'] = [create_date(5,2014),create_date(12,2014),create_date(2,2015)]
        # task_dates['Thesis'] = [create_date(2,2015),create_date(5,2015)]

        # Initialise plot

    fig = plt.figure()
    # ax = fig.add_axes([0.15,0.2,0.75,0.3]) #[left,bottom,width,height]
    ax = fig.add_subplot(111)

    # Plot the data

    start_date,end_date = task_dates[ylabels[0]]
    ax.barh(0.5, end_date - start_date, left=start_date, height=0.3, align='center', color='blue', alpha = 0.75)
    #ax.barh(0.45, (end_date - start_date)*effort[0][0], left=start_date, height=0.1, align='center', color='red', alpha = 0.75, label = "PI Effort")
    #ax.barh(0.55, (end_date - start_date)*effort[0][1], left=start_date, height=0.1, align='center', color='yellow', alpha = 0.75, label = "Student Effort")
    for i in range(0,len(ylabels)-1):
        labels = ['Analysis','Reporting'] if i == 1 else [None,None]
        start_date,mid_date,end_date = task_dates[ylabels[i+1]]
        #piEffort, studentEffort = effort[i+1]
        ax.barh((i*0.5)+1.0, mid_date - start_date, left=start_date, height=0.3, align='center', color='blue', alpha = 0.75)
        #ax.barh((i*0.5)+1.0-0.05, (mid_date - start_date)*piEffort, left=start_date, height=0.1, align='center', color='red', alpha = 0.75)
        #ax.barh((i*0.5)+1.0+0.05, (mid_date - start_date)*studentEffort, left=start_date, height=0.1, align='center', color='yellow', alpha = 0.75)
    # ax.barh((i*0.5)+1.0, end_date - mid_date, left=mid_date, height=0.3, align='center',label=labels[1], color='yellow')

     # Format the y-axis

    locsy, labelsy = yticks(pos,ylabels)
    plt.setp(labelsy, fontsize = 14)

    # Format the x-axis

    ax.axis('tight')
    ax.set_ylim(ymin = -0.1, ymax = 4.5)
    ax.grid(color = 'g', linestyle = ':')

    ax.xaxis_date() #Tell matplotlib that these are dates...

    rule = rrulewrapper(MONTHLY, interval=1)
    loc = RRuleLocator(rule)
    formatter = DateFormatter("%b '%y")

    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(formatter)
    labelsx = ax.get_xticklabels()
    plt.setp(labelsx, rotation=30, fontsize=12)

    # Format the legend

    font = font_manager.FontProperties(size='small')
    ax.legend(loc=1,prop=font)

    # Finish up
    ax.invert_yaxis()
    fig.autofmt_xdate()
    #plt.savefig('gantt.svg')
    plt.show()


'''