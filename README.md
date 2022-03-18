# Temporal History Parser Tools

## history-parser.sh
Reads a folder with history files, emits CSV with tabular list of workflow histories per row, and Temporal Actions in columns

## history-parser.py
    # Parse one history file:
    python3 history-parser.py -i history-examples/bgc-main-wf.json  -o 'path_to_output.csv'

    # Parse a folder of history files:
    python3 history-parser.py -i history-examples/ -o outputfile.csv

    Outputs Workflow name, # of events, duration, action count, and payload size to a formatted CSV file


## TCTL Commands

    tctl workflow list --print_json >> 'list-output-file'

    tctl workflow show -w 'workflow_id' -r 'run_id' --output_filename 'output_file_name.json'


