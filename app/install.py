import sys
import subprocess

# installing requirements
subprocess.check_call([sys.executable, '-m', 'pip', 'install','opencv-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','pyproj'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','rasterio'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','fiona'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install','boto3'])

#creating tables
