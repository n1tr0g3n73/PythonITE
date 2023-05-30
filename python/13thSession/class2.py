class robot:
    robot_name = ""
    turn_left = ""
    turn_right = ""
    move_forward = ""
    move_bakword = ""
    def __init__(self,robot_name):
        self.robot_name = robot_name
    def __str__(self):
        return f"{self.robot_name}\n"

r1 = robot("nitro");
print(r1)

