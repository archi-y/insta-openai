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
