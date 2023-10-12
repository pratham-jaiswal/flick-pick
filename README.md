# FlickPick - Movie Recommendation App
FlickPick is a user-friendly movie recommendation application developed using Python and powered by the [Cohere's AI](https://cohere.com/). This app helps you discover movie titles by generating suggestions based on your input descriptions. It also offers the option to receive a random movie recommendation, ensuring that you always have exciting viewing options.

## Use Case
- Provides a movie recommendation service based on the type of movie a user wants to watch.
- Plan movie nights with friends or family.

## Features
- Choose between the *Classic Mode* and *Memory Mode*.
    - ***Classic Mode*** - uses [Cohere's Generate Endpoint](https://docs.cohere.com/reference/generate) to generate a movie recommendations.
    - ***Memory Mode*** - uses [Cohere's Chat Endpoint](https://docs.cohere.com/reference/chat) and maintains a temporary history of user prompts and its responses, which enables a more non-repetitive and context-aware responses.
- Click the *Get Suggestion* button to receive a movie recommendation based on your input description.
- Click the *Surprise Me* button to get a random movie recommendation.
- Once you receive a recommendation, the app displays various details about the suggested movie, including its title, release year, IMDB rating, Rotten Tomatoes rating, directors, actors, studios, distributors, and plot.
> ***Note:***
> - The app will only be able to close when it is not generating any recommendation.
> - Manual Window resizing is disabled, as it isn't responsive. But the window will still auto resize based on the responses generated.

## Installing and Using the App
> ***Note: This is a windows only application***
- Download the *FlickPickV1.1.0.exe* from [here](https://github.com/pratham-jaiswal/flick-pick/releases/).
- Double click on it to install *FlickPick*.
- Run the *FlickPick* app.
- When the app loads, you'll get a random movie recommendation.
- Choose between the *Classic Mode* and *Memory Mode*.
- Enter the type of movie you want to watch and click on *Get Suggestion* button to get a movie recommendation based on your input description.
- Click the *Surprise Me* button to get a random movie recommendation.

## Get Started with Code
> ***Note: The script used in the executable file provided and the one available in the repository exhibit some differences, primarily for security reasons. However, their core functionality remains consistent.***
- Make sure you have Python installed
- Clone the repository
    ```sh
    git clone https://github.com/pratham-jaiswal/flick-pick.git
    ```
- Install the dependencies
    ```sh
    pip install tkinter python-decouple cohere requests
    ```
- Get your Cohere API Key from [here](https://dashboard.cohere.com/api-keys)
- Edit the *.env* file and add your Cohere API Key to it as
    ```.env
    COHERE_KEY=YOUR-COHERE-API-KEY
    ```
- Run the *flickpick.py*
    ```sh
    python flickpick.py
    ```
- The *FlickPick* app will open.
- When the app loads, you'll get a random movie recommendation.
- Choose between the *Classic Mode* and *Memory Mode*.
- Enter the type of movie you want to watch and click on *Get Suggestion* button to get a movie recommendation based on your input description.
- Click the *Surprise Me* button to get a random movie recommendation.

## Feedback and Contributions
Your feedback is invaluable to me! If you encounter any issues, have suggestions for improvements, or want to contribute to the development of FlickPick, please don't hesitate to [open an issue](https://github.com/pratham-jaiswal/flick-pick/issues) on my GitHub repository.

## License
This project is licensed under the MIT License. Feel free to use and modify the code for your own purposes.