# Adventurer Journey
You are an adventurer trying to navigate to a destination using specific directional instructions. Adventurer Journey will run your instructions and determine the distance from your destination to the starting point as the crow flies. 

## Running The Program
You must have python installed on your local machine, then clone this repository down. 

### Windows
1. Navigate to your local repository with File Explorer or from the command line.
2. Either double click run.bat from File Explorer or run .\run.bat in Powershell

### Mac OS/Unix
1. Navigate to your local repository from a bash terminal
2. Run ./run.sh from the command line.

## Inputting Directions
The directional input is a sequence of instructions, with each instruction containing a number of steps followed by the direction.

The possible directions are:
- F to go forward/north
- B to go backward/south
- R to go right/east
- L to go left/west

The instructions are formatted into a single string with no whitespace or separators.

### Example
`15F6B6B5L`

1. 15 steps forward (15F)
2. 6 steps back (6B)
3. 6 steps back (6B)
4. 5 steps left (5L)

Which will return:
`You are 5.830951894845301 steps from your starting point!`

# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.