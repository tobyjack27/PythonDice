import random
class Error(Exception):
  pass

class ValueTooSmallError(Error):
  pass

def roller(number):
  print(" – Rolling " + str(number) + " dice!")
  results = [random.randint(1, 6) for i in range(number)]
  return results

def result_counter(results):
  print(" – Counting results!")
  counts = [0 for i in range(6)]
  for result in results:
      counts[(result-1)] += 1
  return counts

def dice_output(number):
  results = roller(number)
  counts = result_counter(results)
  numbers = ["one", "two", "three", "four", "five", "six"]
  output_string_1 = " – You have rolled {} dice and got:"
  for i in range(len(counts)):
    if counts[i] > 0:
      if i == 0 or counts[i-1] == 0:
        output_string_1 += " " + str(counts[i]) + " " + numbers[i]
        if counts[i] > 1 and i != 5:
            output_string_1 += "s"
        elif counts[i] > 1 and i == 5:
            output_string_1 += "es"
      else:
        output_string_1 += ", " + str(counts[i]) + " " + numbers[i]
        if counts[i] > 1 and i != 5:
            output_string_1 += "s"
        elif counts[i] > 1 and i == 5:
            output_string_1 += "es"
  return print(output_string_1.format(number) + '. – ')

def get_num_dice():
    while True:
      try:
        num = input(" – How many dice do you want to roll (enter in digits)?\n")
        if not int(num):
          raise ValueError
      except ValueError:
        print("– InputError: Please enter a number greater than zero in digits")
        num = input(" – How many dice do you want to roll (enter in digits)?\n")
      return int(abs(float(num)))

dice_output(get_num_dice())

user_input = input(" – Do you want to roll again?\n – Enter Y for yes.\n")

while user_input == "Y":
    dice_output(get_num_dice())
    user_input = input(" – Do you want to roll again?\n – Enter Y for yes.\n")