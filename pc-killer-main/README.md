# Killer
## Introduction

This Python script generates large text files filled with random ASCII characters. It's useful for simulating scenarios where large volumes of data are needed, such as testing file processing algorithms or storage systems.
## Prerequisites

To run this script, ensure you have Python installed on your system.
## Usage

    Clone or download this repository to your local machine.
    Navigate to the directory containing the script (large_text_file_generator.py).
    Open a terminal or command prompt in that directory.
    Run the script using the following command:

    python killer.py

    The script will prompt you to enter the desired number of large text files to generate. Enter the number and press Enter.
    The script will start generating large text files named large_file_<index>.txt, where <index> ranges from 0 to the specified number minus one. Each file will contain approximately 1GB of random ASCII data.

## Customization

    You can modify the size_gb variable in the script to change the size of each generated file.
    Adjusting the chunk size (chunk_size variable) can also affect the performance and memory usage of the script. Be cautious when changing this value.
