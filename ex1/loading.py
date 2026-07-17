#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/07 15:22:12 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/17 14:32:05 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib.util


def check_package(name):
    spec = importlib.util.find_spec(name)
    return spec is not None


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
        "requests": "Network access"
    }
    status = {}
    versions = {}

    for name in packages.keys():
        if check_package(name):
            try:
                module = importlib.import_module(name)
                versions[name] = module.__version__
                status[name] = "OK"
            except Exception:
                status[name] = "KO"
                versions[name] = None
                print(f"[KO] {name} found but failed to import: {e}")
        else:
            status[name] = "KO"

    for name in packages.keys():
        if status[name] == "OK":
            print(f"[OK] {name} ({versions[name]}) - {packages[name]} ready")
        elif check_package(name):
            continue
        else:
            print(f"[KO] {name} is not installed")
            print(f"To install, use : 'pip install {name}'")
    if "KO" in status:
        return False
    return True


def generating_vis():
    import requests

    URL = "https://opendata.cern.ch/api/records/?size=100"

    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    records = response.json()["hits"]["hits"]
    titles = []
    experiments = []
    
    for record in records:
        


def main():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if check_dependencies() is False:
        exit


if __name__ == "__main__":
    main()
