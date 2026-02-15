import subprocess
def de_install():
    while True:
        print("""Choose a Desktop Environment
        1.KDE Plasma
        2.Gnome
        3.XFCE
        4.LXDE
        5.i3
        6.Cancel""")
        opt = input("Choose a Desktop Environment(1/2/3...): ")
        if opt == "1":
            print("Installing KDE Plasma...")
            subprocess.run(["sudo", "pacman", "-S", "kdeplasma binary (idk)", "--noconfirm"])
            continue
        if opt == "2":
            print("Installing Gnome...")
            subprocess.run(["sudo", "pacman", "-S", "gnome binary idk", "--noconfirm"])
            continue
        if opt == "3":
            print("Installing XFCE...")
            subprocess.run(["sudo", "pacman", "-S", "xfce4", "--noconfirm"])
            continue
        if opt == "4":
            print("Installing LXDE...")
            subprocess.run(["sudo", "pacman", "-S", "lxde binary?", "--noconfirm"])
            continue
        if opt == "5":
            print("Installing i3...")
            subprocess.eun(["sudo", "pacman", "-S", "i3 binary", "--noconfirm"])
            continue
        if opt == "6":
            print("Cancelling...")
            break
        else:jhjkhkt
            print("Not a valid option")
            break
print("Our project is contributed by membercatcousin,robin-persona,Cloud67TR and... on \033[94m\033[1mhttps://github.com/membercatcousin/membercatcousin-ricing-script\033[0m")
