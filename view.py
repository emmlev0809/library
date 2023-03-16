import tkinter as tk
from tkinter import ttk
from controller import Controller
from functools import partial

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Name:')
        self.label.grid(row=1, column=0)

        self.label2 = ttk.Label(self, text='Email:')
        self.label2.grid(row=2, column=0)

        self.label3 = ttk.Label(self, text='Password:')
        self.label3.grid(row=3, column=0)

        # email entry
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=2, column=1, sticky=tk.NSEW)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, width=30)
        self.password_entry.grid(row=3, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=partial(self.save_button_clicked, "name"))
        self.save_button.grid(row=1, column=3, padx=10)


        self.save2_button = ttk.Button(self, text='Save', command=partial(self.save_button_clicked, "email"))
        self.save2_button.grid(row=2, column=3, padx=10)


        self.save3_button = ttk.Button(self, text='Save', command=partial(self.save_button_clicked, "password"))
        self.save3_button.grid(row=3, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=3, column=1, sticky=tk.W)



        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self, type):
        """
        Handle button click event
        :return:
        """
        if self.controller:

            if type == "name":

                try:
                    self.controller.save(self.name_var.get(), "name")

                    return self.show_success(f'The name {self.name_var.get()} saved!')

                except ValueError:
                    # show an error message

                    self.show_error("Failure")

            elif type == "email":

                try:
                    self.controller.save(self.email_var.get(), "email")

                    return self.show_success(f'The email {self.email_var.get()} saved!')

                except ValueError:
                    # show an error message

                    self.show_error("Failure")
            elif type == "password":

                try:
                    self.controller.save(self.password_var.get(), "password")

                    return self.show_success(f'The password {self.password_var.get()} saved!')

                except ValueError:
                    # show an error message

                    self.show_error("Failure")


    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')


    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Emma Tkinter MVC Demo')

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)


        # set the controller to view
        view.set_controller(Controller())


if __name__ == '__main__':
    app = App()
    app.mainloop()
