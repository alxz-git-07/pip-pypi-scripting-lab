import sys
import os

# Force Python to look inside the CodeGrade student workspace directory
student_dir = "/home/codegrade/student"
if student_dir not in sys.path:
    sys.path.insert(0, student_dir)

# Also check inside the lib directory since generate_log lives there
lib_dir = os.path.join(student_dir, "lib")
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)
