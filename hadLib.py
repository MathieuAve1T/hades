import maya.cmds as cmds
import hades.hadEnv as hadEnv

def setScale(object, x, y, z):
    
    cmds.setAttr(object + ".scaleX", x)
    cmds.setAttr(object + ".scaleY", y)
    cmds.setAttr(object + ".scaleZ", z) 

def setRotate(object, x, y, z):
    
    cmds.setAttr(object + ".rotateX", x)
    cmds.setAttr(object + ".rotateY", y)
    cmds.setAttr(object + ".rotateZ", z)
    
def setRotateOrient(object, x, y, z):
    
    cmds.setAttr(object + ".jointOrientX", x)
    cmds.setAttr(object + ".jointOrientY", y)
    cmds.setAttr(object + ".jointOrientZ", z)
    
def setTranslate(object, x, y, z):
    
    cmds.setAttr(object + ".translateX", x)
    cmds.setAttr(object + ".translateY", y)
    cmds.setAttr(object + ".translateZ", z)
    
def getRotate(object):
    
    TempX = cmds.getAttr(object + ".rotateX")
    TempY = cmds.getAttr(object + ".rotateY")
    TempZ = cmds.getAttr(object + ".rotateZ")
    
    return (TempX, TempY, TempZ)
    
def getTranslate(object):
    
    TempX = cmds.getAttr(object + ".translateX")
    TempY = cmds.getAttr(object + ".translateY")
    TempZ = cmds.getAttr(object + ".translateZ")
    
    return (TempX, TempY, TempZ)
    
def getScale(object):
    
    TempX = cmds.getAttr(object + ".ScaleX")
    TempY = cmds.getAttr(object + ".ScaleY")
    TempZ = cmds.getAttr(object + ".ScaleZ")
    
    return (TempX, TempY, TempZ)
    
def freezeTranslate(object):
    
    cmds.setAttr( object +'.translateX', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.translateY', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.translateZ', lock=True , keyable = False , channelBox=False )
    
def freezeRotate(object):
    
    cmds.setAttr( object +'.rotateX', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.rotateY', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.rotateZ', lock=True , keyable = False , channelBox=False )
    
def freezeScale(object):
    
    cmds.setAttr( object +'.scaleX', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.scaleY', lock=True , keyable = False , channelBox=False )
    cmds.setAttr( object +'.scaleZ', lock=True , keyable = False , channelBox=False )


def createLineDisplay(locaA, locaB):
    tempParentCrv = cmds.curve(name='DisplayLine.'+locaA+locaB, degree=1, point=[(0, 0, 0), (0, 0, 0)], knot=[0,1] )
    tempCrv = cmds.listRelatives(tempParentCrv, shapes=True)[0]
    cmds.connectAttr(locaA+".worldPosition[0]", tempCrv+".controlPoints[0]", force=True)
    cmds.connectAttr(locaB+".worldPosition[0]", tempCrv+".controlPoints[1]", force=True)
    cmds.setAttr( tempCrv + ".overrideEnabled", 1)
    cmds.setAttr( tempCrv + ".overrideDisplayType", 2)
    return tempParentCrv
    

def createIKJoints(object):
            
    tempIK = cmds.duplicate(object, renameChildren=True)
    JointsListIK = []
    for item in tempIK[::-1]: 
        shortname = item.rpartition("|")[-1]  
        JointsListIK.append(cmds.rename(item, shortname.replace(item[0:-1], item[0:-1]+"_IK")[:-1])) 
    JointsListIK.reverse()
    return (JointsListIK)    

def createFKJoints(object):    

    tempFK = cmds.duplicate(object, renameChildren=True)
    JointsListFK = []
    for item in tempFK[::-1]: 
        shortname = item.rpartition("|")[-1]  
        JointsListFK.append(cmds.rename(item, shortname.replace(item[0:-1], item[0:-1]+"_FK")[:-1]))
    JointsListFK.reverse()
    return (JointsListFK) 

def createPoleVector(start, middle, end, locaname, ik, side):

    bTStart = cmds.createNode('joint', name= "Start_Temp" +hadEnv.DICTMIRROR[side], skipSelect=True)
    cmds.matchTransform(bTStart , start, position=True, rotation=False, scale=False)
    bTEnd = cmds.createNode('joint', name= "End_Temp" +hadEnv.DICTMIRROR[side], skipSelect=True)
    cmds.matchTransform(bTEnd , end, position=True, rotation=False, scale=False)
   
    cmds.parent(bTEnd, bTStart)
    cmds.select(bTStart)
    cmds.select(hierarchy=True)
    cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")
    cmds.setAttr(bTEnd + ".jointOrientX", 0)
    cmds.setAttr(bTEnd + ".jointOrientY", 0)
    cmds.setAttr(bTEnd + ".jointOrientZ", 0)
        
    tempX = cmds.getAttr(middle + ".translateX")

    if side == 6:
        tempX = tempX * -1

    cmds.setAttr(bTEnd + ".translateX", tempX)

    bTEnd2 = cmds.createNode('joint', name= "End2_Temp" +hadEnv.DICTMIRROR[side], skipSelect=True)
    cmds.matchTransform(bTEnd2 , bTEnd, position=True, rotation=False, scale=False)
    bTMiddle2 = cmds.createNode('joint', name= "Middle2_Temp" +hadEnv.DICTMIRROR[side], skipSelect=True)
    cmds.matchTransform(bTMiddle2 , middle, position=True, rotation=False, scale=False)
        
    cmds.connectJoint( bTMiddle2, bTEnd2, pm=True )
    cmds.select(bTEnd2)
    cmds.select(hierarchy=True)
    cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")
    cmds.setAttr(bTMiddle2 + ".jointOrientX", 0)
    cmds.setAttr(bTMiddle2 + ".jointOrientY", 0)
    cmds.setAttr(bTMiddle2 + ".jointOrientZ", 0)
    cmds.setAttr(bTMiddle2 + ".translateX", tempX)

    TempLocatorEnd = (cmds.listRelatives(cmds.createNode('locator', name='Loc_End'+ locaname + hadEnv.DICTMIRROR[side], skipSelect=True), parent=True)[0])
    tempLocaShapeEnd = cmds.listRelatives(TempLocatorEnd, children=True)[0]
    TempLocatorEnd = cmds.rename(TempLocatorEnd, 'Locator'+tempLocaShapeEnd)    
    TempLocatorStart = (cmds.listRelatives(cmds.createNode('locator', name='Loc_Start'+ locaname + hadEnv.DICTMIRROR[side], skipSelect=True), parent=True)[0]) 
    tempLocaShapeStart = cmds.listRelatives(TempLocatorStart, children=True)[0]
    TempLocatorStart = cmds.rename(TempLocatorStart, 'Locator'+tempLocaShapeStart)  
    cmds.setAttr(TempLocatorEnd +".visibility", 0)
    cmds.setAttr(TempLocatorStart +".visibility", 0)
    cmds.matchTransform(TempLocatorEnd, bTMiddle2)
    cmds.setAttr(TempLocatorEnd+".rotateX", 0)
    cmds.setAttr(TempLocatorEnd+".rotateY", 0)
    cmds.setAttr(TempLocatorEnd+".rotateZ", 0)
    
    cmds.delete(bTStart)
    cmds.delete(bTEnd2)
            
    PoleVectorLeg = cmds.curve(name="Ctrl_"+locaname + hadEnv.DICTMIRROR[side], degree=1, point=[(0, 1, 0) ,(0, 0, 1) ,(0, -1, 0) ,(0, 0, -1) ,(0, 1, 0) ,(-1, 0, 0) ,(0, -1, 0) ,(1, 0, 0) ,(0, 1, 0) ,(-1, 0, 0) ,(0, 0, 1) ,(1, 0, 0) ,(0, 0, -1) ,(-1, 0, 0)], knot = [0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    GrpPoleVectorLeg = cmds.group(PoleVectorLeg, name='Grp*'+PoleVectorLeg)
    
    cmds.matchTransform(GrpPoleVectorLeg, TempLocatorEnd)
    cmds.parent(TempLocatorEnd, PoleVectorLeg)
    cmds.parent(TempLocatorStart, middle, relative=True)
    
    cmds.poleVectorConstraint( PoleVectorLeg, ik)

    tempParentCrv = cmds.curve(name='DisplayLine.'+start+end, degree=1, point=[(0, 0, 0), (0, 0, 0)], knot=[0,1] )
    tempCrv = cmds.listRelatives(tempParentCrv, shapes=True)[0]
    cmds.connectAttr(TempLocatorEnd+".worldPosition[0]", tempCrv+".controlPoints[0]", force=True)
    cmds.connectAttr(TempLocatorStart+".worldPosition[0]", tempCrv+".controlPoints[1]", force=True)
    cmds.setAttr( tempCrv + ".overrideEnabled", 1)
    cmds.setAttr( tempCrv + ".overrideDisplayType", 2)
    
    cmds.setAttr(PoleVectorLeg + ".overrideEnabled", 1)
    cmds.setAttr(PoleVectorLeg + ".overrideColor", 6+side)  
    cmds.parent(tempParentCrv,'Xtra_toHide')

    return PoleVectorLeg
    





def createCircle():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.circle(normal=(0, 1, 0), center=(0, 0, 0), radius=r, name= "Ctrl_"+sele, constructionHistory=False)[0]
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)

def createTriangle():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.circle( normal=(0, 1, 0), center=(0, 0, 0), radius=r, degree=1, sections=1,name="Ctrl_"+sele, constructionHistory=False)[0] 
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)

def createSquare():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point=[(-r, 0, r), (r, 0, r), (r, 0, -r), (-r, 0, -r), (-r, 0, r)] ) 
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)

def createCross():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point=[(-2*r, 0, -1*r), (-1*r, 0, -1*r), (-1*r, 0, -2*r), (1*r, 0, -2*r), (1*r, 0, -1*r), (2*r, 0, -1*r), (2*r, 0, 1*r), (1*r, 0, 1*r), (1*r, 0, 2*r), (-1*r, 0, 2*r), (-1*r, 0, 1*r), (-2*r, 0, 1*r), (-2*r, 0, -1*r), (-1*r, 0, -1*r)])
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)

def createBox():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point=[(-r, -r, r), (-r, r, r), (r, r, r), (r, -r, r), (-r, -r, r), (-r, -r, -r), (-r, r, -r), (-r, r, r), (r, r, r), (r, r, -r), (r, -r, -r), (r, -r, r), (r, -r, -r), (-r, -r, -r), (-r, r, -r), (r, r, -r)] )
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)

def createDiamond():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point = [( r, 0, 0 ), ( 0, 0, -r ), ( -r, 0, 0 ),( 0, 0, r, ), ( 0, -r, 0 ), ( 0, 0, -r ),( 0, r, 0 ), ( -r, 0, 0 ), ( 0, -r, 0 ),( r, 0, 0 ), ( 0, r, 0 ), ( 0, 0, r ),( r, 0, 0 )],knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] )
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)    

def createBall():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=3, point=[	(0.5*r, 0.0, 0.0), (0.462*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r),(0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (-0.19*r, 0.0, 0.46*r),(-0.35*r, 0.0, 0.35*r), (-0.46*r, 0.0, 0.19*r), (-0.5*r, 0.0, 0.0),(-0.46*r, 0.0, -0.19*r), (-0.35*r, 0.0, -0.35*r), (-0.19*r, 0.0, -0.46*r),(0.0, 0.0, -0.5*r), (0.19*r, 0.0, -0.46*r), (0.35*r, 0.0, -0.35*r),(0.46*r, 0.0, -0.19*r), (0.5*r, 0.0, 0.0), (0.46*r, -0.19*r, 0.0*r),(0.35*r, -0.35*r, 0.0), (0.19*r, -0.46*r, 0.0), (0.0, -0.5*r, 0.0), (-0.19*r, -0.46*r, 0.0), (-0.35*r, -0.35*r, 0.0), (-0.46*r, -0.19*r, 0.0), (-0.5*r, 0.0, 0.0), (-0.46*r, 0.19*r, 0.0), (-0.35*r, 0.35*r, 0.0), (-0.19*r, 0.46*r, 0.0), (0.0, 0.5*r, 0.0), (0.19*r, 0.46*r, 0.0), (0.35*r, 0.35*r, 0.0), (0.46*r, 0.19*r, 0.0), (0.5*r, 0.0, 0.0), (0.46*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r), (0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (0.0, 0.24*r, 0.44*r), (0.0, 0.44*r, 0.24*r), (0.0, 0.5*r, 0.0), (0.0, 0.44*r, -0.24*r), (0.0, 0.24*r, -0.44*r), (0.0, 0.0, -0.5*r), (0.0, -0.24*r, -0.44*r), (0.0, -0.44*r, -0.24*r), (0.0, -0.5*r, 0.0), (0.0, -0.44*r, 0.24*r), (0.0, -0.24*r, 0.44*r), (0.0, 0.0, 0.5*r)] )
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)  

def createArrow():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point=[(0, 0, 0), (0, 0, -0.44*r), (0, 0, -0.9*r), (0, 0, -1.23*r), (-0.21*r, 0, -1.37*r), (-0.44*r, 0, -2*r), (0, 0, -2.2*r), (0.44*r, 0, -2*r), (0.21*r, 0, -1.37*r), (0, 0, -1.23*r), (0, 0.21*r, -1.37*r), (0, 0.44*r, -2*r), (0, 0, -2.2*r), (0, -0.44*r, -2*r), (0, -0.21*r, -1.37*r), (0, 0, -1.23*r)] )
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)    

def createLocator():

    x = False
    r = hadEnv.CTRLSIZEVALUE
    if cmds.ls(selection=True):
        sele = cmds.ls(selection=True)[0]
        x = True
    else:
        sele=""
    tempCrv = cmds.curve(name="Ctrl_"+sele, degree=1, point=[(0, 0, r), (0, 0, -r), (0, 0, 0), (r, 0, 0), (-r, 0, 0), (0, 0, 0), (0, r, 0), (0, -r, 0)] )
    if hadEnv.CTRLGRPVALUE:
        tempGrp = cmds.createNode('transform', name='Grp_'+tempCrv, skipSelect=True)
        cmds.parent(tempCrv, tempGrp)
    if x == True and hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempGrp, sele)
    elif x == True and not hadEnv.CTRLGRPVALUE:
        cmds.matchTransform(tempCrv, sele)    

def setZMaterial(value, valueEx):
    sele = cmds.ls(sl=True)
    listZMaterial = []
    if cmds.objectType( sele[0], isType='zMaterial'):
        listZMaterial.append(sele[0])
    else:
        for each in sele:
            allzGeo = cmds.ls( cmds.listConnections(each, destination=True, source=True, type='zGeo'), long=True )
            for sGeo in allzGeo:
                allzTissue = cmds.ls( cmds.listConnections(sGeo, destination=True, source=True, type='zTissue'), long=True ) 
                for zTissue in allzTissue:
                    allzTet = cmds.ls( cmds.listConnections(zTissue, destination=True, source=True, type='zTet'), long=True )
                    for zTet in allzTet:
                        ZMaterial = cmds.ls( cmds.listConnections(zTet, destination=True, source=True, type='zMaterial'), long=True )	
                        for x in ZMaterial:
                            listZMaterial.append(x)	                       
    for each in listZMaterial:
        cmds.setAttr(each+'.youngsModulus',value)
        cmds.setAttr(each+'.youngsModulusExp',valueEx)