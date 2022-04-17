
import holoviews as hv
hv.extension('bokeh')


import numpy as np
import scipy.signal
from IPython.display import YouTubeVideo,Audio


time = np.linspace(-6, 6, num=1000)

hmap = hv.HoloMap(kdims=['Frecuencia'])
for freq in np.arange(0, 1, step=0.02):
    hmap[freq] = hv.Curve((time, np.sin(2*np.pi*freq*time)))

hmap.opts(hv.opts.Curve(width=500, height=300))
hv.output(hmap, holomap='gif', fps=5)

