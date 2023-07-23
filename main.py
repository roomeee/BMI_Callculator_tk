import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int

# Color constants
WM = "#de8e7a"
RED = "#d6382d"
WHITE = "#ebdbda"
BLACK = "#020303"

GREY = "#a39e9e"
DARK_GREY = "#809696"

FONT = 'Calibri'
MAIN_SIZE = 140
INPUT_SIZE = 26
SWITCH = 18


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=WM)
        self.title('')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # data
        self.height = ctk.IntVar(value=170)
        self.weight = ctk.DoubleVar(value=60)
        self.bmi = ctk.StringVar()
        self.update_bmi()
        ResultText(self,self.bmi)
        WeightInput(self)
        HeightInput(self)
        Switch(self)
        self.mainloop()

    def update_bmi(self):
        height_meter = self.height.get() / 100
        weight_kg = self.weight.get()
        bmi_res= weight_kg/height_meter**2
        self.bmi.set(bmi_res)

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35  # DWMWA_COLORIZATIONCOLOR
            COLOR = int(WM[1:], 16)  # Convert the color code from hex to int
            # Update the window attribute to set the title bar color
            windll.dwmapi.DwmSetWindowAttribute(
                HWND,
                DWMWA_ATTRIBUTE,
                byref(c_int(COLOR)),
                sizeof(c_int)
            )
        except Exception as e:
            print(f"Error: {e}")


class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi):
        font_x = ctk.CTkFont(family=FONT, size=MAIN_SIZE, weight='bold')
        super().__init__(master=parent, text=22.5, font=font_x, text_color=WHITE, textvariable=bmi)
        self.grid(column=0, row=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')
        # let's create widgets
        font = ctk.CTkFont(family=FONT, size=INPUT_SIZE)
        label = ctk.CTkLabel(self, text='70kg', text_color=BLACK, font=font)
        label.grid(row=0, column=2)

        minus_btn = ctk.CTkButton(self, text='-', font=font, text_color=BLACK, fg_color=GREY, hover_color=DARK_GREY,
                                  corner_radius=6)
        minus_btn.grid(row=0, column=0, sticky='ns', padx=8, pady=8)
        s_minus_btn = ctk.CTkButton(self, text='-', font=font, text_color=BLACK, fg_color=GREY, hover_color=DARK_GREY,
                                    corner_radius=6)
        s_minus_btn.grid(row=0, column=1, padx=4, pady=4)

        plus_btn = ctk.CTkButton(self, text='+', font=font, text_color=BLACK, fg_color=GREY, hover_color=DARK_GREY,
                                 corner_radius=6)
        plus_btn.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

        s_plus_btn = ctk.CTkButton(self, text='+', font=font, text_color=BLACK, fg_color=GREY, hover_color=DARK_GREY,
                                   corner_radius=6)
        s_plus_btn.grid(row=0, column=3, padx=4, pady=4)


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

        #         widgets
        slider = ctk.CTkSlider(
            self,
            button_color=RED,
            button_hover_color=GREY,
            progress_color=RED,
            fg_color=GREY
        )
        slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

        output_text = ctk.CTkLabel(self, text='1.80', text_color=BLACK, font=ctk.CTkFont(family=FONT, size=INPUT_SIZE))
        output_text.pack(side='left', padx=20)


class Switch(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master=parent, text='metric', text_color=RED,
                         font=ctk.CTkFont(family=FONT, size=SWITCH, weight='bold'))
        self.place(relx=0.98, rely=0.01, anchor='ne')


if __name__ == '__main__':
    App()
