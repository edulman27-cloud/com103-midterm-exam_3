# com103-midterm-exam_3

This program is a Project Progress Tracking System designed for academic groups to monitor task completion, allocate points, and determine if a projects meets the 75% "Ready" threshold. It automates progress calculation based on task types, member assignments, and completion status.

What the Program Does

Assigns Weights: It categorizes task into five types (Program Logic, UI, Testing, Documentation, Presentation), assigning varying effort levels.
Tracks Performance: It records who is assigned to a task and whether it is done (2 points) or pending (1 point).
Calculate Progress: It calculates the percentage of total points earned against the maximum possible points (@ points per assigned task).
Status Reporting: It generates a formatted "Task Board" output and evaluates if the project is "Project Ready" (if progress > 75%).

How to Run It

To execute a program like this (typically written in Python or a similar scripting language), follow these steps:

Prepare the Environment: Ensure you have the programming language interpreter installed on your machine.
Input Data: The program prompts for the following in sequence:
  
   1. Project Title & Group Name: Basic identification.
   2. Task Selection: Enter task number from the predefined menu(1-5). Enter 0 to stop adding tasks.
   3. Member Name: Assign a name to the task.
   4. Status: Type done or pending.

3. Execution: The script processes these inputs using a loop, stores the data in a list or dictionary, and performs the mathematical logic                 
   defined in the sample output.
4. View Output: the program prints the final summary table and status report to the console.

Logic Rules Summary

Done Status: 2 Points
Pending  Status: 1 Point
Project Ready Threshold: > 75% total progress. 
