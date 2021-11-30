param([string]$fileName)
if (-not($fileName)) {
    Throw "You must supply a value for the file"
}

&"C:\ProgramData\chocolatey\bin\exiftool.exe" -filemodifydate -if '(not $datetimeoriginal or ($datetimeoriginal eq "0000:00:00 00:00:00")) and ($filetype eq "JPEG")' "$fileName"