import constantshandler
import matplotlib.pyplot as plt

#Handles plotting of curves
def Curve_Graph(List, Save_Directory, Graph_Name):
    plt.clf()
    plt.plot(List)
    plt.ylabel(Graph_Name)
    plt.savefig(Save_Directory)
    plt.close()
