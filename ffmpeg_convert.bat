@echo off
setlocal enabledelayedexpansion

set "resolution=%1"
set "input_file=%2"
set "output_dir=%~dp2"
set "filename=%~n2"

echo xxx

:: MOV H265
if "%resolution%"=="4k_mov" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(3840,iw)':'min(2160,ih)'" -c:v hevc_nvenc -b:v 30M -c:a aac -b:a 192k -f mov "%output_dir%%filename%_H265_30M_4K_QuickTime.mov"
) else if "%resolution%"=="15m_mov" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v hevc_nvenc -b:v 15M -c:a aac -b:a 192k -f mov "%output_dir%%filename%_H265_15M_QuickTime.mov"
) else if "%resolution%"=="10m_mov" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v hevc_nvenc -b:v 10M -c:a aac -b:a 192k -f mov "%output_dir%%filename%_H265_10M_QuickTime.mov"
) else if "%resolution%"=="1080p_mov" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale=1920:1080" -c:v hevc_nvenc -b:v 6M -c:a aac -b:a 192k -f mov "%output_dir%%filename%_H265_6M_1080P_QuickTime.mov"
)

:: MP4 H265
if "%resolution%"=="4k_mp4_265" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(3840,iw)':'min(2160,ih)'" -c:v hevc_nvenc -b:v 30M -c:a aac -b:a 192k "%output_dir%%filename%_H265_30M_4K.mp4"
) else if "%resolution%"=="15m_mp4_265" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v hevc_nvenc -b:v 15M -c:a aac -b:a 192k "%output_dir%%filename%_H265_15M.mp4"
) else if "%resolution%"=="10m_mp4_265" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v hevc_nvenc -b:v 10M -c:a aac -b:a 192k "%output_dir%%filename%_H265_10M.mp4"
) else if "%resolution%"=="1080p_mp4_265" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale=1920:1080" -c:v hevc_nvenc -b:v 6M -c:a aac -b:a 192k "%output_dir%%filename%_H265_6M_1080P.mp4"
)

:: MP4 H264
if "%resolution%"=="4k_mp4_264" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(3840,iw)':'min(2160,ih)'" -c:v h264_nvenc -b:v 30M -c:a aac -b:a 192k "%output_dir%%filename%_H264_30M_4K.mp4"
) else if "%resolution%"=="15m_mp4_264" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v h264_nvenc -b:v 15M -c:a aac -b:a 192k "%output_dir%%filename%_H264_15M.mp4"
) else if "%resolution%"=="10m_mp4_264" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale='min(iw,iw)':'min(ih,ih)'" -c:v h264_nvenc -b:v 10M -c:a aac -b:a 192k "%output_dir%%filename%_H264_10M.mp4"
) else if "%resolution%"=="1080p_mp4_264" (
    ffmpeg -hwaccel cuda -i "%input_file%" -vf "scale=1920:1080" -c:v h264_nvenc -b:v 6M -c:a aac -b:a 192k "%output_dir%%filename%_H264_6M_1080P.mp4"
)

pause
