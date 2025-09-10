import testpairs


if __name__ == '__main__':
  testpairs.test_number_to_pair(4, 'White', 'Brown')
  testpairs.test_number_to_pair(5, 'White', 'Slate')
  testpairs.test_pair_to_number('Black', 'Orange', 12)
  testpairs.test_pair_to_number('Violet', 'Slate', 25)
  testpairs.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
