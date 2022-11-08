import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as OpenMaya

import hades.hadLib as hadLib
import hades.hadEnv as hadEnv
import hades.hadAutoRig as hadAutoRig

try:
	from zBuilder.ui import zUI as sp1 
	from zBuilder.scenePanel2 import main as sp2
	import zBuilder.zMaya as zMaya
	import zBuilder.utils as utility
except:
	pass


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

	cmds.select(clear=True)

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

	cmds.select(clear=True)

#Skin tool

__myGlobalVar = None

def startEventSelection(self):

	global __myGlobalVar

	if __myGlobalVar is not None:
		return
	__myGlobalVar = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", refreshSelection)
	refreshSelection(self)

	if hadEnv.MESHSKIN:
		if cmds.getAttr(hadEnv.MESHSKIN+".displayColors"):
			cmds.select(hadEnv.MESHSKIN)
			try:
				cmds.polyColorPerVertex(remove=True)
			except:
				pass
		

def endEventSelection():

	global __myGlobalVar 

	if __myGlobalVar:
		OpenMaya.MMessage.removeCallback(__myGlobalVar)
		__myGlobalVar = None

	if hadEnv.MESHSKIN:
		cmds.setAttr(hadEnv.MESHSKIN+".displayColors", 0)

def selectionJoint():
	import maya.cmds as cmds
	import maya.api.OpenMaya as OpenMaya

	global __myGlobalVar 

	if __myGlobalVar:
		OpenMaya.MMessage.removeCallback(__myGlobalVar)
		__myGlobalVar = None

	selectedJoint = hadEnv.TREESKINVALUES.currentItem()	

	hadEnv.CURRENTJOINT = selectedJoint.text(2)

	seleVtx = cmds.ls(selection=True, flatten=True)[0]
	#print('seleVtx', seleVtx)

	if hadEnv.CURRENTSHAPE:
		seleShape = hadEnv.CURRENTSHAPE
	else:
		seleShape = cmds.listRelatives(seleVtx, parent=True, type='shape')[0]
		hadEnv.CURRENTSHAPE = seleShape

	if hadEnv.CURRENTSKINCLUS:
		sCluster = hadEnv.CURRENTSKINCLUS
	else:
		sCluster = cmds.listConnections(seleShape, type = "skinCluster")
		hadEnv.CURRENTSKINCLUS = sCluster
	#print('sCluster', sCluster)
	skinInfluences = cmds.skinCluster(sCluster[0],query=True,influence=True)
	#print('skinInfluences',skinInfluences)
	listeA =[]
	for influence in skinInfluences:
		if hadEnv.CURRENTJOINT == influence:
			cmds.skinCluster(sCluster[0], edit=True, selectInfluenceVerts = influence)
			listeA = (cmds.ls(selection=True,flatten=True))
			break

	if cmds.getAttr(seleShape+".displayColors"):
		cmds.select(seleShape)
		try:
			cmds.polyColorPerVertex(remove=True)
		except:
			pass
	else:
		cmds.setAttr(seleShape+".displayColors", 1)	
	for vtx in listeA:
		tempValue = (cmds.skinPercent( sCluster[0], vtx, transform=selectedJoint.text(2), query=True ))
		cmds.select(vtx)
		if 0 < tempValue < 0.1 :
			cmds.polyColorPerVertex( rgb=(0.0, 0.0, 1) )
		elif 0.1 <= tempValue < 0.2:
			cmds.polyColorPerVertex( rgb=(0.1, 0.5, 1) )
		elif 0.2 <= tempValue < 0.3:
			cmds.polyColorPerVertex( rgb=(0.1, 1, 0.9) )
		elif 0.3 <= tempValue < 0.4:
			cmds.polyColorPerVertex( rgb=(0.1, 1, 0.4) )
		elif 0.4 <= tempValue < 0.5:
			cmds.polyColorPerVertex( rgb=(0.4, 1, 0.1) )
		elif 0.5 <= tempValue < 0.6:
			cmds.polyColorPerVertex( rgb=(0.8, 1, 0.1) )
		elif 0.6 <= tempValue < 0.7:
			cmds.polyColorPerVertex( rgb=(1, 0.7, 0.1) )
		elif 0.7 <= tempValue < 0.8:
			cmds.polyColorPerVertex( rgb=(1, 0.3, 0.1) )
		elif 0.8 <= tempValue < 0.9:
			cmds.polyColorPerVertex( rgb=(1, 0.1, 0.2) )
		elif 0.9 <= tempValue < 1:
			cmds.polyColorPerVertex( rgb=(1, 0.0, 0.7) )


	seleMesh = cmds.listRelatives(seleShape,parent=True, type='transform')
	mel.eval('doMenuComponentSelectionExt({}, "vertex", 0);'.format(seleMesh))
	mel.eval('if (`currentCtx` == "ShowManips") SelectTool;')
	

	cmds.select(hadEnv.CURRENTSELECTION)

	if __myGlobalVar is not None:
		return
	__myGlobalVar = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", refreshSelection)

	hadEnv.MESHSKIN = seleShape


def refreshSelection(self,*args, **kwargs):

	import maya.cmds as cmds
	import maya.mel as mel
	import hades.hadEnv as hadEnv
	from Qt import QtWidgets

	# label selection vertices


	if hadEnv.MESHSKIN:
		cmds.setAttr(hadEnv.MESHSKIN+".displayColors", 1)
	else:
		hadEnv.MESHSKIN = cmds.ls(selection=True, shapes=True) or []
		if hadEnv.MESHSKIN:
			cmds.setAttr(hadEnv.MESHSKIN+".displayColors", 1)


	listSelection = []
	lenVertices = 0
	listSelection = cmds.ls(selection=True)
	if listSelection:
		onlyVertices = cmds.filterExpand(listSelection, sm=31) or []
		lenVertices = len(onlyVertices)
		if lenVertices:
			labelVertices = str(lenVertices)+ " Vertices Selected"
			hadEnv.LABELVERTICESELECTED.setText(labelVertices)
	else:
		hadEnv.LABELVERTICESELECTED.setText("0 Vertices Selected")
	hadEnv.CURRENTSELECTION = cmds.ls(selection=True,flatten=True)


	# list joints

	hadEnv.TREESKINVALUES.clear()
	listSelection = cmds.ls(selection=True,flatten=True)
	if listSelection:
		meshObject = cmds.ls(listSelection[0], o=True)
		skinCluster = mel.eval('findRelatedSkinCluster ' + meshObject[0])
		if skinCluster:
			joints = cmds.skinCluster(skinCluster, query=True, inf=True)
			SkinDict = {}
			for vtx in onlyVertices:
				influenceVals = cmds.skinPercent(skinCluster, vtx, query=1, value=1, ignoreBelow=0.000001)
				influenceNames = cmds.skinPercent(skinCluster, vtx, transform=None, query=1, ignoreBelow=0.000001)
				SkinDict[vtx] = [influenceNames, (influenceVals)]
			for vtx in SkinDict:
				for joint, value in zip(SkinDict[vtx][0],SkinDict[vtx][1]):
					value = format(value, '.4f')
					value = str(value)
					vertice = str(vtx)
					skinToolItem_tree = QtWidgets.QTreeWidgetItem([vertice,value,joint])
					hadEnv.TREESKINVALUES.addTopLevelItem(skinToolItem_tree)
					hadEnv.TREESKINVALUES.resizeColumnToContents(0)
		else:
			raise RuntimeError("Selected mesh has no skinCluster")



def coreSkinToolShrink():
	mel.eval('PolySelectTraverse 2')

def coreSkinToolGrow():
	mel.eval('PolySelectTraverse 1')

def coreSkinToolRing():
	cmds.polySelectSp(ring=True)

def coreSkinToolLoop():
	cmds.polySelectSp(loop=True)

def coreSkinTool0(self):
	hadLib.applyWeight(0)
	refreshSelection(self)

def coreSkinTool01(self):
	hadLib.applyWeight(0.1)
	refreshSelection(self)

def coreSkinTool025(self):
	hadLib.applyWeight(0.25)
	refreshSelection(self)

def coreSkinTool05(self):
	hadLib.applyWeight(0.5)
	refreshSelection(self)

def coreSkinTool075(self):
	hadLib.applyWeight(0.75)
	refreshSelection(self)

def coreSkinTool09(self):
	hadLib.applyWeight(0.9)
	refreshSelection(self)

def coreSkinTool1(self):
	hadLib.applyWeight(1)
	refreshSelection(self)

def coreSkinToolSetWeight():
	pass

def coreSkinToolSetWeightAdd():
	pass

def coreSkinToolSetWeightSub():
	pass

def coreSkinToolScaleWeight():
	pass

def coreSkinToolScaleWeightAdd():
	pass

def coreSkinToolScaleWeightSub():
	pass

def coreSkinToolCopy():
	mel.eval('artAttrSkinWeightCopy;')
	listSelection = []
	lenVertices = 0
	listSelection = cmds.ls(selection=True)
	if listSelection:
		onlyVertices = cmds.filterExpand(listSelection, sm=31) or []
		lenVertices = len(onlyVertices)
		if lenVertices:
			labelVertices = str(lenVertices)+" Vertices In Copy Buffer"
			hadEnv.LABELVERTICEMEMORY.setText(labelVertices)


def coreSkinToolPaste():
	mel.eval('artAttrSkinWeightPaste;')

def coreSkinTooPastePos():
	pass

def coreSkinToolBlend():
	pass



#Tool for maya

def coreDeleteHistory():
	mel.eval('DeleteHistory')

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
	ctrlGeneral = cmds.circle(normal=(0, 1, 0), center=(0, 0, 0), radius=7, name= "Ctrl_General", constructionHistory=False)[0]

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
	cmds.setAttr('Xtra_toHide.visibility', 0)
	cmds.setAttr('Iks.visibility', 0)
	
	cmds.parent("Xtra_toHide", "ExtraNodes")
	cmds.parent("Xtra_toShow", "ExtraNodes")
	cmds.parent("GlobalMove", "Rig_by_Hades")
	cmds.parent("Model", "Rig_by_Hades")
	cmds.parent("BlendShapes", "Rig_by_Hades")
	cmds.parent("Joints", "GlobalMove")
	cmds.parent("Iks", "GlobalMove")
	cmds.parent("ControlObjects", "GlobalMove")
	cmds.parent("ExtraNodes", "Rig_by_Hades")
	
	cmds.parent(ctrlGeneral, "Rig_by_Hades")
	
	cmds.connectAttr(ctrlGeneral + ".translate", "GlobalMove.translate")
	cmds.connectAttr(ctrlGeneral + ".rotate", "GlobalMove.rotate")
	
	cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleX")
	cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleZ")
	
	cmds.connectAttr(ctrlGeneral + ".scaleY", ctrlGeneral +".scaleZ")
	cmds.connectAttr(ctrlGeneral + ".scaleY", ctrlGeneral +".scaleX")
	
	cmds.connectAttr(ctrlGeneral + ".scaleX", "GlobalMove.scaleY")
	
	cmds.setAttr( ctrlGeneral +'.scaleX', lock=True , keyable = False , channelBox=False )
	cmds.setAttr( ctrlGeneral +'.scaleZ', lock=True , keyable = False , channelBox=False ) 

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
	mel.eval('''
		//Find selection...
	string $mirSel[] = `ls -sl`;
	//Make sure objects are selected...
	if (size($mirSel) == 0){
		warning "Select the object(s) to mirror!";
	} else {
		//Duplicate object(s)...
		duplicate -rr;
		//Group object(s) and place the pivot of the group at the origin...
		string $wGrp = `group`;
		xform -os -piv 0 0 0;
		//Mirror the objects by scaling the group -1 in the X axis...
		setAttr ($wGrp + ".sx") -1;
		//Ungroup object(s)...
		select $wGrp; ungroup;
		//Freeze the transformations of the object(s)...
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0;
	}''')

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
	mel.eval('''SetDrivenKey;
setDrivenKeyWindow "" {};''')

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

 #Tools for Ziva

def coreToolZivaPanelOpen():
	sp1.run() if 'ZIVA_ZBUILDER_USE_SCENE_PANEL1' in os.environ else sp2.run()		
def coreToolZivaPanelAddCache():
	mel.eval('''global proc invertZCache()
	{
		$solverTab = `ls -type "zCacheTransform"`;
		$solver = $solverTab[0];
		if(`getAttr(($solver +".cache" ))`)
		{
			setAttr ($solver +".cache" ) 0;
			inViewMessage -smg "zCache disable" -pos topRight -bkc 0x00000000 -fade;
		}
		else
		{
			setAttr ($solver +".cache" ) 1;
			inViewMessage -smg "zCache enable" -pos topRight -bkc 0x00000000 -fade;
		}
	}
	invertZCache;	''')
	print('AddPanelCache')
def coreToolZivaPanelDeleteCache():
	mel.eval('zCache -c')	
def coreToolZivaTissueCreate():
	mel.eval('ziva -t')	
def coreToolZivaTissueDisaRSide():
	def disableRightSide(r='r_',value=False):
		tissue_list = cmds.ls('%s*_zTissue'%r)
		for tissue in tissue_list:
			cmds.setAttr('%s.enable'%tissue,value)
	disableRightSide()	
def coreToolZivaTissueEnaRSide():
	def disableRightSide(r='r_',value=True):
		tissue_list = cmds.ls('%s*_zTissue'%r)
		for tissue in tissue_list:
			cmds.setAttr('%s.enable'%tissue,value)
	disableRightSide()	
def coreToolZivaTissueDamping():
	def disableRightSide(r='',value=1):
		tissue_list = cmds.ls('%s*_zTissue'%r)
		for tissue in tissue_list:
			cmds.setAttr('%s.inertialDamping'%tissue,value)
	disableRightSide()	
def coreToolZivaTetShowHide():
	mel.eval('''global proc showZTets()
	{
		//$solverTab = `ls -type "zSolver"`;
		$solver = "zSolver1Shape";
		if(`getAttr(($solver +".showTetMeshes" ))`)
		{
			setAttr ($solver +".showTetMeshes" ) 0;
			inViewMessage -smg "zTets disable" -pos topRight -bkc 0x00000000 -fade;
		}
		else
		{
			setAttr ($solver +".showTetMeshes" ) 1;
			inViewMessage -smg "zTets enable" -pos topRight -bkc 0x00000000 -fade;
		}
	}
	showZTets;	''')
def coreToolZivaTetX05():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=0.5)	
def coreToolZivaTetX075():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=0.75)	
def coreToolZivaTetX9():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=0.9)	
def coreToolZivaTetX11():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=1.1)	
def coreToolZivaTetX125():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=1.25)
def coreToolZivaTetX2():
	def set_tet_size(t_list=[],mult=0.5):
		if not t_list:
			t_list= mel.eval('zQuery -t zTet')
		for t in t_list:
			t_value=cmds.getAttr('%s.tetSize'%t)
			cmds.setAttr('%s.tetSize'%t,t_value*mult)
	set_tet_size(mult=2)

def coreToolZivaBoneCreate():
	cmds.select(mel.eval('ziva -bone'))	

def coreToolZivaMaterialGelatin():	#1.0*10^0
	hadLib.setZMaterial(1,0)

def coreToolZivaMaterialBrain():	#0.5*10^3
	hadLib.setZMaterial(0.5,3)
def coreToolZivaMaterialLiver():	#0.7*10^3
	hadLib.setZMaterial(0.7,3)
def coreToolZivaMaterialBreastTissue():	#0.9*10^3
	hadLib.setZMaterial(0.9,3)
def coreToolZivaMaterialFat():	#3.0*10^3
	hadLib.setZMaterial(3,3)
def coreToolZivaMaterialSmoothMuscle():	#5.0*10^3
	hadLib.setZMaterial(5,3)
def coreToolZivaMaterialSkeletalMuscle():	#1.2*10^4
	hadLib.setZMaterial(1.2,4)
def coreToolZivaMaterialCartilage():	#2.0*10^4
	hadLib.setZMaterial(2,4)
def coreToolZivaMaterialRubber():	#1.0*10^7
	hadLib.setZMaterial(1,7)
def coreToolZivaMaterialWood():	#0.6*10^9
	hadLib.setZMaterial(0.6,9)
def coreToolZivaMaterialTendon():	#1.0*10^9
	hadLib.setZMaterial(1,9)
def coreToolZivaMaterialPlastic():	#1.5*10^9
	hadLib.setZMaterial(1.5,9)
def coreToolZivaMaterialBone():	#1.4*10^10
	hadLib.setZMaterial(1.4,10)
def coreToolZivaMaterialWalnutShell():	#1.5*10^10
	hadLib.setZMaterial(1.5,10)
def coreToolZivaMaterialSteel():	#2.0*10^11
	hadLib.setZMaterial(2,11)
def coreToolMaterialDiamond():	#1.0*10^12
	hadLib.setZMaterial(1,12)
def coreToolZivaFiberCreate():
	cmds.select(mel.eval('ziva -fiber;'))	
def coreToolZivaFiberSelect():
	if not 'zFiber_i' in locals():
		zFiber_i=0
	if zFiber_i < len(mel.eval('zQuery -t zFiber')):
		cmds.select(mel.eval('zQuery -t zFiber')[zFiber_i])
		zFiber_i+=1
	else :
		cmds.select(mel.eval('zQuery -t zFiber')[0])
		zFiber_i=1	
def coreToolZivaLOACreate():
	cmds.select(mel.eval('ziva -loa;'))	
def coreToolZivaLOASelect():
	cmds.select(mel.eval('zQuery -t lineOfAction'))	
def coreToolZivaLOAAddCrv():
	def get_next_free_mult_index(attr):
		"""For given mutlindex attribute, returns the next available index.
		Arg:
			:attr, (str): node.attr
		Returns:
			:int:
		"""
		used_indexes = cmds.getAttr(attr, multiIndices=True)
		return int(used_indexes[-1] + 1) if used_indexes else 0
		

	def add_curve_to_loa(curve_list=None,zFiber=None):
		selection_list = cmds.ls(sl=True)
		if not curve_list and not zFiber:
			curve_list = [selection_list[0]]
			print (curve_list)
			zFiber  = selection_list[-1]
		
		if not cmds.objectType(zFiber,isType='zFiber'):
			zFiber= mel.eval('zQuery -t zFiber %s'%zFiber)[0]
			print (zFiber)
		if cmds.objectType(zFiber,isType='zFiber'):
			loa = cmds.listConnections(zFiber,p=False,s=True,type='zLineOfAction')[0]
			if loa : 
				attr='%s.curves'%loa
				for curve in curve_list:
					index = get_next_free_mult_index(attr)
					shape=cmds.listRelatives(curve,s=True)[0]
					print (index)
					cmds.connectAttr('%s.worldSpace[0]'%shape,'%s[%s]'%(attr,index),f=True)
			else:
				print ('no loa found')
	add_curve_to_loa()	
def coreToolZivaAttachmentCreate():
	cmds.select(mel.eval('ziva -a'))	
def coreToolZivaAttachmentSliding():
	def set_sliding(a_list=[],mode=2):
		if not a_list:
			a_list= cmds.ls(sl=True,type='zAttachment')
		for a in a_list:
			cmds.setAttr('%s.attachmentMode'%a,mode)
	set_sliding(mode=2)	
def coreToolZivaAttachmentFixed():
	def set_sliding(a_list=[],mode=2):
		if not a_list:
			a_list= cmds.ls(sl=True,type='zAttachment')
		for a in a_list:
			cmds.setAttr('%s.attachmentMode'%a,mode)
	set_sliding(mode=1)
def coreToolZivaAttachment02():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 0.2;
	}	''')
def coreToolZivaAttachment05():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 0.5;
	}	''')
def coreToolZivaAttachment1():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 1;
	}''')	
def coreToolZivaAttachment2():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 2;
	}''')
def coreToolZivaAttachment5():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 5;
	}	''')
def coreToolZivaAttachment10():
	mel.eval('''string $sel[] = `ls -sl`;
	for ($obj in $sel)
	{
	select $obj;
	zPaintAttachmentsByProximity -min 0.1 -max 10;
	}	''')
def coreToolZivaAttachmentPower1():
	hadLib.setZAttachement(1)
def coreToolZivaAttachmentPower2():
	hadLib.setZAttachement(2)
def coreToolZivaAttachmentPower3():
	hadLib.setZAttachement(3)
def coreToolZivaAttachmentPower4():
	hadLib.setZAttachement(4)
def coreToolZivaAttachmentPower5():
	hadLib.setZAttachement(5)
def coreToolZivaAttachmentPower6():
	hadLib.setZAttachement(6)
def coreToolZivaAttachmentPower7():
	hadLib.setZAttachement(7)
def coreToolZivaAttachmentPower8():
	hadLib.setZAttachement(8)
def coreToolZivaAttachmentPower9():
	hadLib.setZAttachement(9)
def coreToolZivaAttachmentPower10():
	hadLib.setZAttachement(10)
def coreToolZivaCopy():
	utility.rig_cut()	
def coreToolZivaPaste():
	utility.rig_paste()	
def coreToolZivaMeshStandart():
	mel.eval('SetMeshSculptTool')
def coreToolZivaMeshMove():
	mel.eval('SetMeshGrabTool')	
def coreToolZivaMeshInFlat():
	mel.eval('SetMeshWaxTool')	
def coreToolZivaMeshFlatten():
	mel.eval('SetMeshFlattenTool')	
def coreToolZivaMeshPinch():
	mel.eval('SetMeshPinchTool')	
def coreToolZivaMeshSmooth():
	mel.eval('SetMeshSmoothTool')	
def coreToolZivaMeshFreeze():
	mel.eval('SetMeshFreezeTool')	
def coreToolZivaMeshUnFreeze():
	mel.eval('SculptMeshUnfreezeAll')	
def coreToolZivaMeshRelax():
	mel.eval('SetMeshRelaxTool')	
def coreToolZivaMeshRemesh():
	mel.eval('PolyRemesh')	
def coreToolZivaMeshRetopo():
	mel.eval('PolyRetopo')
def coreToolZivaMeshMirror():
	sel = cmds.ls(sl=True)
	axis = ['x', 'y', 'z']
	attrs = ['t', 'r', 's']
	for obj in sel:
		for ax in axis:
			for attr in attrs:
				cmds.setAttr(obj+'.'+attr+ax, lock=0)
		cmds.delete(cmds.ls(obj + "ShapeOrig*"))
		cmds.setAttr(obj + ".sx",-1)
	cmds.makeIdentity(apply=True,t=1,r=1,s=1,n=0,pn=1)
	cmds.deformer(type="tweak")
	mel.eval("DeleteHistory;")	
def coreToolZivaMeshTransfer():
	sel=cmds.ls(sl=True)
	cmds.connectAttr((sel[0] + ".outMesh"),(sel[1] + ".inMesh"),f=True)	
def coreToolZivaPaintTool0():
	mel.eval('''artAttrCtx -e -value 0 `currentCtx`''')
def coreToolZivaPaintTool05():
	mel.eval('''artAttrCtx -e -value 0.5 `currentCtx`''')
def coreToolZivaPaintTool1():
	mel.eval('''artAttrCtx -e -value 1 `currentCtx`	''')
def coreToolZivaPaintToolFlood0():
	mel.eval('''artAttrCtx -e -value 0 `currentCtx`
	artAttrCtx -e -clear `currentCtx`''')	
def coreToolZivaPaintToolFlood1():
	mel.eval('''artAttrCtx -e -value 1 `currentCtx`
	artAttrCtx -e -clear `currentCtx`''')	
def coreToolZivaOPaintToolSmooth():
	mel.eval('''artAttrPaintOperation artAttrCtx Smooth
	artAttrCtx -e -clear `currentCtx`
	artAttrPaintOperation artAttrCtx Replace'''	)

def coreToolZivaMirrorLR():
	selection = cmds.ls(sl = True)
	for obj in selection :
		cmds.select(obj)
		zObj = zMaya.Ziva()
		zObj.retrieve_from_scene_selection()
		zObj.string_replace( '^lf_', 'rt_' )
		zObj.string_replace( '^lt_', 'rt_' )
		zObj.string_replace( '^l_', 'r_' )
		zObj.string_replace( '_L', '_R' )
		zObj.build()	
def coreToolZivaMirrorRL():
	selection = cmds.ls(sl = True)
	for obj in selection :
		cmds.select(obj)
		zObj = zMaya.Ziva()
		zObj.retrieve_from_scene_selection()
		zObj.string_replace( '^rt_', 'lf_' )
		zObj.string_replace( '^rt_', 'lt_' )
		zObj.string_replace( '^r_', 'l_' )
		zObj.string_replace( '_R', '_L' )
		zObj.build()	
def coreToolZivaRename():
	zMaya.rename_ziva_nodes() 	
def coreToolZivaActivate():
	sele = cmds.ls(selection=True)
	for each in sele:	
		geoSele = cmds.listConnections( each+".worldMatrix[0]", s=False, d=True) or []	
		for x in geoSele:	
			zTissueSele = cmds.listConnections( x+".oGeo", s=False, d=True, type="zTissue")
			cmds.setAttr(zTissueSele[0]+".enable", not cmds.getAttr(zTissueSele[0]+".enable"))	
def coreToolZivaAllActivate():
	sele = cmds.ls('*__msh')
	print(sele)
	for each in sele:	
		geoSele = cmds.listConnections( each+".worldMatrix[0]", s=False, d=True) or []	
		for x in geoSele:	
			zTissueSele = cmds.listConnections( x+".oGeo", s=False, d=True, type="zTissue")
			if zTissueSele == None:
				pass
			else:
				cmds.setAttr(zTissueSele[0]+".enable", 1)		