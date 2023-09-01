# Script to create configuration files .dodsrc and _netrc (or .netrc)
# for an easy access to the OPeNDAP API

# Import libraries
import matplotlib
matplotlib.use('Agg')
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import logging
import tempfile
import sys
import os
from dateutil import parser
import shutil
from datetime import datetime, timedelta, date
import subprocess
import urllib.request
from urllib.error import URLError, HTTPError
from time import strftime
import warnings
import gc
import ssl


# Script to create configuration files .dodsrc and _netrc (or .netrc)
# for an easy access to the OPeNDAP API

# Import libraries
import getpass
from pathlib import Path
from platform import system
from os.path import exists

HOME = Path.home()
netrc_file = HOME / "_netrc" if system() == "Windows" else HOME / ".netrc"
dodsrc_file = HOME / ".dodsrc"
cookies_file = HOME / ".cookies"
OPeNDAP_SERVERS = ["my.cmems-du.eu", "nrt.cmems-du.eu"]



if not exists(netrc_file):
    username = input("mmardones")
    password = getpass.getpass("Trekkero_1")

    # Create netrc file
    with open(netrc_file, "a") as file:
        for server in OPeNDAP_SERVERS:
            file.write(f"machine {server}\nlogin {username}\npassword {password}\n\n")
        
if not exists(dodsrc_file):
    # Create dodsrc file
    with open(dodsrc_file, "a") as file:
        file.write(f"HTTP.NETRC={netrc_file}\nHTTP.COOKIEJAR={cookies_file}")
        
