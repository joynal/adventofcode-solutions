digit_spelled = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]


def part_1(line):
  digits = []

  for char in line:
    if char.isdigit():
      digits.append(char)

  if not digits:
    return 0

  return int(digits[0] + digits[-1])


def part_2(line):
  digits = []

  for index, char in enumerate(line):
    if char.isdigit():
      digits.append(int(char))
    else:
      substring = line[index:]
      for j, word in enumerate(digit_spelled):
        if substring.startswith(word):
          digits.append(j + 1)

  if not digits:
    return 0

  return digits[0] * 10 + digits[-1]


total_calibration = 0

with open('./input/trebuchet.txt', 'r') as file:
  for line in file:
    total_calibration += part_2(line)

print(total_calibration)
