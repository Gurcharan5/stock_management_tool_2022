import tkinter as tk

window = tk.Tk()

product_code_text = tk.Label(window, text ="What is the product code?", padx="10px", pady="10px")
product_code_text.grid(column=0, row=0)

sort_code_entry_box = tk.Entry(window, width="20")
sort_code_entry_box.grid(column=1, row=0)

product_description_text = tk.Label(window, text="What is the product description?", padx="10px", pady = "10px")
product_description_text.grid(column=0, row=1)

product_description_entry_box = tk.Entry(window, width="20")
product_description_entry_box.grid(column=1, row=1)

product_price_text = tk.Label(window, text="What is the product price?", padx="10px", pady = "10px")
product_price_text.grid(column=0, row=2)

product_price_entry_box = tk.Entry(window, width="20")
product_price_entry_box.grid(column=1, row = 2)

def append_file_with_details():
    product_catalogue = open("catalogue.txt", "a")
    
    product_code = sort_code_entry_box.get()
    product_code = str(product_code)
    
    product_description = product_description_entry_box.get()
    product_description = str(product_description)
    
    product_price = product_price_entry_box.get()
    product_price = str(product_price)

    product_catalogue.write("Code: " + product_code + " " "\n")
    product_catalogue.write("Description: "+ product_description + " "+ "\n")
    product_catalogue.write("Price: " + product_price + " "+ "\n")
    product_catalogue.write(""+ "\n")

    product_catalogue.close

add_details_to_sheet_buttom = tk.Button(window, command=append_file_with_details , padx="10px", pady="5px", text ="Click me to submit the data")
add_details_to_sheet_buttom.grid(column=3, row=2)

window.mainloop()