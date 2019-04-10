from FactorioBlueprint import FactorioBlueprint
from pprint import pprint
import sys

def main():
  if (len(sys.argv) < 4):
    print("Please provide the following args: 'input file', 'current entity name', 'replacement entity name'")
    return 1

  # get input file contents
  with open(sys.argv[1]) as inputFileHandle:
    
    # original content
    content = inputFileHandle.read()

    # make FactorioBlueprint object
    blueprint = FactorioBlueprint(content)

    # perform conversion
    blueprint.convertEntity(sys.argv[2],sys.argv[3])

    # return string
    print(blueprint.raw)

if __name__ == '__main__':
  # example: `python main.py exampleInput.txt fast-transporter-belt express-transporter-belt`
  main()