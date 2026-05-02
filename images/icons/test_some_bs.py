import customtkinter



def segmented_button_callback(value):
    print(segemented_button.get())

app = customtkinter.CTk()



segemented_button = customtkinter.CTkSegmentedButton(app, values=["Cº", "Fº"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 1")

segemented_button.pack()

app.mainloop()