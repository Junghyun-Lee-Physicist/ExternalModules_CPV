#!/bin/bash

runPeriod="UL2017"
channel="di-muon"
#channel="di-electron"
#channel="muon-electron"
outputName="TestRunOutput.root"

ch="un-defined"
if [ "${channel}" = "di-muon" ]; then
    ch="dimuon.config"
elif [ "${channel}" = "di-electron" ]; then
    ch="dielec.config"
elif [ "${channel}" = "muon-electron" ]; then
    ch="muelec.config"
else
    echo "Unknown Channels: ${channel}"
    exit 1
fi

cfg_forAnalyzer="ULSummer20/${runPeriod}/${ch}"
CWD="$(pwd)"

echo -e "Currently, Analyzer path is setted as [ ${AnalyzerPath} ]"
echo "If this path is weird, please check the [ envSetup.sh ]"
echo "Configure file is setted as [ ${cfg_forAnalyzer} ]"
echo "Also, Output file name is setted as [ ${outputName} ] and will be generated at output directory in analyzer"

cp "testList.list" "${AnalyzerPath}/input/testList.list"

cd "${AnalyzerPath}"

./ssb_analysis "testList.list" "TestRunOutput.root" "${cfg_forAnalyzer}"

rm -rf "${AnalyzerPath}/input/testList.list"
mv "${AnalyzerPath}/output/${outputName}" "${CWD}"

cd "${CWD}"
