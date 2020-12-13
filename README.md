# Python for Earth Sciences

### by [Rebekah Esmaili](http://www.rebekahesmaili.com), [Kriti Bhargava](https://cisess.umd.edu/meet-our-scientists/kriti-bhargava/), and [Eviatar Bach](http://eviatarbach.com/)
---

A crash course in Python focusing on reading and visualizing data-sets used in Earth sciences.

Access materials via GitHub: [https://ter.ps/noaapy](https://ter.ps/noaapy)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/modern-tools-workshop/AGU-python-workshop-2020/HEAD)

---

## Getting Started

This workshop will cover:

* Launching Jupyter Notebooks
* Working with arrays using the Numpy package
* Importing text datasets using the Pandas package
* Creating simple graphics with Matplotlib
* Importing scientific data formats, such as netCDF and GRIB2
* Creating maps from datasets

---

Installation requirements

"I am really new to Python!"

* I recommend launching binder, which is a "cloud version" of this course. No installation required!
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/modern-tools-workshop/AGU-python-workshop-2020/HEAD)

* Need help with Binder? Video tutorial on [YouTube](https://youtu.be/3BrfFe4HsAw).

"I have used Python before!"

* If you wish to run the examples locally, I recommend installing [Anaconda](https://www.anaconda.com/products/individual). If you are having trouble with your installation, contact the instructor before the course or use binder.
* Need help installing Anaconda? Video tutorial on [YouTube](https://youtu.be/3BrfFe4HsAw).
* Download the contents of the [GitHub repository](https://ter.ps/noaapy) to your computer.
* Launch Jupyter Notebooks from the Anaconda Navigator. This will open a window in your default browser. Navigate to the folder that contains the notebooks (*.ipynb) and click on the tutorial for the day.
* New to Jupyter? Here's a video tutorial on [YouTube](https://youtu.be/gmMCuR9JPpY).
* Additional packages:
  * Launch the Anaconda Prompt (Windows) or Terminal (MacOS/Linux). Then copy/paste and hit enter:
    ```
    conda install -c conda-forge cartopy
    conda install -c conda-forge netCDF4
    conda install -c conda-forge pygrib
    ```
  * If there are no errors, then you are set-up!
  * Alternatively, if you are familiar with environments, you can use the environments.yml to install the necessary packages.

I *do not* recommend:
* Using Python on a remote server for this tutorial (I cannot help troubleshoot)
* Using your operating system's Python or a shared Python installations unless you are advanced!

---

## Resources

### Packages and Tutorials

<b> Pandas </b>
* Short Introduction: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
* Cookbook for more details: https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook

---
<b> Matplotlib </b>
* Pyplot Tutorial: https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html

---
<b> Reading self describing file </b>
* <b> NETCDF </b>
    * Detailed tutorial https://unidata.github.io/netcdf4-python/netCDF4/index.html.
* <b> HDF files </b>
    * The package [h5py](https://www.h5py.org/) is similar to netcdf4.
    * User manual at http://docs.h5py.org/en/stable/.
* <b> GRIB/GRIB2 files </b>
    * World Meteorology Association standard format, e.g. commonly used with weather-related models like ECMWF and GFS.
    * Can be opened using [pygrib](https://github.com/jswhit/pygrib).
    * Example usage at https://jswhit.github.io/pygrib/docs/.
* <b> BUFR </b>
    * Another common table-driven format.
    * Open with [python-bufr](https://github.com/pytroll/python-bufr), part of the pytroll project.
---    

### General Python resources   

<b> Free online Tutorials</b>
   * YouTube series for absolute beginners [CS Dojo](https://www.youtube.com/watch?v=Z1Yd7upQsXY&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg)
   * [Python for Earth Science with Rebekah] (https://www.youtube.com/channel/UCGa4rhczYNTGBYIMxmR8nHg) ... we are slowly adding content ...
   * Enhance your workflow [Automate Boring Stuff](https://automatetheboringstuff.com/)
