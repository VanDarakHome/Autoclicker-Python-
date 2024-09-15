import keyboard
import time
import mouse

print('Hello! The autoclicker program is almost running enter the language to start it.')
time.sleep(1.5)
print('-------------------------------------------------------------')
print('---1)Deutch---2)English---3)Russian---4)French---5)Chinese---')
print('-------------------------------------------------------------')
Language = input()

while Language != '1' and Language != '2' and Language != '3' and Language != '4' and Language != '5':
    print('Please enter the number 1-5')
    Language = input()

print('Changing language...')
print('1%...')
time.sleep(0.2)
print("3%...")
time.sleep(0.2)
print("6%...")
time.sleep(0.2)
print("10%...")
time.sleep(0.2)
print("15%...")
time.sleep(0.2)
print("21%...")
time.sleep(0.2)
print("28%...")
time.sleep(0.2)
print("36%...")
time.sleep(0.2)
print("45%...")
time.sleep(0.2)
print("55%...")
time.sleep(0.2)
print("66%...")
time.sleep(0.2)
print("78%...")
time.sleep(0.2)
print("91%...")
time.sleep(0.2)
print("95%...")
time.sleep(0.2)
print("98%...")
time.sleep(0.2)
print("99%...")
time.sleep(0.2)
print("100%...")
time.sleep(0.05)
print('Success!')
time.sleep(2)

if Language == '1':  # Deutch
    def main():
        print("Wählen Sie den Typ des Autoklickers:")
        print("1. Maus")
        print("2. Tastatur")
        choice = input("Geben Sie 1 oder 2 ein: ")

        if choice == '1':
            target = 'mouse'
            print("Wählen Sie die Maustaste:")
            print("1. Linke Taste")
            print("2. Rechte Taste")
            mouse_choice = input("Geben Sie 1 oder 2 ein: ")
            if mouse_choice == '1':
                mouse_button = 'left'
            elif mouse_choice == '2':
                mouse_button = 'right'
            else:
                print("Falsche Eingabe. Bitte starten Sie das Programm neu und geben Sie 1 oder 2 ein.")
                return
        elif choice == '2':
            target = 'keyboard'
        else:
            print("Falsche Eingabe. Bitte starten Sie das Programm neu und geben Sie 1 oder 2 ein.")
            return

        trigger_key = input("Geben Sie die Taste ein, um den Autoklicker zu aktivieren: ")
        click_interval = float(input("Geben Sie die Klickfrequenz in Sekunden ein: "))

        if target == 'keyboard':
            click_key = input("Geben Sie die Taste auf der Tastatur ein: ")
        else:
            click_key = None

        print(f"Drücken Sie {trigger_key}, um den Autoklicker zu aktivieren.")

        active = False

        def toggle_autoclicker(e):
            nonlocal active
            if e.name == trigger_key:
                active = not active
                if active:
                    print("Autoklicker aktiviert.")
                else:
                    print("Autoklicker deaktiviert.")

        keyboard.on_press(toggle_autoclicker)

        try:
            while True:
                if active:
                    if target == 'mouse':
                        mouse.click(mouse_button)
                    elif target == 'keyboard':
                        keyboard.send(click_key)
                    time.sleep(click_interval)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Autoklicker gestoppt.")

    if __name__ == "__main__":
        main()

elif Language == '2':  # English
    def main():
        print("Choose the type of autoclicker:")
        print("1. Mouse")
        print("2. Keyboard")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            target = 'mouse'
            print("Choose the mouse button:")
            print("1. Left button")
            print("2. Right button")
            mouse_choice = input("Enter 1 or 2: ")
            if mouse_choice == '1':
                mouse_button = 'left'
            elif mouse_choice == '2':
                mouse_button = 'right'
            else:
                print("Incorrect input. Please restart the program and enter 1 or 2 next time.")
                return
        elif choice == '2':
            target = 'keyboard'
        else:
            print("Incorrect input. Please restart the program and enter 1 or 2 next time.")
            return

        trigger_key = input("Input the button to activate the autoclicker: ")
        click_interval = float(input("Input click repeater in seconds: "))

        if target == 'keyboard':
            click_key = input("Input the key on the keyboard: ")
        else:
            click_key = None

        print(f"Press {trigger_key} to activate the autoclicker.")

        active = False

        def toggle_autoclicker(e):
            nonlocal active
            if e.name == trigger_key:
                active = not active
                if active:
                    print("Autoclicker activated.")
                else:
                    print("Autoclicker deactivated.")

        keyboard.on_press(toggle_autoclicker)

        try:
            while True:
                if active:
                    if target == 'mouse':
                        mouse.click(mouse_button)
                    elif target == 'keyboard':
                        keyboard.send(click_key)
                    time.sleep(click_interval)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Autoclicker has been stopped.")

    if __name__ == "__main__":
        main()

elif Language == '3':  # Russian
    def main():
        print("Выберите тип автокликера:")
        print("1. Мышка")
        print("2. Клавиатура")
        choice = input("Введите 1 или 2: ")

        if choice == '1':
            target = 'mouse'
            print("Выберите кнопку мыши:")
            print("1. Левая кнопка")
            print("2. Правая кнопка")
            mouse_choice = input("Введите 1 или 2: ")
            if mouse_choice == '1':
                mouse_button = 'left'
            elif mouse_choice == '2':
                mouse_button = 'right'
            else:
                print("Неверный выбор. Пожалуйста перезапустите программу и введите 1 или 2.")
                return
        elif choice == '2':
            target = 'keyboard'
        else:
            print("Неверный выбор. Пожалуйста перезапустите программу и введите 1 или 2.")
            return

        trigger_key = input("Введите кнопку для активации автокликера: ")
        click_interval = float(input("Введите частоту кликов в секундах: "))

        if target == 'keyboard':
            click_key = input("Введите клавишу для автокликера на клавиатуре: ")
        else:
            click_key = None

        print(f"Нажмите {trigger_key} для активации автокликера.")

        active = False

        def toggle_autoclicker(e):
            nonlocal active
            if e.name == trigger_key:
                active = not active
                if active:
                    print("Автокликер активирован.")
                else:
                    print("Автокликер деактивирован.")

        keyboard.on_press(toggle_autoclicker)

        try:
            while True:
                if active:
                    if target == 'mouse':
                        mouse.click(mouse_button)
                    elif target == 'keyboard':
                        keyboard.send(click_key)
                    time.sleep(click_interval)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Автокликер остановлен.")

    if __name__ == "__main__":
        main()

elif Language == '4':  # French
    def main():
        print("Choisissez le type de clic automatique:")
        print("1. Souris")
        print("2. Clavier")
        choice = input("Entrez 1 ou 2: ")

        if choice == '1':
            target = 'mouse'
            print("Choisissez le bouton de la souris:")
            print("1. Bouton gauche")
            print("2. Bouton droit")
            mouse_choice = input("Entrez 1 ou 2: ")
            if mouse_choice == '1':
                mouse_button = 'left'
            elif mouse_choice == '2':
                mouse_button = 'right'
            else:
                print("Entrée incorrecte. Veuillez redémarrer le programme et entrer 1 ou 2.")
                return
        elif choice == '2':
            target = 'keyboard'
        else:
            print("Entrée incorrecte. Veuillez redémarrer le programme et entrer 1 ou 2.")
            return

        trigger_key = input("Entrez la touche pour activer le clic automatique: ")
        click_interval = float(input("Entrez la fréquence de clic en secondes: "))

        if target == 'keyboard':
            click_key = input("Entrez la touche du clavier: ")
        else:
            click_key = None

        print(f"Appuyez sur {trigger_key} pour activer le clic automatique.")

        active = False

        def toggle_autoclicker(e):
            nonlocal active
            if e.name == trigger_key:
                active = not active
                if active:
                    print("Clic automatique activé.")
                else:
                    print("Clic automatique désactivé.")

        keyboard.on_press(toggle_autoclicker)

        try:
            while True:
                if active:
                    if target == 'mouse':
                        mouse.click(mouse_button)
                    elif target == 'keyboard':
                        keyboard.send(click_key)
                    time.sleep(click_interval)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Clic automatique arrêté.")

    if __name__ == "__main__":
        main()

elif Language == '5':  # Chinese
    def main():
        print("选择自动点击器类型:")
        print("1. 鼠标")
        print("2. 键盘")
        choice = input("输入 1 或 2: ")

        if choice == '1':
            target = 'mouse'
            print("选择鼠标按钮:")
            print("1. 左键")
            print("2. 右键")
            mouse_choice = input("输入 1 或 2: ")
            if mouse_choice == '1':
                mouse_button = 'left'
            elif mouse_choice == '2':
                mouse_button = 'right'
            else:
                print("输入错误。请重新启动程序并输入 1 或 2。")
                return
        elif choice == '2':
            target = 'keyboard'
        else:
            print("输入错误。请重新启动程序并输入 1 或 2。")
            return

        trigger_key = input("输入激活自动点击器的按钮: ")
        click_interval = float(input("输入点击频率（秒）: "))

        if target == 'keyboard':
            click_key = input("输入键盘上的按键: ")
        else:
            click_key = None

        print(f"按下 {trigger_key} 激活自动点击器。")

        active = False

        def toggle_autoclicker(e):
            nonlocal active
            if e.name == trigger_key:
                active = not active
                if active:
                    print("自动点击器已激活。")
                else:
                    print("自动点击器已停用。")

        keyboard.on_press(toggle_autoclicker)

        try:
            while True:
                if active:
                    if target == 'mouse':
                        mouse.click(mouse_button)
                    elif target == 'keyboard':
                        keyboard.send(click_key)
                    time.sleep(click_interval)
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("自动点击器已停止。")

    if __name__ == "__main__":
        main()
