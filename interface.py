import customtkinter as ct
from main import main

# Initialize main instance
m = main()
m.stemStopWords()
m.buildInvertedIndex()

def clear_previous_results():
    # Clear previous result label
    result_label.configure(text="")

def results(event=None):  # Modified to accept event argument for binding to Enter key
    clear_previous_results()
    val = query_var.get().strip()  # Get the value from the entry widget
    if val:  # Check if query is not empty
        result = m.UserQuery(val)
        # Update the result label with the new result
        result_label.configure(text="Document: {}".format(result))

# Create the CustomTkinter App
ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")
app = ct.CTk()
app.geometry("720x480")
app.title("Boolean Retrieval Search")

# Define font styles
larger_font = ('Comfortaa', 18)
smaller_font = ('Arial', 12)

# Create and format labels
title_frame = ct.CTkFrame(app)
title_frame.pack(fill="x")
title_label = ct.CTkLabel(title_frame, text="Boolean Retrieval Search", font=larger_font)

title_label.pack(padx=10, pady=10)
ct.CTkLabel(app, text="K214889 - Muhammad Qasim Alias Haseeb", font=smaller_font).pack(padx=10, pady=2)
ct.CTkLabel(app, text="-> Boolean Priorities: NOT >> AND >> OR", font=smaller_font).pack(padx=10, pady=2, anchor="w")
ct.CTkLabel(app, text="-> Proximity Query Format: \' t1 t2 /k\ ', k can have slight variations, try different values.  ", font=smaller_font).pack(padx=10, pady=2, anchor="w")
ct.CTkLabel(app, text="-> Total Tokens: {}".format(m.total_tokens), font=smaller_font).pack(padx=10, pady=2, anchor="w")
ct.CTkLabel(app, text="-> Total Terms: {}".format(m.total_terms), font=smaller_font).pack(padx=10, pady=2, anchor="w")
ct.CTkLabel(app, text=f"-> Tokens Dropped: %.2f"%m.droppedP+"%", font=smaller_font).pack(padx=10, pady=2, anchor="w")
ct.CTkLabel(app, text="Enter Boolean Query", font=larger_font).pack(padx=10, pady=7)

# Create and format the search bar
query_var = ct.StringVar()
query = ct.CTkEntry(app, width=350, textvariable=query_var, font=smaller_font)
query.pack(padx=10, pady=5)

# Bind the 'results' function to the button click event and Enter key
searchBtn = ct.CTkButton(app, text="Search", command=results)
searchBtn.pack(padx=10, pady=5)
query.bind("<Return>", results)

# Create and format the result label
result_label = ct.CTkLabel(app, text="", font=larger_font)
result_label.pack(padx=10, pady=10, fill="x")

app.mainloop()
