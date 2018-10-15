### Turtle Race (Python, Turtle, messagebox)
- Created python application where four different turtles are drawn on the main screen and they race with eachother.
- Each four turtles are assigned with random speed everytime untill they finish the racce.
- Worked with python features like turtle and messagebox to design the UI.

## Steps to run the program
> Lets assume you already have python installed.

- In the terminal, Go up to the folder directory.
```
    python practice.py

```

- GUI Window will be open up and the ARROW pointer will start printing the graphics.
- First it will create 15 tracks with dashed lines on which turtles are going to race.

```
    for step1 in range(15):
        forward(10)
        penup()
        forward(5)
        pendown()
```

- Four turtles will be drwan after the tracks and they will be assigned with the speed ranging from 1 to 5 randomly.

```
    for turn in range(100):
        t1.forward(randint(1, 5))
        t2.forward(randint(1, 5))
        t3.forward(randint(1, 5))
        t4.forward(randint(1, 5))
```

- At the end,a message box will pop up with showing the result of the race.
```
    messagebox.showinfo("RESULT OF THE MATCH ", " X TURTLE WINS")
```
