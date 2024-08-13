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
if Language == '3':
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
