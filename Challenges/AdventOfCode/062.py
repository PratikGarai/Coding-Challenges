import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Race:
    def __init__(self):
        self.time = 0
        self.distance = 0

    def get_distance(self, tm: int) -> int:
        speed = tm
        leftover_time = self.time - tm
        return speed * leftover_time

    def binary_left_search(self, left: int, right: int) -> int:
        mid = (left + right) // 2
        if left > right:
            return left
        if self.get_distance(mid) < self.distance:
            return self.binary_left_search(mid+1, right)
        elif self.get_distance(mid) > self.distance:
            return self.binary_left_search(left, mid-1)
        else:
            return mid

    def binary_right_search(self, left: int, right: int) -> int:
        mid = (left + right) // 2
        if left > right:
            return right
        if self.get_distance(mid) > self.distance:
            return self.binary_right_search(mid+1, right)
        elif self.get_distance(mid) < self.distance:
            return self.binary_right_search(left, mid-1)
        else:
            return mid

    def get_count(self):
        left = self.binary_left_search(0, self.time)
        right = self.binary_right_search(0, self.time)
        return right-left+1


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '061.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        datas = list(datas)

        _, times = datas[0].split(':')
        times = [int(''.join(times.strip().split()))]
        _, distances = datas[1].split(':')
        distances = [int(''.join(distances.strip().split()))]

        races = []
        n_races = len(times)
        for i in range(n_races):
            race = Race()
            race.time = times[i]
            race.distance = distances[i]
            races.append(race)

        prod = 1
        for race in races:
            count = race.get_count()
            logging.info(f"count: {count}")
            prod *= count
        print(prod)


if __name__ == "__main__":
    main()
