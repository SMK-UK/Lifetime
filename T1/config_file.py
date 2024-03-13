"""
Config file for T1 measurements
"""

config_params = dict(
    
    # Path to load data from and arguments used to disriminate files loaded
    
    root                = r"C:\Users\keena\Desktop\1221_T1\1221_T1",
    file                = r"power_3",
    extensions          = ['.csv', '.txt'],
    exceptions          = [],
    
    # Index positions for relevant column data in excel files
    
    data_indexes = dict(
    time                = 0,
    trig                = 1,
    ref                 = 3,
    trans               = 2
    ),

    # Index positions for trimming the data

    trim_indexes = dict(
    
    trig                = 50026, 
    ref_off             = 300,
    off                 = 1100, 
    ramp                = 65026
    ),

    # Guess T1 times for the data

    guess_ref_T1 = 1E-6,
    guess_T1 = 160E-6

)

