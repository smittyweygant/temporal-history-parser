import json, argparse, time, collections
from datetime import datetime, timezone
from xml.sax.xmlreader import InputSource
from dateutil.parser import *

class Event:
    def __init__(self, eventId, eventType, eventTime):
        self.eventId = int(eventId)
        self.eventType = eventType
        self.eventTime = parse(eventTime)
        self.isAction = bool

class Workflow:
    def __init__(self):
        self.events = []

    def addevent(self, event):
        # print(event.eventId)
        self.events.append(event)

    def eventcount(self) -> int:
        return len(self.events)

    def geteventtypebyid(self, id) -> str:
        for event in self.events:
            if(event.eventId == id):
                print("ID: ", id, "Matches: ", event.eventId)
                return(event.eventType)

    def geteventtimebyid(self, id) -> str:
        for event1 in self.events:
            # print("self.events Type: ", type(self.events))
            # print("Instance Type: ", type(event1))
            # print("Instance: ", event1)
            # print("id: ", type(id), id)
            # print("event1.eventId: ", type(event1.eventId), event1.eventId)
            if(event1.eventId == int(id)):
                print("ID: ", id, "Matches: ", str(event1.eventId))
                return(event1.eventType)

    def getDuration(self) -> str:
        count = len(self.events)
        starttime = self.events[0].eventTime
        endtime = self.events[count-1].eventTime
        return(endtime-starttime)

class Action:
    actiontypes = ["ChildWorkflow", "Activity", "LocalActivity", "SignalWorkflow", "SignalExternalWorkflow", "Timer", "QuerySearchAttribute"]
    actiondict = {"StartChildWorkflowExecutionInitiated" : "ChildWorkflow", "ActivityTaskStarted" : "Activity", '"markerName" : "LocalActivity"' : "LocalActivity", "WorkflowExecutionSignaled" : "SignalIntoWorkflow", "ExternalWorkflowExecutionSignaled" : "SignalExternalWorkflow", "TimerStarted" : "Timer", "UpsertWorkflowSearchAttributes" : "QuerySearchAttribute"}


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile")
# parser.add_argument("-o", "--outputfile")
args = parser.parse_args()

# example: inputfile = "inputfiles/smitty-bgc-wf.json"

inputfile = args.inputfile

# outputfile = args.outputfile

i = open(inputfile, "r")

# o = open(outputfile, "w")

j = json.loads(i.read())

events = j["events"]

workflow = Workflow()

for event in events:
    eventinst = Event(event["eventId"], event["eventType"], event["eventTime"])
    result = workflow.addevent(eventinst)
    # result = workflow.addevent(Event(event["eventId"], event["eventType"], event["eventTime"]))


print("Event Count in Workflow: ", workflow.eventcount())

print("Event ID: 1 Type: ", workflow.geteventtypebyid(1))

print("Workflow Duration: ", workflow.getDuration())

print("Event Time by ID: 3", workflow.geteventtimebyid(3))

# Event Types with Input fields
# WorkflowExecutionStarted.workflowExecutionStartedEventAttributes.input
# StartChildWorkflowExecutionInitiated.startChildWorkflowExecutionInitiatedEventAttributes.input
# activityTaskScheduled.activityTaskScheduledEventAttributes.input
# WorkflowExecutionSignaled.workflowExecutionSignaledEventAttributes.input


# Event Types with Results
# ChildWorkflowExecutionCompleted.childWorkflowExecutionCompletedEventAttributes.result
# ActivityTaskCompleted.activityTaskCompletedEventAttributes.result
# WorkflowExecutionCompleted.workflowExecutionCompletedEventAttributes.result
