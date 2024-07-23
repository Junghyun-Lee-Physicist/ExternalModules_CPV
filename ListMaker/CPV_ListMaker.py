#!/usr/bin/env python3

import os
import re
import sys
import shutil
from CPV_CfgParser import Parser

class ListMaker:
    def __init__(self, samples, output_dir_path):
        self.samples = samples
        self.output_dir_path = output_dir_path

    def create_lists(self):
        if os.path.exists(self.output_dir_path):
            print(f"  [ListMaker Error] : Output directory '{self.output_dir_path}' already exists")
            sys.exit(1)

        os.makedirs(self.output_dir_path)
        print(f"  [ListMaker Log] : Created output directory '{self.output_dir_path}'")

        result_log = []

        for sample in self.samples:
            sample_dir = os.path.join(self.output_dir_path, sample['name'])
            os.makedirs(sample_dir)
            print(f"  [ListMaker Log] : Created sample directory '{sample_dir}'")

            all_files = []
            for path in sample['paths']:
                dcap_path = path.replace("/pnfs", "dcap://cluster142.knu.ac.kr//pnfs")
                for root, _, files in os.walk(path):
                    for file in sorted(files, key=lambda x: int(re.search(r'\d+', x).group())):  # Ensure files are sorted numerically
                        if file.endswith('.root'):
                            all_files.append(os.path.join(dcap_path, os.path.relpath(os.path.join(root, file), path)))

            num_files_per_list = sample['num_files']
            total_root_files = len(all_files)
            list_count = 0

            for i in range(0, total_root_files, num_files_per_list):
                list_file_path = os.path.join(sample_dir, f"{sample['name']}_{i//num_files_per_list + 1}.list")
                with open(list_file_path, 'w') as list_file:
                    list_file.writelines(f"{file}\n" for file in all_files[i:i + num_files_per_list])
                list_count += 1

            result_log.append(f"%Sample name : {sample['name']}\n"
                              f"    $Number of List : {list_count}\n"
                              f"    $Total Number of Root Files : {total_root_files}\n\n")

        with open(os.path.join(self.output_dir_path, "ListResult.txt"), 'w') as result_file:
            result_file.writelines(result_log)

        print(f"\n  [ListMaker Log] : Output directory '{self.output_dir_path}' created with {len(self.samples)} samples and ListResult.txt")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process CPV list creation.")
    parser.add_argument('cfg_file', type=str, help='Configuration file path')
    parser.add_argument('-rm', '--remove', action='store_true', help='Remove the output directory')
    parser.add_argument('-f', '--force', action='store_true', help='Force remove the output directory and create lists')

    args = parser.parse_args()

    cfg_file = args.cfg_file
    remove_flag = args.remove
    force_flag = args.force

    parser = Parser(cfg_file)

    # Print usage
    parser.print_usage()

    # Parse the CFG file
    parser.parse_cfg()

    # Check the format
    parser.check_format()

    # Check the paths
    parser.check_paths()

    # Get the samples and output directory name
    samples = parser.get_samples()
    output_dir_name = parser.get_output_dir_name()

    # Combine with AnalyzerPath from environment variable
    analyzer_path = os.environ.get("AnalyzerPath")
    if not analyzer_path or not os.path.isdir(analyzer_path):
        print(f"  [ListMaker Error] : AnalyzerPath '{analyzer_path}' does not exist.")
        sys.exit(1)
    output_dir_path = os.path.join(analyzer_path, "input", output_dir_name)

    # Remove the output directory if the remove flag is set
    if remove_flag or force_flag:
        if os.path.exists(output_dir_path):
            print(f"  [ListMaker Log] : Removing directory '{output_dir_path}'")
            shutil.rmtree(output_dir_path)
            shutil.rmtree("__pycache__")

    # Create the lists if the force flag is set or remove flag is not set
    if force_flag or not remove_flag:
        try:
            list_maker = ListMaker(samples, output_dir_path)
            list_maker.create_lists()
        except Exception as e:
            print(f"  [ListMaker Error] : {e}")
            sys.exit(1)

