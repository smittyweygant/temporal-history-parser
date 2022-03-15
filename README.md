# Temporal History Parser Tools

TODO: 
Sh - read single file



## Parser.sh
Reads a folder with history files, emits CSV with tabular list of workflow histories per row, and Temporal Actions in columns


## Parser.py



## TCTL Commands


tctl workflow list --print_json >> ~/Development/temporalio/bgc_wf_list.json


tctl workflow show -w BackgroundCheck:joe123@test.com -r 41c1ebaf-9cf1-4037-b259-33e8fe996766 --output_filename ../joe123.json




## Temporal Event Type Reference

WorkflowExecutionSignaled

WorkflowActivityTaskScheduled
- activityTaskScheduledEventAttributes
    - activityType
        - name: (name)
    - input
        - payloads []

ExternalWorkflowExecutionSignaled

markerRecorded
- markerRecordedEventAttributes
    - markerName (Local Activity)