import json, argparse, datetime
from dateutil.parser import *

class Event:
    def __init__(self, eventId, eventType, eventTime, dataInputResult):
        self.eventId = int(eventId)
        self.eventType = eventType
        self.eventTime = parse(eventTime)
        self.isAction = bool
        self.actionType = str
        self.dataInputResult = dataInputResult

class Workflow:
    def __init__(self):
        self.events = []

    def addevent(self, event):
        # refactor below using match : case statement in Python 3.10+

        if event.eventType == "WorkflowExecutionStarted":
            event.isAction = True
            event.actionType = "Workflow Execution Started"
        elif event.eventType == "StartChildWorkflowExecutionInitiated":
            event.isAction = True
            event.actionType = "Child Workflow Execution Started"
        elif event.eventType == "activityTaskScheduled":
            event.isAction = True
            event.actionType = "Activity Task Scheduled"
        elif event.eventType == "WorkflowExecutionSignaled":
            event.isAction = True
            event.actionType = "Workflow Execution Signaled"   
        elif event.eventType == "ExternalWorkflowExecutionSignaled":
            event.isAction = True
            event.actionType = "External Workflow Signaled"
        elif event.eventType == "ChildWorkflowExecutionCompleted":
            event.isAction = False
            event.actionType = "Child Workflow Execution Completed"
        elif event.eventType == "ActivityTaskCompleted":
            event.isAction = False
            event.actionType = "Activity Task Completed"
        elif event.eventType == "ActivityTaskCompleted":
            event.isAction = False
            event.actionType = "Activity Task Completed"
        elif event.eventType == "TimerStarted":
            event.isAction = True
            event.actionType = "Timer Started"
        else:
            event.isAction = False
        self.events.append(event)

    def eventCount(self) -> int:
        return len(self.events)
    
    def getDuration(self) -> str:
        count = len(self.events)
        starttime = self.events[0].eventTime
        endtime = self.events[count-1].eventTime
        return(endtime-starttime)

    def geteventtypebyid(self, id) -> str:
        for event in self.events:
            if(event.eventId == id):
                return(event.eventType)

    def geteventtimebyid(self, id) -> str:
        for event in self.events:
            if(event.eventId == int(id)):
                return(event.eventType)
    
    def actionCount(self) -> int:
        actioncount = 0
        for event in self.events:
            if event.isAction:
                actioncount += 1
        return actioncount
    
    def payloadSize(self) -> int:
        payloadsize = 0
        for event in self.events:
            if event.dataInputResult != "":
                s = str(event.dataInputResult)
                payloadsize = payloadsize + len(s.encode('utf-8'))
        return payloadsize
                
class Action:
    actiontypes = ["ChildWorkflow", "Activity", "LocalActivity", "SignalWorkflow", "SignalExternalWorkflow", "Timer", "QuerySearchAttribute"]
    actiondict = {"StartChildWorkflowExecutionInitiated" : "ChildWorkflow", "ActivityTaskStarted" : "Activity", '"markerName" : "LocalActivity"' : "LocalActivity", "WorkflowExecutionSignaled" : "SignalIntoWorkflow", "ExternalWorkflowExecutionSignaled" : "SignalExternalWorkflow", "TimerStarted" : "Timer", "UpsertWorkflowSearchAttributes" : "QuerySearchAttribute"}

def get_payload_from_event(event) -> str:
        dataInputResult = ""
        if "workflowExecutionStartedEventAttributes" in event:
            dataInputResult = event["workflowExecutionStartedEventAttributes"]["input"]
        elif "startChildWorkflowExecutionInitiatedEventAttributes" in event:
            dataInputResult = event["startChildWorkflowExecutionInitiatedEventAttributes"]["input"]
        elif "activityTaskScheduledEventAttributes" in event:
            dataInputResult = event["activityTaskScheduledEventAttributes"]["input"]
        elif "workflowExecutionSignaledEventAttributes" in event:
            dataInputResult = event["workflowExecutionSignaledEventAttributes"]["input"]
        elif "childWorkflowExecutionCompletedEventAttributes" in event:
            dataInputResult = event["childWorkflowExecutionCompletedEventAttributes"]["result"]
        elif "activityTaskCompletedEventAttributes" in event:
            dataInputResult = event["activityTaskCompletedEventAttributes"]["result"]
        elif "workflowExecutionCompletedEventAttributes" in event:
            dataInputResult = event["workflowExecutionCompletedEventAttributes"]["result"]
        else:
            pass
        return dataInputResult

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile")
# parser.add_argument("-o", "--outputfile")
args = parser.parse_args()

# example: inputfile = "inputfiles/smitty-bgc-wf.json"

inputfile = args.inputfile
i = open(inputfile, "r")

# outputfile = args.outputfile
# o = open(outputfile, "w")

j = json.loads(i.read())

events = j["events"]

workflow = Workflow()

for event in events:
    dataInputResult = get_payload_from_event(event)
    eventinst = Event(event["eventId"], event["eventType"], event["eventTime"], dataInputResult)
    workflow.addevent(eventinst)

print("Workflow Events: ", workflow.eventCount())

print("Workflow Duration: ", workflow.getDuration())

print ("Actions in Workflow: ", workflow.actionCount())

print ("Payload Size (bytes): ", workflow.payloadSize())
