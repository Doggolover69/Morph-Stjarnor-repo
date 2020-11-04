#latest
import tkinter as tk
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
Credentials = ServiceAccountCredentials.from_json_keyfile_name('Key.json', scope)

gc = gspread.authorize(Credentials)

sheet = gc.open('videoplan ').sheet1


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
Episode_Cret = App()

# here are method calls to the window manager class

Episode_Cret.master.title('Episode selection page')
Episode_Cret.master.maxsize(1000, 1050)
Label = tk.Label(Episode_Cret, text='Please enter episode number')
entry = tk.Entry(Episode_Cret, text='videos')
entry.grid(row=2, column=2)
Label.grid(row=1, column=2)



def search():
    Enum = entry.get()
    entry.delete(0, 100)
    Episode = tk.Tk()
    Episode.title(Enum)
    Episode.maxsize(1680, 525)
    print(Enum)


    lab1 = tk.Label(Episode, text='Episode number ')
    lab2 = tk.Label(Episode, text=Enum)
    lab3 = tk.Label(Episode, text=' has been looked up in the sheet, here are the results')
    lab2.grid(row=1, column=6)
    lab1.grid(row=1, column=5)
    lab3.grid(row=1, column=7)

    find = sheet.find(Enum, in_column=2)
    EpRow = find.row
    print(EpRow)

#### Functions


    def Fil():
        sheet.update('F' + str(EpRow), True)
    def OS():
        sheet.update('G' + str(EpRow), True)
    def DOW():
        sheet.update('H' + str(EpRow), True)
    def EDI():
        sheet.update('I' + str(EpRow), True)
    def OS2():
        sheet.update('J' + str(EpRow), True)
    def OY():
        sheet.update('K' + str(EpRow), True)
    def CY():
        sheet.update('L' + str(EpRow), True)


    #### Buttons
    filmbutt = tk.Button(Episode, text='Filmed', padx=100, pady=50, command=Fil)
    onserverbutt = tk.Button(Episode, text='on server', padx=100, pady=50, command=OS)
    downloadedbutt = tk.Button(Episode, text='Downloaded', padx=100, pady=50, command=DOW)
    editedbutt = tk.Button(Episode, text='Edited', padx=100, pady=50, command=EDI)
    uploaded_to_stjarnor_server = tk.Button(Episode, text='On stjarnor server', padx=100, pady=50, command=OS2)
    uploaded_to_yt = tk.Button(Episode, text='Uploaded to youtube', padx=100, pady=50, command=OY)
    configured_on_yt = tk.Button(Episode, text='Ready to publish', padx=100, pady=50, command=CY)

    Filmed = sheet.acell('F' + str(EpRow)).value
    onserv = sheet.acell('G' + str(EpRow)).value
    downloaded = sheet.acell('H' + str(EpRow)).value
    edited = sheet.acell('I' + str(EpRow)).value
    onserv2 = sheet.acell('J' + str(EpRow)).value
    uploaded = sheet.acell('K' + str(EpRow)).value
    configured = sheet.acell('L' + str(EpRow)).value

    print(Filmed)
    print(onserv)
    print(downloaded)
    print(edited)
    print(onserv2)
    print(uploaded)

    if Filmed == 'TRUE':
        filmbutt.configure(state='disabled')
    elif Filmed == 'FALSE':
       filmbutt.configure(state='active')

    if onserv == 'TRUE':
        onserverbutt.configure(state='disabled')
    elif onserv == 'FALSE':
        onserverbutt.configure(state='active')

    if downloaded == 'TRUE':
        downloadedbutt.configure(state='disabled')
    elif downloaded == 'FALSE':
        downloadedbutt.configure(state='active')

    if edited == 'TRUE':
        downloadedbutt.configure(state='disabled')
    elif edited == 'FALSE':
        downloadedbutt.configure(state='active')

    if onserv2 == 'TRUE':
        uploaded_to_stjarnor_server.configure(state='disabled')
    elif onserv2 == 'FALSE':
        uploaded_to_stjarnor_server.configure(state='active')

    if uploaded == 'TRUE':
        uploaded_to_yt.configure(state='disabled')
    elif uploaded == 'FALSE':
        uploaded_to_yt.configure(state='active')

    if configured == 'TRUE':
        configured_on_yt.configure(state='disabled')
    elif configured == 'FALSE':
        configured_on_yt.configure(state='active')


    filmbutt.grid(row=3, column=0)
    onserverbutt.grid(row=3, column=2)
    downloadedbutt.grid(row=3, column=4)
    editedbutt.grid(row=3, column=6)
    uploaded_to_stjarnor_server.grid(row=3, column=7)
    uploaded_to_yt.grid(row=3, column=8)
    configured_on_yt.grid(row=4, column=0)

Button = tk.Button(Episode_Cret, text='Submit', command=search, bg='#06deec', fg='black')
Button.grid(row=3, column=2)
# start the program
Episode_Cret.mainloop()
