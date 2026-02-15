import subrocess
def install():
    while True:
        print("Installing Browser...")
        print("Choose a browser:")
        print("""
        1.Mozilla Firefox
        2.Chromium
        3.Brave
        4.Opera
        5.Google Chrome
        6.MicroSoft Edge
        7.Cancel and return
        """)
        opt = input("Choose an option(1/2/3...): ")
        if opt == "1":
            print("Installing Firefox...")
            subprocess.run(["sudo", "pacman", "-S", "firefox", "--noconfirm"])
            continue
        if opt == "2":
            print("Installing Chromium...")
            subprocess.run(["sudo", "pacman", "-S", "chromium", "--noconfirm"])
            continue
        if opt == "3":
            print("Installing Brave...")
            subprocess.run(["sudo", "pacman", "-S", "brave-browser", "--noconfirm"])
            continue
        if opt == "4":
            print("Installing Opera...")
            subprocess.run(["sudo", "pacman", "-S", "opera", "--noconfirm"])
            continue
        if opt == "5":
            print("Installing Chrome...")
            subrpocess.run(["sudo", "pacman", "-S", "google-chrome", "--noconfirm"])
            continue
        if opt == "6":
            print("Installing Edge...")
            subprocess.run(["sudo", "pacman", "-S", "microsofr-edge", "--noconfirm"])
            continue
        if opt == "7":
            print("Cancelling...")
            break
        else:
            print("Not valid")
            continue
