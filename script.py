from desktop import de_install
from addons import apps_install
from browser import install
bro = input("Do you want to install a browser(y/n)?: ")
if bro == "y" or "Y":
    install()
else:
    print("Skipping...")

de = input("Do you want to install a Desktop environment(y/n)?: ")
if de == "y" or "Y":
    de_install
else:
    print("Skipping")
app = input("Want to install additional packages?(y/n): ")
if app == "y" or "Y":
    apps_install()
else:
    print("Skipping")
