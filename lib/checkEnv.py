import sys

# Check python version
def checkPythonVersion():
  def version_error():
    print("Sorry, pyPuyo needs python >= 3.4.0 or 2.7.0")
    sys.exit(1)

  version = list(map(int, sys.version.split()[0].split('.')))
  if version[0] == 2 and version < [2, 7, 0]:
    version_error()
  elif version < [3, 4, 0]:
    version_error()


# Run all functions
checkPythonVersion()

