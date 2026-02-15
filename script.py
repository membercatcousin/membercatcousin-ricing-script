from desktop import de_install
from browser import install
bro = input("Do you want to install a browser(y/n): ")
if bro == "y" or "Y":
    install()
else:
    print("Skipping...")

de = input("Do you want to install a Desktop environment(y/n)?: ")
if de == "y" or "Y":
    de_install
else:
    print("Skipping")
