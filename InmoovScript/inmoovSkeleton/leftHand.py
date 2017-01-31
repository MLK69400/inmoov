# ##############################################################################
#						*** LEFT HAND ***
# ##############################################################################

# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
	
except:
	errorSpokenFunc('ConfigParserProblem','lefthand.config')
	pass	
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingLeftHand)
		
		thumb = Runtime.createAndStart("i01.leftHand.thumb","Servo")
		index = Runtime.createAndStart("i01.leftHand.index","Servo")
		majeure = Runtime.createAndStart("i01.leftHand.majeure","Servo")
		ringFinger = Runtime.createAndStart("i01.leftHand.ringFinger","Servo")
		pinky = Runtime.createAndStart("i01.leftHand.pinky","Servo")
		wrist = Runtime.createAndStart("i01.leftHand.wrist","Servo")
		
		leftHand = Runtime.create("i01.leftHand", "InMoovHand")
		leftHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
		leftHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
		leftHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
		leftHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
		leftHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
		leftHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
		
		leftHand.thumb.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'thumb'))
		leftHand.index.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'index'))
		leftHand.majeure.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'majeure'))
		leftHand.ringFinger.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'ringFinger'))
		leftHand.pinky.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'pinky'))
		leftHand.wrist.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'wrist'))
		
		leftHand.thumb.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'thumb'))
		leftHand.index.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'index'))
		leftHand.majeure.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'majeure'))
		leftHand.ringFinger.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'ringFinger'))
		leftHand.pinky.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'pinky'))
		leftHand.wrist.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'wrist'))
		
		leftHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'thumb'))
		leftHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'index'))
		leftHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'majeure'))
		leftHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'ringFinger'))
		leftHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'pinky'))
		leftHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'wrist'))
		
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'):
			leftHand.thumb.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'):
			leftHand.index.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'):
			leftHand.majeure.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'):
			leftHand.ringFinger.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'):
			leftHand.pinky.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'):
			leftHand.wrist.setInverted(True)
		
		i01.startLeftHand(MyLeftPort)
		
		if autoDetach:
			leftHand.thumb.enableAutoAttach(1)
			leftHand.index.enableAutoAttach(1)
			leftHand.majeure.enableAutoAttach(1)
			leftHand.ringFinger.enableAutoAttach(1)
			leftHand.pinky.enableAutoAttach(1)
			leftHand.wrist.enableAutoAttach(1)
		
		leftHand.detach()
		leftHand.thumb.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'thumb'))
		leftHand.index.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'index'))
		leftHand.majeure.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'majeure'))
		leftHand.ringFinger.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'ringFinger'))
		leftHand.pinky.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'pinky'))
		leftHand.wrist.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'wrist'))
			
		leftHand.rest()
		
	else:
		#we force parameter if arduino is off
		isleftHandActivated=0
		
#todo set inverted
