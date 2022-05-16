## PID tools
### Input Parameter
You can use the help function to see the details of the parameters.
```cmd
python pid_tool.py -h
```
![Imgur](https://i.imgur.com/GAUARek.png)

### How to run?
- must input
    - previous y
    - y
    - previous u
    - u
- optional input
    - learning rate

For example:
1. No learning rate
```cmd
python pid_tool.py [PRE_Y] [Y] [PRE_U] [U]
```
![Imgur](https://i.imgur.com/IzK9rG0.png)
2. learning rate
```cmd
python pid_tool.py [PRE_Y] [Y] [PRE_U] [U] -lr [LEARNING_RATE]
```
![Imgur](https://i.imgur.com/OSGafjD.png)