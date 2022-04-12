# `README.md` for [fenghuang](https://github.com/Ai-Yukino/fenghuang)

![fenghuang.jpg](images/fenghuang.jpg)

[🍅 Image source](https://commons.wikimedia.org/wiki/File:Fenghuang-drawing-1664.jpg)

Personal notes and commentary for [Tech Talent South's](https://www.techtalentsouth.com/) Spring 2022 Advanced Data Science course taught by

- Stephanie Farid (main instructor), and
- Erin McConnell (teaching fellow)

---

## How to view Jupyter notebooks (for python)

Jupyter notebooks are bad for version control (e.g. see [here](https://goodresearch.dev/tidy.html#keep-jupyter-notebooks-tidy)), so I push `.py` files that can be used to recover the origin `.ipynb` via [jupytext](https://jupytext.readthedocs.io/en/latest/).

Here are some instructions for how to view the Jupyter notebooks in this repo (via the [Jupyter Lab editor](https://docs.jupyter.org/en/latest/install.html#jupyterlab)).

### Set up virtual environment

In the terminal, run

```
mamba env create -f environment.yml
```

where `environment.yml` is the relevant environment config file in whatever subdirectory of this repo you're viewing. See [here](https://mamba.readthedocs.io/en/latest/index.html) for more details about mamba.

Next, run

```
mamba activate environment
```

where `environment` is the environment's name. By convention, a environment config file `uwu.yml` will create an environment named `uwu`.

### Generate `.ipynb` file

Run

```
jupytext --to ipynb subdirectory.py
```

where the subdirectory you are browsing has a `subdirectory.py` file. This will generate a Jupyter notebook, i.e. a `subdirectory.ipynb` file.

### View `.ipynb` file

Run

```
jupyter-lab subdirectory.ipynb
```

and open the given link in your prefered browser.
