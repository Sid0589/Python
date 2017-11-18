from inputParser import inputParser
import sys

def main(args=None):
	if args is None:
		inputParser.inputParse(sys.argv[1:])

if __name__ == '__main__':
	main()