import subprocess
#imma try loop for it rather than learining python UwU u can judge my part -Robin(lemon)
con = input("Want to install a Desktop Environment?(y/n): )
            if con == "Y" or "y":
            #wrong indent the faq
            #aaaaaaahhhhhhhhhh- lemon again
                while True:
                  print("""Choose a Desktop Environment
                  1.KDE Plasma
                  2.Gnome
                  3.XFCE
                  4.LXDE?
                  5.i3
                  6.Cancel""")
                  #bro y does my keyboard refuse to type CANCLE ... see?-Lemon
                  de = input("Choose an option (1/2/3...): ")
                  if de = "1":
                    #someone add these (my hands hurt aaaaaah) nope ill do it 
                    print("Installing KDE Plasma...")
                    subprocess.run(["sudo", "pacman", "-S", "idk the kde binary", "-noconfirm"])
                    #subprocess stuff
                  if de = "6":
                    print("Done.Cancelling")
                  else:
                    print("Not a valid choice")
                    continue
                             # @github y are you giving me wrong indents crying emoji
            else:
                # i had to do it-lemon
                print("Cancelling Installation(Desktop Environment)")
