#!/bin/bash


RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
ERROR_FLAG=0
CurrentDir="$(pwd)"


# Analyzer ROOT Enviornment & Check if root environment is set
CPVrootEnv="/cvmfs/sft.cern.ch/lcg/views/LCG_102/x86_64-centos7-gcc11-opt/setup.sh"
source "${CPVrootEnv}"
if [ -z "$ROOTSYS" ]; then
  echo -e "${RED}Error : ROOT environment is not properly set. Please check ${CPVrootEnv}.${NC}"
  ERROR_FLAG=1
fi


# Set the AnalyzerPath variable
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(basename "$(dirname "$PWD")")"
if [ "$PARENT_DIR" != "SSBAnalysis" ]; then
  echo -e "${RED}Error : The parent directory is not 'SSBAnalysis'. The current parent directory is. [ $PARENT_DIR ].${NC}"
  ERROR_FLAG=1
fi
cd "${SCRIPT_DIR}/.."
AnalyzerPath="$(pwd)/AnalysisCode"
cd "${CurrentDir}"


# Check if the directory exists
if [ ! -d "$AnalyzerPath" ]; then
  echo -e "${RED}Error : Analyzer Directory $AnalyzerPath does not exist!${NC}"
  ERROR_FLAG=1
fi


# Export the AnalyzerPath variable
export CPVrootEnv
export AnalyzerPath


# Print the log if no errors
if [ $ERROR_FLAG -eq 0 ]; then
  echo -e "${GREEN}\n-----------------------------------------------------------------------------------------${NC}"
  echo -e "${GREEN}\n[ envSetup Log ] : Variables for CPV list maker & condor job are setted as below: \n${NC}"
  echo -e "${GREEN}[ envSetup Log ] : AnalyzerPath (CPV analyzer path)\n      --> [ ${AnalyzerPath} ]${NC}"
  echo -e "${GREEN}[ envSetup Log ] : root environment script\n      --> [ ${CPVrootEnv} ]${NC}"
  echo -e "\n${GREEN}[ envSetup Log ] : Environment Variables are setted\n${NC}"
  echo -e "${GREEN}-----------------------------------------------------------------------------------------${NC}\n"
else
  echo -e "${RED}Error: One or more variables are not properly set. Please check the error messages above.${NC}"
fi
