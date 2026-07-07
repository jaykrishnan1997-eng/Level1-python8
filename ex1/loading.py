#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/07 15:22:12 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/07 16:08:50 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib.util


def check_package(name):
    spec = importlib.util.find_spec(name)
    return spec is not None


def check_dependencies():
    if check_package("pandas"):
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) -  Data manipulation ready")

    if check_package("numpy"):
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")

    if check_package("requests"):
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")

    if check_package("matplotlib"):
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    check_dependencies()
