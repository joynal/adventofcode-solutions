import operator
from functools import reduce

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part_1(line):
  game = line.split(': ')[1].split('; ')

  for game_sets in game:
    cubes = {}
    for color in game_sets.split(', '):
      item = color.split(' ')
      cubes[item[1]] = int(item[0])

    for color in max_cubes:
      if cubes.get(color, 0) > max_cubes[color]:
        return False

  return True


def part_2(line):
  game = line.split(': ')[1].split('; ')
  cubes = {"red": 0, "green": 0, "blue": 0}

  for game_sets in game:
    for color in game_sets.split(', '):
      item = color.split(' ')
      cubes[item[1]] = max(int(item[0]), cubes[item[1]])

  return reduce(operator.mul, cubes.values())


sum = 0

# with open('./input/cube_conundrum.txt', 'r') as file:
#   for index, line in enumerate(file, 1):
#     if part_1(line.rstrip()):
#       sum += index

with open('./input/cube_conundrum.txt', 'r') as file:
  for line in file:
    sum += part_2(line.rstrip())

print(sum)
