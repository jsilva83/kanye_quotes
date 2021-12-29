from tkinter import *
import requests


def get_quote():
    # Get response from website API.
    a_response = requests.get(url='https://api.kanye.rest/')
    a_response.raise_for_status()
    a_response_json = a_response.json()
    a_quote = a_response_json['quote']
    canvas.itemconfig(quote_text, text=a_quote)
    return


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
# Create a canvas to display the quotes.
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="Kanye Quote Goes HERE",
                                width=250,
                                font=("Arial", 25, "bold"),
                                fill="white"
                                )
canvas.grid(row=0, column=0)
# Create button with Kanye face.
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, borderwidth=0, command=get_quote)
kanye_button.grid(row=1, column=0)
# Wait for events.
window.mainloop()
