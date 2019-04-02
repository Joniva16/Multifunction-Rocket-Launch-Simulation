from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


root = Tk()
root.geometry("1030x625")
root.title("Rocket Simulator 1.2")
root.configure(background="white")

frame_input= Frame(root,width=500,height=70)
frame_input.place(x=10,y=10)
lbl_time = Label(frame_input,text="Simulation duration:         ", font=(11),background="white")
lbl_time.pack()
entry_time = Entry(frame_input,bg="white",width=25,fg="blue")
entry_time.pack()

frame_input2= Frame(root,width=500,height=70)
frame_input2.place(x=10,y=60)
lbl_time4 = Label(frame_input2,text="Spacecraft acceleration:  ", font=(11),background="white")
lbl_time4.pack()
entry_time5 = Entry(frame_input2,bg="white",width=25,fg="blue")
entry_time5.pack()
lbl_time5 = Label(root,text="Configure temperature:",font=(13), background="white")
lbl_time5.place(x=10,y=267)

frame_bar= Frame(root,width=5,height=1700, bg="black")
frame_bar.place(x=245,y=-0)

lbl_time = Label(root,text="*Simulate data of launch\nbefore atempting planetary \nsimulation", font=("Arial Bold",11),background="white",fg="red")
lbl_time.place(x=10,y=200)




fig1 = plt.figure(figsize=(4.6,3.77))
ax3 = fig1.add_subplot(111)
ax3.set_title("Rocket launch simulation 2.0")
canvas1 = FigureCanvasTkAgg(fig1)
canvas1.get_tk_widget().place(x=255,y=-10)
fig2 = plt.figure(figsize=(3.25,8))
ax2 = fig2.add_subplot(111)
harvest1 = np.array([[0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0],])
ax2.imshow(harvest1,zorder=1,cmap="YlOrRd", vmin=1.7, vmax=16,extent=[0,10,0,22])
img = plt.imread("vostok.png")
ax2.imshow(img,zorder=2,extent=[0,10,0,22])
def update(a):
    harvest2 = np.array([[int(a)+1.7],
                        [int(a)+2],
                        [int(a)+2.3],
                        [int(a)+2.3],
                        [int(a)+2.4],
                        [int(a)+2.4],
                        [int(a)+2.6],
                        [int(a)+2.6],
                        [int(a)+3],
                        [int(a)+3.2],
                        [int(a)+3.3],
                        [int(a)+3.5],
                        [int(a)+3.8],
                        [int(a)+4.2],
                        [int(a)+4.7],
                        [int(a)+5],
                        [int(a)+5.4],
                        [int(a)+5.5],
                        [int(a)+5.7],
                        [int(a)+6],])
    ax2.axis('off')
    ax2.set_title("Temperature of a space shuttle")
    img = plt.imread("vostok.png")
    ax2.imshow(harvest2,zorder=1,cmap="YlOrRd", vmin=5, vmax=11,extent=[0,10,0,22])
    ax2.imshow(img,zorder=2,extent=[0,10,0,22])
    fig2.canvas.draw_idle()

slider_temp = Scale(root,highlightthickness=0,width=19,from_=0,to=5,orient=HORIZONTAL, bg="white",length=200,command=update, showvalue=0,activebackground="black",borderwidth=0, font=("Arial",13),tickinterval=0.25)
slider_temp.place(x=10,y=297)

ax2.axis('off')
ax2.set_title("Temperature of a space shuttle\nin relation to thrust augmentation")
canvas2 = FigureCanvasTkAgg(fig2)
canvas2.get_tk_widget().place(x=690,y=-80)


def simulate():
    entry_time.configure(state="disabled")
    entry_time5.configure(state="disabled")
    button_input.configure(text="Disabled", bg="grey",state="disabled")
    time_inputed = int(entry_time.get())
    acc_inputed = int(entry_time5.get())

    if time_inputed > 0 and acc_inputed > 0:
        canvas1.get_tk_widget().destroy()
        fig = plt.figure(figsize=(4.6,3.5))
        ax = fig.add_subplot(111)
        x = []
        y = []

        def animate(frame):
            acc_inputed = int(entry_time5.get())
            distance = acc_inputed * (frame**2) /2
            distance_max = acc_inputed * (time_inputed**2) /2
            frame_max = time_inputed
            ax.set_xlim(0,(time_inputed+1)*1.05)
            ax.set_ylim(0,distance_max*1.08)
            y.append(distance)
            x.append(frame)
            ax.plot(x,y, "black")
            ax.set_title("Altitude at constant acceleration\nAltitude "+str(distance/1000)+" [km]")
            return ax

        distance_max = acc_inputed * (time_inputed**2) /2

        if distance_max > 10000000:
            ax.axhspan(distance_max*0.05,1000000000000000, facecolor="#474c72", label = "Exosphere")
            ax.axhspan(distance_max*0.04,distance_max*0.05, facecolor="#82f970", label = "Thermosphere")
            ax.axhspan(distance_max*0.02,distance_max*0.03, facecolor="#ede54e", label = "Mesosphere")
            ax.axhspan(distance_max*0.01,distance_max*0.02, facecolor="#9ee5ff", label = "Stratosphere")
            ax.axhspan(0,distance_max*0.01, facecolor="#ff6666", label="Troposphere")
        else:
            ax.axhspan(120000,1000000000, facecolor="#474c72", label = "Exosphere")
            ax.axhspan(80000,120000, facecolor="#82f970", label = "Thermosphere")
            ax.axhspan(50000,80000, facecolor="#ede54e", label = "Mesosphere")
            ax.axhspan(10000,50000, facecolor="#9ee5ff", label = "Stratosphere")
            ax.axhspan(0,10000, facecolor="#ff6666", label="Troposphere")

        ax.legend(loc='upper left')
        canvas = FigureCanvasTkAgg(fig)
        canvas.get_tk_widget().place(x=255,y=10)
        ani = FuncAnimation(fig, animate, frames=(time_inputed+1), interval=1,repeat=False)


    else:
        exit()

def simulate2():
    time_inputed = int(entry_time.get())
    acc_inputed = int(entry_time5.get())
    button_input2.configure(text="Disabled", bg="grey",state="disabled")
    entry_time.configure(state="disabled")
    entry_time5.configure(state="disabled")
    if time_inputed > 0 and acc_inputed > 0:
        xe = [101500]
        ye= [0.75]
        xm= [486000]
        ym= [0.75]
        canvas5.get_tk_widget().destroy()
        fig5 = plt.figure(figsize=(4.75,2.8))
        ax5 = fig5.add_subplot(111)
        ax5.set_facecolor('xkcd:black')
        ax5.scatter(xe,ye,color="blue",edgecolor="green", s=500,label="Earth",zorder=2)
        ax5.scatter(xm,ym,color="grey",edgecolor="white", s=250,label="Moon",zorder=2)
        ax5.plot([-1],[-1], "red",label="Shuttle Trajectory")
        lgnd = ax5.legend(loc='upper left',scatterpoints=1)
        lgnd.legendHandles[1]._sizes = [130]
        lgnd.legendHandles[2]._sizes = [130]
        ax5.set_xlim(0,500000)
        ax5.set_ylim(0,2)
        ax5.get_xaxis().set_visible(False)
        ax5.get_yaxis().set_visible(False)
        canvas6 = FigureCanvasTkAgg(fig5)
        canvas6.get_tk_widget().place(x=255,y=365)
        x2 = [101500]
        y2 = [0.75]
        z=[0]
        def animate2(frame):
            acc_inputed = int(entry_time5.get())
            distance = acc_inputed * (frame**2) /2
            distance_max = acc_inputed * (time_inputed**2) /2
            frame_max = time_inputed
            finald1 = distance/1000
            y2.append(0.75)
            x2.append(x2[-1]+finald1)
            ax5.plot(x2,y2, "red",scaley=False,scalex=False,zorder=1)
            z.append(z[-1]+finald1)
            if x2[-1] < 486000:
                ax5.set_title("Distance from moon "+str(384500-z[-1])+" [km]")

            elif x2[-1] >= 486000:
                ax5.set_title("Distance from moon "+str(0)+" [km]")
            if x2[-1] >= 486000:
                u = x2[-1] - 486000
                x2[-1] = u + 486000
            if x2[-1] >= 486000:
                anim.event_source.stop()

            return ax5


        anim = FuncAnimation(fig5, animate2, frames=(time_inputed+1),interval=100,repeat=False)


fig5 = plt.figure(figsize=(4.75,2.8))
ax5 = fig5.add_subplot(111)
ax5.set_facecolor('xkcd:black')
ax5.set_xlim(0,500000)
ax5.set_ylim(0,2)
ax5.get_xaxis().set_visible(False)
ax5.get_yaxis().set_visible(False)
ax5.set_title("Mission Control")
canvas5 = FigureCanvasTkAgg(fig5)
canvas5.get_tk_widget().place(x=255,y=360)


frame_btn= Frame(root,width=500,height=70)
frame_btn.place(x=10, y=120)
button_input = Button(frame_btn, text="Simulate Data ", command=simulate, background="#ff001d", fg="black", font=("Arial", 14))
button_input.pack()
button_input2 = Button(root, text="Simulate Moon",command=simulate2, background="orange", fg="black", font=("Arial", 14))
button_input2.place(x=10, y=160)

root.mainloop()

