# wordy
Console interaction program to solve Wordle game https://www.nytimes.com/games/wordle/index.html

```bash
python main.py
```

```
Hi, I'm Wordy. 🤖🙏🏻
I will suggest you the word for guessing in Wordle game base on feedback in each round.
Feedback consist of:
	"g" (Green) that represent to correctness
	"y" (Yellow) that represent to presenting
	"w" (White) that represent to absent
Once you've guessed the word in each round, please provide me the feedback as a sequence of color like an example below.
feedback: ywwgg << 🟨⬜⬜🟩🟩
----------------------------
Calculating the most suitable word... (This process takes long time)
[Round 1] Please guess "arose"
Feedback: gwwwy
🟩⬜⬜⬜🟨

Calculating the most suitable word... (This process takes long time)
[Round 2] Please guess "lined"
Feedback: wwwyg
⬜⬜⬜🟨🟩

Calculating the most suitable word... (This process takes long time)
[Round 3] Please guess "ahead"
Feedback: ggggg
Hoolay!! We won with in round 3 🎉
```

## Build and run

### To run locally:

Clone the repo then perform these command
```
poetry install
pyhon main.py
```

### To build/run docker container:
```bash
$> docker build -t wordy:1.0.0 -f docker/Dockerfile .
$> docker run -it wordy:1.0.0
```
