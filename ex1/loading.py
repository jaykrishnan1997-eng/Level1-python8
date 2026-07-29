#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/07 15:22:12 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/29 12:35:23 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib.util
import sys


def check_package(name: str) -> bool:
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
                versions[name] = getattr(module, "__version__", "unknown")
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


def generating_vis(
    lat: float = 48.7758,
    lon: float = 9.1829,
    location_name: str = "Stuttgart"
) -> str:
    import requests
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    URL = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(
            "There was an error either in fetching the url"
            f" or in the input you provided for generating_vis: {e}"
        )
        return ""

    data = response.json()["daily"]
    df = pd.DataFrame({
        "date": data["time"],
        "temp_max": data["temperature_2m_max"],
        "temp_min": data["temperature_2m_min"],
    })
    max_temp = np.array(df["temp_max"])
    min_temp = np.array(df["temp_min"])
    df["avg_temp"] = np.mean(np.vstack([max_temp, min_temp]), axis=0)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(df["date"], df["avg_temp"], marker="o", color="tab:orange")
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


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if check_dependencies() is False:
        print("\nMissing dependencies, aborting.")
        sys.exit(1)

    print("\nGenerating weather visualization:")
    result = generating_vis()
    if not result:
        print("Visualization failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
# python3 -m pip install types-requests
# pip uninstall requests pandas numpy matplotlib -y
