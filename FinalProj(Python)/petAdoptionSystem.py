from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
root.title('FurEver Homes')
root.geometry("800x600")
root.resizable(0, 0)
# Global list to store pet data
pets_list = []  # dictionary representing a pet

def init_db():
    """Initialize the SQLite database and create tables."""
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    #cursor.execute('''DROP TABLE health''') # If magdedelete ng table,just remove the hashtag to reset the table
    #cursor.execute('''DROP TABLE pets''') # If magdedelete ng table,just remove the hashtag to reset the table
    #cursor.execute('''DROP TABLE adopters''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS health (
        health_id INTEGER PRIMARY KEY,
        health_status TEXT NOT NULL,
        vitamins TEXT,
        weight TEXT,
        adoption_fee INT,
        height TEXT,
        pet_id INT,
        FOREIGN KEY(pet_id) REFERENCES pets(pet_id)
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_name VARCHAR(20) NOT NULL,
        pet_age TEXT,
        pet_gender TEXT,
        pet_breed TEXT,
        vaccine_date DATE,
        looks_descrip TEXT,
        adopted TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS adopters (
        adopter_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        l_name VARCHAR(50) NOT NULL,
        age TEXT,
        address TEXT,
        contact_number INT,
        valid_id INT,
        pet_id INTEGER, 
        FOREIGN KEY(pet_id) REFERENCES pets(pet_id) 
    )''')
    conn.commit()
    conn.close()

def clear_screen(): # Function to clear the window (just in case)
    for widget in root.winfo_children():
        widget.grid_forget()

def main_menu(): # Function to show the main menu
    clear_screen()

    image = Image.open("C:\\Users\\Admin\\Downloads\\cat.jpg") #kapag mag iinsert ng pic, locate the image first then copy the location
    image = image.resize((800, 600), Image.Resampling.LANCZOS)  # Resize image to fit window
    global bg_image  # Make the image reference global
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Make the image cover the entire window
    
    root.grid_columnconfigure(0, weight=1)  # Allow first column to stretch
    root.grid_columnconfigure(1, weight=2)  
    root.grid_columnconfigure(1, weight=1)  
    root.grid_columnconfigure(3, weight=1) 
   
    admin_but = Button(root, text="Admin", command=adminLogIn, fg="black", bg="Orange", font=("Arial", 12, "bold"),
                       bd=2, relief=RAISED, highlightthickness=0, pady=0, width=2, height=2).grid(row=0, column=1, padx=5, pady=9, sticky="ew")
    user_but = Button(root, text="User / Adopter",command=user, fg="black", bg="Orange", font=("Arial", 12, "bold"),
                      bd=2, relief=RAISED, highlightthickness=0, pady=0, width=5, height=2).grid(row=1, column=1, padx=5, pady=9, sticky="ew")
    exit_but = Button(root, text="Exit", command=root.quit, fg="black", bg="Red", font=("Arial", 12, "bold"),
                      bd=2, relief=RAISED, highlightthickness=0, pady=0, width=5, height=2).grid(row=2, column=1, padx=5, pady=9, sticky="ew")

def adminLogIn(): # Function for admin login
    clear_screen()

    imagee = Image.open("C:\\Users\\Admin\\Downloads\\admin.jpg")
    imagee = imagee.resize((800, 600), Image.Resampling.LANCZOS)
    global bgimage  # Make the image reference global
    bgimage = ImageTk.PhotoImage(imagee)  
    bglabel = Label(root, image=bgimage) 
    bglabel.place(relwidth=1, relheight=1) 

    adminname_label = Label(root, text="Username: ", font=(10))
    adminname_label.grid(row=0, column=0, padx=10, pady=5)
    admin_username = Entry(root, width=30, font=(10))
    admin_username.grid(row=0, column=1, padx=20, pady=5)

    adminusername_label = Label(root, text="Password: ", font=(10))
    adminusername_label.grid(row=1, column=0, padx=10, pady=5)
    admin_password = Entry(root, width=30, font=(10), show="*")
    admin_password.grid(row=1, column=1, padx=20, pady=5)

    Log_In_Admin = Button(root, text="Log In", command=lambda: authenticate_admin(admin_username, admin_password), fg="black", bg="yellow", font=(10))
    Log_In_Admin.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    exitbutton = Button(root, text="Menu", command=main_menu, fg="black", bg="orange", font=(10))
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def authenticate_admin(admin_username, admin_password):
    if admin_username.get() == "admin" and admin_password.get() == "jhonmark20": 
        messagebox.showinfo("Welcome admin", f"You have succesfully log in!") 
        menu()  
    else:
        error_label = Label(root, text="Invalid Username or Password", fg="red", font=("Arial", 10))
        error_label.grid(row=3, column=0, columnspan=2)

def menu():
    clear_screen()
    button_width = 25 
    button_height = 2 

    addbutton = Button(root, text="Add/Update", command=addOrUpdate, fg="black", bg="orange", width=button_width, height=button_height)
    addbutton.grid(row=6, column=0, columnspan=1, pady=15, padx=10)

    viewbutton = Button(root, text="View Pets", command=viewPets, fg="black", bg="orange", width=button_width, height=button_height)
    viewbutton.grid(row=8, column=0, columnspan=1, pady=15, padx=10)

    markbutton = Button(root, text="Mark as Adopted", command=mark_adopted, fg="black", bg="orange", width=button_width, height=button_height)
    markbutton.grid(row=8, column=1, columnspan=2, pady=15, padx=10)

    delMarkbutton = Button(root, text="Mark as Available", command=delete_markAdopt, fg="black", bg="orange", width=button_width, height=button_height)
    delMarkbutton.grid(row=8, column=2, columnspan=2, pady=15, padx=10)

    deletebutton = Button(root, text="Delete Pet", command=deletePet, fg="black", bg="orange", width=button_width, height=button_height)
    deletebutton.grid(row=6, column=1, columnspan=1, pady=15, padx=10)

    adoptInfobutton = Button(root, text="View adopter Information",command=viewAdopters,  fg="black", bg="orange", width=button_width, height=button_height)
    adoptInfobutton.grid(row=6, column=2, columnspan=2, pady=15, padx=10)

    adoptdelbutton = Button(root, text="Delete Adopter Information",command=deleteAdopter, fg="black", bg="orange", width=button_width, height=button_height)
    adoptdelbutton.grid(row=12, column=0, columnspan=1, pady=15, padx=10)

    exitbutton = Button(root, text="Menu", command=main_menu, fg="black", bg="orange", width=button_width, height=button_height)
    exitbutton.grid(row=12, column=2, columnspan=2, pady=15, padx=10)

def addOrUpdate():
    
    quest_label = Label(root, text="ADD OR UPDATE PET INFO", font=(50))
    quest_label.grid(row=18, column=0, padx=10, pady=5)
    button_widthh = 25  
    button_heightt = 2 

    questionbutton = Button(root, text="Add pet Info", command=addInfo, fg="black", bg="lightblue", width=button_widthh, height=button_heightt)
    questionbutton.grid(row=20, column=0, columnspan=1, pady=15, padx=10)
    questbutton = Button(root, text="Edit pet Info", command=asking_id_for_edit, fg="black", bg="lightblue", width=button_widthh, height=button_heightt)
    questbutton.grid(row=22, column=0, columnspan=1, pady=15, padx=10)

def addInfo():
    clear_screen()
    pet_name = Label(root, text="Pet Name: ", font=(10))
    pet_name.grid(row=0, column=0, padx=5, pady=5)
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=5)
    
    pet_age = Label(root, text="Pet Age: ", font=(10))
    pet_age.grid(row=1, column=0, padx=5, pady=5)
    pet_ageEntry = Entry(root, width=30)
    pet_ageEntry.grid(row=1, column=1, padx=20, pady=5)

    pet_gender_label = Label(root, text="Gender: ", font=(10))
    pet_gender_label.grid(row=2, column=0, padx=5, pady=5)
    pet_gender = Entry(root, width=30)
    pet_gender.grid(row=2, column=1, padx=20, pady=5)

    pet_breed_label = Label(root, text="Breed: ", font=(10))
    pet_breed_label.grid(row=3, column=0, padx=5, pady=5)
    pet_breed = Entry(root, width=30)
    pet_breed.grid(row=3, column=1, padx=20, pady=5)

    vacc_label = Label(root, text="Last Vaccine Date: ", font=(10))
    vacc_label.grid(row=4, column=0, padx=5, pady=5)
    vaccine_dateEntry = Entry(root, width=30)
    vaccine_dateEntry.grid(row=4, column=1, padx=20, pady=5)

    looks_label = Label(root, text="Looks description: ", font=(10))
    looks_label.grid(row=5, column=0, padx=5, pady=5)
    looks_descripEntry = Entry(root, width=30)
    looks_descripEntry.grid(row=5, column=1, padx=20, pady=5)
    
    button_width = 20 
    button_height = 2 
    add_button = Button(root, text="Add Information", command=lambda: save_pet_info(f_name, pet_ageEntry, pet_gender, pet_breed, vaccine_dateEntry,looks_descripEntry), fg="black", bg="lightblue", width=button_width, height=button_height)
    add_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", width=button_width, height=button_height)
    exitbutton.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

def save_pet_info(f_name, pet_ageEntry, pet_gender, pet_breed, vaccine_dateEntry, looks_descripEntry):
    pet_name = f_name.get()
    pet_age = pet_ageEntry.get()
    pet_gender = pet_gender.get()
    pet_breed = pet_breed.get()
    vaccine_date = vaccine_dateEntry.get()
    looks_descrip = looks_descripEntry.get()

    if not pet_name or not pet_age or not pet_gender or not pet_breed or not vaccine_date or not looks_descrip:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM pets WHERE pet_name=?", (pet_name,))
    if cursor.fetchone()[0] > 0:
        messagebox.showerror("Duplicate Pet", f"A pet with the name '{pet_name}' already exists.")
        conn.close()
        return

    cursor.execute('''INSERT INTO pets (pet_name, pet_age, pet_gender, pet_breed, vaccine_date, looks_descrip, adopted)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                      (pet_name, pet_age, pet_gender, pet_breed, vaccine_date, looks_descrip, 'Available'))
    
    pet_id = cursor.lastrowid 
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Pet {pet_name} added successfully.")
    clear_screen()
    health_Label = Label(root, text="Health Status: ", font=(10))
    health_Label.grid(row=0, column=0, padx=5, pady=5)
    health_statusEntry = Entry(root, width=30)
    health_statusEntry.grid(row=0, column=1, padx=20, pady=5)
    
    vitaminsLabel = Label(root, text="Vitamins: ", font=(10))
    vitaminsLabel.grid(row=1, column=0, padx=5, pady=5)
    vitaminsEntry = Entry(root, width=30)
    vitaminsEntry.grid(row=1, column=1, padx=20, pady=5)

    weight_label = Label(root, text="Weight (kg): ", font=(10))
    weight_label.grid(row=2, column=0, padx=5, pady=5)
    weightEntry = Entry(root, width=30)
    weightEntry.grid(row=2, column=1, padx=20, pady=5)

    height_label = Label(root, text="Height (cm): ", font=(10))
    height_label.grid(row=3, column=0, padx=5, pady=5)
    heightEntry = Entry(root, width=30)
    heightEntry.grid(row=3, column=1, padx=20, pady=5)

    fee_label = Label(root, text="Adoption Fee (For overall expenses from vet to med): ", font=(10))
    fee_label.grid(row=4, column=0, padx=5, pady=5)
    feeEntry = Entry(root, width=30)
    feeEntry.grid(row=4, column=1, padx=20, pady=5)

    button_width = 20 
    button_height = 2
    add_button = Button(root, text="Add Health Information",command=lambda: save_pet_health(pet_id, health_statusEntry, vitaminsEntry, weightEntry, heightEntry,feeEntry), fg="black", bg="orange", width=button_width, height=button_height)
    add_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", width=button_width, height=button_height)
    exitbutton.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

def save_pet_health(pet_id, health_statusEntry, vitaminsEntry, weightEntry, heightEntry,feeEntry):
    health_status = health_statusEntry.get()
    vitamins = vitaminsEntry.get()
    weight = weightEntry.get()
    height = heightEntry.get()
    adoption_fee = feeEntry.get()

    if not health_status or not vitamins or not weight or not height or not adoption_fee:
        messagebox.showerror("Error", "All fields must be filled out.")
        return
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO health (health_status, vitamins, weight, height,adoption_fee , pet_id)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                      (health_status, vitamins, weight, height,adoption_fee ,pet_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Pet health information added successfully.")
    menu()

def asking_id_for_edit():
    clear_screen()
    petID = Label(root, text="ENTER PET ID TO EDIT", font=(20))
    petID.grid(row=0, column=0, padx=5, pady=5)
    pet_id = Entry(root, width=30)
    pet_id.grid(row=0, column=1, padx=20, pady=5)
    # Using lambda to pass pet_id to edit_pet_info
    editbutton = Button(root, text="EDIT", command=lambda: edit_pet_info(pet_id.get()), fg="black", bg="lightblue",height=2,width=15)
    editbutton.grid(row=20, column=0, columnspan=2, pady=15, padx=10)
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2,width=15)
    exitbutton.grid(row=22, column=0, columnspan=2, pady=15, padx=10)

def edit_pet_info(pet_id):
    clear_screen()
    if not pet_id:  # If the pet_id is empty
        messagebox.showwarning("Input Error", "Please enter a Pet ID to edit.")
        asking_id_for_edit()  
        return  
    
    try:
        pet_id = int(pet_id)
    except ValueError:
        messagebox.showwarning("Input Error", "Pet ID must be a number.")
        asking_id_for_edit() 
        return  
    
    try:
        conn = sqlite3.connect('pets.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets WHERE pet_id=?", (pet_id,))
        pet = cursor.fetchone()

        if pet: 
            pet_name = Label(root, text="Pet Name: ", font=(10))
            pet_name.grid(row=0, column=0, padx=5, pady=5)
            pet_name_entry = Entry(root, width=30)
            pet_name_entry.grid(row=0, column=1, padx=20, pady=5)
            pet_name_entry.insert(0, pet[1]) 

            pet_age = Label(root, text="Pet Age: ", font=(10))
            pet_age.grid(row=1, column=0, padx=5, pady=5)
            pet_ageEntry = Entry(root, width=30)
            pet_ageEntry.grid(row=1, column=1, padx=20, pady=5)
            pet_ageEntry.insert(0, pet[2]) 

            pet_gender_label = Label(root, text="Gender: ", font=(10))
            pet_gender_label.grid(row=2, column=0, padx=5, pady=5)
            pet_gender = Entry(root, width=30)
            pet_gender.grid(row=2, column=1, padx=20, pady=5)
            pet_gender.insert(0, pet[3])  

            pet_breed_label = Label(root, text="Breed: ", font=(10))
            pet_breed_label.grid(row=3, column=0, padx=5, pady=5)
            pet_breed = Entry(root, width=30)
            pet_breed.grid(row=3, column=1, padx=20, pady=5)
            pet_breed.insert(0, pet[4])  

            vacc_label = Label(root, text="Last Vaccine Date: ", font=(10))
            vacc_label.grid(row=4, column=0, padx=5, pady=5)
            vaccine_dateEntry = Entry(root, width=30)
            vaccine_dateEntry.grid(row=4, column=1, padx=20, pady=5)
            vaccine_dateEntry.insert(0, pet[5])

            looks_label = Label(root, text="Looks Description: ", font=(10))
            looks_label.grid(row=5, column=0, padx=5, pady=5)
            looks_descripEntry = Entry(root, width=30)
            looks_descripEntry.grid(row=5, column=1, padx=20, pady=5)
            looks_descripEntry.insert(0, pet[6]) 

            update_button = Button(root, text="Update Information", command=lambda: update_pet_info(pet_id, pet_name_entry, pet_ageEntry, pet_gender, pet_breed, vaccine_dateEntry,looks_descripEntry), fg="black", bg="lightblue", width=20, height=2)
            update_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
            exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange")
            exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        else:
            messagebox.showwarning("Not Found", "Pet with this ID does not exist.")
            asking_id_for_edit()
        conn.close()
    except Exception as k:
        print("Error fetching pet info:", k)

def update_pet_info(pet_id, pet_name_entry, pet_ageEntry, pet_gender, pet_breed, vaccine_dateEntry, looks_descripEntry):
    new_pet_name = pet_name_entry.get()
    new_pet_age = pet_ageEntry.get()
    new_pet_gender = pet_gender.get()
    new_pet_breed = pet_breed.get()
    new_vaccine_date = vaccine_dateEntry.get()
    new_looks_descrip = looks_descripEntry.get()

    if not new_pet_name or not new_pet_age or not new_pet_gender or not new_pet_breed or not new_vaccine_date or not new_looks_descrip:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    try:
        conn = sqlite3.connect('pets.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE pets
                          SET pet_name=?, pet_age=?, pet_gender=?, pet_breed=?, vaccine_date=?, looks_descrip=?
                          WHERE pet_id=?''', 
                          (new_pet_name, new_pet_age, new_pet_gender, new_pet_breed, new_vaccine_date, new_looks_descrip, pet_id))
        
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Update Failed", "No pet was updated. Ensure the Pet ID exists.")
        else:
            messagebox.showinfo("Pet Info Updated", f"Pet {new_pet_name} updated successfully.")
        conn.close()
        menu()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update pet info: {e}")

def viewPets():
    clear_screen()
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.pet_id, p.pet_name, p.pet_age, p.pet_gender, p.pet_breed, 
               p.vaccine_date, p.looks_descrip, p.adopted,
               h.health_status, h.vitamins, h.weight, h.height, h.adoption_fee
        FROM pets p
        LEFT JOIN health h ON p.pet_id = h.pet_id
    """)
    pets = cursor.fetchall()
    conn.close()
    
    if not pets:
        messagebox.showinfo("No Pets", "No pets available for adoption.")
        menu()
        return
    
    unique_pets = {}
    for pet in pets:
        pet_id = pet[0]  # pet_id is the first column in the pet tuple
        if pet_id not in unique_pets:
            unique_pets[pet_id] = pet  # Store pet details with pet_id as the key
    
    # Convert dictionary values back to a list of pets
    unique_pets_list = list(unique_pets.values())
    
    canvas = Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=4, sticky="ns", padx=(0, 10), pady=10)
    canvas.configure(yscrollcommand=scrollbar.set)
    pet_frame = Frame(canvas)
    canvas.create_window((0, 0), window=pet_frame, anchor="nw")
    
    row = 0
    for pet in unique_pets_list:
        pet_id, pet_name, pet_age, pet_gender, pet_breed, vaccine_date, looks_description, adoption_status, health_status, vitamins, weight, height , adoption_fee = pet
        pet_info = f"""Pet ID: {pet_id}
Pet Name              : {pet_name}
Age                        : {pet_age}
Gender                  : {pet_gender}
Breed                    : {pet_breed}
Vaccine Date       : {vaccine_date}
Looks                    : {looks_description}
Adoption Status   : {adoption_status}
Health Status        : {health_status if health_status else "Not Available"}
Vitamins                : {vitamins if vitamins else "Not Available"}
Weight                   : {weight if weight else "Not Available"}
Height                    : {height if height else "Not Available"}
Adoption Fee        : {adoption_fee}
"""
        Label(pet_frame, text=pet_info, font=("Arial", 12), anchor="w", justify="left").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        row += 1
    pet_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2).grid(row=row, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def mark_adopted():
    clear_screen()
    petID_Entry = Entry(root, width=30, font=11)
    petID_Entry.grid(row=0, column=1, padx=20, pady=5)

    petID_label = Label(root, text="ID number to Mark as Adopted: ", font=11)
    petID_label.grid(row=0, column=0, padx=10, pady=5)
   
    markAdopt_button = Button(root, text="Adopt", command=lambda: markASadopt_pet(petID_Entry), fg="black", bg="lightblue", height=2)
    markAdopt_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def markASadopt_pet(petID_Entry):
    try:
        pet_id = int(petID_Entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid pet ID number.")
        return
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets WHERE pet_id=?", (pet_id,))
    pet = cursor.fetchone()

    if pet:
        if pet[5] == 'Adopted':
            messagebox.showinfo("Already Adopted", f"Pet {pet[1]} has already been adopted.")
        else:
            cursor.execute("UPDATE pets SET adopted='Adopted' WHERE pet_id=?", (pet_id,))
            conn.commit()
            messagebox.showinfo("Success", f"Pet {pet[1]} has been adopted!")
    else:
        messagebox.showerror("Not Found", "Pet ID not found.")
    conn.close()

def delete_markAdopt():
    clear_screen()
    _petID_Entry = Entry(root, width=30, font=11)
    _petID_Entry.grid(row=0, column=1, padx=20, pady=5)
    _petID_label = Label(root, text="ID number to mark as Available: ", font=11)
    _petID_label.grid(row=0, column=0, padx=10, pady=5)
   
    markAvailable_button = Button(root, text="Available", command=lambda: markAvail(_petID_Entry), fg="black", bg="lightgreen", height=2)
    markAvailable_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def markAvail(_petID_Entry):
    try:
        pet_id = int(_petID_Entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid pet ID number.")
        return
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets WHERE pet_id=?", (pet_id,))
    pet = cursor.fetchone()

    if pet:
        if pet[5] == 'Available':
            messagebox.showinfo("Still Available", f"Pet {pet[1]} is still available for adoption.")
        else:
            cursor.execute("UPDATE pets SET adopted='Available' WHERE pet_id=?", (pet_id,))
            conn.commit()
            messagebox.showinfo("Success", f"Pet {pet[1]} has been marked as Available!")
    else:
        messagebox.showerror("Not Found", "Pet ID not found.")
    conn.close()

def deletePet():
    clear_screen()
    pet_idd = Entry(root, width=30, font=11)
    pet_idd.grid(row=0, column=1, padx=20, pady=5)
    f_name_label = Label(root, text="ID number of pet to delete: ", font=11)
    f_name_label.grid(row=0, column=0, padx=10, pady=5)

    delete_button = Button(root, text="Delete Pet", command=lambda: confirm_delete(pet_idd), fg="black", bg="red", height=2)
    delete_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=40)

    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

def confirm_delete(pet_idd):
    pet_id_input = pet_idd.get().strip()
    if not pet_id_input:
        messagebox.showerror("Error", "Please enter a valid pet ID.")
        return
    try:
        pet_id = int(pet_id_input)
    except ValueError:
        messagebox.showerror("Error", "Invalid ID format. Please enter a numeric ID.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets WHERE pet_id=?", (pet_id,))
    pet = cursor.fetchone()

    if pet:
        response = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the pet with ID: {pet_id}?")
        if response:
            cursor.execute("DELETE FROM pets WHERE pet_id=?", (pet_id,))
            # Reset AUTOINCREMENT counter after deleting the pet
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='pets'")
            conn.commit()
            messagebox.showinfo("Success", f"Successfully deleted the pet with ID: {pet_id}")
            delete_health_info()
        else:
            messagebox.showinfo("Cancelled", "Pet deletion cancelled.")
    else:
        messagebox.showerror("Error", "Pet ID not found.")
    conn.close()

def delete_health_info():
    clear_screen()
    health_idd = Entry(root, width=30, font=11)
    health_idd.grid(row=0, column=1, padx=20, pady=5)
    
    f_name_label = Label(root, text="Health History ID to delete: ", font=11)
    f_name_label.grid(row=0, column=0, padx=10, pady=5)

    delete_button = Button(root, text="Delete Health Record", 
                           command=lambda: confirm_delete_health_info(health_idd), 
                           fg="black", bg="orange", height=2)
    delete_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=40)

    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

def confirm_delete_health_info(health_idd):
    health_id_input = health_idd.get().strip()
    if not health_id_input:
        messagebox.showerror("Error", "Please enter a valid health ID.")
        return
    try:
        health_id = int(health_id_input)
    except ValueError:
        messagebox.showerror("Error", "Invalid ID format. Please enter a numeric ID.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health WHERE health_id=?", (health_id,))
    health_info = cursor.fetchone()

    if health_info:
        response = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the health record with ID: {health_id}?")
        if response:
            cursor.execute("DELETE FROM health WHERE health_id=?", (health_id,))
            conn.commit()
            messagebox.showinfo("Success", f"Successfully deleted the health record with ID: {health_id}")
        else:
            messagebox.showinfo("Cancelled", "Health record deletion cancelled.")
    else:
        messagebox.showerror("Error", "Health record ID not found.")
    
    conn.close()
    menu()  

def deleteAdopter():
    clear_screen()
    adopter_id_entry = Entry(root, width=30,font=11)
    adopter_id_entry.grid(row=0, column=1, padx=20, pady=5)
    adopter_id_label = Label(root, text="ID number of adopter to delete: ", font=11)
    adopter_id_label.grid(row=0, column=0, padx=10, pady=5)
   
    delete_button = Button(root, text="Delete Adopter", command=lambda: confirm_delete_adopter(adopter_id_entry), fg="black", bg="red",height=2)
    delete_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=30)
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=55)

def viewAdopters():
    clear_screen()  
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    # JOIN query to fetch adopter and pet information
    cursor.execute("""
        SELECT adopters.*, pets.pet_name FROM adopters
        JOIN pets ON adopters.pet_id = pets.pet_id
    """)
    adopters = cursor.fetchall()
    conn.close()

    if not adopters:
        messagebox.showinfo("No Adopters", "No adopters available.")
        menu()
        return

    canvas = Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=4, sticky="ns", padx=(0, 10), pady=10)
    canvas.configure(yscrollcommand=scrollbar.set)
    adopter_frame = Frame(canvas)
    canvas.create_window((0, 0), window=adopter_frame, anchor="nw")

    row = 0
    for adopter in adopters:
        adopter_info = f"""
        Adopter ID      : {adopter[0]}
        First Name      : {adopter[1]}
        Last Name      : {adopter[2]}
        Age                  : {adopter[3]}
        Address          : {adopter[4]}
        Contact            : {adopter[5]}
        Valid ID           : {adopter[6]}
        Adopted Pet   : {adopter[7]}
        """

        adopter_label = Label(adopter_frame, text=adopter_info, font=("Arial", 12), anchor="w", justify="left")
        adopter_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        row += 1
    adopter_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    exitbutton = Button(root, text="Menu", command=menu, fg="black", bg="orange", height=2)
    exitbutton.grid(row=row, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def confirm_delete_adopter(adopter_id_entry):
    adopter_id_input = adopter_id_entry.get().strip()
    if not adopter_id_input:
        messagebox.showerror("Error", "Please enter a valid adopter ID.")
        return
    try:
        adopter_id = int(adopter_id_input)
    except ValueError:
        messagebox.showerror("Error", "Invalid ID format. Please enter a numeric ID.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM adopters WHERE adopter_id=?", (adopter_id,))
    adopter = cursor.fetchone()

    if adopter:
        response = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the adopter with ID: {adopter_id}?")
        if response:
            cursor.execute("DELETE FROM adopters WHERE adopter_id=?", (adopter_id,))
            conn.commit()
            messagebox.showinfo("Success", f"Successfully deleted the adopter with ID: {adopter_id}")
        else:
            messagebox.showinfo("Cancelled", "Adopter deletion cancelled.")
    else:
        messagebox.showerror("Error", "Adopter ID not found.")
    conn.close()
    menu() 

def user():
    clear_screen()
    button_widthh = 33 
    button_heightt = 2  

    user_viewbutton = Button(root, text="View Pets",font=("Arial", 12), command=user_viewPets, fg="black", bg="violet", width=button_widthh, height=button_heightt)
    user_viewbutton.grid(row=8, column=0, columnspan=2, pady=15, padx=10)
    user_adopt_button = Button(root, text="Adopt Pet",font=("Arial", 12), command=user_adopt, fg="black", bg="lightblue", width=button_widthh, height=button_heightt)
    user_adopt_button.grid(row=10, column=0, columnspan=2, pady=15, padx=10)
    commitmentkbutton = Button(root, text="Fur Parents Commitment (MUST READ)",command=commitment,font=("Arial", 12), fg="black", bg="lightgreen", height=button_heightt)
    commitmentkbutton.grid(row=8, column=2, columnspan=2, pady=15, padx=10)
    backbutton = Button(root, text="Back", command=main_menu,font=("Arial", 12), fg="black", bg="orange", width=button_widthh, height=button_heightt)
    backbutton.grid(row=10, column=2, columnspan=2, pady=15, padx=10)

def user_viewPets():
    clear_screen()
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.pet_id, p.pet_name, p.pet_age, p.pet_gender, p.pet_breed, 
               p.vaccine_date, p.looks_descrip, p.adopted, 
               h.health_status, h.vitamins, h.weight, h.height, h.adoption_fee
        FROM pets p
        LEFT JOIN health h ON p.pet_id = h.pet_id
    """)
    pets = cursor.fetchall()
    conn.close()

    if not pets:
        messagebox.showinfo("No Pets", "No pets available for adoption.")
        ()
        return

    canvas = Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=4, sticky="ns", padx=(0, 10), pady=10)
    canvas.configure(yscrollcommand=scrollbar.set)
    pet_frame = Frame(canvas)
    canvas.create_window((0, 0), window=pet_frame, anchor="nw")

    row = 0
    for pet in pets:
        health_status = pet[8] if pet[8] else "No health status available"
        vitamins = pet[9] if pet[9] else "No vitamin info available"
        weight = pet[10] if pet[10] else "No weight info available"
        height = pet[11] if pet[11] else "No height info available"
        adoption_fee = pet[12] if pet[12] else "No Fee available"

        pet_info = f"""Pet ID: {pet[0]}
Pet Name              : {pet[1]}
Age                        : {pet[2]}
Gender                  : {pet[3]}
Breed                    : {pet[4]}
Vaccine Date       : {pet[5]}
Looks                    : {pet[6]}
Adoption Status   : {pet[7]}
Health Status        : {health_status}
Vitamins                : {vitamins}
Weight                   : {weight}
Height                    : {height}
Adoption Fee        : {adoption_fee}
"""
        Label(pet_frame, text=pet_info, font=("Arial", 12), anchor="w", justify="left").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        row += 1

    pet_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    Button(root, text="Menu", command=user, fg="black", bg="orange", height=2).grid(row=row, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def user_adopt():
    clear_screen()
    petID_Entry = Entry(root, width=30, font=11)
    petID_Entry.grid(row=0, column=1, padx=20, pady=5)

    petID_label = Label(root, text="ID number you want to adopt: ", font=11)
    petID_label.grid(row=0, column=0, padx=10, pady=5)
  
    markAdopt_button = Button(root, text="Adopt", command=lambda: user_adopt_pet (petID_Entry), fg="black", bg="lightgreen",height=2)
    markAdopt_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    exitbutton = Button(root, text="Menu", command=user, fg="black", bg="orange",height=2)
    exitbutton.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def user_adopt_pet(petID_Entry):
    try:
        pet_id = int(petID_Entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid pet ID number.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets WHERE pet_id=?", (pet_id,))
    pet = cursor.fetchone()

    if pet:
        if pet[7] == 'Adopted':  # Assuming the adoption status is stored at index 7
            messagebox.showinfo("Already Adopted", f"Pet {pet[1]} has already been adopted. Please enter another Pet ID.")
            petID_Entry.delete(0, 'end')
        else:
            confirm_adopt = messagebox.askyesno("Confirm Adoption", f"Are you sure you want to adopt {pet[1]}?")
            if confirm_adopt:
                cursor.execute("UPDATE pets SET adopted='Adopted' WHERE pet_id=?", (pet_id,))
                conn.commit() 
                # After adopting the pet, prompt user to fill in their information
                userInfo(pet_id)  # Pass the pet_id to link it to the adopter
                messagebox.showinfo("Success", f"Pet {pet[1]} has been adopted!")
            else:
                messagebox.showinfo("Adoption Cancelled", "Adoption process has been cancelled.")
    else:
        messagebox.showerror("Not Found", "Pet ID not found.")
    conn.close()

def save_user_info(fname, lnameEntry, agee, user_address, contact_User, user_ValidID, pet_id):
    name = fname.get()
    l_name = lnameEntry.get()
    age = agee.get()
    address = user_address.get()
    contact_number = contact_User.get()
    valid_id = user_ValidID.get()
   
    if not name or not l_name or not age or not address or not contact_number or not valid_id:
        messagebox.showerror("Error", "All fields must be filled out.")
        return
   
    if not contact_number.isdigit() :
        messagebox.showerror("Error", "Contact number must be numeric.")
        return

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO adopters (name, l_name, age, address, contact_number, valid_id, pet_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (name, l_name, age, address, contact_number, valid_id, pet_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Thank you for using our Pet Adoption System, the FURever Homes. \n" 
        "\nPlease wait to process your Adoption application. Kindly check time to time for evaluation and Final Agreements.We will call you for the schedule of your visit and the additional requirements you need to bring. Once again, THANK YOU  FUR PARENTS! ")
    user()

def userInfo(pet_id):
    clear_screen()

    user_name = Label(root, text="First Name: ", font=(10))
    user_name.grid(row=0, column=0, padx=5, pady=5)
    fname = Entry(root, width=30)
    fname.grid(row=0, column=1, padx=20, pady=5)
    
    lname = Label(root, text="Last Name: ", font=(10))
    lname.grid(row=1, column=0, padx=5, pady=5)
    lnameEntry = Entry(root, width=30)
    lnameEntry.grid(row=1, column=1, padx=20, pady=5)

    age_label = Label(root, text="Age: ", font=(10))
    age_label.grid(row=2, column=0, padx=5, pady=5)
    agee = Entry(root, width=30)
    agee.grid(row=2, column=1, padx=20, pady=5)

    User_adress = Label(root, text="Address: ", font=(10))
    User_adress.grid(row=3, column=0, padx=5, pady=5)
    user_address = Entry(root, width=30)
    user_address.grid(row=3, column=1, padx=20, pady=5)

    user_contact = Label(root, text="Contact Number: ", font=(10))
    user_contact.grid(row=4, column=0, padx=5, pady=5)
    contact_User = Entry(root, width=30)
    contact_User.grid(row=4, column=1, padx=20, pady=5)

    user_validID = Label(root, text="Any Valid ID number: ", font=(10))
    user_validID.grid(row=5, column=0, padx=5, pady=5)
    user_ValidID = Entry(root, width=30)
    user_ValidID.grid(row=5, column=1, padx=20, pady=5)

    button_width = 20
    button_height = 2 
    add_button = Button(root, text="Apply", command=lambda: save_user_info(fname, lnameEntry, agee, user_address, contact_User, user_ValidID, pet_id), fg="black", bg="lightgreen", width=button_width, height=button_height)
    add_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
    exitbutton = Button(root, text="Menu", command=user, fg="black", bg="orange", width=button_width, height=button_height)
    exitbutton.grid(row=8, column=0, columnspan=2, pady=10, padx=10)

def commitment():
    clear_screen()
    widthh = 200  
    heightt = 23  
    commitmentt = Label(root, text="What to Consider When Adopting Pets from Shelters When choosing a pet from adoption shelters, it is        \n"
    "important to consider these factors to prepare yourself before taking them into their new home with you\n\n"
    "COST: Pets can be expensive. You will need to factor in the cost of pet food, pet treats, toys, veterinary care   \n"
    ",and other supplies. Be ready for the financial responsibility of pet ownership including food,\n"
    "grooming, vet care, and unexpected expenses.\n\n"
    "COMMITMENT: Be prepared for a long-term commitment, as most pets can live for many years. Make sure       \n"
    "you're ready for the financial and time commitments required to care for a pet.\n\n"
    "FAMILY AND LIFESTYLE: Consider your living situation. Think about your daily routine and how much time     \n"
    "you can dedicate to a pet. Determine what size, breed, and age of the pet would best suit your\n"
    "lifestyle and preferences. Consider any allergies or phobias you or your family members may have. \n\n"
    "COMPATIBILITY:Consider the compatibility of the pet with you,your family members, other pets, and children.  \n\n "
    "TRAINING AND SOCIALIZATION: Be prepared to invest time in training and socializing your new pet                  \n"
    "especially if they have behavioral issues or if they are young."
    "Adopting a pet is a significant decision \nthat comes with responsibilities and rewards. When done "
    "thoughtfully and with care, it can lead to a loving and \nfulfilling relationship between you and your "
    "new furry friend. ", font=("Arial", 10, "bold"),width=widthh, height=heightt,anchor="w")
    commitmentt.grid(row=1, column=0, padx=20, pady=5)

    backbutton = Button(root, text="Back", command=agree_comitment,font=("Arial", 12), fg="black", bg="orange",width=25, height=2)
    backbutton.grid(row=9, column=0)

def agree_comitment():
    responsee = messagebox.askyesno("AGREE FOR COMMITMENT", f"DO YOU UNDERSTAND THE CONSIDERATION OF ADOPTING PETS?")
    if responsee:
        messagebox.showinfo("Success", f"You can now choose a pet, Fur Parent")
        user()
    else:
        messagebox.showinfo("Cancelled", "Please understand it first before adopting pet")

init_db()
main_menu()
root.mainloop()

