"""
Config file for T1 measurements
"""

config_params = dict(
    
    # Path to load data from and arguments used to disriminate files loaded
    
    root                = "C:/Users/keena/Downloads/",
    file                = "0403_T2",
    extensions          = ['.csv', '.txt'],
    exceptions          = [],
    
    # Index positions for relevant column data in excel files
    
    data_indexes = dict(
    time                = 0,
    trig                = 1,
    pulse               = 3,
    echo                = 2
    ),

    # Index positions for trimming the data

    trim_indexes = dict(
    
    trig                = 48297, 
    off                 = 1250, 
    ramp                = 62047
    ),

)

