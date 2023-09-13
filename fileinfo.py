#this is a python code to show details of a forler files.
#also do for sub folders
#if there are any video files in your folder it helps to find the the duration of a playlist
#sometime we need to know a playlist duration to complete any course
#processing time will depend on your total files and sizes

#instruction
#install libraries if not installed
#run these in your terminal
'''
pip install moviepy
pip install opencv-python
pip install pydub
'''

#for audio file you need to install ffmpeg and add path to your pc
#here is the tutorial
#https://www.youtube.com/watch?v=IECI72XEox0&ab_channel=TroubleChute

#change at 34 & 40 like
#follow this format of path
#"C:/use/your/path/like this format"

import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from time import sleep
import warnings


warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")

# Set the path to the FFmpeg executable.
ffmpeg_executable = "C:/ffmpeg-6.0-essentials_build/bin/ffmpeg.exe"  # Replace with the actual path to ffmpeg.exe

# Set the FFmpeg executable path
AudioSegment.converter = ffmpeg_executable

# Specify the main directory path you want to explore
main_directory_path = "Q:/4.2/Prototype 39 (Fall-2020)/Theories/CSE-4213 (PR)"

print("Wait a bit......", end='')
# Function to convert bytes to a human-readable format (KB, MB, GB, etc.)
def convert_bytes_to_readable(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 * 1024:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 * 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_in_bytes / (1024 * 1024 * 1024):.2f} GB"

# Function to format an integer with a leading zero if its length is 1
def format_with_zero(number):
    return f"0{number}" if len(str(number)) == 1 else str(number)

# Function to convert duration to hours:minutes:seconds format
def format_duration(duration_seconds):
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{format_with_zero(int(hours))}:{format_with_zero(int(minutes))}:{format_with_zero(int(round(seconds)))}"

# Function to collect file information in a directory and its subdirectories

# Function to collect file information in a directory and its subdirectories
def collect_file_info(directory_path):

    file_info_list = []
    total_video_duration = 0
    total_audio_duration = 0  # Initialize total audio duration

    for root, _, files in os.walk(directory_path):
        for item in files:
            item_path = os.path.join(root, item)
            if os.path.isfile(item_path):
                item_type = "File"
                item_size = os.path.getsize(item_path)
                item_modification_time = os.path.getmtime(item_path)

                # Get the duration for video files
                duration = None
                if item_path.endswith((".mp4", ".avi", ".mkv")):
                    video = VideoFileClip(item_path)
                    duration = video.duration
                    total_video_duration += duration
                    try:
                        video.close()
                    except Exception as e:
                        pass
                elif item_path.endswith((".mp3", ".wav", ".ogg")):
                    audio = AudioSegment.from_file(item_path)  # Create an AudioSegment object
                    duration = len(audio) / 1000.0  # Calculate duration in seconds
                    total_audio_duration += duration  # Add to the total audio duration

                readable_size = convert_bytes_to_readable(item_size)
                formatted_duration = format_duration(duration) if duration is not None else ""


                sleep(.1)
                print('.', end='')
                sleep(.5)
                print('.', end='')
                sleep(.5)
                print('.', end='')
                sleep(.5)
                print('.', end='')
                sleep(.5)
                print('\b\b\b\b',end='')


                file_info_list.append({
                    "Name": item,
                    "Type": os.path.splitext(item)[1],
                    "Size": readable_size,
                    "Duration": formatted_duration
                })

    return file_info_list, total_video_duration, total_audio_duration

file_info_list = []
total_duration =0
total_audio_duration = 0
i = 1
# Ensure the specified path exists and is a directory
if os.path.exists(main_directory_path) and os.path.isdir(main_directory_path):
    # Collect file information for the main directory and its subdirectories
    file_info_list, total_duration, total_audio_duration = collect_file_info(main_directory_path)

else:
    print(f"The specified path '{main_directory_path}' does not exist or is not a directory.")
    i=0

# Display the total duration of video files
total_duration_hours = int(total_duration // 3600)
total_duration_minutes = int((total_duration % 3600) // 60)
total_duration_seconds = int(total_duration % 60)
formatted_total_duration = f"{format_with_zero(total_duration_hours)}:{format_with_zero(total_duration_minutes)}:{format_with_zero(total_duration_seconds)}"

# Display the total duration of video files
total_duration_hours_a = int(total_audio_duration // 3600)
total_duration_minutes_a = int((total_audio_duration % 3600) // 60)
total_duration_seconds_a = int(total_audio_duration % 60)
formatted_total_duration_a = f"{format_with_zero(total_duration_hours_a)}:{format_with_zero(total_duration_minutes_a)}:{format_with_zero(total_duration_seconds_a)}"


text_counts = {}




# Print the collected file information
for file_info in file_info_list:
    text = file_info['Type']
    if text in text_counts:
        text_counts[text] += 1
    else:
        text_counts[text] = 1

print('\b'*20,end='')
print("Complete!!!")
sleep(2)
while i:
    sleep(2)
    # Display menu and get user's choice
    print("\nChoose an option:")
    print("1. Show file information")
    print("2. Show total video duration")
    print("3. Show total audio duration")
    print("4. Show count of files of each types")
    print("0. Exit")
    choice = input("Enter your choice (1/2/3/4/0): ")

    if choice == '0':
        i = 0
        break

    if choice == "1":
        print()
        # Print the collected file information
        for file_info in file_info_list:
            text = file_info['Type']
            print(f"Name: {file_info['Name']}")
            print(f"Type: {file_info['Type']}")
            print(f"Size: {file_info['Size']}")
            # print(f"Modification Time: {file_info['Modification Time']}")
            if file_info['Duration']:
                print(f"Duration: {file_info['Duration']}")
            print()
    elif choice == "2":
        print(f"\nTotal Video Duration: {formatted_total_duration}")
    elif choice == "3":
        print(f"\nTotal Audio Duration: {formatted_total_duration_a}")
    elif choice == "4":
        print()
        # Print the counts in the desired format
        for text, count in text_counts.items():
            print(f"{text} = {count}")

warnings.resetwarnings()