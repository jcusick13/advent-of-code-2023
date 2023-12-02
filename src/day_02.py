from src.base import Solution


class Day02(Solution):
    name = "02"

    def part_one(self, game_results: list[str]):
        possible_id_total = 0
        max_cube_map = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        for result in game_results:
            impossible = False
            iden, res = result.split(":")
            game_id = int(iden.split(" ")[-1])

            for draw in res.strip().split(";"):
                if impossible:
                    break

                for cube in draw.split(","):
                    count, color = cube.strip().split(" ")
                    if int(count) > max_cube_map[color]:
                        impossible = True
                        break

            if not impossible:
                possible_id_total += game_id

        return possible_id_total


    def part_two(self, game_results: list[str]):
        total_power = 0

        for result in game_results:
            _, res = result.split(":")
            min_cube_map = {
                "red": 0,
                "green": 0,
                "blue": 0,
            } 

            for draw in res.strip().split(";"):
                for cube in draw.split(","):
                    count, color = cube.strip().split(" ")
                    min_cube_map[color] = max(int(count), min_cube_map[color])
            
            game_power = (
                min_cube_map["red"] *
                min_cube_map["green"] *
                min_cube_map["blue"]
            )
            total_power += game_power
        
        return total_power


if __name__ == "__main__":
    Day02().solve()
