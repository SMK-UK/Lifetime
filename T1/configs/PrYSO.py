"""
Config file for T1 measurements
"""

# Path to load data from and arguments used to disriminate files loaded

root                = r"c:\Users\keena\Downloads"
file                = r"0927"
extensions          = ['.csv', '.json']

# Index positions for relevant column data in excel files

data_indexes = dict(
time                = 0,
trig                = 1,
ref                 = 1,
trans               = 1
)

# Index positions for trimming the data

trim_indexes = dict(

trig                = 50026,    # mark position of the trigger
ref_off             = 300,      # ref offset from the trigger
off                 = 5500,     # trans offset from the trigger 
ramp                = 7500      # for plotting - extend data to show on initial plots
)

# Guess T1 times for the data

guess_ref_T1 = 1E-6
guess_T1 = 180E-6