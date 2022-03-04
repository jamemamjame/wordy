# wordy
Console interaction pProgram to solve Wordle game https://www.nytimes.com/games/wordle/index.html

```bash
python main.py
```

```
Hi, I'm Wordy. I'm ready to solve Wordle game.
I will suggest you the word for guessing then please provide me the feedback back.
Feedback consist of:
	"g" stand for Green that represent to correctness
	"y" stand for Yellow that represent to presenting
	"w" stand for black that represent to absent
Please provide me the feedback like below example.
feedback: ywwgg << 🟨⬜⬜🟩🟩
----------------------------
[Round 1] Please guess "arose"
Feedback: gwwwy
🟩⬜⬜⬜🟨

[Round 2] Please guess "lined"
Feedback: wwwyg
⬜⬜⬜🟨🟩

[Round 3] Please guess "ahead"
Feedback: ggggg
Congrats! We won 🎉
```

Build and run
___
To Run Locally:
Clone the repo then perform these command
```
poetry install
pyhon main.py
```

