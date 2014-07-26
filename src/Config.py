# MAC of the robot
KHEPERA_ADDRESS                     = '00:07:80:84:8d:c0'

# Port of the robot
KHEPERA_PORT                        = 1

# Bluetooth communication enabled only when this value is set to True
ENABLE_COMM                         = False

# The maximum motor speed used, 120000 is the maximum allowed
MAXIMUM_MOTOR_SPEED                 = 12000

# The minimum motor speed used
MINIMUM_MOTOR_SPEED                 = -12000

# The maximum value of the light sensor, this value must be the vale of the "white" color
MAXIMUM_AMBIENT_LIGHT_SENSOR_VALUE  = 3900

# The threshold under which the values are considered as black
GROUND_PROXIMITY_SENSOR_THRESHOLD     = 3750

# Anything above this value will be ignored
FRONT_PROXIMITY_SENSOR_THRESHOLD      = 500

# Time duration for one step (sleep)
MAIN_LOOP_SLEEP_STEP                = 0.005

# The number of steps for intreruped line, the time is computed as BROKEN_LINE_STEPS_NUMBER * MAIN_LOOP_SLEEP_STEP
BROKEN_LINE_STEPS_NUMBER            = 30

# Time needed to do 90 degree rotation at the MAXIMUM_MOTOR_SPEED
TURN_90_DEGREES_TIME                = 0.7

# Time needed to "overtake" an obstacle going at the MAXIMUM_MOTOR_SPEED
GO_PARALLEL_TIME                    = 1.6
GO_PARALLEL_ALONG_TIME              = 2.5

# Debugger options
DEBBUGER_PRINT_COMMAND              = False
DEBBUGER_PRINT_ACTION               = True
DEBBUGER_PRINT_CONFIG               = True
