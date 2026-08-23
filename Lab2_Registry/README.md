# Lab 2 – Windows Registry Forensics

## Objective
To analyse a Windows NTUSER.DAT Registry hive and identify forensic artefacts related to user activity, recently accessed documents, applications, and file paths.

## Tools Used
- REMnux
- Python python-registry
- Linux command-line tools
- Windows Registry NTUSER.DAT

## Analysis Performed
- Verified the NTUSER.DAT evidence file using SHA-256 hashing.
- Examined Registry keys and subkeys.
- Analysed RecentDocs for recently accessed documents.
- Examined UserAssist for evidence of application activity.
- Analysed TypedPaths for previously accessed locations.
- Reviewed Registry timestamps to help reconstruct user activity.

## Key Findings
- Recent document artefacts were successfully recovered from NTUSER.DAT.
- DOCX-related artefacts included files such as `Payment info.docx`.
- UserAssist contained evidence of application activity.
- TypedPaths revealed previously accessed locations including:
  - `C:\ProjectWorkingFolder\ShellBagsExplorer`
  - `C:\`
  - `D:\`
  - `Recycle Bin`

## Conclusion
This lab demonstrated how Windows Registry artefacts within NTUSER.DAT can be analysed during a digital forensic investigation to identify recent documents, application activity, accessed locations, and historical user activity.