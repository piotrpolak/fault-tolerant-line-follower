from Khepera import *
import thread, time
import Config

class RobotLogic:

	def __init__(self):
		print '* Fault tolerant line-follower'
		print '* Author: Piotr Polak'
		print '* Date: May 28th 2009\n\n'
		
		Debugger.printAction( 'Initializing RobotLogic' )
		
		print ''
		Debugger.printConfig('KHEPERA_ADDRESS', Config.KHEPERA_ADDRESS)
		Debugger.printConfig('KHEPERA_PORT', Config.KHEPERA_PORT)
		Debugger.printConfig('ENABLE_COMM', Config.ENABLE_COMM)
		Debugger.printConfig('MAXIMUM_MOTOR_SPEED', Config.MAXIMUM_MOTOR_SPEED)
		Debugger.printConfig('MINIMUM_MOTOR_SPEED', Config.MINIMUM_MOTOR_SPEED)
		Debugger.printConfig('MAXIMUM_AMBIENT_LIGHT_SENSOR_VALUE', Config.MAXIMUM_AMBIENT_LIGHT_SENSOR_VALUE)
		Debugger.printConfig('GROUND_PROXIMITY_SENSOR_THRESHOLD', Config.GROUND_PROXIMITY_SENSOR_THRESHOLD)
		Debugger.printConfig('FRONT_PROXIMITY_SENSOR_THRESHOLD', Config.FRONT_PROXIMITY_SENSOR_THRESHOLD)
		Debugger.printConfig('MAIN_LOOP_SLEEP_STEP', Config.MAIN_LOOP_SLEEP_STEP)
		Debugger.printConfig('BROKEN_LINE_STEPS_NUMBER', Config.BROKEN_LINE_STEPS_NUMBER)
		Debugger.printConfig('TURN_90_DEGREES_TIME', Config.TURN_90_DEGREES_TIME)
		Debugger.printConfig('GO_PARALLEL_TIME', Config.GO_PARALLEL_TIME)
		
		print ''
		
		
		self.__doloop     = True;
		self.__state      = 0;		
		self.__khepera    = Khepera( Config.KHEPERA_ADDRESS, Config.KHEPERA_PORT )
		
		self.__broken_line_current_steps = 0;
		
	
	def run(self):
		while( self.__doloop ):
			if self.__state == 0:
				self.__followLineRoutine()
			elif self.__state == 1:
				self.__followObstacleRoutine()
			elif self.__state == 2:
				self.__brokenLineRoutine()
				
			time.sleep(Config.MAIN_LOOP_SLEEP_STEP)
	
	
	
	
	
	
	def __followLineRoutine(self):
		
		self.__state = 0
		self.__khepera.enableDiode(True)
		

		# Check ProximitySensors
		s = self.__khepera.getFrontProximitySensors()
		leftFrontProximitySensor  = int(s[0])
		rightFrontProximitySensor = int(s[1])
		
		
		
		#print leftFrontProximitySensor
		
		if leftFrontProximitySensor > Config.FRONT_PROXIMITY_SENSOR_THRESHOLD or rightFrontProximitySensor > Config.FRONT_PROXIMITY_SENSOR_THRESHOLD:
			Debugger.printAction( 'RobotLogic: followObstacleRoutine' )
			self.__state = 1
			return
		
		
		
		# Check AmbientLightSensors
		s = self.__khepera.getGroundSensors()
		leftGroundSensor  = int(s[1])
		rightGroundSensor = int(s[0])
		
		broken_trashhole = Config.GROUND_PROXIMITY_SENSOR_THRESHOLD
		
		#print "Ambient", leftGroundSensor, rightGroundSensor
		
		if rightGroundSensor < Config.GROUND_PROXIMITY_SENSOR_THRESHOLD and leftGroundSensor < Config.GROUND_PROXIMITY_SENSOR_THRESHOLD:
			# Continue going straight (following line)
			self.__khepera.setMotorSpeeds(Config.MAXIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED)
			
			
			
			
		elif rightGroundSensor > broken_trashhole and leftGroundSensor > broken_trashhole:
			# Continue going straight (broken line)
			Debugger.printAction( 'RobotLogic: brokenLineRoutine' )
			self.__state = 2
			return
		
		
		
		
		elif rightGroundSensor > Config.GROUND_PROXIMITY_SENSOR_THRESHOLD:
			# Adjust speed, turn left
			
			light_proportion = float(rightGroundSensor)/Config.MAXIMUM_AMBIENT_LIGHT_SENSOR_VALUE
			light_proportion = light_proportion/2

			slow_motor_speed = Config.MAXIMUM_MOTOR_SPEED - light_proportion*Config.MAXIMUM_MOTOR_SPEED
			self.__khepera.setMotorSpeeds( int(slow_motor_speed), Config.MAXIMUM_MOTOR_SPEED )
		
		
		
		
		elif leftGroundSensor > Config.GROUND_PROXIMITY_SENSOR_THRESHOLD:
			# Adjust speed, turn right
			
			light_proportion = float(leftGroundSensor)/Config.MAXIMUM_AMBIENT_LIGHT_SENSOR_VALUE		
			light_proportion = light_proportion/2

			slow_motor_speed = Config.MAXIMUM_MOTOR_SPEED - light_proportion*5*Config.MAXIMUM_MOTOR_SPEED
			self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, int(slow_motor_speed) )
		
		
		  
	
	def __followObstacleRoutine(self):
		self.__state = 1
		
		scenario = 1
		
		# Turn left
		Debugger.printAction( 'RobotLogic: followLineRoutine - Turn left' )
		self.__khepera.setMotorSpeeds( Config.MINIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED )
		time.sleep( Config.TURN_90_DEGREES_TIME )
		
		# Go parallel
		Debugger.printAction( 'RobotLogic: followLineRoutine - Go parallel' )
		self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED )
		time.sleep( Config.GO_PARALLEL_TIME )
		
		# Turn right
		Debugger.printAction( 'RobotLogic: followLineRoutine - Turn right' )
		self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, Config.MINIMUM_MOTOR_SPEED )
		time.sleep( Config.TURN_90_DEGREES_TIME )
		
		# Go parallel
		Debugger.printAction( 'RobotLogic: followLineRoutine - Go parallel' )
		self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED )
		time.sleep( Config.GO_PARALLEL_ALONG_TIME )
		
		# Go right
		Debugger.printAction( 'RobotLogic: followLineRoutine - Turn right' )
		self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, Config.MINIMUM_MOTOR_SPEED )
		time.sleep( Config.TURN_90_DEGREES_TIME )
		
		
		if scenario != 0:
			# Go parallel
			Debugger.printAction( 'RobotLogic: followLineRoutine - Go parallel' )
			self.__khepera.setMotorSpeeds( Config.MAXIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED )
			time.sleep( Config.GO_PARALLEL_TIME )
			
			# Turn left
			Debugger.printAction( 'RobotLogic: followLineRoutine - Turn left' )
			self.__khepera.setMotorSpeeds( Config.MINIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED )
			time.sleep( Config.TURN_90_DEGREES_TIME )
			
			
			Debugger.printAction( 'RobotLogic: followLineRoutine' )
			self.__state = 0
			return
		
		else:
			# Go parallel using broken line routine
			Debugger.printAction( 'RobotLogic: brokenLineRoutine' )
			self.__state = 2
			return
		
	
	
	
	def __brokenLineRoutine(self):
		self.__state = 2
		
		
		self.__khepera.setMotorSpeeds(Config.MAXIMUM_MOTOR_SPEED, Config.MAXIMUM_MOTOR_SPEED)
		
		self.__khepera.enableDiode(False)
		
		s = self.__khepera.getGroundSensors()
		leftGroundSensor  = int(s[1])
		rightGroundSensor = int(s[0])
		
		if leftGroundSensor < Config.GROUND_PROXIMITY_SENSOR_THRESHOLD or rightGroundSensor < Config.GROUND_PROXIMITY_SENSOR_THRESHOLD:
			Debugger.printAction( 'RobotLogic: followLineRoutine' )
			self.__broken_line_current_steps = 0
			self.__state = 0
			return
		
		self.__broken_line_current_steps = self.__broken_line_current_steps+1;
		if self.__broken_line_current_steps > Config.BROKEN_LINE_STEPS_NUMBER:
			Debugger.printAction( 'RobotLogic: Found no line' )
			self.__broken_line_current_steps = 0
			return self.stop();
	
	
	
	def stop(self):
		Debugger.printAction( 'RobotLogic: Stop' )
		self.__doloop = 0;
		self.__khepera.setMotorSpeeds(0, 0)
		
		
