# Job Submission Script for HTCondor

This Python script automates the process of creating and submitting jobs to HTCondor for high-energy physics analyses. It generates Condor submit files based on the input lists provided and submits them to the Condor scheduler. The script also handles the creation of necessary directories and symbolic links for organizing output files.

## Description

- **Creates Condor submit files** for each sample directory found in the input list directories.
- **Submits jobs** to HTCondor using the generated submit files.
- **Creates necessary directories** for logs and submissions.
- **Creates a symbolic link** from the local output directory to the storage path, ensuring that outputs are stored correctly.
- **Checks for existing paths** to prevent overwriting existing data or symbolic links.

## Requirements

- **Python 3.x**
- **HTCondor** installed and configured.
- **Environment Variables**:
  - `AnalyzerPath`: Path to your analyzer directory.
  - `CPVrootEnv`: Path to your ROOT environment setup script.

## Usage

1. **Set Environment Variables**:

   Make sure to export the necessary environment variables before running the script:

   ```bash
   export AnalyzerPath=/path/to/your/analyzer
   export CPVrootEnv=/path/to/your/root/envSetup.sh

2. **Configure the Script**:

   Modify the following variables in the script as needed:

   - JobName: A unique name for this set of jobs.
   - MCListDirName: Directory name containing MC input lists.
   - DataListDirName: Directory name containing Data input lists.
   - outputPath: Path to the storage directory where output files will be saved.
   - cfgName: Path to your configuration file.

3. **Run the Script**:

```bash
python3 submit_condor_jobs.py

Replace submit_condor_jobs.py with the actual filename of your script.

## Important Notes
Job Name Uniqueness:

The JobName should be unique to prevent conflicts with existing jobs.
If a symbolic link or directory with the same JobName already exists in the output directory, the script will exit with an error message.
Directory Permissions:

Ensure you have the necessary permissions to create directories and symbolic links in both the local and storage paths.
Sample Types:

The script currently processes MC samples. To process Data samples, you can modify the script to call submit_jobs("Data", inputListData) accordingly.
Script Overview
Environment Variables:

Retrieves AnalyzerPath and CPVrootEnv from the environment.
Directory Setup:

Creates condorLog and condorSubmit directories for logs and submit files.
Symbolic Link Creation:

Checks for existing symbolic links or directories to prevent overwriting.
Creates a symbolic link from {AnalyzerPath}/output/{JobName} to {outputPath}/{JobName}.
Job Submission Function (submit_jobs):

Iterates over sample directories in the input list path.
Constructs Condor submit file content with the appropriate arguments.
Writes the submit file and submits the job using condor_submit.

Error Handling
If the symbolic link or target path already exists, the script will output an error message and exit.
Ensure that JobName does not conflict with existing jobs or directories.



작업 제출 스크립트 (HTCondor용)
이 파이썬 스크립트는 고에너지 물리 분석을 위한 HTCondor 작업 생성 및 제출 과정을 자동화합니다. 제공된 입력 목록을 기반으로 Condor 제출 파일을 생성하고 Condor 스케줄러에 제출합니다. 또한 출력 파일을 정리하기 위해 필요한 디렉토리와 심볼릭 링크를 생성합니다.

설명
Condor 제출 파일 생성: 입력 목록 디렉토리에서 각 샘플 디렉토리에 대해 제출 파일을 생성합니다.
작업 제출: 생성된 제출 파일을 사용하여 HTCondor에 작업을 제출합니다.
필요한 디렉토리 생성: 로그 및 제출 파일을 위한 디렉토리를 생성합니다.
심볼릭 링크 생성: 로컬 출력 디렉토리에서 스토리지 경로로 심볼릭 링크를 생성하여 출력이 올바르게 저장되도록 합니다.
기존 경로 확인: 기존 데이터나 심볼릭 링크를 덮어쓰지 않도록 경로를 확인합니다.

요구 사항
Python 3.x
HTCondor 설치 및 구성 완료
환경 변수:
AnalyzerPath: 분석기 디렉토리의 경로
CPVrootEnv: ROOT 환경 설정 스크립트의 경로

사용법
환경 변수 설정:

스크립트를 실행하기 전에 필요한 환경 변수를 설정하세요:

export AnalyzerPath=/path/to/your/analyzer
export CPVrootEnv=/path/to/your/root/envSetup.sh

스크립트 구성:

스크립트 내에서 다음 변수를 필요에 따라 수정하세요:

JobName: 이 작업 집합에 대한 고유한 이름
MCListDirName: MC 입력 목록을 포함하는 디렉토리 이름
DataListDirName: 데이터 입력 목록을 포함하는 디렉토리 이름
outputPath: 출력 파일이 저장될 스토리지 디렉토리 경로
cfgName: 구성 파일의 경로

스크립트 실행:

python3 submit_condor_jobs.py
스크립트 파일 이름이 다르면 해당 이름으로 변경하세요.

중요 사항
작업 이름의 고유성:

JobName은 충돌을 방지하기 위해 고유해야 합니다.
출력 디렉토리에 동일한 JobName의 심볼릭 링크나 디렉토리가 이미 존재하는 경우 스크립트는 오류 메시지를 출력하고 종료합니다.
디렉토리 권한:

로컬 및 스토리지 경로에서 디렉토리와 심볼릭 링크를 생성할 수 있는 권한이 있는지 확인하세요.
샘플 유형:

현재 스크립트는 MC 샘플을 처리합니다. 데이터 샘플을 처리하려면 스크립트를 수정하여 submit_jobs("Data", inputListData)를 호출하세요.
스크립트 개요
환경 변수:

AnalyzerPath와 CPVrootEnv를 환경에서 가져옵니다.
디렉토리 설정:

로그와 제출 파일을 위한 condorLog와 condorSubmit 디렉토리를 생성합니다.
심볼릭 링크 생성:

기존 심볼릭 링크나 디렉토리가 있는지 확인하여 덮어쓰지 않도록 합니다.
{AnalyzerPath}/output/{JobName}에서 {outputPath}/{JobName}으로 심볼릭 링크를 생성합니다.
작업 제출 함수 (submit_jobs):

입력 목록 경로의 샘플 디렉토리를 반복합니다.
적절한 인수를 사용하여 Condor 제출 파일 내용을 구성합니다.
제출 파일을 작성하고 condor_submit을 사용하여 작업을 제출합니다.

오류 처리
심볼릭 링크나 대상 경로가 이미 존재하는 경우 스크립트는 오류 메시지를 출력하고 종료합니다.
JobName이 기존 작업이나 디렉토리와 충돌하지 않는지 확인하세요.

