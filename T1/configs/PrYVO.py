"""
Config file for T1 measurements
"""

# Path to load data from and arguments used to disriminate files loaded

root                = r"C:\Users\sk88\Heriot-Watt University Team Dropbox\RES_EPS_Quantum_Photonics_Lab\Experiments\Current Experiments\BB Telecom QM\2023_Pr_YVO\Visible\0.5%\T1"
file                = r"0329_Fluor_duration"
extensions          = ['.csv', '.txt']

# Index positions for relevant column data in excel files

data_indexes = dict(
time                = 0,
trig                = 1,
ref                 = 3,
trans               = 2
)

# Index positions for trimming the data

trim_indexes = dict(

trig                = 50026, 
ref_off             = 300,
off                 = 1100, 
ramp                = 65026
)

# Guess T1 times for the data

guess_ref_T1 = 1E-6
guess_T1 = 10E-6


