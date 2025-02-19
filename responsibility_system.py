class Responsibility:
    def __init__(self, role_responsibility, ability_responsibility, obligation_responsibility, cause_responsibility):
        self.role_responsibility = role_responsibility
        self.ability_responsibility = ability_responsibility
        self.obligation_responsibility = obligation_responsibility
        self.cause_responsibility = cause_responsibility

    def evaluate_responsibility(self):
        total_responsibility = (
            self.role_responsibility +
            self.ability_responsibility +
            self.obligation_responsibility +
            self.cause_responsibility
        )
        return total_responsibility

    def display_responsibility(self):
        print(f"角色责任（R1）: {self.role_responsibility}")
        print(f"能力责任（R2）: {self.ability_responsibility}")
        print(f"义务责任（R3）: {self.obligation_responsibility}")
        print(f"原因责任（R4）: {self.cause_responsibility}")
        print(f"总责任: {self.evaluate_responsibility()}")

# 示例：评估某个机器人的责任表现
robot_responsibility = Responsibility(
    role_responsibility=0,  # 高阶 R1(0)
    ability_responsibility=1,  # 高阶 R2(N)
    obligation_responsibility=1,  # 高阶 R3(+1)
    cause_responsibility=1  # 高阶 R4(C)
)

robot_responsibility.display_responsibility()
