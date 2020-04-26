
An AI to play the Rock Paper Scissors game

## Requirements
- Python 3
- Keras
- Tensorflow
- OpenCV

## Set up instructions
1. Clone the repo.
```sh
$ git clone https://github.com/ShubhamDogra112/rock-paper-scissors.git
$ cd rock-paper-scissors
```

2. Install the dependencies
```sh
$ pip install requirements
```

3. Gather Images for each gesture (rock, paper and scissors and None):
In this example, we gather 200 images for the "rock" gesture
```sh
$ python collecting_images.py rock 200
```

4. Train the model
```sh
$ python train-model.py
```

5. Test and Play the game with your computer!
```sh
$ python testing_model.py
```
