import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class AlmanacMap:
    def __init__(self, beg: str, end: str):
        self.beg = beg
        self.end = end
        self.mappings = []

    def add_mapping(self, start1: int, start2: int, step: int) -> None:
        self.mappings.append((start1, start2, step))

    def get_value(self, val: int):
        for (start1, start2, step) in self.mappings:
            if val >= start2 and val <= start2+step:
                return start1 + val - start2
        return val


class Almanac:
    def __init__(self):
        self.maps = []
        self.seeds = []

    def parse(self, datas: list[str]) -> None:
        seeds_line = datas[0]
        datas = datas[1:]

        _, seeds_line = seeds_line.split(':')
        seeds_line = seeds_line.strip()
        self.seeds = list(map(int, seeds_line.split(' ')))

        beg = None
        end = None
        map_name = None
        data = {}
        current_map = None

        for data in datas:
            if not data:
                continue
            if len(data.split()) == 2:
                map_name, _ = data.split()
                map_name = map_name.strip()
                beg, _, end = map_name.split('-')
                current_map = AlmanacMap(beg, end)
                self.maps.append(current_map)
                # logging.info(f"map_name: {map_name}, beg: {beg}, end: {end}")
            elif len(data.split()) == 3:
                start1, start2, step = map(int, data.split())
                current_map.add_mapping(start1, start2, step)
                # logging.info(
                    # f"start1: {start1}, start2: {start2}, step: {step}")

    def find_location(self, seed: int) -> int:
        prev = None
        for map in self.maps:
            # logging.info(f"map: {map.beg} - {map.end}")
            prev, seed = seed, map.get_value(seed)
            logging.info(f"Map: {map.beg} - {map.end}, seed: {prev} -> {seed}")
        return seed


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '051.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        datas = list(datas)
        almanac = Almanac()
        almanac.parse(datas)

        locations = []

        for seed in almanac.seeds:
            location = almanac.find_location(seed)
            logging.info(f"Seed: {seed}, Location: {location}")
            locations.append(location)

        print(min(locations))


if __name__ == "__main__":
    main()
