import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)

class Race : 
    def __init__(self) :
        self.time = None
        self.distance = None
    
    def get_count(self) :
        count = 0
        for i in range(self.time) :
            speed = i
            leftover_time = self.time - i
            if speed * leftover_time > self.distance : 
                logging.info(f"speed: {speed}, leftover_time: {leftover_time}")
                count += 1
        return count

def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '061.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        datas = list(datas)

        _, times = datas[0].split(':')
        times = list(map(int, times.strip().split()))
        _, distances = datas[1].split(':')
        distances = list(map(int, distances.strip().split()))

        races = []
        n_races = len(times)
        for i in range(n_races) :
            race = Race()
            race.time = times[i]
            race.distance = distances[i]
            races.append(race)

        prod = 1
        for race in races : 
            count = race.get_count()
            logging.info(f"count: {count}")
            prod *= count
        print(prod)

if __name__ == "__main__":
    main()
