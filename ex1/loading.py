#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/07 15:22:12 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/15 14:09:44 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib.util


def check_package(name):
    spec = importlib.util.find_spec(name)
    return spec is not None


def check_dependencies():
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "requests": "Network access",
        "matplotlib": "Visualization",
    }
    status = {}
    for name in packages.keys():
        if check_package(name):
            module = importlib.import_module(name)
            version = module.__version__
            status[name] = "OK"
        else:
            status[name] = "KO"

    for name in packages.keys():
        if status[name] == "OK":
            print(f"[OK] {name} {version} {packages[name]} ready")
        else:
            print(f"[KO] {name} is not installed")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    check_dependencies()
