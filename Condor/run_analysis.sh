#!/bin/bash

# Define the main path and change to that directory
MainPath=$1
cd "${MainPath}"
echo "  [ Condor Exe Log ] Setted Main Work Directory"
echo "  [ Condor Exe Log ]   -->  ${MainPath}"

# Set up the environment
# Below is the ROOT Env setting from envSetup
rootEnv="$2"
source "${rootEnv}"
echo "  [ Condor Exe Log ] Root envrionment for condor system is setted as"
echo "  [ Condor Exe Log ]   --> ${rootEnv}"

# Get the input arguments
inputListPath=$3
inputListName=$4
outputDir=$5
outputName=$6
outputPath=$7
cfgName=$8

echo "inputListPath: ${inputListPath}"
echo "inputListName: ${inputListName}"
echo "outputDir: ${outputDir}"
echo "outputName: ${outputName}"

# Create the output directory if it doesn't exist
# in ssb_analysis.cpp, you need to set the dsipcap path for using SE_Storage
mkdir -p "${outputPath}/${outputDir}"

# Run the analysis
echo "  [ Condor Exe Log ] Now jobs will be proceeded"
./ssb_analysis "${inputListPath}/${inputListName}.list" "${outputDir}/${outputName}" "${cfgName}"
echo "  [ condor Exe Log ] Jobs done!!!"

