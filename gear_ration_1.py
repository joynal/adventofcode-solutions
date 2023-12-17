with open('./input/gear_ratios.txt', 'r') as file:
  input_data = file.read()

lines = input_data.split('\n')
col_length, row_length = len(lines), len(lines[0])


def is_symbol(row, col):
  return 0 <= row < col_length and 0 <= col < row_length and lines[row][
      col] != '.' and not lines[row][col].isdigit()


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
      if is_symbol(row_index, start - 1) or is_symbol(row_index, col):
        sum_result += num
        continue

      for k in range(start - 1, col + 1):
        if is_symbol(row_index - 1, k) or is_symbol(row_index + 1, k):
          sum_result += num
          break

    col += 1

print(sum_result)
