from tkinter import *
from functools import partial
import All_Constants as c

class Converter:

    def __init__(self):

        self.all_calculations_list = [['10.0°F is -12°C', '20.0°F is -7°C',
                                       '30.0°F is -1°C', '40.0°F is 4°C',
                                       '50.0°F is 10°C', '60.0°F is 16°C']
]

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", 14, "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):

        HistoryExport(self, self.all_calculations_list)

class HistoryExport:

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCS} / {len(calculations)}")

        recent_intro_text = (f"Below are {calc_amount} calculations "
                             "(to the nearest degree).")

        export_instruction_txt = ("Please push <Export> to save your calculations in a"
                                  "file. If the filename already exists, it will be")

        calculations = ""

        history_labels_list = [
            ["History / Export", ("Arial", 16, "bold"), None],
            [recent_intro_text, ("Arial", 11), None],
            ["calculation list", ("Arial", 14), calc_back],
            [export_instruction_txt, ("Arial", 11), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        self.export_filename_label = history_label_ref[3]

        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        button_details_list = [
            ["Export", "#004C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", 12, "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):

        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()





