"""
Config file for T1 measurements
"""
from Function_files.addresses import Init_Directories
dirs = Init_Directories()

# Path to load data from and arguments used to disriminate files loaded

directory           = "BB Telecom QM/2024_PrYSO/Fluorescence/0814/single_photon/"
sub_folder          = "Stitched HWP40"
extensions          = ['.ptu', '.phu', '.dat']
exceptions          = []

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
guess_T1 = 180E-6