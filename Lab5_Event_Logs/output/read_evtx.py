from Evtx.Evtx import Evtx

evtx_file = "/home/remnux/Lab5_Event_Logs/evidence/4624_mimikatz_sekurlsa_pth_source_machine.evtx"

with Evtx(evtx_file) as log:
    for record in log.records():
        print(record.xml())
