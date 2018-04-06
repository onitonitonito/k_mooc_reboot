""" 환경변수 path 다른 점 비교 : set() _a, _b 집합 교집합 긁어낸 코드
  _a = 관리자권한 / _b = Win+'R'
 """
print(__doc__)

def get_string_a_b():
    _a = """C:_ProgramData_Anaconda3;C:_ProgramData_Anaconda3_Library_mingw-w64_bin;C:_ProgramData_Anaconda3_Library_usr_bin;C:_ProgramData_Anaconda3_Library_bin;C:_ProgramData_Anaconda3_Scripts;C:_Program Files (x86)_Intel_iCLS Client_;C:_ProgramData_Oracle_Java_javapath;C:_Program Files_Intel_iCLS Client_;C:_WINDOWS_system32;C:_WINDOWS;C:_WINDOWS_System32_Wbem;C:_WINDOWS_System32_WindowsPowerShell_v1.0_;C:_Program Files_Git_cmd;C:_Users_nitt0_AppData_Local_Programs_Python_Python36;C:_Users_nitt0_AppData_Local_Programs_Python_Python36_lib;C:_Users_nitt0_AppData_Local_Programs_Python_Python36_lib_site-packages;C:_Program Files (x86)_Intel_Intel(R) Management Engine Components_DAL;C:_Program Files_Intel_Intel(R) Management Engine Components_DAL;C:_Program Files (x86)_Intel_Intel(R) Management Engine Components_IPT;C:_Program Files_Intel_Intel(R) Management Engine Components_IPT;C:_Program Files_Java_jdk-9.0.1_bin_;C:_opencv_build_x64_vc15_bin;C:_Program Files_Intel_WiFi_bin_;C:_Program Files_Common Files_Intel_WirelessCommon_;C:_ProgramData_Anaconda3_Lib_site-packages;C:_uncrustify;C:_Program Files (x86)_Brackets_command;C:_Users_nitt0_AppData_Local_Microsoft_WindowsApps;C:_Users_nitt0_AppData_Local_atom_bin;C:_Users_nitt0_AppData_Local_Microsoft_WindowsApps;C:_Program Files_Java_jdk-9.0.1_bin_"""

    _b = """C:_ProgramData_Anaconda3;C:_ProgramData_Anaconda3_Library_mingw-w64_bin;C:_ProgramData_Anaconda3_Library_usr_bin;C:_ProgramData_Anaconda3_Library_bin;C:_ProgramData_Anaconda3_Scripts;C:_Program Files (x86)_Intel_iCLS Client_;C:_ProgramData_Oracle_Java_javapath;C:_Program Files_Intel_iCLS Client_;C:_WINDOWS_system32;C:_WINDOWS;C:_WINDOWS_System32_Wbem;C:_WINDOWS_System32_WindowsPowerShell_v1.0_;C:_Program Files_Git_cmd;C:_Users_nitt0_AppData_Local_Programs_Python_Python36;C:_Users_nitt0_AppData_Local_Programs_Python_Python36_lib;C:_Users_nitt0_AppData_Local_Programs_Python_Python36_lib_site-packages;C:_Program Files (x86)_Intel_Intel(R) Management Engine Components_DAL;C:_Program Files_Intel_Intel(R) Management Engine Components_DAL;C:_Program Files (x86)_Intel_Intel(R) Management Engine Components_IPT;C:_Program Files_Intel_Intel(R) Management Engine Components_IPT;C:_Program Files_Java_jdk-9.0.1_bin_;C:_opencv_build_x64_vc15_bin;C:_Program Files_Intel_WiFi_bin_;C:_Program Files_Common Files_Intel_WirelessCommon_;C:_ProgramData_Anaconda3_Lib_site-packages;C:_uncrustify;C:_Program Files (x86)_Brackets_command;C:_Users_nitt0_AppData_Local_Microsoft_WindowsApps;C:_Users_nitt0_AppData_Local_atom_bin;C:_Users_nitt0_AppData_Local_Microsoft_WindowsApps"""
    return _a, _b

def show_list_from_string(string):
    return string.split(';')

def show_num_list(list):
    for idx, dir in enumerate(list, 1):
        print("%2s. %s" % (idx, dir))



if True:
    try:
        _a_set, _b_set = [set(show_list_from_string(str)) for str in get_string_a_b()]

        print("The two sets are equal : ", _a_set == _b_set)
        print("----------------------------")

        show_num_list(_a_set)

    except:
        print("... ERROR ...")

else:


    try:
        _a_set, _b_set = [set(show_list_from_string(str)) for str in get_string_a_b()]

        print("The two sets are equal : ", _a_set == _b_set)
        print("----------------------------")

        show_num_list(_a_set)

    except:
        print("... ERROR ...")
