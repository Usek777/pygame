import tkinter as tk
from PIL import ImageTk, Image
import random
import time
# Создал окно
win = tk.Tk()
# Вывожу окно на центр монитора
w = 600
h = 600
win.geometry(f'{w}x{h}+{(win.winfo_screenwidth()-w)//2}+{(win.winfo_screenheight()-h)//2}')
win.resizable(False, False)
# Ставлю картинку на фон окна
pic = 'StonePicFixed.jpg'
image = Image.open(pic)
width = 700
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

canvas = tk.Canvas(win, width=width, height=height)
canvas.pack(side="top", fill="both", expand="no")

canvas.create_image(0, 0, anchor="nw", image=image)

# Задаю название окна
win.title('100-7')
# Создаю функцию которая вычитает из начального счета 7 очков, функция будет привязана к кнопке
score = 100
def randomm():
    global score
    score = score - 7
    btn['text'] = f'{score}'
    btn['fg'] = 'red'
# Создаю кнопку, привязываю к ней функцию, задаю размер, текст в ней это количество очков(score)
btn = tk.Button(text=f'{score}', command=randomm, padx=18, pady=15)
# Случайная генерация координат кнопки с помощью цикла и метода рандом
while score > 0:
    # Пока счет будет больше нуля функция будет выполнятся
    btn.place(relx=round(random.uniform(0.1, 0.85), 2), rely=round(random.uniform(0.1, 0.85), 2))
    btn.update()
    time.sleep(1.3)
    # Когда счет будет меньше нуля, кнопка ломается и на экран выводится лейбл 'you win'
    if score < 0:
        btn.destroy()
        text = tk.Label(text='You win', font=('Robotic', 35), bg='#8B3011', fg='red')
        text.place(relx=0.27, rely=0.358)
        # Это цикл который делает финальный текст мигающим
        while score < 100:
            text.update()
            text['fg'] = 'red'
            time.sleep(0.5)
            text.update()
            text['fg'] = 'blue'
            time.sleep(0.5)

win.mainloop()