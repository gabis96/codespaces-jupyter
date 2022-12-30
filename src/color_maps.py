import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.colors import ListedColormap

class PlotColorMap:
    def __init__(self, colormap):
        self.colormap = colormap

    def plotColormap(self):
        np.random.seed(19680801)
        data = np.random.randn(30, 30)
        
        fig, ax = plt.subplots(1, figsize=(3, 3), constrained_layout=True)
        
        psm = ax.pcolormesh(data, cmap=self.colormap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
        
        plt.show()


class Colormaping:
    def __init__(self):
        self.colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    def get_colormap(self):
        colormap = cm.get_cmap()
        newcolors = colormap(np.linspace(0, 1, 256))         

        sets = len(self.colors)
        values = self.aux_divisions(sets)

        k = sets
        for i, color in enumerate(self.colors):
            r, g, b = color
            newcolors[:values[i], :] = np.array([r/256, g/256, b/256, 1])
            k -= 1

        newcmap = ListedColormap(newcolors)
        return newcmap    

    def aux_divisions(self, sets):
        start_val = int(255/sets)

        values = [0] * sets
        for i in range(sets):
            values[i] = (start_val * (i+1)) + 1
        
        values.reverse()
        return values

class PinkColormap(Colormaping):
    def __init__(self):
        self.colors = [(120, 47, 64), (168, 85, 102), (207, 111, 119), (221, 135, 141), (255, 166, 173)]

class BlueColormap(Colormaping):
    def __init__(self):
        self.colors = [(3, 31, 75), (4, 57, 108), (3, 91, 150), (100, 151, 177), (179, 205, 224)]

class BlueColormap2(Colormaping):
    def __init__(self):
        self.colors = [(35, 71, 123), (20, 52, 121), (87, 114, 155), (153, 186, 221), (175, 202, 221)]

class BlueColormap3(Colormaping):
    def __init__(self):
        self.colors = [(8, 48, 107), (26, 98, 154), (92, 158, 193), (153, 186, 221), (239, 248, 255)]

class BlueColormap4(Colormaping):
    def __init__(self):
        self.colors = [(8, 48, 107), (153, 186, 221), (239, 248, 255), (153, 186, 221), (239, 248, 255)]

class PurpleColormap(Colormaping):
    def __init__(self):
        self.colors = [(89, 41, 65), (130, 38, 65), (142, 68, 124), (86, 71, 135), (249, 184, 223)]

class GreenColormap(Colormaping):
    def __init__(self):
        self.colors = [(76, 108, 10), (88, 129, 7), (111, 143, 45), (221, 224, 152), (231, 239, 201)]

class RedColormap(Colormaping):
    def __init__(self):
        self.colors = [(101, 13, 27), (212, 33, 30), (163, 22, 33), (247, 80, 66), (254, 209, 216)]

class OrangeColormap(Colormaping):
    def __init__(self):
        self.colors = [(238, 80, 1), (254, 103, 38), (252, 147, 66), (240, 101, 67), (242, 192, 120)]


def createColormap(color):

    if color == 'pink':
        colormap = PinkColormap().get_colormap()
    elif color == 'purple':
        colormap = PurpleColormap().get_colormap()
    elif color == 'green':
        colormap = GreenColormap().get_colormap()
    elif color == 'red':
        colormap = RedColormap().get_colormap()
    elif color == 'orange':
        colormap = OrangeColormap().get_colormap()
    elif color == 'blue1':
        colormap = BlueColormap().get_colormap()    
    elif color == 'blue2':
        colormap = BlueColormap2().get_colormap()  
    elif color == 'blue4':
        colormap = BlueColormap4().get_colormap()    
    else:
        colormap = BlueColormap3().get_colormap()

    return colormap
