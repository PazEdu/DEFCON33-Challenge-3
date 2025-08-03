#  Crash Dump

**Flag Format**: `aeroCTF{random_string}`  
**Files Provided**: `crash_dump.csv`



##  Lore

Following an onboard anomaly, a space vehicle automatically logged raw telemetry from several key subsystems into storage. The log was later recovered by mission control for diagnostics. The data appears to be just typical sensor output… but one engineer on the team insists there's something odd about the encoding.

Some suspect there is an embedded, hidden string — a sort of digital "Easter egg."

Can you recover the message from the telemetry?



##  Challenge Overview

You're given a single CSV file with several hundred rows of sensor data collected during the spacecraft’s final moments before reboot. Each row contains values from three key systems:

- `thruster_cmd`
- `gyro_raw`
- `diag_code`

If these values are interpreted in the correct order and format, they reveal a message encoded by the system before it crashed — including a flag in the format `aeroCTF{...}`.

Your task is to extract that flag.



##  Solve Path

1. **Ignore the `time` column** — it’s just metadata.
2. **For each row**, read the three sensor values: `thruster_cmd`, `gyro_raw`, and `diag_code`.
3. **Concatenate those values row-wise**, converting each to its ASCII representation using something like Python’s `chr()`.
4. Filter out non-printable values (e.g., outside ASCII 32–126), and search for a flag string using a regex pattern like `aeroCTF{.*?}`.



##  Hints 

1. *"The CSV is just numbers... or is it?"*
2. *"Only some columns contain signal intelligence — the timestamp isn’t one of them."*
3. *"Try reading each row like a sentence, in the order it was logged."*
4. *"ASCII values can hide in plain sight — convert the integers into characters and look for patterns."*



##   Flag

aeroCTF{m3m0ry_dump_d3crypt3d}







