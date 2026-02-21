from desktop import de_install
from browser import install
bro = input("Do you want to install a browser (Y/N): ")
if bro == "y" or "Y":
    install()
else:
    print("Skipping...")

de = input("Do you want to install a Desktop environment (Y/N)?: ")
if de == "y" or "Y":
    de_install
else:
    print("Skipping")
