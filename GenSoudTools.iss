[Setup]
AppName=ExportSDHC
AppVersion=1.0

DefaultDirName=C:\GenSoudTools
DisableDirPage=Yes

OutputBaseFilename=GenSoudTools_Installer

UsePreviousAppDir=No
DisableProgramGroupPage=Yes
AllowRootDirectory=No
AlwaysShowDirOnReadyPage=Yes
DirExistsWarning=No
ShowComponentSizes=yes
ChangesAssociations=Yes

[Files]
Source: "Export.py"; DestDir: "{app}"
Source: "ExportSDHC.cmd"; DestDir: "{app}"
Source: "ExportSDHC.reg"; DestDir: "{app}"
Source: "env\*"; DestDir: "{app}\env"  ; Flags: recursesubdirs

[Run]
Filename: "REGEDIT.EXE"; Parameters: "/S {app}\ExportSDHC.reg"