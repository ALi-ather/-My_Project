import subprocess
import psutil
import os

# تشغيل لعبة البايثون
game_script = "alien_invasion.py"
process = subprocess.Popen(["python", game_script])

# الحصول على PID للعملية
pid = process.pid
print(f"PID للعبة: {pid}")
