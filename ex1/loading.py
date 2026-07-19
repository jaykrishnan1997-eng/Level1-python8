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
import sys


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
                versions[name] = getattr(module,"__version__", "unknown")
                status[name] = "OK"
            except Exception as e:
                status[name] = "KO"
                versions[name] = None
                print(f"[KO] {name} found but failed to import: {e}")
        else:
            status[name] = "KO"

    for name in packages.keys():
        if status[name] == "OK":
            print(f"[OK] {name} ({versions[name]}) - {packages[name]} ready")
        else:
            print(f"[KO] {name} is not installed")
            print(f"To install, use : 'pip install {name}'")
    if "KO" in status.values():
        return False
    return True


def generating_vis(lat=48.7758, lon=9.1829, location_name="Stuttgart"):
    import requests
    import matplotlib.pyplot as plt

    URL = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    data = response.json()["daily"]
    dates = data["time"]
    max_temp = data["temperature_2m_max"]
    min_temp = data["temperature_2m_min"]
    avg_temp = [(max + min) / 2 for max, min in zip(max_temp, min_temp)]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(dates, avg_temp, marker="o", color="tab:orange")
    ax.set_ylabel("Average Temperature (°C)")
    ax.set_xlabel("Date")
    ax.set_title(f"Average daily temperature - {location_name}")
    ax.grid(True, alpha=0.3)

    plt.xticks(rotation=45)
    plt.tight_layout()

    out_path = "weather_forecast.png"
    plt.savefig(out_path, dpi=150)
    print(f"[OK] saved plot to {out_path}")
    return out_path       

def main():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if check_dependencies() is False:
        print("\nMissing dependencies, aborting.")
        sys.exit(1)

    print("\nGenerating weather visualization:")
    generating_vis()


if __name__ == "__main__":
    main()
