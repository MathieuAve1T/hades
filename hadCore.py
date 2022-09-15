import maya.cmds as cmds
import maya.mel as mel

import hades.hadLib as hadLib
import hades.hadEnv as hadEnv
import hades.hadAutoRig as hadAutoRig

#AutoRig

def coreAutoRigGuide():

	preAutoRig = hadAutoRig.AutoRigCreateGuide()
	preAutoRig.autoRigPreModule()

	if hadEnv.AUTORIGCHEST:
		chestAutoRig = hadAutoRig.AutoRigCreateGuide()
		chestAutoRig.autoRigChestModule()

	if hadEnv.AUTORIGARM:
		armAutoRig = hadAutoRig.AutoRigCreateGuide()
		armAutoRig.autoRigArmModule()
	
	if hadEnv.AUTORIGLEG:
		legAutoRig = hadAutoRig.AutoRigCreateGuide()
		legAutoRig.autoRigLegModule()
		
	if hadEnv.AUTORIGHEAD:
		headAutoRig = hadAutoRig.AutoRigCreateGuide()
		headAutoRig.autoRigHeadModule()	

def coreAutoRigGenerator():

	armAutoRig = hadAutoRig.AutoRigGenerateRig()
	armAutoRig.autoRigCreateJoints()

	if hadEnv.AUTORIGMIRROR:
		armAutoRig.autoRigCheckMirror()
		LeftRight = [0,6]
	else:
		LeftRight = [17]

	armAutoRig.autoRigCreateRigWithOutSide()

	for side in LeftRight:

		armAutoRig = hadAutoRig.AutoRigGenerateRig()   
		armAutoRig.autoRigCreateRigWithSide(side)

            
    



#Tool for maya

def coreDeleteHistory():
	mel.eval('DeleteAllHistory')

def coreFreezeTransform():
	sele=cmds.ls(selection=True)
	for each in sele:
		cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1 )

def coreCenterPivot():
	mel.eval('CenterPivot')

def coreCreateJoints():
	mel.eval('JointToolOptions')

def coreJointSize():
	mel.eval('jdsWin')

def coreLocalRotationAxis():
	mel.eval('ToggleLocalRotationAxes')

def coreCharacterGroup():
	CtrlGeneral = cmds.circle(normal=(0, 1, 0), center=(0, 0, 0), radius=7, name= "Ctrl_General", constructionHistory=False)[0]

	cmds.group( em=True, name="Rig_by_Hades" )
	cmds.group( em=True, name="GlobalMove" )
	cmds.group( em=True, name="Joints" )
	cmds.group( em=True, name="Iks" )
	cmds.group( em=True, name="ControlObjects" )
	cmds.group( em=True, name="Model" )
	cmds.group( em=True, name="BlendShapes" )
	cmds.group( em=True, name="ExtraNodes" )
	cmds.group( em=True, name="Xtra_toShow" )
	cmds.group( em=True, name="Xtra_toHide" )
	
	cmds.parent("Xtra_toHide", "ExtraNodes")
	cmds.parent("Xtra_toShow", "ExtraNodes")
	cmds.parent("GlobalMove", "AutoRig_By_Mathieu")
	cmds.parent("Model", "AutoRig_By_Mathieu")
	cmds.parent("BlendShapes", "AutoRig_By_Mathieu")
	cmds.parent("Joints", "GlobalMove")
	cmds.parent("Iks", "GlobalMove")
	cmds.parent("ControlObjects", "GlobalMove")
	cmds.parent("ExtraNodes", "AutoRig_By_Mathieu")
	
	cmds.parent(CtrlGeneral, "AutoRig_By_Mathieu")
	
	cmds.connectAttr(CtrlGeneral + ".translate", "GlobalMove.translate")
	cmds.connectAttr(CtrlGeneral + ".rotate", "GlobalMove.rotate")
	
	cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleX")
	cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleZ")
	
	cmds.connectAttr(CtrlGeneral + ".scaleY", CtrlGeneral +".scaleZ")
	cmds.connectAttr(CtrlGeneral + ".scaleY", CtrlGeneral +".scaleX")
	
	cmds.connectAttr(CtrlGeneral + ".scaleX", "GlobalMove.scaleY")
	
	cmds.setAttr( CtrlGeneral +'.scaleX', lock=True , keyable = False , channelBox=False )
	cmds.setAttr( CtrlGeneral +'.scaleZ', lock=True , keyable = False , channelBox=False ) 

def coreMirrorJoints():
	mel.eval('MirrorJointOptions')

def coreOrientJoints():
	mel.eval('OrientJointOptions')

def coreReOrientLastJoint():
	sele=cmds.ls(selection=True)
	for each in sele:
		x, y, z = hadLib.getRotate(each)
		hadLib.setRotateOrient(each, x, y, z)
		hadLib.setRotate(each, 0, 0, 0)

def coreMirrorCurves():
	sele=cmds.ls(selection=True)
	for each in sele:
		x = cmds.duplicate(each)
		tempGrp = cmds.createNode('transform')
		cmds.parent(x, tempGrp)
		hadLib.setScale(tempGrp, -1, 1, 1)
		cmds.parent(x, world=True)
		cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1 )

def coreParentCurves():
	allSele=cmds.ls(selection=True)
	lastSele = allSele[-1]
	for each in allSele[:-1]:
		cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1 )
		tempRel = cmds.listRelatives(each, shapes=True)
		cmds.parent(tempRel, lastSele, relative=True, shape=True)
		cmds.delete(each)
		cmds.select(lastSele)

def coreConnectionEditor():
	mel.eval('ConnectionEditor')

def coreShapeEditor():
	mel.eval('ShapeEditor')

def coreDrivenKey():
	mel.eval('SetDrivenKeyOptions')

def coreCreateLocator():
	x = False
	if cmds.ls(selection=True):
		sele = cmds.ls(selection=True)[0]
		x = True
	else:
		sele=""
	tempCrv = cmds.createNode('locator', name="Locator_"+sele )
	if x == True:
		cmds.matchTransform(tempCrv, sele)   

def coreNodeEditor():
	mel.eval('NodeEditorWindow')

def coreComponentEditor():
	mel.eval('ComponentEditor')

def coreColorYellow():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 17) 

def coreColorRed():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 13) 

def coreColorBlue():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 6) 

def coreColorPink():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 9) 

def coreColorGreen():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 14) 

def coreColorPurple():
	sele = cmds.ls(selection=True)
	for each in sele:
		cmds.setAttr( each + ".overrideEnabled", 1)
		cmds.setAttr( each + ".overrideColor", 30) 



#Create Ctrl

def coreCreateCircle():
	hadLib.createCircle()
def coreCreateTriangle():
	hadLib.createTriangle()
def coreCreateSquare():
	hadLib.createSquare()
def coreCreateCross():
	hadLib.createCross()
def coreCreateBox():
	hadLib.createBox()
def coreCreateDiamond():
	hadLib.createDiamond()
def coreCreateBall():
	hadLib.createBall()
def coreCreateArrow():
	hadLib.createArrow()
def coreCreateLocator():
	hadLib.createLocator()
