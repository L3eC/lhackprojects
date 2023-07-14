drive = None
with open("driver_recording.txt") as recording:
    for line in recording:
        command_list = line.split(" ")
        drive.drive(command_list[0], command_list[1], command_list[2])
        if "concurrently_runnable_command" in command_list:
            # run concurrently_runnable_command. Will work differently based on how the command is written
        if "blocking_command" in command_list:
            # run the blocking command, ensuring that it runs for a set amount of time. Use .withtimeout() if possible.
        