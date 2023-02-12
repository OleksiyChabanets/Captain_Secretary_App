import tkinter as tk
from datetime import datetime
from tkinter import ttk
# from calendar import DateEntry, Calendar
import sqlite3

VERSION = 'Software Ver: 0.2'


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db

    def part_of_day(self):

        """Function finding out present part of day (Morning, Day, Afternoon, Evening - depends of
        System time and return parameter day"""

        global day
        hour_now = datetime.now().hour

        if 4 <= hour_now <= 9:
            day = "Morning"
        elif 10 <= hour_now <= 11:
            day = "Day"
        elif 12 <= hour_now <= 17:
            day = "Afternoon"
        elif 18 <= hour_now <= 23 or 0 <= hour_now <= 3:
            day = "Evening"
        return day

    def init_main(self):

        self.logo_img = tk.PhotoImage(file='logo.gif')
        label_logo = tk.Label(image=self.logo_img)
        label_logo.pack()

        cap_name = '$$$'
        label_hello1 = tk.Label(root, text="Good " + Main.part_of_day(
            self) + ", Captain " + cap_name + "\n How can I help you today?",
                                font="Arial 18")
        label_hello1.pack()

        dmf_labelframe = tk.LabelFrame(root, text="Data Management Functions")
        dmf_labelframe.pack(ipadx=3, ipady=3)

        separation = tk.Frame(root, height=5)
        separation.pack()

        dmf_top = tk.Frame(dmf_labelframe)
        dmf_top.pack()

        separation = tk.Frame(dmf_labelframe, height=5)
        separation.pack()

        btn_update_crew_db = tk.Button(dmf_top, width=25, height=3, text="Update Crew DB",
                                       command=self.open_crew_db_child)
        btn_update_crew_db.pack(side=tk.LEFT)

        btn_update_ship_db = tk.Button(dmf_top, width=25, height=3, text="Update Ship DB",
                                       command=self.update_ship_db)
        btn_update_ship_db.pack(side=tk.RIGHT)

        dmf_bot = tk.Frame(dmf_labelframe)
        dmf_bot.pack()

        separation = tk.Frame(dmf_labelframe, height=5)
        separation.pack()

        dmf_bot_bot = tk.Frame(dmf_labelframe)
        dmf_bot_bot.pack()

        btn_update_passenger_db = tk.Button(dmf_bot, width=25, height=3, text="Update Passenger DB",
                                            command=self.update_pass_db)
        btn_update_passenger_db.pack(side=tk.LEFT)

        btn_update_canteen_db = tk.Button(dmf_bot, width=25, height=3, text="Update Canteen DB",
                                          command=self.update_canteen_db)
        btn_update_canteen_db.pack(side=tk.RIGHT)

        btn_current_ship_cond = tk.Button(dmf_bot_bot, width=50, height=3, text="Update Current Ship's Condition",
                                          command=self.current_ship_condition)
        btn_current_ship_cond.pack(side=tk.LEFT)

        dpf_labelframe = tk.LabelFrame(root, text="Document Preparation Functions")
        dpf_labelframe.pack(ipadx=3, ipady=3)

        separation = tk.Frame(root, height=5)
        separation.pack()

        dpf_top = tk.Frame(dpf_labelframe)
        dpf_top.pack(side=tk.TOP)

        btn_prep_pre_arr = tk.Button(dpf_top, width=25, height=3, text="Pre-arrival documents",
                                     command=self.prep_pre_arr)
        btn_prep_pre_arr.pack(side=tk.LEFT)

        btn_prep_monthly_adm = tk.Button(dpf_top, width=25, height=3, text="Monthly Administration",
                                         command=self.prep_month_adm)
        btn_prep_monthly_adm.pack(side=tk.RIGHT)

        mon_labelframe = tk.LabelFrame(root, text="Monitoring and Overview Functions")
        mon_labelframe.pack(ipadx=3, ipady=3)

        separation = tk.Frame(root, height=5)
        separation.pack()

        mon = tk.Label(mon_labelframe, width=50, height=5, text="monitoring widgets")
        mon.pack()

        info_labelframe = tk.LabelFrame(root, text="Information Back Up Functions")
        info_labelframe.pack(ipadx=3, ipady=3)

        btn_create_backup_db = tk.Button(info_labelframe, width=25, height=3, text="Create Back-up DB",
                                         command=self.create_backup_db)
        btn_create_backup_db.pack(side=tk.LEFT)

        btn_update_from_backup = tk.Button(info_labelframe, width=25, height=3, text="Update Program from Back-up",
                                           command=self.update_from_backup)
        btn_update_from_backup.pack(side=tk.LEFT)

        separation = tk.Frame(root, height=15)
        separation.pack()

        cancel_top = tk.Frame(root)
        cancel_top.pack(side=tk.TOP)

        self.copyright_img = tk.PhotoImage(file='CopyRightsLogo1.gif')
        label_copyright = tk.Label(image=self.copyright_img)
        label_copyright.pack(side=tk.RIGHT)

        btn_cancel_main = tk.Button(cancel_top, width=25, height=3, text="Nothing for a moment \n Thank you",
                                    command=root.destroy)
        btn_cancel_main.pack(side=tk.TOP)

        label_version = tk.Label(text=VERSION, font="Arial 10")
        label_version.pack(side=tk.LEFT)

    def update_ship_db(self):
        print("Update Ship's DB")

    def update_pass_db(self):
        print("Update Passenger's DB")

    def update_canteen_db(self):
        print("Update Canteen DB")

    def prep_pre_arr(self):
        print('Prepare Pre-arrivals')

    def prep_month_adm(self):
        print('Prepare Monthly Administration')

    def current_ship_condition(self):
        print("Update Current Ship's Condition")

    def create_backup_db(self):
        print('create back-up DB(possible separate class)')

    def update_from_backup(self):
        print('Update from Back-up DB (possible separate class)')

    def cancel_main_window(self):
        print('Close Main Window')

    def open_crew_db_child(self):
        CrewDBWindow()


class CrewDBWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_crew_db_child()
        self.db = db
        self.view_records()

    def init_crew_db_child(self):
        toolbar = tk.Frame(self, bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')

        btn_add_crew = tk.Button(toolbar, text='Add new Crew', command=self.add_crew_info,
                                 bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
        btn_add_crew.pack(side=tk.LEFT)

        self.title('Crew DB options')
        self.geometry("1000x600+300+300")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.tree = ttk.Treeview(self, columns=('ID', 'surname', 'name', 'rank', 'nationality', 'date_ob',
                                                'place_ob', 'passport_no', 'passport_doi', 'passport_doe',
                                                'seam_book_no', 'seam_book_doi', 'seam_book_doe', 'join_vsl_date',
                                                'join_vsl_port'), height=25, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('surname', width=150, anchor=tk.CENTER)
        self.tree.column('name', width=120, anchor=tk.CENTER)
        self.tree.column('rank', width=100, anchor=tk.CENTER)
        self.tree.column('nationality', width=150, anchor=tk.CENTER)
        self.tree.column('date_ob', width=100, anchor=tk.CENTER)
        self.tree.column('place_ob', width=120, anchor=tk.CENTER)
        self.tree.column('passport_no', width=80, anchor=tk.CENTER)
        self.tree.column('passport_doi', width=150, anchor=tk.CENTER)
        self.tree.column('passport_doe', width=150, anchor=tk.CENTER)
        self.tree.column('seam_book_no', width=120, anchor=tk.CENTER)
        self.tree.column('seam_book_doi', width=170, anchor=tk.CENTER)
        self.tree.column('seam_book_doe', width=170, anchor=tk.CENTER)
        self.tree.column('join_vsl_date', width=100, anchor=tk.CENTER)
        self.tree.column('join_vsl_port', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('surname', text='Surname')
        self.tree.heading('name', text='Name')
        self.tree.heading('rank', text='Rank')
        self.tree.heading('nationality', text='Nationality')
        self.tree.heading('date_ob', text='Date of Birth')
        self.tree.heading('place_ob', text='Place of Birth')
        self.tree.heading('passport_no', text='Passport No')
        self.tree.heading('passport_doi', text='Passport Date of Issue')
        self.tree.heading('passport_doe', text='Passport Exp Date')
        self.tree.heading('seam_book_no', text="Seaman's Book No")
        self.tree.heading('seam_book_doi', text="Seaman's Book Date of issue")
        self.tree.heading('seam_book_doe', text="Seaman's Book Exp Date")
        self.tree.heading('join_vsl_date', text="Date of Join Ship")
        self.tree.heading('join_vsl_port', text="Port of Join Ship")

        self.tree.pack()

    def records(self, surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi, passport_doe,
                seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port):
        self.db.insert_data(surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi,
                            passport_doe, seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM crew''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def add_crew_info(self):
        AddCrewDBWindow()


class AddCrewDBWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.init_add_crew_db_child()
        self.view = CrewDBWindow


    def init_add_crew_db_child(self):
        self.title("Crew Member's Personal Data Input")
        self.geometry("648x400+50+50")
        self.resizable(False, False)


        logo_frame = tk.Frame(self)
        logo_frame.pack(fill=tk.X)

        self.logo_img = tk.PhotoImage(file='logo.gif')
        self.label_logo = tk.Label(logo_frame, image=self.logo_img)
        self.label_logo.pack(side=tk.LEFT)

        self.copyright_img = tk.PhotoImage(file='CopyRightsLogo1.gif')
        label_copyright = tk.Label(logo_frame, image=self.copyright_img)
        label_copyright.pack(side=tk.RIGHT)

        crew_info_frame = tk.Frame(self)
        crew_info_frame.pack(fill=tk.X)

        initial_info_labelframe = tk.LabelFrame(crew_info_frame, text="Initial Information")
        initial_info_labelframe.pack(side=tk.LEFT, ipadx=3, ipady=3)

        left_name_frame = tk.Frame(initial_info_labelframe)
        left_name_frame.pack(side=tk.LEFT)

        label_separator = tk.Label(left_name_frame, text="_______________")
        label_separator.pack()

        label_surname = tk.Label(left_name_frame, text="Surname:")
        label_surname.pack()

        label_name = tk.Label(left_name_frame, text="Name:")
        label_name.pack()

        label_dob = tk.Label(left_name_frame, text="Date of birth:")
        label_dob.pack()

        label_pob = tk.Label(left_name_frame, text="Place of birth:")
        label_pob.pack()

        label_rank = tk.Label(left_name_frame, text="Rank:")
        label_rank.pack()

        label_nationality = tk.Label(left_name_frame, text="Nationality:")
        label_nationality.pack()

        label_join_vsl_date = tk.Label(left_name_frame, text="Join Ship, [Date]:")
        label_join_vsl_date.pack()

        left_input_frame = tk.Frame(initial_info_labelframe)
        left_input_frame.pack(side=tk.RIGHT)

        label_separator = tk.Label(left_input_frame, text="                    ")
        label_separator.pack()

        self.entry_surname = ttk.Entry(left_input_frame, justify=tk.RIGHT)
        self.entry_surname.pack()

        self.entry_name = ttk.Entry(left_input_frame, justify=tk.RIGHT)
        self.entry_name.pack()

        self.entry_dob = ttk.Entry(left_input_frame)
        self.entry_dob.pack()

        self.entry_pob = ttk.Entry(left_input_frame, justify=tk.RIGHT)
        self.entry_pob.pack()

        self.combo_rank = ttk.Combobox(left_input_frame, values=[u'Captain', u'Chief Officer', u'2nd Officer',
                                                                 u'3rd Officer', u'Chief Engineer', u'2nd Engineer',
                                                                 u'3rd Engineer', u'Cook', u'AB', u'OS', u'Cadet',
                                                                 u'Fitter', u'Electrician'])
        self.combo_rank.current(0)
        self.combo_rank.pack()

        self.combo_nationality = ttk.Combobox(left_input_frame,
                                              values=[u'Ukrainian', u'Dutch', u'Russian', u'Indonesian'])
        self.combo_nationality.current(0)
        self.combo_nationality.pack()

        self.entry_join_vsl_date = ttk.Entry(left_input_frame)
        self.entry_join_vsl_date.pack()

        travel_info_labelframe = tk.LabelFrame(crew_info_frame, width=580, height=300, text="Travel Information")
        travel_info_labelframe.pack(side=tk.RIGHT, ipadx=3, ipady=3)

        right_name_frame = tk.Frame(travel_info_labelframe)
        right_name_frame.pack(side=tk.LEFT)

        label_separator = tk.Label(right_name_frame, text="_______________")
        label_separator.pack()

        label_passport_no = tk.Label(right_name_frame, text="Passport No:")
        label_passport_no.pack()

        label_passport_issue = tk.Label(right_name_frame, text="Issue Date:")
        label_passport_issue.pack()

        label_passport_exp = tk.Label(right_name_frame, text="Exp Date:")
        label_passport_exp.pack()

        label_seam_book_no = tk.Label(right_name_frame, text="Seaman's Book No:")
        label_seam_book_no.pack()

        label_seam_book_issue = tk.Label(right_name_frame, text="Issue Date:")
        label_seam_book_issue.pack()

        label_seam_book_exp = tk.Label(right_name_frame, text="Exp Date:")
        label_seam_book_exp.pack()

        label_join_vsl_port = tk.Label(right_name_frame, text="Join Ship, [Port]:")
        label_join_vsl_port.pack()

        right_input_frame = tk.Frame(travel_info_labelframe)
        right_input_frame.pack(side=tk.RIGHT)

        label_separator = tk.Label(right_input_frame, text="                    ")
        label_separator.pack()

        self.entry_passport_no = ttk.Entry(right_input_frame, justify=tk.RIGHT)
        self.entry_passport_no.pack()

        self.entry_passport_issue = ttk.Entry(right_input_frame)
        self.entry_passport_issue.pack()

        self.entry_passport_exp = ttk.Entry(right_input_frame)
        self.entry_passport_exp.pack()

        self.entry_seam_book_no = ttk.Entry(right_input_frame, justify=tk.RIGHT)
        self.entry_seam_book_no.pack()

        self.entry_seam_book_issue = ttk.Entry(right_input_frame)
        self.entry_seam_book_issue.pack()

        self.entry_seam_book_exp = ttk.Entry(right_input_frame)
        self.entry_seam_book_exp.pack()

        self.entry_join_vsl_port = ttk.Entry(right_input_frame, justify=tk.RIGHT)
        self.entry_join_vsl_port.pack()

        ok_cancel_button_frame = tk.Frame(self)
        ok_cancel_button_frame.pack(fill=tk.X)

        self.btn_ok = ttk.Button(ok_cancel_button_frame, text='  Add information \n to Crew Data Base')
        self.btn_ok.pack(side=tk.LEFT)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_surname.get(),
                                                                       self.entry_name.get(),
                                                                       self.combo_rank.get(),
                                                                       self.combo_nationality.get(),
                                                                       self.entry_dob.get(),
                                                                       self.entry_pob.get(),
                                                                       self.entry_passport_no.get(),
                                                                       self.entry_passport_issue.get(),
                                                                       self.entry_passport_exp.get(),
                                                                       self.entry_seam_book_no.get(),
                                                                       self.entry_seam_book_issue.get(),
                                                                       self.entry_seam_book_exp.get(),
                                                                       self.entry_join_vsl_date.get(),
                                                                       self.entry_join_vsl_port.get()))

        btn_cancel = ttk.Button(ok_cancel_button_frame, text='Cancel Window', command=self.destroy)
        btn_cancel.pack(side=tk.RIGHT)

        self.grab_set()
        self.focus_set()


# class AddPersonalRecord:
#     def __init__(self):
#         self.db = db
#         self.view_records()
#         self.tree = CrewDBWindow.
#
#
#     def records(self, surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi, passport_doe,
#                 seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port):
#         self.db.insert_data(surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi,
#                             passport_doe, seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port)
#         self.view_records()
#
#     def view_records(self):
#         self.db.c.execute('''SELECT * FROM crew''')
#         [self.tree.delete(i) for i in self.tree.get_children()]
#         [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
#
#     def add_crew_info(self):
#         AddCrewDBWindow()


class CrewDB:
    def __init__(self):
        self.conn = sqlite3.connect('crew.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS crew (id integer primary key, surname text, name text, rank text, 
        nationality text, date_ob text, place_ob text, passport_no text, passport_doi text, passport_doe text, 
        seam_book_no text, seam_book_doi text, seam_book_doe text, join_vsl_date text, join_vsl_port text)''')
        self.conn.commit()

    def insert_data(self, surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi, passport_doe,
                    seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port):
        self.c.execute('''INSERT INTO crew (surname, name, rank, nationality, date_ob, place_ob, passport_no, 
                        passport_doi, passport_doe, seam_book_no, seam_book_doi, seam_book_doe, 
                        join_vsl_date, join_vsl_port) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (surname, name, rank, nationality, date_ob, place_ob, passport_no, passport_doi, passport_doe,
                        seam_book_no, seam_book_doi, seam_book_doe, join_vsl_date, join_vsl_port))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = CrewDB()
    app = Main(root)
    app.pack()


    root.title("Captain's Secretary App")
    root.geometry("480x730+400+100")
    root.resizable(False, False)

    root.mainloop()
