
from tkinter import *
from socket import *
import platform, os

def get_ip():
	# frame2.destroy()
	ip = gethostbyname(gethostname())
	liste.insert(END, "your ip address is :")
	liste.insert(END, ip)

def get_os():
	# frame2.destroy()
	p = platform.uname()
	liste.insert(END, "your os is: ")
	liste.insert(END, p.system)
	liste.insert(END, platform.uname().release)
	liste.insert(END, "your version is: ")
	liste.insert(END, p.version)

def get_user():
	userinfo = platform.uname()
	username = os.environ["USERNAME"]
	liste.insert(END, "your computer name is:")
	liste.insert(END, userinfo.node)
	liste.insert(END, "your processor is:")
	liste.insert(END, userinfo.processor)
	liste.insert(END, "your user name is:")
	liste.insert(END, username)
	# user_title2 = Label(frame3, text="your MAC address is: ", font=("Calibri", 15), bg='white', fg='red')
	# user_title3 = Label(frame3, text=os.system("getmac"), font=("Calibri", 15), bg='white', fg='red')
	# user_title2.pack()
	# user_title3.pack()

def save():
	# os.chdir("C:/Users/Default/Desktop")
	username = os.environ["USERNAME"]
	fichier = open("systeminfo.txt", "w")
	fichier.write("My System informations \n")
	fichier.write("My ip is: " + gethostbyname(gethostname()) + "\n")
	fichier.write("My os is: " +  platform.uname().system + platform.uname().release + "\n")
	fichier.write("This version is: " + platform.uname().version + "\n")
	fichier.write("My conputer name is: " + platform.uname().node + "\n")
	fichier.write("My user name is: " + username + "\n")
	fichier.write("My processor is: " + platform.uname().processor + "\n")
	fichier.close()

window = Tk()
window.title("information for your system")
window.geometry("720x480")
# window.iconbitmap("logo.ico")
window.config(background='#2D9DC6')

frame = Frame(window, bg='#2D9DC6')
frame2 = Frame(window, bg='#2D9DC6')
frame3 = Frame(window, bg='white')
frame4 = Frame(window, bg='#2D9DC6')
# frame = Frame(window, bg='#B3B3B3', bd=1, relief=SUNKEN)
liste = Listbox(frame3)

label_title = Label(frame, text="Bienvenue sur mon application", font=("Calibri", 30), bg='#2D9DC6', fg='white')
label_title.pack()

label_subtitle = Label(frame, text="Voici toutes les informations", font=("Calibri", 20), bg='#2D9DC6', fg='white')
label_subtitle.pack()

ip_button = Button(frame2, text="showing my ip", font=("Calibri", 20), bg='white', fg='#2D9DC6', command=get_ip)
ip_button.pack(pady=25, side="right")

os_button = Button(frame2, text="showing my OS", font=("Calibri", 20), bg='white', fg='#2D9DC6', command=get_os)
os_button.pack(pady=25, side="left")

user_button = Button(frame2, text="showing my systeminfo", font=("Calibri", 20), bg='white', fg='#2D9DC6', command=get_user)
user_button.pack(pady=25, side="right")

save_button = Button(frame4, text="save in txt file", font=("Calibri", 20), bg='white', fg='#2D9DC6', command=save)
save_button.pack(pady=25)

liste.pack()
frame.pack(expand=YES)
frame2.pack(expand=YES)
frame3.pack(expand=YES)
frame4.pack(expand=YES)

window.mainloop()
