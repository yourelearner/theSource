import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# Database connection function
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='inventory',
            user='root',
            password=''
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)
        messagebox.showerror("Database Error", "Unable to connect to the database.")
        return None

# Function to register a new user
def register(username, password):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            messagebox.showinfo("Registration Successful", "User registered successfully.")
        except Error as e:
            print(e)
            messagebox.showerror("Database Error", "Failed to register user.")
        finally:
            cursor.close()
            conn.close()

username = ""  # Global variable to store logged-in username

# Function to handle login
def login(username_input, password):
    global username  # Use the global variable username
    if username_input == "" or password == "":
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return

    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username_input, password))
            row = cursor.fetchone()
            if row:
                messagebox.showinfo("Login Successful", "Welcome!")
                username = username_input  # Store the logged-in username globally
                clear_frame()
                show_buttons()
                # Add code here to transition to the main application screen
            else:
                messagebox.showerror("Login Error", "Invalid username or password.")
        except Error as e:
            print(e)
            messagebox.showerror("Database Error", "Failed to login.")
        finally:
            cursor.close()
            conn.close()

# Function to display the login screen
def show_login_screen():
    clear_frame()
    # Your login screen UI code goes here

# Function to display the registration screen
def show_register_screen():
    clear_frame()
    # Your registration screen UI code goes here

# Function to store order in database
def store_order(username, item, price, quantity):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO orders (username, item, price, quantity) VALUES (%s, %s, %s, %s)", (username, item, price, quantity))
            conn.commit()
            print("Order stored successfully in database")
        except Error as e:
            print(e)
            messagebox.showerror("Database Error", "Failed to store order.")
        finally:
            cursor.close()
            conn.close()

def show_login_screen():
    clear_frame()
    login_label = tk.Label(frame, text="Login", font=("Arial", 24, "bold"), bg="#F0E68C", fg="#800000")
    login_label.grid(row=0, column=0, pady=20)

    username_label = tk.Label(frame, text="Username:", font=("Arial", 14), bg="#F0E68C", fg="#800000")
    username_label.grid(row=1, column=0, padx=20, pady=(10, 5))
    username_entry = tk.Entry(frame, width=30, font=("Arial", 12), bd=3, relief=tk.RIDGE)
    username_entry.grid(row=1, column=1, padx=20, pady=(10, 5))

    password_label = tk.Label(frame, text="Password:", font=("Arial", 14), bg="#F0E68C", fg="#800000")
    password_label.grid(row=2, column=0, padx=20, pady=5)
    password_entry = tk.Entry(frame, show='*', width=30, font=("Arial", 12), bd=3, relief=tk.RIDGE)
    password_entry.grid(row=2, column=1, padx=20, pady=5)

    login_button = tk.Button(frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get()), width=15, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
    login_button.grid(row=3, column=1, pady=10)

    register_button = tk.Button(frame, text="Register", command=show_register_screen, width=15, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
    register_button.grid(row=4, column=1, pady=10)    
def show_register_screen():
    clear_frame()
    register_label = tk.Label(frame, text="Register", font=("Arial", 24, "bold"), bg="#F0E68C", fg="#800000")
    register_label.grid(row=0, column=0, pady=20)

    username_label = tk.Label(frame, text="Username:", font=("Arial", 14), bg="#F0E68C", fg="#800000")
    username_label.grid(row=1, column=0, padx=20, pady=(10, 5))
    username_entry = tk.Entry(frame, width=30, font=("Arial", 12), bd=3, relief=tk.RIDGE)
    username_entry.grid(row=1, column=1, padx=20, pady=(10, 5))

    password_label = tk.Label(frame, text="Password:", font=("Arial", 14), bg="#F0E68C", fg="#800000")
    password_label.grid(row=2, column=0, padx=20, pady=5)
    password_entry = tk.Entry(frame, show='*', width=30, font=("Arial", 12), bd=3, relief=tk.RIDGE)
    password_entry.grid(row=2, column=1, padx=20, pady=5)

    register_button = tk.Button(frame, text="Register", command=lambda: register(username_entry.get(), password_entry.get()), width=15, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
    register_button.grid(row=3, column=1, pady=10)

    back_button = tk.Button(frame, text="Back to Login", command=show_login_screen, width=15, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
    back_button.grid(row=4, column=1, pady=10)


# store item
cart = {}

# item prices
prices = {
    "Wintermelon": 120.00,
    "Vanilla": 120.00,
    "Okinawa": 120.00,
    "Red Velvet": 120.00,
    "Cookies & Cream": 120.00,
    "Chocolate": 120.00,
    "Dark Chocolate": 120.00,
    "Java Chip": 130.00,
    "Hokkaido": 120.00,
    "Matcha": 100.00,
    "Fructose (Sugar)": 100.00,
    "Flavored Syrups": 150.00,
    "Jams":90.00,
    "Cups with Lid": 100.00,
    "Tea Barrel": 100.00,
    "Sealer Machine": 500.00,
    "Tapioca Pearl": 100.00,
    "tubig": 100.00,
    "water": 50.00,
    "purified water": 100.00
}

# balik ng mga buttons and stuff
def order_again():
    # Reset cart
    cart.clear()
    clear_frame()
    show_buttons()
    

        
#hide ng buttons pag submit ng order 
def hide_buttons():
    solid.place_forget()
    liquid.place_forget()
    cart_button.place_forget()
    
#balik ng mga buttons para sa order again
def show_buttons():
    solid.place(x=320, y=580, anchor='se')
    liquid.place(x=620, y=580, anchor='se')
    cart_button.place(x=920, y=580, anchor='se')
    
#items
solid_buttons = ["Wintermelon", "Vanilla", "Okinawa", "Red Velvet", "Cookies & Cream", "Chocolate", "Dark Chocolate", "Java Chip", "Hokkaido", "Matcha"]
liquid_buttons = ["Fructose (Sugar)", "Flavored Syrups", "Jams", "Cups with Lid", "Tea Barrel", "Sealer Machine", "Tapioca Pearl", "tubig", "water", "purified water"]

#flavored items functions 
def solidReveal():
    clear_frame()
    for i in range(len(solid_buttons)):
        item = solid_buttons[i]
        # frame para sa items
        row_frame = tk.Frame(frame, bg="#F0E68C", highlightbackground="#800000", highlightthickness=2, bd=0, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
        row_frame.grid(row=i, column=0, sticky="ew")

        # item buttons
        main_button = tk.Button(row_frame, text=solid_buttons[i], width=25, height=2, bg="#800000", fg="#F0E68C", font=("Arial", 12, "bold"), bd=3, relief=tk.RAISED, pady=5)
        main_button.pack(side="left", padx=(10, 20))
        
         # Price label
        price_label = tk.Label(row_frame, text=f"₱{prices[item]:.2f}", width=10, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
        price_label.pack(side="left", padx=(0, 10))

        # para mag sipag right side yung minus plus addtocart
        right_frame = tk.Frame(row_frame, bg="#F0E68C")
        right_frame.pack(side="right", padx=(0, 10))

        # Minus button
        number_label = tk.Label(right_frame, text="0", width=3, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
        minus_button = tk.Button(right_frame, text="-", command=lambda label=number_label: button_action(-1, label), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        minus_button.pack(side="left", padx=(222, 0))

        # Number display
        number_label.pack(side="left", padx=5)

        # Plus button
        plus_button = tk.Button(right_frame, text="+", command=lambda label=number_label: button_action(1, label), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        plus_button.pack(side="left")

        # Add to Cart button
        add_to_cart_button = tk.Button(right_frame, text="Add to Cart", command=lambda label=number_label, item=solid_buttons[i]: add_to_cart(item, label), width=10, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        add_to_cart_button.pack(side="left", padx=(10, 0))

        # command para sa main button
        main_button.config(command=lambda label=number_label: button_action(0, label))

#liquid items funtions
def liquidReveal():
    clear_frame()
    for i in range(len(liquid_buttons)):
        item = liquid_buttons[i]
        # frame para sa items
        row_frame = tk.Frame(frame, bg="#F0E68C", highlightbackground="#800000", highlightthickness=2, bd=0, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
        row_frame.grid(row=i, column=0, sticky="ew")

        # item buttons
        main_button = tk.Button(row_frame, text=liquid_buttons[i], width=25, height=2, bg="#800000", fg="#F0E68C", font=("Arial", 12, "bold"), bd=3, relief=tk.RAISED, pady=5)
        main_button.pack(side="left", padx=(10, 20))
        
         # Price label
        price_label = tk.Label(row_frame, text=f"₱{prices[item]:.2f}", width=10, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
        price_label.pack(side="left", padx=(0, 10))

        # para mag sipag right side yung minus plus addtocart
        right_frame = tk.Frame(row_frame, bg="#F0E68C")
        right_frame.pack(side="right", padx=(0, 10))

        # Minus button
        number_label = tk.Label(right_frame, text="0", width=3, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
        minus_button = tk.Button(right_frame, text="-", command=lambda label=number_label: button_action(-1, label), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        minus_button.pack(side="left", padx=(222, 0))

        # Number display
        number_label.pack(side="left", padx=5)

        # Plus button
        plus_button = tk.Button(right_frame, text="+", command=lambda label=number_label: button_action(1, label), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        plus_button.pack(side="left")

        # Add to Cart button
        add_to_cart_button = tk.Button(right_frame, text="Add to Cart", command=lambda label=number_label, item=liquid_buttons[i]: add_to_cart(item, label), width=10, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
        add_to_cart_button.pack(side="left", padx=(10, 0))

        # command para sa main button
        main_button.config(command=lambda label=number_label: button_action(0, label))

#cart function
def cart_items():
    clear_frame()
    total_cost = 0.0
    for i, (item, quantity) in enumerate(cart.items()):
        if quantity > 0:
            row_frame = tk.Frame(frame, bg="#F0E68C", highlightbackground="#800000", highlightthickness=2, bd=0, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
            row_frame.grid(row=i, column=0, sticky="ew")

            item_label = tk.Label(row_frame, text=item, width=25, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            item_label.pack(side="left", padx=(5, 20))

            price_label = tk.Label(row_frame, text=f"₱{prices[item]:.2f}", width=10, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            price_label.pack(side="left", padx=(0, 20))

            minus_button = tk.Button(row_frame, text="-", command=lambda item=item: modify_cart(item, -1), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
            minus_button.pack(side="left", padx=(305,0))

            quantity_label = tk.Label(row_frame, text=str(quantity), width=5, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            quantity_label.pack(side="left", padx=5)

            plus_button = tk.Button(row_frame, text="+", command=lambda item=item: modify_cart(item, 1), width=5, height=2, bg="#800000", fg="#F0E68C", bd=3, relief=tk.RAISED)
            plus_button.pack(side="left")

            total_cost += prices[item] * quantity

            # Display total cost
            total_label = tk.Label(frame, text=f"Total Cost: ₱{total_cost:.2f}", bg="#F0E68C", fg="#800000", font=("Arial", 14, "bold"))
            total_label.grid(row=len(cart.items()), column=0, pady=10)
            
            submit_order_button = tk.Button(frame, text="Submit Order", command=show_submit_panel, width=25, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
            submit_order_button.grid(row=len(cart.items()) + 1, column=0, pady=10)
            
#resibo after ng submit order
def show_submit_panel():
    global username  # Use the global variable username
    clear_frame()
    total_cost = 0.0
    for i, (item, quantity) in enumerate(cart.items()):
        if quantity > 0:
            row_frame = tk.Frame(frame, bg="#F0E68C", highlightbackground="#800000", highlightthickness=2, bd=0, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
            row_frame.grid(row=i, column=0, sticky="ew")

            item_label = tk.Label(row_frame, text=item, width=25, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            item_label.pack(side="left", padx=(5, 20))

            price_label = tk.Label(row_frame, text=f"₱{prices[item]:.2f}", width=10, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            price_label.pack(side="left", padx=(0, 20))

            quantity_label = tk.Label(row_frame, text=str(quantity), width=5, height=2, bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"))
            quantity_label.pack(side="left", padx=(390, 20))

            store_order(username, item, prices[item], quantity)

            total_cost += prices[item] * quantity

    total_label = tk.Label(frame, text=f"Total Cost: ₱{total_cost:.2f}", bg="#F0E68C", fg="#800000", font=("Arial", 14, "bold"))
    total_label.grid(row=len(cart.items()), column=0, pady=10)

    order_again_button = tk.Button(frame, text="Order Again", command=order_again, width=25, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, relief=tk.FLAT, highlightthickness=2)
    order_again_button.grid(row=len(cart.items()) + 1, column=0, pady=10)

    hide_buttons()
            


#clear ng frame
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
        
#para sa quantity
def button_action(num, label):
    current_value = int(label["text"])
    new_value = current_value + num
    if new_value >= 0:
        label["text"] = str(new_value)

#notif pag na add to cart
def show_notification(message):
    notification_label.config(text=message)
    notification_label.place(relx=0.5, rely=0.1, anchor="center")
    root.after(1500, hide_notification)

#pag hide ng notif
def hide_notification():
    notification_label.place_forget()

#label ng notif kada add to cart
def add_to_cart(item, label):
    quantity = int(label["text"])
    if quantity > 0:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} of {item} to cart")
        show_notification(f"{quantity} of {item} added to cart")
        label.config(text="0")

#modify ng items sa cart
def modify_cart(item, amount):
    if item in cart:
        cart[item] += amount
        if cart[item] <= 0:
            del cart[item]
            
        cart_items()

# window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    root.title("The Source (Milktea Supplies)")
    root.configure(bg="#F0E68C")
    root.resizable(False, False)

#image logo
try:
    image_path = "logo (1).png"
    img = tk.PhotoImage(file=image_path)
    image_label = tk.Label(root, image=img, bg="#F0E68C")
    image_label.place(relx=0.5, y=50, anchor="center")
except tk.TclError:
    print(f"Image file '{image_path}' not found or not supported.")

# buttons sa baba
solid = tk.Button(root, text="Flavored Powder", command=solidReveal, width=25, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, borderwidth=2, relief=tk.FLAT, highlightthickness=2)
liquid = tk.Button(root, text="Others", command=liquidReveal, width=25, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, borderwidth=2, relief=tk.FLAT, highlightthickness=2)
cart_button = tk.Button(root, text="Cart", command=cart_items, width=25, height=2, bg="#800000", fg="#F0E68C", font=("Times New Roman", 12, "bold"), bd=3, borderwidth=2, relief=tk.FLAT, highlightthickness=2)


# Notification label
notification_label = tk.Label(root, text="", bg="#F0E68C", fg="#800000", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", highlightbackground="red", highlightthickness=1)

# panel para sa laman ng solid tsaka liquid button
canvas = tk.Canvas(root, bg="#F0E68C")
frame = tk.Frame(canvas, bg="#F0E68C")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor='nw')

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# center the panel
canvas.place(relx=0.5, rely=0.5, anchor="center", width=900, height=400)

show_login_screen()
root.mainloop()
