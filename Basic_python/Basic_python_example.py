
command = ""
started = False
while True:

    command = input("> ").lower()

    if command == 'help':
        print("""
            start --- To start the car.
            stop --- To stop the car. 
            quit --- To exit the car.
            
            """)

    elif command == 'start':
        if started:
            print("Car already started..........")
        else:
            started = True
            print("Car started...Ready to go .........")

    elif command == 'stop':
        if not started:
            print("Car already Stopped")
        else:
            started = False
            print("car stopped............")
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand you.")
