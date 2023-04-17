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

# Use PySide2 or PyQt5.
try: from PySide2 import QtCore, QtGui, QtWidgets
except: from PyQt5 import QtCore, QtGui, QtWidgets
finally: __qt_binding__ = QtCore.__name__.partition('.')[0]

import sys
import os



#Skin tool

__myGlobalVar = None

def startEventSelection():

	global __myGlobalVar
 	
	if __myGlobalVar is not None:
		return
	__myGlobalVar = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", refreshSelectionVtx)
	refreshSelectionVtx()#Variable global qui active lactualisation du treeview en fonction des vertex selectiones
	if hadEnv.SHAPE:
		if cmds.getAttr(hadEnv.SHAPE+".displayColors"):
			cmds.select(hadEnv.SHAPE)
			try:
				cmds.polyColorPerVertex(remove=True)
			except:
				pass
	#Retire la colorisation des vertexs	

def endEventSelection():

	global __myGlobalVar
 	

	if __myGlobalVar:
		OpenMaya.MMessage.removeCallback(__myGlobalVar)
		__myGlobalVar = None
	#Supression de la variable global
	if hadEnv.SHAPE:
		cmds.setAttr(hadEnv.SHAPE+".displayColors", 0)
		cmds.listConnection(hadEnv.SHAPE, type = "polyColorPerVertex")
	#Cache la colorisation des vertexs

def refreshSelectionVtx(obsoleteArg=None):
	"""_summary_

	Args:
		obsoleteArg (None, optional): Use to avoid error on CallBack in startEventSelection and endEventSelection. Defaults to None.
	"""    
 
    #Fonction qui se lance a chaque fois que la selection change


	# import maya.cmds as cmds
	# import maya.mel as mel
	# import hades.hadEnv as hadEnv
	# try: from PySide2 import QtCore, QtGui, QtWidgets
	# except: from PyQt5 import QtCore, QtGui, QtWidgets
	# finally: __qt_binding__ = QtCore.__name__.partition('.')[0]

	# label selection vertices

	if hadEnv.SHAPE:
     	#Selectionne et sauvegarde la shape du mesh selectionne et active sa couleur
		cmds.setAttr(hadEnv.SHAPE+".displayColors", 1)
		print("TrueMesh", hadEnv.SHAPE)
	else:
		temp = cmds.ls(selection=True, flatten=True)[0]
		print("temp",temp)
		hadEnv.SHAPE = cmds.listRelatives(temp, parent=True, shapes=True)[0] or []
		if hadEnv.SHAPE:
			cmds.setAttr(hadEnv.SHAPE+".displayColors", 1)
		print("FalseMesh", hadEnv.SHAPE)
 

	listSelection = []
	lenVertices = 0
	listSelection = cmds.ls(selection=True)
	if listSelection:
		onlyVertices = cmds.filterExpand(listSelection, sm=31) or []#Filtre pour selectionne seulement les vertexs
		lenVertices = len(onlyVertices)
		if lenVertices:
			labelVertices = str(lenVertices)+ " Vertices Selected"
			hadEnv.LABEL_VERTICE_SELECTED.setText(labelVertices)
   		#Affiche le nombre de vertex selectionne
	else:
		hadEnv.LABEL_VERTICE_SELECTED.setText("0 Vertices Selected")
		return
	hadEnv.CURRENT_SELECTION = onlyVertices
 	#Sauvegarde le nombre de vertex de selectionne

	# list joints

	hadEnv.TREE_SKIN_VALUES.clear()#vide le treeview
 
	if hadEnv.CURRENT_SELECTION:#recupere un vtx
		refreshSelectionValue()

def refreshSelectionValue(obsoleteArg=None):
    
	if hadEnv.CURRENT_SKIN_CLUS:#Recupere le skin cluester et le sauvegarde
		skinCluster = hadEnv.CURRENT_SKIN_CLUS
	else:
		print("SHAPE" , hadEnv.SHAPE)

		skinCluster = hadLib.get_skinCluster(hadEnv.SHAPE)#recupre le skin cluster
		hadEnv.CURRENT_SKIN_CLUS = skinCluster

 
	print(skinCluster)
	if skinCluster:
		SkinDict = {}
		for vtx in hadEnv.CURRENT_SELECTION:#pour chaque vtx de la selection, recupere ses joints influences et les influences et les mets dans un dictionnaire
			influenceVals = cmds.skinPercent(skinCluster, vtx, query=1, value=1, ignoreBelow=0.000001)
			influenceNames = cmds.skinPercent(skinCluster, vtx, transform=None, query=1, ignoreBelow=0.000001)
			SkinDict[vtx] = [influenceNames, (influenceVals)]
		for vtx in SkinDict:#pour chaque vtx dans ce dico, les ajoutes dans le treeview
			for joint, value in zip(SkinDict[vtx][0],SkinDict[vtx][1]):
				value = format(value, '.4f')
				value = str(value)
				vertice = str(vtx)
				thanatosItem_tree = QtWidgets.QTreeWidgetItem([vertice,value,joint])
				hadEnv.TREE_SKIN_VALUES.addTopLevelItem(thanatosItem_tree)
				hadEnv.TREE_SKIN_VALUES.resizeColumnToContents(0)
	else:
		raise RuntimeError("Selected mesh has no skinCluster")

    

def selectionJoint():
	# import maya.cmds as cmds
	# import maya.api.OpenMaya as OpenMaya

	global __myGlobalVar 

	if __myGlobalVar:#Desactive la variable global pour evite dactualise inutilement et perdre la selection
		OpenMaya.MMessage.removeCallback(__myGlobalVar)
		__myGlobalVar = None

	selectedJoint = hadEnv.TREE_SKIN_VALUES.currentItem()#Recupere le joint quon aura selectioner	

	hadEnv.CURRENT_JOINT = selectedJoint.text(2)#sauvegarde le nom de ce joint

	if hadEnv.CURRENT_SHAPE:#Recupere et sauvegarde la shape du mesh
		seleShape = hadEnv.CURRENT_SHAPE
	else:
		
		seleShape = hadEnv.SHAPE
		hadEnv.CURRENT_SHAPE = seleShape

	if hadEnv.CURRENT_SKIN_CLUS:#Recupere le skin cluester et le sauvegarde
		sCluster = hadEnv.CURRENT_SKIN_CLUS
	else:
		sCluster = hadLib.get_skinCluster(hadEnv.SHAPE)
		hadEnv.CURRENT_SKIN_CLUS = sCluster
  
	skinInfluences = cmds.skinCluster(sCluster,query=True,influence=True)#recupere tous les joints de ce skincluster

	listeVtx =[]
	for influence in skinInfluences:
		if hadEnv.CURRENT_JOINT == influence:
			cmds.skinCluster(sCluster, edit=True, selectInfluenceVerts = influence)#pour le joint selectionne, selectionne tous les vtx qui ont une influence avec lui
			listeVtx = (cmds.ls(selection=True,flatten=True))
			break

	if cmds.getAttr(seleShape+".displayColors"):#enleve la couleur si il en a
		cmds.select(seleShape)
		try:
			cmds.polyColorPerVertex(remove=True)
		except:
			pass
	else:
		cmds.setAttr(seleShape+".displayColors", 1)	#active la couleur
	for vtx in listeVtx:#pour chaque vtx de ce joint...
		tempValue = (cmds.skinPercent( sCluster, vtx, transform=selectedJoint.text(2), query=True ))#...recupere sa valeur d influence...
		cmds.select(vtx)#...puis le selectionne...
		if 0 < tempValue < 0.1 :#...et applique la bonne couleur
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
	
	cmds.selectMode(component=True)#force la selectione de vtx
	cmds.select(hadEnv.CURRENT_SELECTION)#reselectione les vtx du debut


	tempMesh = cmds.listRelatives(hadEnv.SHAPE, parent=True)
	cmds.select(tempMesh, replace=True)

	cmds.selectMode(component=True)
	cmds.selectType(allComponents=False, vertex=True)

	cmds.select(hadEnv.CURRENT_SELECTION)








	if __myGlobalVar is not None:#reactive la variable global
		return
	__myGlobalVar = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", refreshSelectionVtx)

 
def corethanatosShrink():
	mel.eval('PolySelectTraverse 2')

def corethanatosGrow():
	mel.eval('PolySelectTraverse 1')

def corethanatosRing():
	cmds.polySelectSp(ring=True)

def corethanatosLoop():
	cmds.polySelectSp(loop=True)

def corethanatos0(self):
	hadLib.applyWeight(0)
	refreshSelectionValue(self)

def corethanatos01(self):
	hadLib.applyWeight(0.1)
	refreshSelectionValue(self)

def corethanatos025(self):
	hadLib.applyWeight(0.25)
	refreshSelectionValue(self)

def corethanatos05(self):
	hadLib.applyWeight(0.5)
	refreshSelectionValue(self)

def corethanatos075(self):
	hadLib.applyWeight(0.75)
	refreshSelectionValue(self)

def corethanatos09(self):
	hadLib.applyWeight(0.9)
	refreshSelectionValue(self)

def corethanatos1(self):
	hadLib.applyWeight(1)
	refreshSelectionValue(self)

def corethanatosSetWeight():
	pass

def corethanatosSetWeightAdd():
	pass

def corethanatosSetWeightSub():
	pass

def corethanatosScaleWeight():
	pass

def corethanatosScaleWeightAdd():
	pass

def corethanatosScaleWeightSub():
	pass

def corethanatosCopy():
	mel.eval('artAttrSkinWeightCopy;')
	listSelection = []
	lenVertices = 0
	listSelection = cmds.ls(selection=True)
	if listSelection:
		onlyVertices = cmds.filterExpand(listSelection, sm=31) or []
		lenVertices = len(onlyVertices)
		if lenVertices:
			labelVertices = str(lenVertices)+" Vertices In Copy Buffer"
			hadEnv.LABEL_VERTICE_MEMORY.setText(labelVertices)


def corethanatosPaste():
	mel.eval('artAttrSkinWeightPaste;')

def coreSkinTooPastePos():
	pass

def corethanatosBlend():
	pass




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