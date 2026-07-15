#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/06 11:12:18 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/15 13:29:24 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        # py_v = f"python{sys.version_info.major}.{sys.version_info.minor}"
        # package_path = os.path.join(sys.prefix, "lib", py_v, "site-packages")
        print("Package installation path:")
        # print(f"{package_path}")
        print(site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")
