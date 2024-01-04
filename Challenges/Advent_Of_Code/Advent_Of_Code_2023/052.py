import os

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

    def get_reverse_value(self, val: int):
        for (start1, start2, step) in self.mappings:
            if val >= start1 and val <= start1+step:
                return start2 + val - start1
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
            elif len(data.split()) == 3:
                start1, start2, step = map(int, data.split())
                current_map.add_mapping(start1, start2, step)

    def find_location(self, seed: int) -> int:
        prev = None
        for map in self.maps:
            prev, seed = seed, map.get_value(seed)
        return seed

    def find_seed(self, location: int) -> int:
        prev = None
        for map in self.maps[::-1]:
            prev, location = location, map.get_reverse_value(location)
        return location


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '051.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        datas = list(datas)
        almanac = Almanac()
        almanac.parse(datas)

        # Brute force
        # min_location = float('inf')
        # l = len(almanac.seeds)
        # print(f"l: {l}")
        # for idx in range(0, l, 2):
        #     seed_start = almanac.seeds[idx]
        #     seed_range = almanac.seeds[idx+1]
        #     print(f"idx: {idx} seed_start: {seed_start} seed_range: {seed_range}")
        #     for seed in tqdm(range(seed_start, seed_start+seed_range)):
        #         location = almanac.find_location(seed)
        #         print(f"Seed: {seed}, Location: {location}")
        #         min_location = min(location, min_location)
        #     print(min_location)

        # Reverse Brute force
        def search_seed(seed: int):
            for idx in range(0, len(almanac.seeds), 2):
                seed_start = almanac.seeds[idx]
                seed_range = almanac.seeds[idx+1]
                if seed >= seed_start and seed <= seed_start+seed_range:
                    return True
            return False

        location = 0
        while True:
            seed_from_location = almanac.find_seed(location)
            if search_seed(seed_from_location):
                print(
                    f"location: {location}, seed_from_location: {seed_from_location}")
                break
            location += 1
            if location % 1000000 == 0:
                print(f"location: {location}")


if __name__ == "__main__":
    main()
