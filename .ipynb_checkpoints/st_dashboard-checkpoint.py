{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "57e8a5fa-0fc2-424d-b269-cc1dd1211d39",
   "metadata": {},
   "source": [
    "# Creating a “.py” file for my Streamlit application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b218b38-525f-419c-b121-2493d42323fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing libraries\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.express as px\n",
    "from plotly.subplots import make_subplots\n",
    "import plotly.graph_objects as go\n",
    "import matplotlib.pyplot as plt\n",
    "from datetime import datetime as dt\n",
    "from streamlit_keplergl import keplergl_static"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc40349f-197c-4cc1-aa12-633fabf54213",
   "metadata": {},
   "source": [
    "# configuring my page"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f9f12ee-d76c-4ae4-a584-c4eb6d7226fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(page_title=\"NewYork Bikes Strategy Dashboard\", layout=\"wide\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea8fd743-f30d-4f56-a254-1e8faf611d9e",
   "metadata": {},
   "source": [
    "# Title and intro"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8df24b92-e5a1-4fec-99f3-5550749c475a",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"NewYork Bikes Strategy Dashboard\")\n",
    "st.markdown(\"The dashboard will help with the expansion problems NewYork city currently faces\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:venv_citibikes]",
   "language": "python",
   "name": "conda-env-venv_citibikes-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
