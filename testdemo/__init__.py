import sys

def execute_from_command(argv=None):
	utility = ManagementUtility(argv)
	utility.execute()


class ManagementUtility(object):
	def __init__(self, argv=None):
		self.argv = argv or sys.argv[:]
	def execute(self):
		try:
			subcommand = self.argv[1]
			print(subcommand)
		except IndexError:
			subcommand = 'help' # Display help if no arguments were given.