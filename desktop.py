import subprocess
def de_install():
    while True:
        print("""Choose a Desktop Environment
        1. KDE Plasma
        2. Gnome
        3. XFCE
        4. LXDE
        5. i3
        6.Cancel""")
        opt = input("Choose a Desktop Environment(1/2/3...): ")
        if opt == "1":
            print("Installing KDE Plasma...")
            subprocess.run(["sudo", "pacman", "-S", "plasma-meta kde-applications-meta", "--noconfirm"])
            continue
        if opt == "2":
            print("Installing Gnome...")
            subprocess.run(["sudo", "pacman", "-S", "gnome gnome-circle", "--noconfirm"])
            continue
        if opt == "3":
            print("Installing XFCE...")
            subprocess.run(["sudo", "pacman", "-S", "xfce4", "--noconfirm"])
            continue
        if opt == "4":
            print("Installing LXDE...")
            subprocess.run(["sudo", "pacman", "-S", "lxde-common lxsession", "--noconfirm"])
            continue
        if opt == "5":
            print("Installing i3...")
            subprocess.eun(["sudo", "pacman", "-S", "i3-wm", "--noconfirm"])
            continue
        if opt == "6":
            print("Cancelling...")
            break
        else:
            print("Not a valid option")
            break
#removed the contribution coz it is already in ADDONS
