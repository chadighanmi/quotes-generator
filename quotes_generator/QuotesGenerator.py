import tkinter as tk
from typing import Text
import requests
from threading import Thread

api = "http://api.quotable.io/random"
quotes = []
quote_number = 0

window = tk.Tk()
window.geometry("1280x720")
window.title("Quotes Generator")
window.grid_columnconfigure(0, weight=1)
window.configure(bg="lightblue")


def loading_quotes():
    global quotes

    print("More Quotes Are Loading...")
    for i in range(10):
        new_quote = requests.get(api).json()
        content = new_quote["content"]
        author = new_quote["author"]
        quote = content + "\n\n" + "By " + author
        print(content)

        quotes.append(quote)
    
    print("Quotes Are Loaded !")

loading_quotes()

def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number += 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target= loading_quotes)
        thread.start()

# User Interface

quote_label = tk.Label(window, text="Click Below to generate a random quote !",
                        height=28,
                        pady=10,
                        wraplength=800,
                        font=("Helvetica", 14))

quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Generate", command=get_random_quote, bg="#0052cc", fg="#ffffff", 
                    activebackground="lightblue", font=("Helvetica", 14))

button.grid(row=1, column=0, stick="WE", padx=20, pady=10)


# Keeps the window always open (infinite loop)
if __name__ == "__main__":
    window.mainloop()