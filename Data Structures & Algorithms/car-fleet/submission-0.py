class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [val for _, val in sorted(zip(position, speed), reverse=True)]
        position = sorted(position, reverse=True)
        print(speed)
        print(position)
        time = [0 for x in range(len(speed))]
        counter = 0
        for i in range(len(position)):
            time[i] = (target - position[i]) / speed[i]
            if i - 1 >= 0:
                if time[i - 1] < time[i]:
                    counter += 1
                else:
                    time[i] = time[i - 1]
            else:
                counter += 1
        return counter