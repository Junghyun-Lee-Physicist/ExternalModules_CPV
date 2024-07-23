#!/bin/bash

cfg_forAnalyzer="analysis_config_2017.config"
CWD="$(pwd)"

echo -e "Currently, Analyzer path is setted as [ ${AnalyzerPath} ]"
echo "If this path is weird, please check the [ envSetup.sh ]"

cp "testList.list" "${AnalyzerPath}/input/testList.list"

cd "${AnalyzerPath}"

./ssb_analysis "testList.list" "${CWD}/TestRunOutput.root" "${cfg_forAnalyzer}"

rm -rf "${AnalyzerPath}/input/testList.list"

cd "${CWD}"
