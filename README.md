# Temporal History Parser Tools

## Parser.sh
Reads a folder with history files, emits CSV with tabular list of workflow histories per row, and Temporal Actions in columns

## Parser.py
<<<<<<< HEAD
    python3 history-parser.py -i history-examples/bgc-main-wf.json  

    Workflow Events:  59
    Workflow Duration:  0:00:59.380927
    Actions in Workflow:  7
    Payload Size (bytes):  5324
=======
python3 history-parser.py -i history-examples/bgc-main-wf.json  
Workflow Events:  59
Workflow Duration:  0:00:59.380927
Actions in Workflow:  7
Payload Size (bytes):  5324
>>>>>>> d401a6001e5f113af4ef1eaaca00efcd8434404d


## TCTL Commands

    tctl workflow list --print_json >> 'list-output-file'

<<<<<<< HEAD
    tctl workflow show -w 'workflow_id' -r 'run_id' --output_filename 'output_file_name.json'
=======
tctl workflow list --print_json >> 'list-output-file'

tctl workflow show -w 'workflow_id' -r 'run_id' --output_filename 'output_file_name.json'
>>>>>>> d401a6001e5f113af4ef1eaaca00efcd8434404d


