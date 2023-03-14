speed=0
while True:
    command=input("> ").lower()
    if command== "help":
        print(""" 
start --to start car
run --to accelerate
stop --to stop the car
quit --to quit the game
        """)
    elif command== "start":
        print("Car is started, ready to  go...")
    elif command == "run":
        print("car is accelerating with", speed)
        speed += 10
    elif(command== "stop"):
        print("car stoped")
        speed=0
    else:
        print("Unknown command enter help to help")