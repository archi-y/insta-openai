# insta-openai
A python script for instagram that answers automatically to unread private messages using openai api and instagrapi !
![logo](https://user-images.githubusercontent.com/26002863/208255649-19667d52-b016-4dbe-bfdd-96c3f13ebf9a.png)

# Table of Contents 

- [How it works](#how-it-works)
- [Use cases](#use-cases)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Important](#important)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Docker](#docker-recommended-for-multiple-accounts)
- [It's not working !!!](#its-not-working-)
- [Notes](#notes)



# How it works
Using the same model from [openai](https://beta.openai.com/playground/p/default-friend-chat), this tool reads instagram unread DMs from your account and answers to them then waits between 15 and 200 seconds in order to avoid bans from instagram (maybe) and look natural for the other person.

***Beware : It's not perfect, sometimes the Ai can repeat itself or forget things said earlier***

## Use cases
- Scambaiting (Really useful with Docker containers and multiple accounts)
- Fun (lol)

## Requirements

- Valid instagram account
- [OpenAI API Key](https://beta.openai.com/account/api-keys)

- Python 3 with [OpenAI](https://github.com/openai/openai-python), [Instagrapi](https://github.com/adw0rd/instagrapi) and [Pillow](https://github.com/python-pillow/Pillow)

- [Docker](https://docs.docker.com/engine/install/) (if you want to use the Dockerfile)

# Installation

## Important
First describe your character in `context_base.txt`

Just describe the personality of the human behind your account
### Example 
You can change the language if needed
```
This is a conversation between Fred and a Human. 
Fred is natural, helpful, naive and innocent, creative and very friendly. 
Fred often writes in simple, unprofessional language. 
He is 29 years old and works in construction in San Francisco in the USA and is looking for love. 
His phone number is +415 989 262.

Human: Hey, how are you ?

Fred: I'm good thank you for asking.

Human: 
```
Leave the last line like this so the AI can answer

## Windows
With Python installed :
  - Just launch install.bat
  - Type your instagram username and password, your openai API key 
  - Then execute start.bat and you're done

## Linux

With Python installed : 
  ```
  pip install -r requirements.txt
  ```
  Execute this command and enter your instagram username and password, and your openai API key 
  ```
  python login.py
  ```
  Then just start the python script with
  ```
  python instagpt.py
  ```
## Docker (Recommended for multiple accounts)

With [Docker](https://docs.docker.com/engine/install/) and Python installed :

- **You need to have, in the same folder : `Dockerfile`, `context_base.txt`, `instagpt.py`, `login.py`, and the generated files `login.json` and `openai.key`**

  To obtain `login.json` and `openai.key` files just enter this command :
    ```
    python login.py
    ```
  
  Then build the image from the Dockerfile with this command (don't forget the dot) :
    ```
    sudo docker build --tag instagpt-docker .
    ```
  Then just start the container with
    ```
    sudo docker run -it instagpt-docker
    ```

## It's not working !!!

Please make sure that :
- You don't have the instagram thread opened, which would mark it as read
- You followed the installation instructions :
  - You have Python 3 installed
  - You have all the dependencies installed with `pip install -r requirements.txt`

If it's still not working you can open an issue

### Notes

I'm not an experienced python coder and this script is new so if you have problems with it, make an Issue and I will try to help you with it.
