# Temporal History Parser Tools

## Parser.sh
Reads a folder with history files, emits CSV with tabular list of workflow histories per row, and Temporal Actions in columns

## Parser.py
    python3 history-parser.py -i history-examples/bgc-main-wf.json  

    Workflow Events:  59
    Workflow Duration:  0:00:59.380927
    Actions in Workflow:  7
    Payload Size (bytes):  5324


## TCTL Commands

    tctl workflow list --print_json >> 'list-output-file'

    tctl workflow show -w 'workflow_id' -r 'run_id' --output_filename 'output_file_name.json'


