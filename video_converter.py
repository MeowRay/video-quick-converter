import os
import winreg as reg
import ctypes
import sys
import shutil

# 注册表路径模板和支持的视频格式列表
video_extensions = ['.mov', '.mp4', '.avi', '.mkv', '.wmv', '.flv', '.m4v']

def delete_existing_keys():
    try:
        for ext in video_extensions:
            reg_path = fr"SystemFileAssociations\{ext}\shell"
            try:
                # 尝试删除整个shell键
                reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path)
                print(f"已删除 {reg_path}")
            except WindowsError as e:
                # 如果键不存在，继续处理下一个
                print(f"跳过 {reg_path}: {e}")
                continue
        print("已完成清理注册表项")
    except Exception as e:
        print(f"删除过程中发生错误: {e}")

def create_registry_key():
    try:
        scripts_dir = r"C:\scripts"
        bat_path = os.path.join(scripts_dir, "ffmpeg_convert.bat")
        
        # 定义所有子命令的键名
        subcommands = [
            "转换为原始分辨率30M_H265_MOV",
            "转换为原始分辨率15M_H265_MOV",
            "转换为原始分辨率10M_H265_MOV",
            "转换为1080P_6M_H265_MOV",
            "转换为原始分辨率30M_H265_MP4",
            "转换为原始分辨率15M_H265_MP4",
            "转换为原始分辨率10M_H265_MP4",
            "转换为1080P_6M_H265_MP4",
            "转换为原始分辨率30M_H264_MP4",
            "转换为原始分辨率15M_H264_MP4",
            "转换为原始分辨率10M_H264_MP4",
            "转换为1080P_6M_H264_MP4"
        ]
        
        # 为每种视频格式创建右键菜单
        for ext in video_extensions:
            reg_path = fr"SystemFileAssociations\{ext}\shell\视频转换"
            
            # 创建主菜单项，并列出所有子命令
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path) as menu_key:
                reg.SetValueEx(menu_key, "MUIVerb", 0, reg.REG_SZ, "视频转换")
                reg.SetValueEx(menu_key, "SubCommands", 0, reg.REG_SZ, ";".join(subcommands))

            # 创建子菜单项目的基础路径
            subcommands_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell"
            
            # MOV H265 选项
            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率30M_H265_MOV") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 30M H265 MOV")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 4k_mov %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率15M_H265_MOV") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 15M H265 MOV")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 15m_mov %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率10M_H265_MOV") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 10M H265 MOV")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 10m_mov %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为1080P_6M_H265_MOV") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为1080P 6M H265 MOV")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 1080p_mov %1')

            # MP4 H265 选项
            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率30M_H265_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 30M H265 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 4k_mp4_265 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率15M_H265_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 15M H265 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 15m_mp4_265 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率10M_H265_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 10M H265 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 10m_mp4_265 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为1080P_6M_H265_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为1080P 6M H265 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 1080p_mp4_265 %1')

            # MP4 H264 选项
            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率30M_H264_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 30M H264 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 4k_mp4_264 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率15M_H264_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 15M H264 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 15m_mp4_264 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为原始分辨率10M_H264_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为原始分辨率 10M H264 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 10m_mp4_264 %1')

            with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, f"{subcommands_path}\\转换为1080P_6M_H264_MP4") as command_key:
                reg.SetValueEx(command_key, "", 0, reg.REG_SZ, "转换为1080P 6M H264 MP4")
                with reg.CreateKey(command_key, "command") as sub_command_key:
                    reg.SetValueEx(sub_command_key, "", 0, reg.REG_SZ, fr'cmd.exe /k {bat_path} 1080p_mp4_264 %1')

        print("所有视频格式的右键菜单项创建成功！")
    
    except Exception as e:
        print(f"发生错误: {e}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def setup_environment():
    scripts_dir = r"C:\scripts"
    bat_path = os.path.join(scripts_dir, "ffmpeg_convert.bat")
    
    # 创建目录（如果不存在）
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_bat = os.path.join(current_dir, "ffmpeg_convert.bat")
    
    # 拷贝bat文件
    try:
        shutil.copy2(source_bat, bat_path)
        print(f"已成功将 ffmpeg_convert.bat 复制到 {scripts_dir}")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not is_admin():
        print("请以管理员权限运行此脚本！")
        sys.exit(1)
    
    setup_environment()
    delete_existing_keys()
    create_registry_key()