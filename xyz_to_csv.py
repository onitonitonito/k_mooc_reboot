"""
# 스페이스 구분 txt 화일을 읽어들임 (x,y,z)
# Pandas DF로 변환 -- 분석 / csv 화일로 결과 저장
#
# http://www.micromouse.ca/xyz_files.html
# http://www.ransen.com/pointor/xyz-file-format-conversion.htm
"""
# pandas 3d plot examples
# https://stackoverflow.com/questions/36589521/
# how-to-surface-plot-3d-plot-from-dataframe
# --------------------------------------------------------------
# Import Point data formats: XYZ, PTS, PTX, LAS, E57, ZFS, DP, FLS, FLW
# Project data from Leica Geosystems HDS and Pegasus scanners
# Image/Camera and model data: COE, BMP, TIFF, JPEG, PNG, NCTRI, SPH
# Control data from ASCII & X-Function DBX
# Export Point data formats: XYZ, PTS, PTX, E57, DXF, PCI/CWF, DBX
# Image and model data: COE, BMP, TIFF, JPEG, PNG
#
# Store in JetStream ProjectVault**
# ---------------------------------------------------------------
# https://en.wikipedia.org/wiki/XYZ_file_format
# http://www.micromouse.ca/xyz_files.html

print(__doc__)
from os import getcwd
from os.path import join
from pprint import pprint

import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # remain for scatter3D

filename_target = join(getcwd(), "_static", "txt_plan_xyz.txt")
filename_result = join(getcwd(), "_static", "conv_plan_xyz.csv")

def get_array_xyz_float(array_lines):
    """ read text file contains x,y,z data seperated by space"""
    array_xyz_float = []

    for line_str in array_lines:
        line_str = line_str.strip()
        is_alpha = line_str[0].isalpha()    # True / False

        # print(f"{is_alpha:2}: {line_str}")  # 0: -7.430273 -6.964596 8.349577

        if not is_alpha:
            array_xyz_float.append([
                float(coord)
                for coord in line_str.split(' ')
            ])
    return array_xyz_float

with open(file=filename_target, mode='r', encoding='utf8') as f:
    array_xyz_float = get_array_xyz_float(array_lines=f.readlines())


# pprint(array_xyz_float)
df = pd.DataFrame(data=array_xyz_float, columns=['x', 'y', 'z'])

print(df.info())
print(df.describe())
print(df)

# fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(
    df.x, df.y, df.z,
    cmap='viridis',
    linewidth=0.5,
)

plt.show()


# save to result file *.csv
df.to_csv(filename_result)
