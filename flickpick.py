import cohere
import tkinter as tk
from tkinter import messagebox
from decouple import config
import threading
import requests

def checkInternet():
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def getRecommendation(prompt):
    if not checkInternet():
        messagebox.showerror("Error", "Internet connection is not available.")
        return

    try:
        cohereAPIKey = cohere.Client(config("COHERE_KEY"))
        while True:
            response = cohereAPIKey.generate(
                model='command',
                prompt=f'{prompt}\n\nPlease provide the following details in the suggested movie title:\n\n"Movie":\n\n"Release Year":\n\n"IMDB Rating":\n\n"Rotten Tomatoes Rating":\n\n"Directors" (Comma-separated list):\n\n"Actors" (Comma-separated list):\n\n"Studios" (Comma-separated list):\n\n"Distributors" (Comma-separated list):\n\n"Plot" (In no more than 3 lines, and write properly):\n\n---\n\nNow, suggest a movie title that adheres to the specified format, with accurate details. Ensure that all the mentioned fields are named exactly as specified, along with the accurate corresponding values.',
                max_tokens=900,
                temperature=2,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE')
                
            movieData = response.generations[0].text.strip()
            details = extractDetails(movieData)
            if all(details.values()):
                break

        root.after(0, updateDetails, details)
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred while fetching data. Please try again or contact the developer. (Check README.txt for more information)")
    finally:
        root.after(0, enableActions)

def extractDetails(movieData):
    lines = movieData.strip().split('\n')
    details = {}

    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            details[key] = value

    return details

def updateDetails(details):
    movieTitleLabel.config(text="Movie: " + details.get("Movie", ""))
    releaseYearLabel.config(text="Release Year: " + details.get("Release Year", ""))
    imdbRatingLabel.config(text="IMDB Rating: " + details.get("IMDB Rating", "")+"/10")
    rottenTomatoesLabel.config(text="Rotten Tomatoes Rating: " + details.get("Rotten Tomatoes Rating", ""))
    directorsLabel.config(text="Director(s): " + details.get("Directors", ""))
    actorsLabel.config(text="Actor(s): " + details.get("Actors", ""))
    studiosLabel.config(text="Studio(s): " + details.get("Studios", ""))
    distributorsLabel.config(text="Distributor(s): " + details.get("Distributors", ""))
    plotLabel.config(text="Plot: " + details.get("Plot", ""))

def describeMovie():
    disableActions()
    prompt = 'Suggest another real movie based on the following description:\n\n'+inputDescriptionLabel.get()
    threading.Thread(target=getRecommendation, args=(prompt,)).start()

def randomMovie():
    disableActions()
    prompt = 'Surprise me with a real movie I should watch'
    threading.Thread(target=getRecommendation, args=(prompt,)).start()

def checkInput(event):
    if inputDescriptionLabel.get().strip():
        generateButton.config(state="normal")
    else:
        generateButton.config(state="disabled")

def enableActions():
    inputText = inputDescriptionLabel.get().strip()
    generateButton.config(state="normal" if inputText else "disabled")
    randomButton.config(state="normal")
    inputDescriptionLabel.config(state="normal")

def disableActions():
    generateButton.config(state="disabled")
    randomButton.config(state="disabled")
    inputDescriptionLabel.config(state="disabled")

root = tk.Tk()
root.configure(bg='#BEADFA')
root.title("FlickPick")

icon_image = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon_image)

inputLabel = tk.Label(root, text="Tell me what type of movie you'd like to watch and I'd suggest you a title!", font=("Candara", 14), bg='#BEADFA')
inputLabel.grid(row=0, padx=25, pady=(20,5), columnspan=2)

inputDescriptionLabel = tk.Entry(root, width=50, relief="raised", font=("Candara", 14))
inputDescriptionLabel.grid(sticky="we", row=1, padx=25, pady=(5,20), ipady=3, ipadx=3, columnspan=2)
inputDescriptionLabel.bind("<KeyRelease>", checkInput)

generateButton = tk.Button(root, text="Get Suggestion", padx=10, height=2, bg="#FFF8C9", fg="#A75FE3", font=("Candara", 13, "bold"), command=describeMovie)
generateButton.grid(row=3, column=0, padx=5, pady=(5,20))

randomButton = tk.Button(root, text="Surprise Me", padx=10, height=2, bg="#FFF8C9", fg="#A75FE3", font=("Candara", 13, "bold"), command=randomMovie)
randomButton.grid(row=3, column=1, padx=5, pady=(5,20))

movieTitleLabel = tk.Label(root, text="Movie:", font=("Candara", 14), bg='#BEADFA', wraplength=700, justify="left")
movieTitleLabel.grid(sticky='w', row=5, padx=25, pady=5, columnspan=2)

releaseYearLabel = tk.Label(root, text="Release Year:", font=("Candara", 14), bg='#BEADFA', justify="left")
releaseYearLabel.grid(sticky='w', row=6, padx=25, pady=5, columnspan=2)

imdbRatingLabel = tk.Label(root, text="IMDB Rating:", font=("Candara", 14), bg='#BEADFA', justify="left")
imdbRatingLabel.grid(sticky='w', row=7, padx=25, pady=5, columnspan=2)

rottenTomatoesLabel = tk.Label(root, text="Rotten Tomatoes Rating:", font=("Candara", 14), bg='#BEADFA', justify="left")
rottenTomatoesLabel.grid(sticky='w', row=8, padx=25, pady=5, columnspan=2)

directorsLabel = tk.Label(root, text="Directors:", font=("Candara", 14), bg='#BEADFA', wraplength=700, justify="left")
directorsLabel.grid(sticky='w', row=9, padx=25, pady=5, columnspan=2)

actorsLabel = tk.Label(root, text="Actors:", font=("Candara", 14), bg='#BEADFA', wraplength=700, justify="left")
actorsLabel.grid(sticky='w', row=10, padx=25, pady=5, columnspan=2)

studiosLabel = tk.Label(root, text="Studios:", font=("Candara", 14), bg='#BEADFA', wraplength=700, justify="left")
studiosLabel.grid(sticky='w', row=11, padx=25, pady=5, columnspan=2)

distributorsLabel = tk.Label(root, text="Distributors:", font=("Candara", 14), bg='#BEADFA', wraplength=700, anchor='w')
distributorsLabel.grid(sticky='w', row=12, padx=25, pady=5, columnspan=2)

plotLabel = tk.Label(root, text="Plot:", font=("Candara", 14), bg='#BEADFA', wraplength=700, justify="left")
plotLabel.grid(sticky='w', row=13, padx=25, pady=(5,30), columnspan=2)

randomMovie()

root.mainloop()