import customtkinter
import tkinter
import tkinter.filedialog

customtkinter.set_appearance_mode("ark") #light, dark
customtkinter.set_default_color_theme("blue") # "blue" (standard), "green", "dark-blue"

class Number_file(customtkinter.CTkFrame): # создаём класс application, наследуемся от базового класса
    
    def __init__(self, app): #
        super().__init__(app) # вызываем инициализацию из класса CTkFrame

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        self.label_number_file = customtkinter.CTkLabel(self, text="Выберите количество файлов для загрузки от 1 до 4")
        self.label_number_file.grid(row=0, column=0, padx=10, pady=(10,250), sticky="ew")

        self.button_add_1_file = customtkinter.CTkButton(app, text ="1", width =40, command = self.function_add_1_file)
        self.button_add_1_file.grid(row=0, column=0, padx=20, pady=(10,380),  sticky="w")

        self.button_add_2_file = customtkinter.CTkButton(app, text ="2", width =40, command = self.function_add_2_file)
        self.button_add_2_file.grid(row=0, column=0, padx=20, pady=(10,270), sticky="w")
        
        self.button_add_3_file = customtkinter.CTkButton(app, text ="3", width =40, command = self.function_add_3_file)
        self.button_add_3_file.grid(row=0, column=0, padx=20, pady=(10,160), sticky="w")

        self.button_add_4_file = customtkinter.CTkButton(app, text ="4", width =40, command = self.function_add_4_file)
        self.button_add_4_file.grid(row=0, column=0, padx=20, pady=(10,50), sticky="w")

        self.button_open_1_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 1")
        self.button_open_1_file.grid(row=0, column=0, padx=100, pady=(10,380), sticky="w")  

        self.button_open_2_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 2")
        self.button_open_2_file.grid(row=0, column=0, padx=100, pady=(10,270), sticky="w")

        self.button_open_3_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 3")
        self.button_open_3_file.grid(row=0, column=0, padx=100, pady=(10,160), sticky="w")

        self.button_open_4_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 4")
        self.button_open_4_file.grid(row=0, column=0, padx=100, pady=(10,50), sticky="w")
        
    def function_add_1_file(self):
            
        self.button_open_1_file = customtkinter.CTkButton(app, text="Выбрать файл 1", command = self.function_choose_1_file)
        self.button_open_1_file.grid(row=0, column=0, padx=100, pady=(10,380), sticky="w")

        self.button_open_2_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 2")
        self.button_open_2_file.grid(row=0, column=0, padx=100, pady=(10,270), sticky="w")

        self.button_open_3_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 3")
        self.button_open_3_file.grid(row=0, column=0, padx=100, pady=(10,160), sticky="w")

        self.button_open_4_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 4")
        self.button_open_4_file.grid(row=0, column=0, padx=100, pady=(10,50), sticky="w")

    def function_add_2_file(self):
        self.button_open_1_file = customtkinter.CTkButton(app, text="Выбрать файл 1", command = self.function_choose_1_file)
        self.button_open_1_file.grid(row=0, column=0, padx=100, pady=(10,380), sticky="w")

        self.button_open_2_file = customtkinter.CTkButton(app, text="Выбрать файл 2", command = self.function_choose_2_file)
        self.button_open_2_file.grid(row=0, column=0, padx=100, pady=(10,270), sticky="w")
        
        self.button_open_3_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 3")
        self.button_open_3_file.grid(row=0, column=0, padx=100, pady=(10,160), sticky="w")

        self.button_open_4_file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 4")
        self.button_open_4_file.grid(row=0, column=0, padx=100, pady=(10,50), sticky="w") 

    def function_add_3_file(self):
        self.button_open_1file = customtkinter.CTkButton(app, text="Выбрать файл 1", command = self.function_choose_1_file)
        self.button_open_1file.grid(row=0, column=0, padx=100, pady=(10,380), sticky="w")

        self.button_open_2file = customtkinter.CTkButton(app, text="Выбрать файл 2", command = self.function_choose_2_file)
        self.button_open_2file.grid(row=0, column=0, padx=100, pady=(10,270), sticky="w")
        
        self.button_open_3file = customtkinter.CTkButton(app, text="Выбрать файл 3", command = self.function_choose_3_file)
        self.button_open_3file.grid(row=0, column=0, padx=100, pady=(10,160), sticky="w")

        self.button_open_4file = customtkinter.CTkButton(app, state= "disabled", text="Выбрать файл 4")
        self.button_open_4file.grid(row=0, column=0, padx=100, pady=(10,50), sticky="w")

    def function_add_4_file(self):
        self.button_open_1_file = customtkinter.CTkButton(app, text="Выбрать файл 1", command = self.function_choose_1_file)
        self.button_open_1_file.grid(row=0, column=0, padx=100, pady=(10,380), sticky="w")

        self.button_open_2_file = customtkinter.CTkButton(app, text="Выбрать файл 2", command = self.function_choose_2_file)
        self.button_open_2_file.grid(row=0, column=0, padx=100, pady=(10,270), sticky="w")

        self.button_open_3_file = customtkinter.CTkButton(app, text="Выбрать файл 3", command = self.function_choose_3_file)
        self.button_open_3_file.grid(row=0, column=0, padx=100, pady=(10,160), sticky="w")

        self.button_open_4_file = customtkinter.CTkButton(app, text="Выбрать файл 4", command = self.function_choose_4_file)
        self.button_open_4_file.grid(row=0, column=0, padx=100, pady=(10,50), sticky="w")
    
    def function_choose_1_file(self):
        filetypes = (("Звуковой файл", "*.wav"),("Звуковой файл", "*.wav"))
        filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="D:\Тестовое задание на Python", filetypes=filetypes) #initialdir="/"
        if filename:
            self.path_1=customtkinter.CTkEntry(app, width=500, placeholder_text=filename)
            self.path_1.grid(row=0, column=1, padx=10, pady=(10,380), sticky="w")

    def function_choose_2_file(self):
        filetypes = (("Звуковой файл", "*.wav"),("Звуковой файл", "*.wav"))
        filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="D:\Тестовое задание на Python", filetypes=filetypes) #initialdir="/"
        if filename:
            self.path_2=customtkinter.CTkEntry(app, width=500, placeholder_text=filename)
            self.path_2.grid(row=0, column=1, padx=10, pady=(10,270), sticky="w")

    def function_choose_3_file(self):
        filetypes = (("Звуковой файл", "*.wav"),("Звуковой файл", "*.wav"))
        filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="D:\Тестовое задание на Python", filetypes=filetypes) #initialdir="/"
        if filename:
            self.path_3=customtkinter.CTkEntry(app, width=500, placeholder_text=filename)
            self.path_3.grid(row=0, column=1, padx=10, pady=(10,160), sticky="w")

    def function_choose_4_file(self):
        filetypes = (("Звуковой файл", "*.wav"),("Звуковой файл", "*.wav"))
        filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="D:\Тестовое задание на Python", filetypes=filetypes) #initialdir="/"
        if filename:
            self.path_3=customtkinter.CTkEntry(app, width=500, placeholder_text=filename)
            self.path_3.grid(row=0, column=1, padx=10, pady=(10,50), sticky="w")

class Transfer_file(customtkinter.CTkFrame):
    def __init__(self, app):
        super().__init__(app)

        # self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=1)
        self.label_transfer_file = customtkinter.CTkLabel(self, text="Управление передачей файлов   ")
        self.label_transfer_file.grid(row=1, column=0, padx=10, pady=(10,100), sticky="ew")

        button_start = customtkinter.CTkButton(app, text ="Старт")
        button_start.grid(row=2, column=0, padx=20, pady=(20, 140), sticky="w")

        button_pause = customtkinter.CTkButton(app, text ="Пауза")
        button_pause.grid(row=2, column=0, padx=20, pady=(20,75), sticky="w")

        button_stop = customtkinter.CTkButton(app, text ="Стоп")
        button_stop.grid(row=2, column=0, padx=20, pady=(20,10), sticky="w")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Симулятор сигнала микрофонов")
        # self.geometry("400x180")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.number_file=Number_file(self)
        self.number_file.grid(row=0, column=0, padx=10, pady=(10, 250), sticky="nsw")

        self.transfer_file=Transfer_file(self)
        self.transfer_file.grid(row=2, column=0, padx=10, pady=(10,100), sticky="nsw")

    
app=App()
app.mainloop()