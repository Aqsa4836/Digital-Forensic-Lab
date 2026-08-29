# Lab 3 – Windows Prefetch Forensics

## Objective

To analyse a Windows Prefetch (`.pf`) file and identify forensic artefacts related to application execution.

## Tools Used

- REMnux
- Python
- Windows Prefetch Parser
- Linux command-line tools

## Evidence Analysed

**File:** `CMD.EXE-4A81B364.pf`

The Prefetch file was verified using SHA-256 hashing before analysis to support evidence integrity.

## Analysis Performed

- Identified the Prefetch evidence file.
- Calculated its SHA-256 hash.
- Parsed the Prefetch file using a Python-based Prefetch parser.
- Examined the executable name and recorded run count.
- Examined the recorded last execution timestamp.
- Examined volume information and loaded resources.

## Key Findings

- **Executable:** `CMD.EXE`
- **Recorded Run Count:** `2`
- **Last Executed:** `2016-01-16 20:26:42`
- **Volume:** `\DEVICE\HARDDISKVOLUME2`
- **Volume Serial Number:** `88008c2f`

The Prefetch artefact provides evidence associated with the execution of `CMD.EXE`.

## Conclusion

This lab demonstrated how Windows Prefetch artefacts can provide useful evidence of historical application execution. The analysis identified the executable, recorded run count, last execution timestamp, and associated volume information.

Prefetch evidence should be correlated with other forensic artefacts before drawing conclusions about a user's activity.

## Evidence

### 1. SHA-256 Evidence Verification

_Add your SHA-256 screenshot here._

### 2. Prefetch Analysis

_Add your Prefetch parser screenshot here._
