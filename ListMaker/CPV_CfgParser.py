#!/usr/bin/env python3

import os
import re
import sys

class Parser:
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.samples = []
        self.output_dir_name = ""

    def print_usage(self):
        usage = """
        --------------------------------------------------------
        How to write configuration file to make CPV list

        Usage:
           !OutputDirName: "<Directory to store output lists>"
           % name: "<Sample Name>"
           % numberOfFiles: <Number of Files per list>
               path: "<Path to Sample Directory 1>",
                     "<Path to Sample Directory 2>"
        Symbols:
        - [ ! ] : Defines the output directory name
        - [ % ] : Defines a new sample entry
        - [ : ] : Separates attribute names and values
        --------------------------------------------------------
        """
        print(f"  [Parser Log] : {usage}")

    def parse_cfg(self):
        with open(self.cfg_file, 'r') as file:
            lines = file.readlines()

        current_sample = {}
        output_dir_found = False

        for line in lines:
            line = line.strip()

            # Output directory name
            output_dir_match = re.match(r'!\s*OutputDirName\s*:\s*"(.+)"', line)
            if output_dir_match:
                self.output_dir_name = output_dir_match.group(1)
                print(f"  [Parser Log] : Output Directory Name set to {self.output_dir_name}")
                output_dir_found = True
                continue

            # Sample name
            name_match = re.match(r'%\s*name\s*:\s*"(.+)"', line)
            if name_match:
                if current_sample:
                    self.samples.append(current_sample)
                current_sample = {
                    'name': name_match.group(1),
                    'paths': []
                }
                continue

            # Number of files
            num_match = re.match(r'%\s*numberOfFiles\s*:\s*(\d+)', line)
            if num_match:
                current_sample['num_files'] = int(num_match.group(1))
                continue

            # Paths
            path_match = re.match(r'\s*\$path\s*:\s*"(.+)"\s*,?', line)
            if path_match:
                current_sample['paths'].append(path_match.group(1))
            else:
                additional_path_match = re.match(r'\s*"\s*(.+)"\s*,?', line)
                if additional_path_match:
                    current_sample['paths'].append(additional_path_match.group(1))

        if current_sample:
            self.samples.append(current_sample)

        if not output_dir_found:
            print(f"  [Parser Error] : Output directory name not defined in the configuration file.")
            sys.exit(1)

    def check_format(self):
        for sample in self.samples:
            if 'name' not in sample or 'num_files' not in sample or 'paths' not in sample:
                print(f"  [Parser Error] : Sample format is incorrect.")
                sys.exit(1)
            if not sample['paths']:
                print(f"  [Parser Error] : No paths defined for sample '{sample['name']}'")
                sys.exit(1)

    def check_paths(self):
        for sample in self.samples:
            print(f"  [Parser Log] : Checking paths for sample '{sample['name']}'")
            for path in sample['paths']:
                if not os.path.exists(path):
                    print(f"  [Parser Error] : Path does not exist - {path}")
                    sys.exit(1)
                else:
                    total_files = 0
                    for root, _, files in os.walk(path):
                        num_files = len([f for f in files if f.endswith('.root')])
                        total_files += num_files
                    if total_files == 0:
                        print(f"  [Parser Error] : Path '{path}' contains 0 root files")
                        sys.exit(1)
                    else:
                        print(f"  [Parser Log] : Path '{path}' contains {total_files} root files")

    def get_samples(self):
        return self.samples

    def get_output_dir_name(self):
        return self.output_dir_name

