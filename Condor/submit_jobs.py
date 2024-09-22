import os
import subprocess

MainPath = os.environ.get("AnalyzerPath") # It will bring AnalyzerPath variables from envSetup.sh
rootEnv = os.environ.get("CPVrootEnv") # It will bring ROOT Environment variables from envSetup.sh

JobName = "UL2017_dimuon"
MCListDirName = "2017MCList"
DataListDirName = "2017DataList"
logDir = os.path.join(os.getcwd(), "condorLog")
submitDir = os.path.join(os.getcwd(), "condorSubmit")
runScriptPath = os.path.join(os.getcwd(), "run_analysis.sh")
outputPath = "/pnfs/knu.ac.kr/data/cms/store/user/junghyun/CPV"
cfgName = "ULSummer20/UL2017/dimuon.config"

inputListMC = os.path.join(MainPath, "input", MCListDirName)
inputListData = os.path.join(MainPath, "input", DataListDirName)

# Create the necessary directories if they don't exist
os.makedirs(logDir, exist_ok=True)
os.makedirs(submitDir, exist_ok=True)

# Create symbolic link from {MainPath}/output/{JobName} to {outputPath}/{JobName}
symlink_dir = os.path.join(MainPath, "output")
symlink_path = os.path.join(symlink_dir, JobName)
target_path = os.path.join(outputPath, JobName)

# Check if the symbolic link already exists
if os.path.islink(symlink_path):
    print(f"  [Error] Symbolic link '{symlink_path}' already exists. Please check the job name.")
    sys.exit(1)
elif os.path.exists(symlink_path):
    # If a file or directory with the same name exists but is not a symbolic link
    print(f"  [Error] Path '{symlink_path}' already exists and is not a symbolic link. Please check the job name.")
    sys.exit(1)
else:
    # Ensure the directory for the symbolic link exists
    os.makedirs(symlink_dir, exist_ok=True)

    # Check if the target path already exists
    if os.path.exists(target_path):
        print(f"  [Error] Target path '{target_path}' already exists. Please check the job name.")
        sys.exit(1)
    else:
        # Make output directory at Storage
        os.makedirs(target_path)

    # Create the symbolic link
    os.symlink(target_path, symlink_path)
    print(f"  [Log] Created symbolic link '{symlink_path}' pointing to '{target_path}'")


#################################################################################################

def submit_jobs(sampleType, inputListPath):

    for sampleDir in os.listdir(inputListPath):
        fullSampleDir = os.path.join(inputListPath, sampleDir)
        if os.path.isdir(fullSampleDir):
            if(sampleType == "MC"):
                inputDir = f"{MCListDirName}"
                outputDir = os.path.join(JobName, "MC", sampleDir)
            elif(sampleType == "Data"):
                inputDir = f"{DataListDirName}"
                outputDir = os.path.join(JobName, "Data", sampleDir)
           
            submit_file_content = f"""Universe   = vanilla
Executable = {runScriptPath}
Log        = {logDir}/{sampleDir}.log
Output     = {logDir}/{sampleDir}.out
Error      = {logDir}/{sampleDir}.err
RequestMemory = 4 GB
RequestCpus = 1
Arguments  = {MainPath} {rootEnv} {inputDir}/{sampleDir} $(InputListName) {outputDir} $(OutputName) {outputPath} {cfgName}
Queue InputListName, OutputName from (
"""
            for listFile in os.listdir(os.path.join(inputListPath, sampleDir)):
                if listFile.endswith(".list"):
                    listFileName = os.path.splitext(listFile)[0]
                    outputName = f"{listFileName}.root"
                    submit_file_content += f"{listFileName} {outputName}\n"
    
            submit_file_content += ")\n"
            
            submit_file_path = os.path.join(submitDir, f"submit_{sampleDir}.sub")
            with open(submit_file_path, "w") as submit_file:
                submit_file.write(submit_file_content)
            
            subprocess.run(["condor_submit", submit_file_path])

#####################################################

# Submit jobs for MC samples
submit_jobs("MC", inputListMC)

# Submit jobs for Data samples
submit_jobs("Data", inputListData)

#####################################################

