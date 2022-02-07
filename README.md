# Duskers-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/136

## Work on project. Stage 1/6: Greetings, Commander

### Objectives
1. Choose a name for your game and display it using online generated ASCII art. 
Your title should take up a maximum of 8 lines; if your title takes up less space, fill the rest with blank lines. For this task, it will be useful to look at some examples of text art.
2. Display the player's options in the main menu. In this stage, these options are ```Play``` and ```Exit``` shown in this 
exact order on separate lines right below the title.
3. The program should take commands from a user. The input should be case-insensitive, 
which means that ```PLAY```, ```pLAY```, and ```play``` are all valid options.
4. If the player chooses ```Play```, the program should prompt them to enter their name, 
after which they are personally greeted and asked if they are ready to start the game.
5. If they respond ```yes```, the program should print a short message telling the user to get back 
to coding and end the program. If they choose ```no```, keep asking the same question until they choose ```yes```.
6. If the player chooses ```exit``` on the title screen, print a message and end the program.

Note: Make sure that after each command input you leave a blank line before displaying text.

If the player enters an invalid command, make sure you point it out and ask for a valid input.

#### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

##### Example 1:

```shell
██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗ ███████╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║  ██║██║   ██║███████╗█████╔╝ █████╗  ██████╔╝███████╗
██║  ██║██║   ██║╚════██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
██████╔╝╚██████╔╝███████║██║  ██╗███████╗██║  ██║███████║
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝

[Play]
[Exit]

Your command:
> play

Enter your name:
> Hyper

Greetings, commander Hyper!
Are you ready to begin?
    [Yes] [No]

Your command:
> no

How about now.
Are you ready to begin?
    [Yes] [No]

Your command:
> yes

Great, now let's go code some more ;)
```

##### Example 2:
```shell
██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗ ███████╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║  ██║██║   ██║███████╗█████╔╝ █████╗  ██████╔╝███████╗
██║  ██║██║   ██║╚════██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
██████╔╝╚██████╔╝███████║██║  ██╗███████╗██║  ██║███████║
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝

[Play]
[Exit]

Your command:
> exit

Thanks for playing, bye!
```