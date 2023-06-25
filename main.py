from new_post import post_enrichment
from profiles import prof_scrape
import time
from importer import Importer
import tkinter as tk
from PIL import ImageTk, Image
import re
import csv
#vis when working and when done

def main():
    #cleaning up after the last time
    clean_up()
    links =store_input()[0]
    final_file_name = f"output/{store_input()[1]}"
    profile_and_12_posts_scrape(links=links,final_file_name=final_file_name)

    with open("credentials.csv", "w") as file:
        file.truncate()

def clean_up():
    with open("new_post.csv", "w") as file:
        file.truncate()
    with open("profiles.csv", "w") as file:
        file.truncate()

def store_input():
    #getting the variables from the gui 
    user_input = entry_input.get().strip()
    user_output = entry_output.get().strip()
    credentials = {'Username': entry_username.get().strip(), "Password": entry_password.get().strip()}
    #I decided to store them in a csv file that will be cleaned after each scrape
    with open("credentials.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(credentials.keys())
        writer.writerow(credentials.values())  
    #some basic pre-caution in case user inputs a wrong file format
    if re.match(r"^.+\.csv$",user_input) and re.match(r"^.+\.csv$",user_output):
         return (user_input,user_output)
    else:
        raise ValueError


def profile_and_12_posts_scrape(links, final_file_name):
    #timimng the program to see the improvements 
    start = time.perf_counter()
    links_l = Importer(links)
    print(start)

    post_enrichment(prof_scrape(links_l.list_of_inputted_links),final_file_name)

    finish = time.perf_counter()
    print(f"finished in {round(finish-start,2)} sec") 

#gui stuff below
window = tk.Tk()
#size of the window
win_geo ="680x360"
window.geometry(win_geo)
#making sure that the user cannot increase it - because the design will suffer then
window.resizable(False, False)
window.title("Your datasets from Instagrams")


#bg image
img_file = "final_bg.png"
#fitting the image to the screensize 
img = Image.open(img_file).resize([680,360])
photo = ImageTk.PhotoImage(img)
background_label = tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# coordinates for easier adjustment of the items. As they will always remain in the same line. 
user_y = 105
user_x = 40
username = tk.Label(window,text = " SP Username")
username.configure(background="#1A2B45", fg="white",font=('Helvetica', 12, 'bold'))
username.place(x=user_x+85,y=user_y)
entry_username = tk.Entry(window)
entry_username.configure(width=13,font=("Arial",11))
entry_username.place(x=user_x+170,y=user_y)

password = tk.Label(window,text = " SP Password")
password.configure(background="#1A2B45", fg="white",font=('Helvetica', 12, 'bold'))
password.place(x=user_x+300,y=user_y)
entry_password = tk.Entry(window)
entry_password.configure(width=13,font=("Arial",11))
entry_password.place(x=user_x+385,y=user_y)

password = tk.Label(window,text = "Password")

#input and output labels
input_x= 160
input_y= 145
label_input_file = tk.Label(window,text="Input CSV*",padx=10,pady=10)
label_input_file.configure(background="#1A2B45", fg="white",font=('Helvetica', 18, 'bold'))
label_input_file.place(x=input_x,y=input_y-8)
entry_input = tk.Entry(window)
entry_input.place(x=input_x+120,y=input_y)

output_x = 160
output_y = 190
label_output_file = tk.Label(window,text="Output CSV*",padx=0,pady=0)
label_output_file.configure(background="#1A2B45", fg="white",font=('Helvetica', 18, 'bold'))
label_output_file.place(x=output_x,y=output_y)
entry_output = tk.Entry(window)
entry_output.place(x=output_x+120,y=output_y)



#checkboxes (not operational yet)
c_v_y = 237
c_v_x =180
fg = 'white'
bg ="#1F3851"
checkbox = tk.Checkbutton(window, text="Posts",font=("Arial",14,"bold"),foreground=fg,background=bg)
#checkbox.place(x=c_v_x,y=c_v_y)

checkbox = tk.Checkbutton(window, text="Profiles",font=("Arial",14,"bold"),foreground=fg,background=bg)
#checkbox.place(x=c_v_x+67,y=c_v_y)

checkbox = tk.Checkbutton(window, text="Posts and Profiles",font=("Arial",14,"bold"),foreground=fg,background=bg)
checkbox.place(x=c_v_x+147,y=c_v_y)


#button to trigger the main function
go_btn = tk.Button(window,text="START THE SCRAPE",font=("Arial",26,"bold"), width=20,height=2, bg="#D14860",command=main)
go_btn.configure(foreground='#1A2B45')
go_btn.place(y=270, x = 160)
window.mainloop()

