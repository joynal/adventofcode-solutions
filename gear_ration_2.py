with open('./input/gear_ratios.txt', 'r') as file:
  input_data = file.read()

lines = input_data.split('\n')
col_length, row_length = len(lines), len(lines[0])

gears_with_parts = [[[] for _ in range(row_length)] for _ in range(col_length)]


def is_symbol(row, col, num):
  if 0 <= row < col_length and 0 <= col < row_length and lines[row][col] == '*':
    gears_with_parts[row][col].append(num)
    return True
  return False


sum_result = 0

for row_index, line in enumerate(lines):
  start, col = 0, 0

  while col < row_length:
    start = col
    num = ""

    while col < row_length and line[col].isdigit():
      num += line[col]
      col += 1

    if num:
      num = int(num)
      is_symbol(row_index, start - 1, num) or is_symbol(row_index, col, num)

      for k in range(start - 1, col + 1):
        is_symbol(row_index - 1, k, num) or is_symbol(row_index + 1, k, num)

    col += 1

for row in range(col_length):
  for col in range(row_length):
    nums = gears_with_parts[row][col]
    if lines[row][col] == '*' and len(nums) == 2:
      sum_result += nums[0] * nums[1]

print(sum_result)
