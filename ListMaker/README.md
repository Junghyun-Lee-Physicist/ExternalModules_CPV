
English README:
ListMaker is a Python script designed to generate lists of ROOT files from specified directories. It reads configurations from a CFG file and utilizes CPV_CfgParser.py to parse these configurations.


Requirements
Python 3.x
CPV_CfgParser.py: Ensure this module is in the same directory or accessible in your Python path.
Environment Variable: Set AnalyzerPath to your analyzer's directory path.

Usage
To run the script, use the following command:

Example
python3 CPV_ListMaker.py ListMakerCfg/<config_file>.cfg
This command executes the script using <config_file>.cfg as the configuration file.

Notes
The script uses CPV_CfgParser.py to parse the configuration file.
Ensure the AnalyzerPath environment variable is correctly set before running the script.


한글 설명:
ListMaker는 지정된 디렉토리에서 ROOT 파일 목록을 생성하기 위한 파이썬 스크립트입니다. CFG 파일에서 설정을 읽고 CPV_CfgParser.py를 사용하여 해당 설정을 파싱합니다.

요구 사항
Python 3.x
CPV_CfgParser.py: 이 모듈이 동일한 디렉토리에 있거나 Python 경로에서 접근 가능해야 합니다.
환경 변수: AnalyzerPath를 분석기 디렉토리의 경로로 설정하세요.

사용법
스크립트를 실행하려면 다음 명령어를 사용합니다:

예시
python3 CPV_ListMaker.py ListMakerCfg/<config_file>.cfg
이 명령은 <config_file>.cfg를 설정 파일로 사용하여 스크립트를 실행합니다.

참고 사항
스크립트는 CPV_CfgParser.py를 사용하여 설정 파일을 파싱합니다.
스크립트를 실행하기 전에 AnalyzerPath 환경 변수가 올바르게 설정되어 있는지 확인하세요.
