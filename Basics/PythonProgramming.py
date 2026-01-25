# เคลียร์ หน้าจอในระบบ Unix-based ก่อนรัน Python
import os
import sys
if sys.platform.startswith("win"):
    os.system("cls")
else:
    os.system("printf '\\033c'")
