import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = randint(8, 10)
  nr_symbols = randint(2, 4)
  nr_numbers = randint(2, 4)

  password_leters = [choice(letters) for _ in range(nr_letters)]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_leters + password_symbols + password_numbers


  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)


  print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")
        return
    
    else:
    
        is_ok = messagebox.askokcancel(
        title="Confirmation",
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?"
    )
        
        if is_ok == True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, tkinter.END)
                email_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
            

            messagebox.showinfo(title="Success", message="Password saved successfully!")
        
        
        

# ---------------------------- UI SETUP ------------------------------- #


#Start a window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

#label


#canvas -> create a widigtes 

my_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo = tkinter.PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=logo)
my_canvas.grid(row=0, column=1)

#label 

my_label = tkinter.Label(text="Web-Site:", font=("Calibri", 12, "italic"))
my_label.grid (row=1, column=0)
my_label = tkinter.Label(text="Email/Username:", font=("Calibri", 12, "italic"))
my_label.grid(row=2, column=0)
my_label = tkinter.Label(text="Password:", font=("Calibri", 12, "italic"))
my_label.grid(row=3, column=0)


#entry

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()


email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "Your email or username.")



password_entry = tkinter.Entry(width=25)
password_entry.grid(row=3, column=1)
password_entry.config(show="*")




#buttons 

generate_button = tkinter.Button(text="Generate Password", command=genarate_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=25, command=save)
add_button.grid(row=4, column=0, columnspan=2)



window.mainloop()