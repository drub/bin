#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------
import sys
import os

# ----------------------------------------------------------------------
# My Libraries
# ----------------------------------------------------------------------
lib_path = os.environ['HOME'] + "/bin/lib"
sys.path.append(lib_path)
import format_str
from format_str import Test_DotCol

# ----------------------------------------------------------------------
# Main MAIN main
# ----------------------------------------------------------------------

print(f"format_str v{format_str.__version__}")
print()
print("Usage - importing this library from another program:")
print("  import os, sys")
print("  lib_path = os.environ['HOME'] + \"/bin/lib\"")
print("  sys.path.append(lib_path)")
print("  import format_str")
print("  from format_str import StrCol, DotCol")
print()
print("  Query the library version:")
print("  print(format_str.__version__)")
print()

Test_DotCol()

# ----------------------------------------------------------------------
# End END end
# ----------------------------------------------------------------------
