
def floorFactors(x):
  return list(reversed([ x // i for i in range(1, x+1)]))


if __name__ == '__main__':
  for x in range(100):
    print(",".join(map(lambda i: str(i), floorFactors(x))))
