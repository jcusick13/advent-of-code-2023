import re

from src.base import Solution


class Day01(Solution):
    name = "01"

    def part_one(self, calibration_document):
        total = 0
        for line in calibration_document:
            nums = re.findall(f"\d", line)
            total += int(nums[0] + nums[-1])
        
        return total


    def part_two(self, calibration_document):
        digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        total = 0

        for line in calibration_document:
            i = 1
            while True:
                s = line[:i]
                for alpha, num in digit_map.items():
                    # Replace word for digit if able
                    orig_len = len(s)
                    s = s.replace(alpha, num)

                    if len(s) != orig_len:
                        # We've swapped out word for digit, combined the
                        # now truncated digit string back with the
                        # remaining string to search through
                        index_diff = orig_len - len(s)
                        i -= index_diff
                        line = s + line[i:]
                        break
                i += 1

                if i > len(line):
                    break

            nums = re.findall(f"\d", line)
            total += int(nums[0] + nums[-1])

        return total


if __name__ == "__main__":
    Day01().solve()
