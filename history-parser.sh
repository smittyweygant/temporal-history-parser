#!/bin/bash

while getopts d:f:o: flag
do
    case "${flag}" in
        d) directory=${OPTARG};;
        f) filename=${OPTARG};;
        o) output=${OPTARG};;
    esac
done
touch $output
echo "file,childworkflow,activitytaskstarted,localactivitymarker,workflowexecutionsignaled,externalworkflowexecutionsignaled,timerstarted,searchattribute" >> $output

for file in "$directory"/*; do
    childworkflows=$(grep -o -i '"StartChildWorkflowExecutionInitiated"' "$file" | wc -l)
    activitytasks=$(grep -o -i '"ActivityTaskStarted"' "$file" | wc -l)
    localactivities=$(grep -o -i '"markerName":"LocalActivity"' "$file" | wc -l)
    workflowsignals=$(grep -o -i '"WorkflowExecutionSignaled"' "$file" | wc -l  )
    externalworkflowsignals=$(grep -o -i '"ExternalWorkflowExecutionSignaled"' "$file" | wc -l)
    timers=$(grep -o -i '"TimerStarted"' "$file" | wc -l)
    searchattribute=$(grep -o -i '"UpsertWorkflowSearchAttributes"' "$file" | wc -l)

    echo $(basename "$file")
    echo "ChildWorkflow: " $childworkflows
    echo "ActivityTaskStarted: " $activitytasks
    echo "markerName: Local Activity: " $localactivities
    echo "WorkflowExecutionSignaled: " $workflowsignals
    echo "ExternalWorkflowExecutionSignaled: " $externalworkflowsignals
    echo "TimerStarted: " $timers
    echo "Search Attribute Updated: " $searchattribute

    echo "${file##*/},$childworkflows,$activitytasks,$localactivities,$workflowsignals,$externalworkflowsignals,$timers,$searchattribute" >> $output
    
done

