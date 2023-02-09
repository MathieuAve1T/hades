import maya.cmds as cmds
import hades.hadLib as hadLib
import hades.hadEnv as hadEnv


class AutoRigCreateGuide(object):

    def autoRigPreModule(self):

        hadEnv.GUIDE_LINE_GRP = cmds.createNode('transform', name='Grp_GuideLine', skipSelect=True)

    def AUTO_RIG_CHESTModule(self):

        if hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_CHEST_GUIDE = []
            hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE = []
        
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Root', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 11, -0.434], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_CHEST_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Hip', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 11, 0.295], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_CHEST_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='SpineA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 12.448, -0.735], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_CHEST_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='SpineC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 13.867, -0.828], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_CHEST_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Chest', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 15.135, -1.096], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_CHEST_GUIDE.append(tempLoca)       

        for each in hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            r=0.25
            tempCrv = cmds.curve(name="Guide_"+each, degree=3, point=[	(0.5*r, 0.0, 0.0), (0.462*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r),(0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (-0.19*r, 0.0, 0.46*r),(-0.35*r, 0.0, 0.35*r), (-0.46*r, 0.0, 0.19*r), (-0.5*r, 0.0, 0.0),(-0.46*r, 0.0, -0.19*r), (-0.35*r, 0.0, -0.35*r), (-0.19*r, 0.0, -0.46*r),(0.0, 0.0, -0.5*r), (0.19*r, 0.0, -0.46*r), (0.35*r, 0.0, -0.35*r),(0.46*r, 0.0, -0.19*r), (0.5*r, 0.0, 0.0), (0.46*r, -0.19*r, 0.0*r),(0.35*r, -0.35*r, 0.0), (0.19*r, -0.46*r, 0.0), (0.0, -0.5*r, 0.0), (-0.19*r, -0.46*r, 0.0), (-0.35*r, -0.35*r, 0.0), (-0.46*r, -0.19*r, 0.0), (-0.5*r, 0.0, 0.0), (-0.46*r, 0.19*r, 0.0), (-0.35*r, 0.35*r, 0.0), (-0.19*r, 0.46*r, 0.0), (0.0, 0.5*r, 0.0), (0.19*r, 0.46*r, 0.0), (0.35*r, 0.35*r, 0.0), (0.46*r, 0.19*r, 0.0), (0.5*r, 0.0, 0.0), (0.46*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r), (0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (0.0, 0.24*r, 0.44*r), (0.0, 0.44*r, 0.24*r), (0.0, 0.5*r, 0.0), (0.0, 0.44*r, -0.24*r), (0.0, 0.24*r, -0.44*r), (0.0, 0.0, -0.5*r), (0.0, -0.24*r, -0.44*r), (0.0, -0.44*r, -0.24*r), (0.0, -0.5*r, 0.0), (0.0, -0.44*r, 0.24*r), (0.0, -0.24*r, 0.44*r), (0.0, 0.0, 0.5*r)] )
            cmds.matchTransform(tempCrv, each)
            cmds.parent(each, tempCrv)
            cmds.setAttr(each+".visibility", 0)
        
        listLocaA = [hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[0],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[0],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[2],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[3]]
        listLocaB = [hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[1],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[2],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[3],hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[4]]
       
        for parentLocaA, parentLocaB in zip(listLocaA, listLocaB):

            locaA = cmds.listRelatives( parentLocaA, children=True, shapes=True)[0]
            locaB = cmds.listRelatives( parentLocaB, children=True, shapes=True)[0]

            masterLocaA = cmds.listRelatives( parentLocaA, parent=True)[0]
            masterLocaB = cmds.listRelatives( parentLocaB, parent=True)[0]

            cmds.parent(masterLocaB, masterLocaA)
        
            hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE.append(hadLib.createLineDisplay(locaA, locaB))

            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE[-1], hadEnv.GUIDE_LINE_GRP)

 

    def AUTO_RIG_ARMModule(self, *args):  

        if hadEnv.AUTO_RIG_LIST_ARM_GUIDE and not hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_ARM_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_ARM_GUIDE = []
            hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE = []
        elif hadEnv.AUTO_RIG_LIST_ARM_GUIDE and hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            for each in hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_ARM_GUIDE = []
            hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE = []
        else:
            pass

        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Clavicle', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0.488, 15.281, 0.17], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Shoulder', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.49, 15.212, -0.668], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Elbow', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[3.46, 13.554, -0.931], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Wrist', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[5.323, 11.897, 0.283], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='ThumbA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[5.388, 11.459, 0.759], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='ThumbB', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[5.339, 11.178, 1.044], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='ThumbC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[5.362, 10.839, 1.111], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Metacarp', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[5.531, 11.708, 0.405], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='IndexA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.04, 11.002, 1.156], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='IndexB', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.175, 10.742, 1.22], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='IndexC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.144, 10.443, 1.238], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='MidA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.204, 11.078, 0.858], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='MidB', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.312, 10.663, 0.954], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='MidC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.295, 10.36, 0.969], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='RingA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.242, 11.017, 0.556], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='RingB', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.335, 10.62, 0.655], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='RingC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.311, 10.339, 0.708], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='PinkyA', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.166, 11.019, 0.304], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='PinkyB', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.306, 10.659, 0.371], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='PinkyC', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[6.272, 10.417, 0.412], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_ARM_GUIDE.append(tempLoca)

        for each in hadEnv.AUTO_RIG_LIST_ARM_GUIDE:
            tempChild = cmds.listRelatives(each, children=True)[0]
            r=0.25
            tempCrv = cmds.curve(name="Guide_"+tempChild, degree=3, point=[	(0.5*r, 0.0, 0.0), (0.462*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r),(0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (-0.19*r, 0.0, 0.46*r),(-0.35*r, 0.0, 0.35*r), (-0.46*r, 0.0, 0.19*r), (-0.5*r, 0.0, 0.0),(-0.46*r, 0.0, -0.19*r), (-0.35*r, 0.0, -0.35*r), (-0.19*r, 0.0, -0.46*r),(0.0, 0.0, -0.5*r), (0.19*r, 0.0, -0.46*r), (0.35*r, 0.0, -0.35*r),(0.46*r, 0.0, -0.19*r), (0.5*r, 0.0, 0.0), (0.46*r, -0.19*r, 0.0*r),(0.35*r, -0.35*r, 0.0), (0.19*r, -0.46*r, 0.0), (0.0, -0.5*r, 0.0), (-0.19*r, -0.46*r, 0.0), (-0.35*r, -0.35*r, 0.0), (-0.46*r, -0.19*r, 0.0), (-0.5*r, 0.0, 0.0), (-0.46*r, 0.19*r, 0.0), (-0.35*r, 0.35*r, 0.0), (-0.19*r, 0.46*r, 0.0), (0.0, 0.5*r, 0.0), (0.19*r, 0.46*r, 0.0), (0.35*r, 0.35*r, 0.0), (0.46*r, 0.19*r, 0.0), (0.5*r, 0.0, 0.0), (0.46*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r), (0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (0.0, 0.24*r, 0.44*r), (0.0, 0.44*r, 0.24*r), (0.0, 0.5*r, 0.0), (0.0, 0.44*r, -0.24*r), (0.0, 0.24*r, -0.44*r), (0.0, 0.0, -0.5*r), (0.0, -0.24*r, -0.44*r), (0.0, -0.44*r, -0.24*r), (0.0, -0.5*r, 0.0), (0.0, -0.44*r, 0.24*r), (0.0, -0.24*r, 0.44*r), (0.0, 0.0, 0.5*r)] )
            cmds.matchTransform(tempCrv, each)
            cmds.parent(each, tempCrv)
            cmds.setAttr(each+".visibility", 0)
        
        listLocaA = [hadEnv.AUTO_RIG_LIST_ARM_GUIDE[0],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[1],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[2],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[3],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[4],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[5],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[3],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[7],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[8],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[9],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[7],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[11],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[12],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[7],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[14],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[15],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[7],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[17],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[18]]
        listLocaB = [hadEnv.AUTO_RIG_LIST_ARM_GUIDE[1],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[2],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[3],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[4],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[5],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[6],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[7],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[8],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[9],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[10],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[11],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[12],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[13],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[14],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[15],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[16],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[17],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[18],hadEnv.AUTO_RIG_LIST_ARM_GUIDE[19]]
        
        if hadEnv.AUTO_RIG_CHEST:
            listLocaA.append(hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[4])
            listLocaB.append(hadEnv.AUTO_RIG_LIST_ARM_GUIDE[0])

        for parentLocaA, parentLocaB in zip(listLocaA, listLocaB):

            locaA = cmds.listRelatives( parentLocaA, children=True, shapes=True)[0]
            locaB = cmds.listRelatives( parentLocaB, children=True, shapes=True)[0]

            masterLocaA = cmds.listRelatives( parentLocaA, parent=True)[0]
            masterLocaB = cmds.listRelatives( parentLocaB, parent=True)[0]

            cmds.parent(masterLocaB, masterLocaA)
        
            hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE.append(hadLib.createLineDisplay(locaA, locaB))

            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE[-1], hadEnv.GUIDE_LINE_GRP)



    def AUTO_RIG_LEGModule(self):

        if hadEnv.AUTO_RIG_LIST_LEG_GUIDE and not hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_LEG_GUIDE[-1], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_LEG_GUIDE = []
            hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE = []
        elif hadEnv.AUTO_RIG_LIST_LEG_GUIDE and hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            for each in hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_LEG_GUIDE = []
            hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE = []
        else:
            pass
        
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Heel', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.681, 0, -1.373], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Toe', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.857, 0.5, 1.238], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='TiltIn', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.288, 0, 0.137], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='TiltOut', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[2.425, 0, 0.137], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Foot', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.768, 0.5, 0.108], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Ankle', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.681, 1.309, -0.773], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Knee', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.369, 5.728, -0.229], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Thigh', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[1.092, 10.583, -0.239], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_LEG_GUIDE.append(tempLoca)       

        for each in hadEnv.AUTO_RIG_LIST_LEG_GUIDE:
            r=0.25
            tempCrv = cmds.curve(name="Guide_"+each, degree=3, point=[	(0.5*r, 0.0, 0.0), (0.462*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r),(0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (-0.19*r, 0.0, 0.46*r),(-0.35*r, 0.0, 0.35*r), (-0.46*r, 0.0, 0.19*r), (-0.5*r, 0.0, 0.0),(-0.46*r, 0.0, -0.19*r), (-0.35*r, 0.0, -0.35*r), (-0.19*r, 0.0, -0.46*r),(0.0, 0.0, -0.5*r), (0.19*r, 0.0, -0.46*r), (0.35*r, 0.0, -0.35*r),(0.46*r, 0.0, -0.19*r), (0.5*r, 0.0, 0.0), (0.46*r, -0.19*r, 0.0*r),(0.35*r, -0.35*r, 0.0), (0.19*r, -0.46*r, 0.0), (0.0, -0.5*r, 0.0), (-0.19*r, -0.46*r, 0.0), (-0.35*r, -0.35*r, 0.0), (-0.46*r, -0.19*r, 0.0), (-0.5*r, 0.0, 0.0), (-0.46*r, 0.19*r, 0.0), (-0.35*r, 0.35*r, 0.0), (-0.19*r, 0.46*r, 0.0), (0.0, 0.5*r, 0.0), (0.19*r, 0.46*r, 0.0), (0.35*r, 0.35*r, 0.0), (0.46*r, 0.19*r, 0.0), (0.5*r, 0.0, 0.0), (0.46*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r), (0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (0.0, 0.24*r, 0.44*r), (0.0, 0.44*r, 0.24*r), (0.0, 0.5*r, 0.0), (0.0, 0.44*r, -0.24*r), (0.0, 0.24*r, -0.44*r), (0.0, 0.0, -0.5*r), (0.0, -0.24*r, -0.44*r), (0.0, -0.44*r, -0.24*r), (0.0, -0.5*r, 0.0), (0.0, -0.44*r, 0.24*r), (0.0, -0.24*r, 0.44*r), (0.0, 0.0, 0.5*r)] )
            cmds.matchTransform(tempCrv, each)
            cmds.parent(each, tempCrv)
            cmds.setAttr(each+".visibility", 0)
        
        listLocaA = [hadEnv.AUTO_RIG_LIST_LEG_GUIDE[4],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[4],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[4],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[4],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[5],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[6],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[7]]
        listLocaB = [hadEnv.AUTO_RIG_LIST_LEG_GUIDE[0],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[1],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[2],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[3],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[4],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[5],hadEnv.AUTO_RIG_LIST_LEG_GUIDE[6]]
        
        if hadEnv.AUTO_RIG_CHEST:
            listLocaA.append(hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[1])
            listLocaB.append(hadEnv.AUTO_RIG_LIST_LEG_GUIDE[-1])

        for parentLocaA, parentLocaB in zip(listLocaA, listLocaB):

            locaA = cmds.listRelatives( parentLocaA, children=True, shapes=True)[0]
            locaB = cmds.listRelatives( parentLocaB, children=True, shapes=True)[0]

            masterLocaA = cmds.listRelatives( parentLocaA, parent=True)[0]
            masterLocaB = cmds.listRelatives( parentLocaB, parent=True)[0]

            cmds.parent(masterLocaB, masterLocaA)
        
            hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE.append(hadLib.createLineDisplay(locaA, locaB))

            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE[-1], hadEnv.GUIDE_LINE_GRP)




    def AUTO_RIG_HEADModule(self):

        if hadEnv.AUTO_RIG_LIST_HEAD_GUIDE and not hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDE = []
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE = []
        elif hadEnv.AUTO_RIG_LIST_HEAD_GUIDE and hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            for each in hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDE = []
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE = []
        else:
            pass
        
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Neck', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 16.074, -0.585], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_HEAD_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='Head', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 16.806, -0.382], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_HEAD_GUIDE.append(tempLoca)
        tempLoca = (cmds.listRelatives(cmds.createNode('locator', name='HeadEnd', skipSelect=True), parent=True)[0])
        cmds.xform(tempLoca, translation=[0, 18, -0.382], worldSpace=True)
        tempLocaShape = cmds.listRelatives(tempLoca, children=True)[0]
        tempLoca = cmds.rename(tempLoca, 'Locator'+tempLocaShape)
        hadEnv.AUTO_RIG_LIST_HEAD_GUIDE.append(tempLoca)      

        for each in hadEnv.AUTO_RIG_LIST_HEAD_GUIDE:
            r=0.25
            tempCrv = cmds.curve(name="Guide_"+each, degree=3, point=[	(0.5*r, 0.0, 0.0), (0.462*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r),(0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (-0.19*r, 0.0, 0.46*r),(-0.35*r, 0.0, 0.35*r), (-0.46*r, 0.0, 0.19*r), (-0.5*r, 0.0, 0.0),(-0.46*r, 0.0, -0.19*r), (-0.35*r, 0.0, -0.35*r), (-0.19*r, 0.0, -0.46*r),(0.0, 0.0, -0.5*r), (0.19*r, 0.0, -0.46*r), (0.35*r, 0.0, -0.35*r),(0.46*r, 0.0, -0.19*r), (0.5*r, 0.0, 0.0), (0.46*r, -0.19*r, 0.0*r),(0.35*r, -0.35*r, 0.0), (0.19*r, -0.46*r, 0.0), (0.0, -0.5*r, 0.0), (-0.19*r, -0.46*r, 0.0), (-0.35*r, -0.35*r, 0.0), (-0.46*r, -0.19*r, 0.0), (-0.5*r, 0.0, 0.0), (-0.46*r, 0.19*r, 0.0), (-0.35*r, 0.35*r, 0.0), (-0.19*r, 0.46*r, 0.0), (0.0, 0.5*r, 0.0), (0.19*r, 0.46*r, 0.0), (0.35*r, 0.35*r, 0.0), (0.46*r, 0.19*r, 0.0), (0.5*r, 0.0, 0.0), (0.46*r, 0.0, 0.19*r), (0.35*r, 0.0, 0.35*r), (0.19*r, 0.0, 0.46*r), (0.0, 0.0, 0.5*r), (0.0, 0.24*r, 0.44*r), (0.0, 0.44*r, 0.24*r), (0.0, 0.5*r, 0.0), (0.0, 0.44*r, -0.24*r), (0.0, 0.24*r, -0.44*r), (0.0, 0.0, -0.5*r), (0.0, -0.24*r, -0.44*r), (0.0, -0.44*r, -0.24*r), (0.0, -0.5*r, 0.0), (0.0, -0.44*r, 0.24*r), (0.0, -0.24*r, 0.44*r), (0.0, 0.0, 0.5*r)] )
            cmds.matchTransform(tempCrv, each)
            cmds.parent(each, tempCrv)
            cmds.setAttr(each+".visibility", 0)

        listLocaA = [hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[0],hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[1]]
        listLocaB = [hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[1],hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[2]]

        if hadEnv.AUTO_RIG_CHEST:
            listLocaA.append(hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[4])
            listLocaB.append(hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[0])
        
        for parentLocaA, parentLocaB in zip(listLocaA, listLocaB):

            locaA = cmds.listRelatives( parentLocaA, children=True, shapes=True)[0]
            locaB = cmds.listRelatives( parentLocaB, children=True, shapes=True)[0]

            masterLocaA = cmds.listRelatives( parentLocaA, parent=True)[0]
            masterLocaB = cmds.listRelatives( parentLocaB, parent=True)[0]

            cmds.parent(masterLocaB, masterLocaA)
        
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE.append(hadLib.createLineDisplay(locaA, locaB))

            cmds.parent(hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE[-1], hadEnv.GUIDE_LINE_GRP)

class AutoRigGenerateRig(object):

    def autoRigCreateJoints(self):

        if hadEnv.AUTO_RIG_MIRROR:
            side=0
        else:
            side=17

        if hadEnv.AUTO_RIG_LIST_LEG_GUIDE:

            for each in hadEnv.AUTO_RIG_LIST_LEG_GUIDE:
                locaShape = cmds.listRelatives(each, children=True, shapes=True)[0]
                hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.createNode('joint', name="Bs_"+ locaShape + hadEnv.DICT_MIRROR[side], skipSelect=True))
                cmds.matchTransform(hadEnv.AUTO_RIG_LIST_LEG_JOINT[-1], each, rotation=False, scale=False)

            x, y, z = hadLib.getTranslate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[1])

            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.createNode('joint', name="Bdrv_Toe" + hadEnv.DICT_MIRROR[side], skipSelect=True))
            cmds.setAttr(hadEnv.AUTO_RIG_LIST_LEG_JOINT[-1] + ".translateX", x)
            cmds.setAttr(hadEnv.AUTO_RIG_LIST_LEG_JOINT[-1] + ".translateY",0)
            cmds.setAttr(hadEnv.AUTO_RIG_LIST_LEG_JOINT[-1] + ".translateZ", z)

            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[4], name= 'Bdrv_BallMaster' + hadEnv.DICT_MIRROR[side], parentOnly=True)[0])
            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[4], name= 'Bdrv_BallToe' + hadEnv.DICT_MIRROR[side], parentOnly=True)[0])
            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[1], name= 'Bdrv_BallToeEnd' + hadEnv.DICT_MIRROR[side], parentOnly=True)[0])
            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[4], name= 'Bdrv_BallAnkle' + hadEnv.DICT_MIRROR[side], parentOnly=True)[0])
            hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_LEG_JOINT[5], name= 'Bdrv_BallAnkleEnd' + hadEnv.DICT_MIRROR[side], parentOnly=True)[0])

            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[1], hadEnv.AUTO_RIG_LIST_LEG_JOINT[4])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[4], hadEnv.AUTO_RIG_LIST_LEG_JOINT[5])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[5], hadEnv.AUTO_RIG_LIST_LEG_JOINT[6])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[6], hadEnv.AUTO_RIG_LIST_LEG_JOINT[7])

            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[3], hadEnv.AUTO_RIG_LIST_LEG_JOINT[2])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0], hadEnv.AUTO_RIG_LIST_LEG_JOINT[3])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[8], hadEnv.AUTO_RIG_LIST_LEG_JOINT[0])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[9], hadEnv.AUTO_RIG_LIST_LEG_JOINT[8])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[10], hadEnv.AUTO_RIG_LIST_LEG_JOINT[9])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[11], hadEnv.AUTO_RIG_LIST_LEG_JOINT[10])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[12], hadEnv.AUTO_RIG_LIST_LEG_JOINT[9])
            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[13], hadEnv.AUTO_RIG_LIST_LEG_JOINT[12])

            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_LEG_GUIDE[-1], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_LEG_GUIDE = []
            hadEnv.AUTO_RIG_LIST_LEG_GUIDELINE = []

            cmds.select(hadEnv.AUTO_RIG_LIST_LEG_JOINT[8])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            cmds.select(hadEnv.AUTO_RIG_LIST_LEG_JOINT[7])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            TempEndJoint = [hadEnv.AUTO_RIG_LIST_LEG_JOINT[1], hadEnv.AUTO_RIG_LIST_LEG_JOINT[13], hadEnv.AUTO_RIG_LIST_LEG_JOINT[11]]
            for each in TempEndJoint:
                for attr in [".jointOrientX", ".jointOrientY", ".jointOrientZ"]:
                    cmds.setAttr(each+attr, 0)

            tempSeleA = cmds.listRelatives(hadEnv.AUTO_RIG_LIST_LEG_JOINT[7], allDescendents=True)
            tempSeleA.append(hadEnv.AUTO_RIG_LIST_LEG_JOINT[7])
            tempSeleB = cmds.listRelatives(hadEnv.AUTO_RIG_LIST_LEG_JOINT[2], allDescendents=True)
            tempSeleB.append(hadEnv.AUTO_RIG_LIST_LEG_JOINT[2])

            tempSeleA.reverse()
            tempSeleB.reverse()

            tempSeleC = [tempSeleB[0],tempSeleB[1],tempSeleB[2],tempSeleB[3],tempSeleB[4],tempSeleB[7],tempSeleB[8],tempSeleB[5],tempSeleB[6]]

            hadEnv.AUTO_RIG_LIST_LEG_JOINT = []
            for each in tempSeleA:
                hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(each)
            for each in tempSeleC:
                hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(each)

        if hadEnv.AUTO_RIG_LIST_ARM_GUIDE:

            for each in hadEnv.AUTO_RIG_LIST_ARM_GUIDE:
                locaShape = cmds.listRelatives(each, children=True, shapes=True)[0]
                hadEnv.AUTO_RIG_LIST_ARM_JOINT.append(cmds.createNode('joint', name="Bs_"+ locaShape + hadEnv.DICT_MIRROR[side], skipSelect=True))
                cmds.matchTransform(hadEnv.AUTO_RIG_LIST_ARM_JOINT[-1], each, rotation=False, scale=False) 

            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[1], hadEnv.AUTO_RIG_LIST_ARM_JOINT[0])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[2], hadEnv.AUTO_RIG_LIST_ARM_JOINT[1])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[3], hadEnv.AUTO_RIG_LIST_ARM_JOINT[2])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4], hadEnv.AUTO_RIG_LIST_ARM_JOINT[3])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[5], hadEnv.AUTO_RIG_LIST_ARM_JOINT[4])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[6], hadEnv.AUTO_RIG_LIST_ARM_JOINT[5])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[7], hadEnv.AUTO_RIG_LIST_ARM_JOINT[3])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[8], hadEnv.AUTO_RIG_LIST_ARM_JOINT[7])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[9], hadEnv.AUTO_RIG_LIST_ARM_JOINT[8])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[10], hadEnv.AUTO_RIG_LIST_ARM_JOINT[9])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[11], hadEnv.AUTO_RIG_LIST_ARM_JOINT[7])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[12], hadEnv.AUTO_RIG_LIST_ARM_JOINT[11])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[13], hadEnv.AUTO_RIG_LIST_ARM_JOINT[12])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[14], hadEnv.AUTO_RIG_LIST_ARM_JOINT[7])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[15], hadEnv.AUTO_RIG_LIST_ARM_JOINT[14])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[16], hadEnv.AUTO_RIG_LIST_ARM_JOINT[15])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[17], hadEnv.AUTO_RIG_LIST_ARM_JOINT[7])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[18], hadEnv.AUTO_RIG_LIST_ARM_JOINT[17])
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[19], hadEnv.AUTO_RIG_LIST_ARM_JOINT[18])

            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_ARM_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_ARM_GUIDE = []
            hadEnv.AUTO_RIG_LIST_ARM_GUIDELINE = [] 

            cmds.select(hadEnv.AUTO_RIG_LIST_ARM_JOINT[0])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            cmds.select(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xzy", secondaryAxisOrient="yup")

            cmds.parent( hadEnv.AUTO_RIG_LIST_ARM_JOINT[5], world=True )       
            TempX = cmds.getAttr(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4] + ".jointOrientX")
            TempY = cmds.getAttr(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4] + ".jointOrientY")
            TempX = TempX - TempY         
            cmds.setAttr(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4] + ".jointOrientX", TempX)
            cmds.setAttr(hadEnv.AUTO_RIG_LIST_ARM_JOINT[4] + ".jointOrientZ", 0)           
            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[5], hadEnv.AUTO_RIG_LIST_ARM_JOINT[4])

            cmds.parent( hadEnv.AUTO_RIG_LIST_ARM_JOINT[4], world=True )
            cmds.parent( hadEnv.AUTO_RIG_LIST_ARM_JOINT[7], world=True )

            TempEndJoint = [hadEnv.AUTO_RIG_LIST_ARM_JOINT[3], hadEnv.AUTO_RIG_LIST_ARM_JOINT[19], hadEnv.AUTO_RIG_LIST_ARM_JOINT[16], hadEnv.AUTO_RIG_LIST_ARM_JOINT[13],hadEnv.AUTO_RIG_LIST_ARM_JOINT[10], hadEnv.AUTO_RIG_LIST_ARM_JOINT[6]]
            for each in TempEndJoint:
                for attr in [".jointOrientX", ".jointOrientY", ".jointOrientZ"]:
                    cmds.setAttr(each+attr, 0)

            cmds.parent( hadEnv.AUTO_RIG_LIST_ARM_JOINT[4], hadEnv.AUTO_RIG_LIST_ARM_JOINT[3] )
            cmds.parent( hadEnv.AUTO_RIG_LIST_ARM_JOINT[7], hadEnv.AUTO_RIG_LIST_ARM_JOINT[3] )

        if hadEnv.AUTO_RIG_LIST_HEAD_GUIDE:

            for each in hadEnv.AUTO_RIG_LIST_HEAD_GUIDE:
                locaShape = cmds.listRelatives(each, children=True, shapes=True)[0]
                hadEnv.AUTO_RIG_LIST_HEAD_JOINT.append(cmds.createNode('joint', name="Bs_"+ locaShape, skipSelect=True))
                cmds.matchTransform(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[-1], each, rotation=False, scale=False)  

            cmds.parent(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[2], hadEnv.AUTO_RIG_LIST_HEAD_JOINT[1])
            cmds.parent(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[1], hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0])

            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_HEAD_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDE = []
            hadEnv.AUTO_RIG_LIST_HEAD_GUIDELINE = []

            cmds.select(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            hadLib.setRotateOrient(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[-1],0,0,0)


        if hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
            
            for each in hadEnv.AUTO_RIG_LIST_CHEST_GUIDE:
                locaShape = cmds.listRelatives(each, children=True, shapes=True)[0]
                hadEnv.AUTO_RIG_LIST_CHEST_JOINT.append(cmds.createNode('joint', name="Bs_"+ locaShape, skipSelect=True))
                cmds.matchTransform(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[-1], each, rotation=False, scale=False)

            hadEnv.AUTO_RIG_LIST_CHEST_JOINT.append(cmds.createNode('joint', name="SpineB", skipSelect=True))
            cmds.delete(cmds.parentConstraint(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[2], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[-1]))
            hadEnv.AUTO_RIG_LIST_CHEST_JOINT.append(cmds.createNode('joint', name="SpineD", skipSelect=True))
            cmds.delete(cmds.parentConstraint(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[-1]))   

            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[6])
            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[6], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3])
            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[5])
            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[5], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[2])
            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[2], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0])
            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0])
            

            cmds.delete(cmds.listRelatives(hadEnv.AUTO_RIG_LIST_CHEST_GUIDE[0], parent=True)[0])
            for each in hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE:
                cmds.delete(each)
            hadEnv.AUTO_RIG_LIST_CHEST_GUIDE = []
            hadEnv.AUTO_RIG_LIST_CHEST_GUIDELINE = []

            cmds.select(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[2])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            hadLib.setRotateOrient(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4],0,0,0)        

        cmds.delete(hadEnv.GUIDE_LINE_GRP)


    def autoRigCheckMirror(self):

        if hadEnv.AUTO_RIG_LIST_ARM_JOINT:
            tempSele = cmds.mirrorJoint(hadEnv.AUTO_RIG_LIST_ARM_JOINT[0],mirrorBehavior=True,mirrorYZ=True, searchReplace= (hadEnv.DICT_MIRROR[0], hadEnv.DICT_MIRROR[6]))
            for each in tempSele:
                hadEnv.AUTO_RIG_LIST_ARM_JOINT.append(each)
        if hadEnv.AUTO_RIG_LIST_LEG_JOINT:
            tempSele = cmds.mirrorJoint(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0],mirrorBehavior=True,mirrorYZ=True, searchReplace= (hadEnv.DICT_MIRROR[0], hadEnv.DICT_MIRROR[6]))
            for each in tempSele:
                hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(each)
            tempSele = cmds.mirrorJoint(hadEnv.AUTO_RIG_LIST_LEG_JOINT[5],mirrorBehavior=True,mirrorYZ=True, searchReplace= (hadEnv.DICT_MIRROR[0], hadEnv.DICT_MIRROR[6]))
            for each in tempSele:
                hadEnv.AUTO_RIG_LIST_LEG_JOINT.append(each)
            cmds.select(hadEnv.AUTO_RIG_LIST_LEG_JOINT[22])
            cmds.select(hierarchy=True)
            cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")
    
    def autoRigCreateRigWithOutSide(self):

        def CTRL_GENERAL(self):
            
            self.CTRL_GENERAL = cmds.circle(normal=(0, 1, 0), center=(0, 0, 0), radius=7, name= "Ctrl_General", constructionHistory=False)[0]
            
            cmds.setAttr(self.CTRL_GENERAL + ".overrideEnabled", 1)
            cmds.setAttr(self.CTRL_GENERAL + ".overrideColor", 9)

            cmds.group( em=True, name="AutoRig_By_Mathieu" )
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
            cmds.parent("GlobalMove", "AutoRig_By_Mathieu")
            cmds.parent("Model", "AutoRig_By_Mathieu")
            cmds.parent("BlendShapes", "AutoRig_By_Mathieu")
            cmds.parent("Joints", "GlobalMove")
            cmds.parent("Iks", "GlobalMove")
            cmds.parent("ControlObjects", "GlobalMove")
            cmds.parent("ExtraNodes", "AutoRig_By_Mathieu")
            
            cmds.parent(self.CTRL_GENERAL, "AutoRig_By_Mathieu")
            
            cmds.connectAttr(self.CTRL_GENERAL + ".translate", "GlobalMove.translate")
            cmds.connectAttr(self.CTRL_GENERAL + ".rotate", "GlobalMove.rotate")
            
            cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleX")
            cmds.connectAttr("GlobalMove.scaleY", "GlobalMove.scaleZ")
            
            cmds.connectAttr(self.CTRL_GENERAL + ".scaleY", self.CTRL_GENERAL +".scaleZ")
            cmds.connectAttr(self.CTRL_GENERAL + ".scaleY", self.CTRL_GENERAL +".scaleX")
            
            cmds.connectAttr(self.CTRL_GENERAL + ".scaleX", "GlobalMove.scaleY")
            
            cmds.setAttr( self.CTRL_GENERAL +'.scaleX', lock=True , keyable = False , channelBox=False )
            cmds.setAttr( self.CTRL_GENERAL +'.scaleZ', lock=True , keyable = False , channelBox=False )  

            hadEnv.CTRL_GENERAL = self.CTRL_GENERAL

        CTRL_GENERAL(self)
        
        def rigHead(self):

            #Neck and Head controller

            hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0]
        
            self.ctrlNeck = cmds.circle(normal=(1, 0, 0), center=(0, 0, 0), radius=1.4, name= "Ctrl_" + hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0] , constructionHistory=False)[0]        
            ctrlHead = cmds.curve(name= "Ctrl_" + hadEnv.AUTO_RIG_LIST_HEAD_JOINT[1], d=3, p=[(0, -1, 0), (-0.5, -0.9, 0), (-1.3, -0.7, 0), (-2.5, 1.5, 0), (-1.7, 3.3, 0), (0, 3.3, 0), (1.7, 3.3, 0), (2.5, 1.5, 0), (1.3, -0.7, 0), (0.5, -0.9, 0), (0, -1, 0)] )

            hadLib.setRotate(ctrlHead, 0, 90, -90)
            hadLib.setScale(ctrlHead, 0.7, 0.7, 0.7)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            grpCtrlHead = cmds.group( em=True, name="Grp_"+ctrlHead  )
            cmds.parent(ctrlHead, grpCtrlHead)

            self.grpCtrlNeck = cmds.group( self.ctrlNeck, n= "Grp_"+self.ctrlNeck ) 

            cmds.matchTransform(self.grpCtrlNeck, hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0])
            cmds.matchTransform(grpCtrlHead, hadEnv.AUTO_RIG_LIST_HEAD_JOINT[1]) 
            
            cmds.parent(grpCtrlHead, self.ctrlNeck)
            
            range = [self.ctrlNeck, ctrlHead]           
            x=0
            for each in range:
                hadLib.freezeTranslate(each)
                hadLib.freezeScale(each)
                cmds.parentConstraint(each, hadEnv.AUTO_RIG_LIST_HEAD_JOINT[x])
                x = 1 
                cmds.setAttr(each + ".overrideEnabled", 1)
                cmds.setAttr(each + ".overrideColor", 17)

            #clean 

            cmds.parent(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0], 'Joints')
            cmds.parent(self.grpCtrlNeck, 'ControlObjects')

        def rigChest(self):

            #Create Root Ctrl
        
            ctrlRoot = cmds.curve(n= "Ctrl_" + hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0], d=1, p=[(2, 1, 2),(2,1,-2) ,(2, -1, -2) ,(2, -1, 2) ,(-2, -1, 2) ,(-2, 1, 2) ,(2, 1, 2) ,(2, -1, 2) ,(-2, -1, 2) ,(-2, -1, -2) ,(-2, 1, -2) ,(2, 1, -2) ,(2, -1, -2) ,(-2, -1, -2) ,(-2, 1, -2) ,(-2, 1, 2)], k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            grpCtrlRoot = cmds.group( em=True, name='Grp*'+ ctrlRoot )
            cmds.parent(ctrlRoot, grpCtrlRoot)
            cmds.matchTransform(grpCtrlRoot, hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0])
            hadLib.freezeScale(ctrlRoot)
            cmds.setAttr(ctrlRoot + ".overrideEnabled", 1)
            cmds.setAttr(ctrlRoot + ".overrideColor", 17)

            #Create Spine IK
               
            ikSpine = cmds.ikHandle( name = "Ik_Spine_IK", startJoint= hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0], endEffector= hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4] , solver='ikSplineSolver',parentCurve=False,simplifyCurve=False, createCurve= True)[0]
            crvSpine = cmds.rename('curve1', 'Crv_Spine_IK')
            
            jointSpineIklist = []
            jointSpineIklist.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0], parentOnly=True, name= "Spine_Start_IK")[0])
            hadLib.setRotateOrient(jointSpineIklist[-1], -90, 0, 90)
            jointSpineIklist.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3], parentOnly=True, name= "Spine_Mid_IK")[0])
            cmds.parent(jointSpineIklist[-1], world=True)
            jointSpineIklist.append(cmds.duplicate(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4], parentOnly=True, name= "Spine_End_IK")[0])
            cmds.parent(jointSpineIklist[-1], world=True)
            
            cmds.skinCluster(jointSpineIklist[0], jointSpineIklist[1], jointSpineIklist[2], crvSpine, tsb=True)

            hadEnv.JOINT_IK_CHEST = jointSpineIklist

            #Create Spine Ctrl IK

            ctrlSpineIK = []
            grpCtrlSpineIK = []
            for each in jointSpineIklist:
                ctrlSpineIK.append(cmds.curve(n= "Ctrl_" + each, d=1, p=[(0, 1.5, 1.5),(0,1.5,-1.5) ,(0, -1.5, -1.5) ,(0, -1.5, 1.5) ,(0, 1.5, 1.5)], k = [0,1,2,3,4]))
                grpCtrlSpineIK.append(cmds.group( ctrlSpineIK[-1], n= "Grp_"+ctrlSpineIK[-1] ))
                cmds.matchTransform(grpCtrlSpineIK[-1], each)
                cmds.parentConstraint(ctrlSpineIK[-1], each)
                hadLib.freezeScale(ctrlSpineIK[-1])
                cmds.setAttr(ctrlSpineIK[-1] + ".overrideEnabled", 1)
                cmds.setAttr(ctrlSpineIK[-1] + ".overrideColor", 20)

            cmds.connectAttr(ctrlSpineIK[-1]+".rotateX", ikSpine+".twist")

            jointSpineFKlist = [hadEnv.AUTO_RIG_LIST_CHEST_JOINT[2], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[5], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[3], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[6], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4]]

            ctrlSpineFK = []
            grpCtrlSpineFK = []
            for each in jointSpineFKlist:

                ctrlSpineFK.append(cmds.circle(normal=(1, 0, 0), center=(0, 0, 0), radius=1.4, name= "Ctrl_"+each, constructionHistory=False)[0])
                grpCtrlSpineFK.append(cmds.group( ctrlSpineFK[-1], n= "Grp_"+ctrlSpineFK[-1]))
                cmds.matchTransform(grpCtrlSpineFK[-1], each)
                hadLib.freezeTranslate(ctrlSpineFK[-1])
                hadLib.freezeScale(ctrlSpineFK[-1])
                cmds.setAttr(ctrlSpineFK[-1] + ".overrideEnabled", 1)
                cmds.setAttr(ctrlSpineFK[-1] + ".overrideColor", 22)
                
            #Parent Ctrl Spine
        
            cmds.parent(grpCtrlSpineFK[4], ctrlSpineFK[3])
            cmds.parent(grpCtrlSpineFK[3], ctrlSpineFK[2])
            cmds.parent(grpCtrlSpineFK[2], ctrlSpineFK[1])
            cmds.parent(grpCtrlSpineFK[1], ctrlSpineFK[0])
            cmds.parent(grpCtrlSpineFK[0], ctrlRoot)
            cmds.parent(grpCtrlSpineIK[0], ctrlRoot)
            cmds.parent(grpCtrlSpineIK[1], ctrlSpineFK[2])
            cmds.parent(grpCtrlSpineIK[2], ctrlSpineFK[4])

            #Create Hip Ctrl                

            ctrlHip = cmds.curve(name='Ctrl_Hip', degree=3, point=[	(0.5, 0.0, 0.0), (0.462, 0.0, 0.19), (0.35, 0.0, 0.35),(0.19, 0.0, 0.46), (0.0, 0.0, 0.5), (-0.19, 0.0, 0.46),(-0.35, 0.0, 0.35), (-0.46, 0.0, 0.19), (-0.5, 0.0, 0.0),(-0.46, 0.0, -0.19), (-0.35, 0.0, -0.35), (-0.19, 0.0, -0.46),(0.0, 0.0, -0.5), (0.19, 0.0, -0.46), (0.35, 0.0, -0.35),(0.46, 0.0, -0.19), (0.5, 0.0, 0.0), (0.46, -0.19, 0.0),(0.35, -0.35, 0.0), (0.19, -0.46, 0.0), (0.0, -0.5, 0.0), (-0.19, -0.46, 0.0), (-0.35, -0.35, 0.0), (-0.46, -0.19, 0.0), (-0.5, 0.0, 0.0), (-0.46, 0.19, 0.0), (-0.35, 0.35, 0.0), (-0.19, 0.46, 0.0), (0.0, 0.5, 0.0), (0.19, 0.46, 0.0), (0.35, 0.35, 0.0), (0.46, 0.19, 0.0), (0.5, 0.0, 0.0), (0.46, 0.0, 0.19), (0.35, 0.0, 0.35), (0.19, 0.0, 0.46), (0.0, 0.0, 0.5), (0.0, 0.24, 0.44), (0.0, 0.44, 0.24), (0.0, 0.5, 0.0), (0.0, 0.44, -0.24), (0.0, 0.24, -0.44), (0.0, 0.0, -0.5), (0.0, -0.24, -0.44), (0.0, -0.44, -0.24), (0.0, -0.5, 0.0), (0.0, -0.44, 0.24), (0.0, -0.24, 0.44), (0.0, 0.0, 0.5)] )
            hadLib.setScale(ctrlHip, 2, 2, 2)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            hadLib.freezeTranslate(ctrlHip)
            hadLib.freezeScale(ctrlHip)
            grpCtrlHip = cmds.group( ctrlHip, n= "Grp_"+ctrlHip ) 
            cmds.matchTransform(grpCtrlHip, ctrlRoot)
            cmds.setAttr(grpCtrlHip+'.translateX', 3.2)
            cmds.parent(grpCtrlHip, ctrlRoot)
            cmds.setAttr(grpCtrlHip+'.rotateY', 90) 
            cmds.orientConstraint( ctrlHip, hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1] )
            cmds.setAttr(ctrlHip + ".overrideEnabled", 1)
            cmds.setAttr(ctrlHip + ".overrideColor", 22)

            #Clean

            cmds.parent(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[0], 'Joints')
            for each in jointSpineIklist:
                cmds.parent(each, 'Joints')
                cmds.setAttr(each+'.visibility', 0)
            cmds.parent(ikSpine, 'Iks')
            cmds.parent(crvSpine, 'Xtra_toHide')
            cmds.parent(grpCtrlRoot, 'ControlObjects')

            hadEnv.JOINT_IK_CHEST = jointSpineIklist
            hadEnv.CTRL_IK_CHEST = ctrlSpineIK
        
        if hadEnv.AUTO_RIG_LIST_HEAD_JOINT:
            rigHead(self)
        if hadEnv.AUTO_RIG_LIST_CHEST_JOINT:
            rigChest(self)
            if hadEnv.AUTO_RIG_LIST_HEAD_JOINT:

                cmds.parent(hadEnv.AUTO_RIG_LIST_HEAD_JOINT[0], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4])
                cmds.parentConstraint(hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4], self.grpCtrlNeck, maintainOffset=True)

        x = 0
        for each in hadEnv.AUTO_RIG_LIST_CHEST_JOINT:
            print(x, '=', each)
            x +=1
        x = 0
        for each in hadEnv.AUTO_RIG_LIST_LEG_JOINT:
            print(x, '=', each)
            x +=1
        x = 0
        for each in hadEnv.AUTO_RIG_LIST_HEAD_JOINT:
            print(x, '=', each)
            x +=1
        x = 0
        for each in hadEnv.AUTO_RIG_LIST_ARM_JOINT:
            print(x, '=', each)
            x +=1
                

    def autoRigCreateRigWithSide(self, side):

        def rigLegs(side):

            if side == 6:
                step = hadEnv.DICT_MIRROR['stepLeg']
            else:
                step = 0

            #CreateIKFK

            self.jointsListLegIK = hadLib.createIKJoints(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0+step])           
            self.jointsListLegFK = hadLib.createFKJoints(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0+step])

            #Create IK handle

            tempIkAnkle = cmds.ikHandle(name='Ik_Legs'+ hadEnv.DICT_MIRROR[side], startJoint=self.jointsListLegIK[0], endEffector=self.jointsListLegIK[2])[0]
            tempIkFoot = cmds.ikHandle(name='Ik_Foot'+ hadEnv.DICT_MIRROR[side], startJoint=self.jointsListLegIK[2], endEffector=self.jointsListLegIK[3])[0]
            tempIkToe = cmds.ikHandle(name='Ik_Toe'+ hadEnv.DICT_MIRROR[side], startJoint=self.jointsListLegIK[3], endEffector=self.jointsListLegIK[4])[0]

            cmds.parent(tempIkAnkle, hadEnv.AUTO_RIG_LIST_LEG_JOINT[13+step])
            cmds.parent(tempIkFoot, hadEnv.AUTO_RIG_LIST_LEG_JOINT[9+step])
            cmds.parent(tempIkToe, hadEnv.AUTO_RIG_LIST_LEG_JOINT[11+step])

            #Create pole vector for legs

            ctrlPLLeg = hadLib.createPoleVector(self.jointsListLegIK[0], self.jointsListLegIK[1], self.jointsListLegIK[2], 'locPoleVectorLeg', tempIkAnkle, side)

            #Create IK Ctrl for legs
        
            ctrlLegIk = cmds.curve(name="Ctrl_Leg" + hadEnv.DICT_MIRROR[side] , d=1, p=[(0.5, 0, 2.5),(0.5, 1 ,-0.5) ,(0.5, -1, -0.5) ,(0.5, -1, 2.5) ,(-0.5, -1, 2.5) ,(-0.5, 0, 2.5) ,(0.5, 0, 2.5) ,(0.5, -1, 2.5) ,(-0.5, -1, 2.5) ,(-0.5, -1, -0.5) ,(-0.5, 1, -0.5) ,(0.5, 1, -0.5) ,(0.5, -1, -0.5) ,(-0.5, -1, -0.5) ,(-0.5, 1, -0.5) ,(-0.5, 0, 2.5)], k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            cmds.addAttr(shortName='HeelSwivel', longName='HeelSwivel', defaultValue=0, k=True)
            cmds.addAttr(shortName='HeelLift', longName='HeelLift', defaultValue=0, k=True)
            cmds.addAttr(shortName='ToeSwivel', longName='ToeSwivel', defaultValue=0, k=True)
            cmds.addAttr(shortName='ToeLift', longName='ToeLift', defaultValue=0, k=True)
            cmds.addAttr(shortName='BallSwivel', longName='BallSwivel', defaultValue=0, k=True)
            cmds.addAttr(shortName='Tilt', longName='Tilt', defaultValue=0, minValue= -60, maxValue= 60, k=True)
            cmds.addAttr(shortName='RollLimit', longName='RollLimit', defaultValue=30, k=True)
            cmds.addAttr(shortName='RollReset', longName='RollReset', defaultValue=60, k=True)
            cmds.addAttr(shortName='Roll', longName='Roll', defaultValue=0, minValue=0, k=True)
            cmds.addAttr(shortName='ToeTap', longName='ToeTap', defaultValue=0, k=True)
            cmds.setAttr(ctrlLegIk + ".overrideEnabled", 1)
            cmds.setAttr(ctrlLegIk + ".overrideColor", 6+side) 
            grpctrlLegIk = cmds.group( em=True, name='Grp*'+ctrlLegIk, )
            cmds.parent(ctrlLegIk, grpctrlLegIk)
            cmds.matchTransform(grpctrlLegIk, hadEnv.AUTO_RIG_LIST_LEG_JOINT[2+step])
            hadLib.setRotate(grpctrlLegIk, 0, 0, 0)
            
            GrpFootRool = cmds.group(hadEnv.AUTO_RIG_LIST_LEG_JOINT[5+step], name='Grp_FootRoll*'+ hadEnv.AUTO_RIG_LIST_LEG_JOINT[5+step])
            
            cmds.parentConstraint( ctrlLegIk, GrpFootRool, maintainOffset=True )

            cmds.connectAttr(ctrlLegIk+'.HeelSwivel', hadEnv.AUTO_RIG_LIST_LEG_JOINT[7+step]+'.rotateY')
            cmds.connectAttr(ctrlLegIk+'.HeelLift', hadEnv.AUTO_RIG_LIST_LEG_JOINT[7+step]+'.rotateX')
            cmds.connectAttr(ctrlLegIk+'.ToeSwivel', hadEnv.AUTO_RIG_LIST_LEG_JOINT[8+step]+'.rotateY')
            cmds.connectAttr(ctrlLegIk+'.BallSwivel', hadEnv.AUTO_RIG_LIST_LEG_JOINT[9+step]+'.rotateY')
            cmds.connectAttr(ctrlLegIk+'.ToeTap', hadEnv.AUTO_RIG_LIST_LEG_JOINT[10+step]+'.rotateY')
                
            #Tilt : 
                
            condFoot = cmds.createNode('condition', name='conditionTilt_Foot' + hadEnv.DICT_MIRROR[side] , skipSelect=True)
            cmds.setAttr(condFoot+'.operation', 3)
            cmds.connectAttr(ctrlLegIk+'.Tilt', condFoot+'.firstTerm')
            cmds.connectAttr(ctrlLegIk+'.Tilt', condFoot+'.colorIfTrueR')
            cmds.connectAttr(ctrlLegIk+'.Tilt', condFoot+'.colorIfFalseG')
            cmds.setAttr(condFoot+'.colorIfFalseR', 0)
            cmds.setAttr(condFoot+'.colorIfTrueG', 0)
            cmds.connectAttr(condFoot+'.outColorR', hadEnv.AUTO_RIG_LIST_LEG_JOINT[5+step] + ".rotateZ")

            cmds.connectAttr(condFoot+'.outColorG', hadEnv.AUTO_RIG_LIST_LEG_JOINT[6+step] + ".rotateZ")
                
            #FootRoll
        
            setRangeFootRoll = cmds.createNode('setRange', name='SetRange_FootRoll'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.connectAttr(ctrlLegIk+'.Roll',setRangeFootRoll+'.valueX')
            cmds.connectAttr(ctrlLegIk+'.Roll',setRangeFootRoll+'.valueY')
            cmds.connectAttr(ctrlLegIk+'.RollLimit',setRangeFootRoll+'.oldMinX')
            cmds.connectAttr(ctrlLegIk+'.RollLimit',setRangeFootRoll+'.oldMaxY')
            cmds.connectAttr(ctrlLegIk+'.RollReset',setRangeFootRoll+'.oldMaxX')
            cmds.setAttr(setRangeFootRoll+'.maxX', 1)
            cmds.setAttr(setRangeFootRoll+'.maxY', 1)       
                
            revFootRoll = cmds.createNode('reverse', name='Reverse_FootRool'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            mulFootRollA = cmds.createNode('multiplyDivide', name='MultiplyDivide_FootRollA'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulFootRollA + '.operation', 1)
            mulFootRollB = cmds.createNode('multiplyDivide', name='MultiplyDivide_FootRollB'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulFootRollB + '.operation', 1)
            mulFootRollC = cmds.createNode('multiplyDivide', name='MultiplyDivide_FootRollC'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulFootRollC + '.operation', 1)
            addFootRollD = cmds.createNode('addDoubleLinear', name='AddDoubleLinear_FootRollD'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                
            cmds.connectAttr(setRangeFootRoll+'.outValueX', mulFootRollA+'.input1X')
            cmds.connectAttr(ctrlLegIk+'.Roll', mulFootRollA+'.input2X')
            
            cmds.connectAttr(setRangeFootRoll+'.outValueX', revFootRoll+'.inputX')
            
            cmds.connectAttr(revFootRoll+'.outputX', mulFootRollB+'.input1X')
            cmds.connectAttr(setRangeFootRoll+'.outValueY', mulFootRollB+'.input2X')
            
            cmds.connectAttr(mulFootRollB+'.outputX', mulFootRollC+'.input1X')
            cmds.connectAttr(ctrlLegIk+'.Roll', mulFootRollC+'.input2X')
            mulFootRollD = cmds.createNode('multiplyDivide', name='MultiplyDivide_FootRoolD'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulFootRollD + '.operation', 1)
            cmds.setAttr(mulFootRollD + '.input2X', -1)
            cmds.connectAttr(mulFootRollC+'.outputX', mulFootRollD+'.input1X')
            cmds.connectAttr(mulFootRollD+'.outputX', hadEnv.AUTO_RIG_LIST_LEG_JOINT[12+step]+'.rotateZ')           
            
            mulFootRollE = cmds.createNode('multiplyDivide', name='MultiplyDivide_FootRoolE'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulFootRollE + '.operation', 1)
            cmds.setAttr(mulFootRollE + '.input2X', -1)
            cmds.connectAttr(mulFootRollA+'.outputX', mulFootRollE+'.input1X')
            cmds.connectAttr(mulFootRollE+'.outputX', addFootRollD+'.input1')
            cmds.connectAttr(ctrlLegIk+'.ToeLift', addFootRollD+'.input2')
            cmds.connectAttr(addFootRollD+'.output', hadEnv.AUTO_RIG_LIST_LEG_JOINT[8+step]+'.rotateZ')  
            
            #hide Foot Roll
                
            cmds.setAttr(GrpFootRool + ".visibility", 0)

            #Lock Attribut IK Ctrl Legs 

            hadLib.freezeRotate(ctrlPLLeg)
            hadLib.freezeScale(ctrlPLLeg)
            hadLib.freezeScale(ctrlLegIk)

            #create FK ctrls
                
            self.grpCtrlLegFK = []
            ctrlLegFK = []
            for each in self.jointsListLegFK:
                tempCtrl = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), r=1, n='Ctrl*'+each+ hadEnv.DICT_MIRROR[side], constructionHistory=False)[0]
                ctrlLegFK.append(tempCtrl)
                tempGrp = cmds.group(tempCtrl, name='Grp*'+tempCtrl)
                self.grpCtrlLegFK.append(tempGrp)    
                cmds.matchTransform(tempGrp, each)
                cmds.orientConstraint(tempCtrl, each)
                hadLib.freezeTranslate(tempCtrl)
                hadLib.freezeScale(tempCtrl)
                cmds.setAttr( tempCtrl + ".overrideEnabled", 1)
                cmds.setAttr( tempCtrl + ".overrideColor", 6+side)                    
            
            cmds.parent( self.grpCtrlLegFK[1], ctrlLegFK[0] )
            cmds.parent( self.grpCtrlLegFK[2], ctrlLegFK[1] ) 
            cmds.parent( self.grpCtrlLegFK[3], ctrlLegFK[2] )
            cmds.parent( self.grpCtrlLegFK[4], ctrlLegFK[3] )

            #Create Ctrls for swicth IK FK

            ctrlLegIKFK = cmds.curve(name="Ctrl_Switch_IK/Fk_Leg"+ hadEnv.DICT_MIRROR[side], d=1, p=[(-0.5, 0, 2.5), (-0.5, 0, 2.5), (-0.5, 0, 2), (0.5, 0, 2), (0.5, 0, 2.5), (1, 0, 2.5), (1, 0, 3.5), (0.5, 0, 3.5), (0.5, 0, 4), (-0.5, 0, 4), (-0.5, 0, 3.5), (-1, 0, 3.5), (-1, 0, 2.5), (-0.5, 0, 2.5)]) 
            cmds.addAttr( shortName='SwitchIKFK', longName='SwitchIKFK', defaultValue=0, minValue=0, maxValue=1, k=True)
            grpCtrlLegIKFK = cmds.group( em=True, name='Grp*'+ ctrlLegIKFK )
            if side == 6:
                cmds.setAttr(ctrlLegIKFK + ".rotateX", 180)
                cmds.select(ctrlLegIKFK)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            else:
                pass
            cmds.parent(ctrlLegIKFK, grpCtrlLegIKFK)
            cmds.matchTransform(grpCtrlLegIKFK, hadEnv.AUTO_RIG_LIST_LEG_JOINT[1+step])
            cmds.parentConstraint( hadEnv.AUTO_RIG_LIST_LEG_JOINT[1+step], grpCtrlLegIKFK ) 
            
            hadLib.freezeTranslate(ctrlLegIKFK)  
            hadLib.freezeRotate(ctrlLegIKFK)
            hadLib.freezeScale(ctrlLegIKFK)         
            cmds.setAttr( ctrlLegIKFK + ".overrideEnabled", 1)
            cmds.setAttr( ctrlLegIKFK + ".overrideColor", 17)

            #Create PairBlend

            jointsListLegSK = [hadEnv.AUTO_RIG_LIST_LEG_JOINT[0+step], hadEnv.AUTO_RIG_LIST_LEG_JOINT[1+step], hadEnv.AUTO_RIG_LIST_LEG_JOINT[2+step], hadEnv.AUTO_RIG_LIST_LEG_JOINT[3+step], hadEnv.AUTO_RIG_LIST_LEG_JOINT[4+step]]
 
            for jointSK, jointIK, jointFK in zip(jointsListLegSK, self.jointsListLegIK , self.jointsListLegFK):    
        
                pairBlendLeg = cmds.createNode('pairBlend', name= jointSK + '_pairBlend'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(pairBlendLeg+'.rotInterpolation', 1)
                cmds.connectAttr(jointIK+'.translate', pairBlendLeg+'.inTranslate1')
                cmds.connectAttr(jointIK+'.rotate', pairBlendLeg+'.inRotate1')
                cmds.connectAttr(jointFK+'.translate', pairBlendLeg+'.inTranslate2')
                cmds.connectAttr(jointFK+'.rotate', pairBlendLeg+'.inRotate2')
                cmds.connectAttr(pairBlendLeg+'.outTranslate', jointSK+'.translate')
                cmds.connectAttr(pairBlendLeg+'.outRotate', jointSK+'.rotate')
                cmds.connectAttr(ctrlLegIKFK+'.SwitchIKFK', pairBlendLeg+'.weight')
    
            #hide joints FK and IK
            
            cmds.setAttr(self.jointsListLegIK[0]+'.visibility', 0)     
            cmds.setAttr(self.jointsListLegFK[0]+'.visibility', 0)

            #set visibility switch IK FK
            
            cmds.connectAttr(ctrlLegIKFK+'.SwitchIKFK', self.grpCtrlLegFK[0]+'.visibility')   
            reverseIK = cmds.createNode('reverse', name='reverseIK'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.connectAttr(ctrlLegIKFK+'.SwitchIKFK', reverseIK+'.inputX')
            cmds.connectAttr(reverseIK+'.outputX', grpctrlLegIk+'.visibility')
            grpCtrlPLLeg = cmds.listRelatives(ctrlPLLeg, parent=True)[0]
            cmds.connectAttr(reverseIK+'.outputX', grpCtrlPLLeg+'.visibility')
            cmds.setAttr(tempIkAnkle+'.visibility', False)
            cmds.setAttr(tempIkFoot+'.visibility', False)
            cmds.setAttr(tempIkToe+'.visibility', False)

            #Clean

            cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0+step], 'Joints')
            cmds.parent(self.jointsListLegIK[0], 'Joints')
            cmds.parent(self.jointsListLegFK[0], 'Joints')
            cmds.parent(grpCtrlPLLeg, 'ControlObjects')
            cmds.parent(grpctrlLegIk , 'ControlObjects')
            cmds.parent(grpCtrlLegIKFK , 'ControlObjects')
            cmds.parent(self.grpCtrlLegFK[0] , 'ControlObjects')
            cmds.parent(GrpFootRool , 'ControlObjects')

        def rigArms(side):

            if side == 6:
                step = hadEnv.DICT_MIRROR['stepArm']
            else:
                step = 0

            jointsListArmIK = hadLib.createIKJoints(hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step])           
            jointsListArmFK = hadLib.createFKJoints(hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step])

            cmds.delete(jointsListArmIK[3])
            cmds.delete(jointsListArmIK[6])

            cmds.delete(jointsListArmFK[3])
            cmds.delete(jointsListArmFK[6])

            jointsListArmIK = [jointsListArmIK[0], jointsListArmIK[1], jointsListArmIK[2]]
            jointsListArmFK = [jointsListArmFK[0], jointsListArmFK[1], jointsListArmFK[2]]

            #Create Clavicle Ctrl
        
            ctrlClavicle = cmds.circle(name=  "Ctrl_Clavicle" + hadEnv.DICT_MIRROR[side], normal=(0, 1, 0), center=(0, -1, 0), radius=0.7, degree=1, sections=1, constructionHistory=False)[0]         
            if side == 6:
                tempA = 180
                tempB = 180
            else:
                tempA = 1
                tempB = 1
            cmds.setAttr(ctrlClavicle+'.rotateY', -90)
            cmds.setAttr(ctrlClavicle+'.rotateX', tempB)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            self.grpCtrlClavicle = cmds.group( em=True, name='Grp*'+ctrlClavicle )
            cmds.parent(ctrlClavicle , self.grpCtrlClavicle)
            cmds.matchTransform(self.grpCtrlClavicle, hadEnv.AUTO_RIG_LIST_ARM_JOINT[0+step])
            cmds.setAttr(ctrlClavicle + ".overrideEnabled", 1)
            cmds.setAttr(ctrlClavicle + ".overrideColor", 6+side) 
            hadLib.freezeTranslate(ctrlClavicle)  
            hadLib.freezeScale(ctrlClavicle)      

            #Create Scapula Ctrl for Clavicle
        
            ctrlScapula = cmds.curve( name = "Ctrl_Scapula" + hadEnv.DICT_MIRROR[side], degree=3, point=[(0, -0.6, 0), (-0.2, -0.6, 0), (-0.5, -0.6, 0), (-0.2, 0, 1), (-0.5, 0.6, 0), (0, 0.8, 0), (0.5, 0.6, 0), (0.2, 0, 1), (0.5, -0.6, 0), (0.2, -0.6, 0), (0, -0.6, 0)] )
            cmds.setAttr(ctrlScapula+'.rotateX', tempA)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            grpCtrlScapula = cmds.group( em=True, name='Grp*'+ctrlScapula )
            cmds.parent(ctrlScapula , grpCtrlScapula)
            cmds.matchTransform(grpCtrlScapula, hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step]) 
            cmds.setAttr(ctrlScapula + ".overrideEnabled", 1)
            cmds.setAttr(ctrlScapula + ".overrideColor", 6+side) 
            hadLib.freezeRotate(ctrlScapula)  
            hadLib.freezeScale(ctrlScapula)  

            #Contraints Scapula
        
            cmds.parent(grpCtrlScapula, ctrlClavicle)           
            cmds.aimConstraint( ctrlScapula, hadEnv.AUTO_RIG_LIST_ARM_JOINT[0+step] , maintainOffset = True )

            #Create IK handle

            tempIkArm = cmds.ikHandle(name='Ik_Arms'+ hadEnv.DICT_MIRROR[side], startJoint=jointsListArmIK[0], endEffector=jointsListArmIK[2])[0]

            #Create pole vector for legs

            ctrlPLArm = hadLib.createPoleVector(jointsListArmIK[0], jointsListArmIK[1], jointsListArmIK[2], 'locPoleVectorArm', tempIkArm, side)

            hadLib.freezeRotate(ctrlPLArm)  
            hadLib.freezeScale(ctrlPLArm) 

            #Create Ctrl IK Arm  
        
            ctrlWristIK = cmds.curve(name = "Ctrl_Wrist" + hadEnv.DICT_MIRROR[side], degree=1, point=[(0, 1, 1),(0,1,-1) ,(0, -1, -1) ,(0, -1, 1) ,(0, 1, 1)], knot = [0,1,2,3,4])        
            cmds.addAttr( shortName='Stretch', longName='Stretch', defaultValue=0, minValue=0, maxValue=1 , keyable = True)
            cmds.addAttr( shortName='Squash', longName='Squash', defaultValue=0, minValue=0, maxValue=1 , keyable = True)
            grpCtrlWristIK = cmds.group( ctrlWristIK, name= "Grp_"+ctrlWristIK ) 
            cmds.setAttr( ctrlWristIK + ".overrideEnabled", 1)
            cmds.setAttr( ctrlWristIK + ".overrideColor", 6+side)         
            cmds.matchTransform(grpCtrlWristIK, jointsListArmIK[2])

            cmds.orientConstraint(ctrlWristIK, jointsListArmIK[2])
            cmds.pointConstraint(ctrlWristIK, tempIkArm)
            hadLib.freezeScale(ctrlWristIK) 

            #create FK ctrls
                
            grpCtrlArmFK = []
            ctrlArmFK = []
            for each in jointsListArmFK:
                tempCtrl = cmds.circle(nr=(1, 0, 0), c=(0, 0, 0), r=1, n='Ctrl*'+each+ hadEnv.DICT_MIRROR[side], constructionHistory=False)[0]
                ctrlArmFK.append(tempCtrl)
                tempGrp = cmds.group(tempCtrl, name='Grp*'+tempCtrl)
                grpCtrlArmFK.append(tempGrp)    
                cmds.matchTransform(tempGrp, each)
                cmds.orientConstraint(tempCtrl, each)
                hadLib.freezeTranslate(tempCtrl)
                hadLib.freezeScale(tempCtrl)
                cmds.setAttr( tempCtrl + ".overrideEnabled", 1)
                cmds.setAttr( tempCtrl + ".overrideColor", 6+side)                    
            
            cmds.parent( grpCtrlArmFK[1], ctrlArmFK[0] )
            cmds.parent( grpCtrlArmFK[2], ctrlArmFK[1] ) 

            #Create Ctrls for swicth IK FK
        
            ctrlLArmIKFK = cmds.curve(name="Ctrl_L_Switch_IK/Fk_Arm"+ hadEnv.DICT_MIRROR[side], d=1, p=[(-1, -0.5, 1), (-0.5, -0.5, 1), (-0.5, -1, 1), (0.5, -1, 1), (0.5, -0.5, 1), (1, -0.5, 1), (1, 0.5, 1), (0.5, 0.5, 1), (0.5, 1, 1), (-0.5, 1, 1), (-0.5, 0.5, 1), (-1, 0.5, 1), (-1, -0.5, 1), (-0.5, -0.5, 1)]) 
            cmds.addAttr( shortName='SwitchIKFK', longName='SwitchIKFK', defaultValue=0, minValue=0, maxValue=1, k=True)
            cmds.addAttr( shortName='ThumbCurl', longName='ThumbCurl', defaultValue=0, minValue=-20, maxValue=60, k=True)
            cmds.addAttr( shortName='IndexCurl', longName='IndexCurl', defaultValue=0, minValue=-20, maxValue=60, k=True)
            cmds.addAttr( shortName='MidCurl', longName='MidCurl', defaultValue=0, minValue=-20, maxValue=60, k=True)
            cmds.addAttr( shortName='RingCurl', longName='RingCurl', defaultValue=0, minValue=-20, maxValue=60, k=True)
            cmds.addAttr( shortName='PinkyCurl', longName='PinkyCurl', defaultValue=0, minValue=-20, maxValue=60, k=True)
            cmds.addAttr( shortName='Spread', longName='Spread', defaultValue=0, minValue=-30, maxValue=30, k=True)
            if side == 6:
                cmds.setAttr(ctrlLArmIKFK + ".rotateX", 180)
                cmds.select(ctrlLArmIKFK)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            else:
                pass
            GrpctrlLArmIKFK = cmds.group( em=True, name='Grp*'+ ctrlLArmIKFK )
            cmds.parent(ctrlLArmIKFK, GrpctrlLArmIKFK)
            cmds.matchTransform(GrpctrlLArmIKFK, hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step])
            cmds.parentConstraint( hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step], GrpctrlLArmIKFK ) 

            hadLib.freezeTranslate(ctrlLArmIKFK)  
            hadLib.freezeRotate(ctrlLArmIKFK)
            hadLib.freezeScale(ctrlLArmIKFK)         
            cmds.setAttr( ctrlLArmIKFK + ".overrideEnabled", 1)
            cmds.setAttr( ctrlLArmIKFK + ".overrideColor", 17)

            #Create PairBlend

            jointsListArmSK = [hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[2+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step]]

            for jointSK, jointIK, jointFK in zip(jointsListArmSK, jointsListArmIK , jointsListArmFK):    
        
                pairBlendArm = cmds.createNode('pairBlend', name= jointSK + '_pairBlend'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(pairBlendArm+'.rotInterpolation', 1)
                cmds.connectAttr(jointIK+'.translate', pairBlendArm+'.inTranslate1')
                cmds.connectAttr(jointIK+'.rotate', pairBlendArm+'.inRotate1')
                cmds.connectAttr(jointFK+'.translate', pairBlendArm+'.inTranslate2')
                cmds.connectAttr(jointFK+'.rotate', pairBlendArm+'.inRotate2')
                cmds.connectAttr(pairBlendArm+'.outTranslate', jointSK+'.translate')
                cmds.connectAttr(pairBlendArm+'.outRotate', jointSK+'.rotate')
                cmds.connectAttr(ctrlLArmIKFK+'.SwitchIKFK', pairBlendArm+'.weight')
    
            #hide joints FK and IK
            
            cmds.setAttr(jointsListArmIK[0]+'.visibility', 0)     
            cmds.setAttr(jointsListArmFK[0]+'.visibility', 0)

            #set visibility switch IK FK
            
            cmds.connectAttr(ctrlLArmIKFK+'.SwitchIKFK', grpCtrlArmFK[0]+'.visibility')   
            reverseIK = cmds.createNode('reverse', name='reverseIK'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.connectAttr(ctrlLArmIKFK+'.SwitchIKFK', reverseIK+'.inputX')
            cmds.connectAttr(reverseIK+'.outputX', grpCtrlWristIK+'.visibility')
            grpCtrlPLArm = cmds.listRelatives(ctrlPLArm, parent=True)[0]
            cmds.connectAttr(reverseIK+'.outputX', grpCtrlPLArm+'.visibility')
            cmds.setAttr(tempIkArm+'.visibility', False)

            #Parent FkCtrl Scapula
        
            cmds.parent(grpCtrlArmFK[0], grpCtrlScapula)

            #Fix Last Fingers orient : 

            range = [hadEnv.AUTO_RIG_LIST_ARM_JOINT[6+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[10+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[13+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[16+step], hadEnv.AUTO_RIG_LIST_ARM_JOINT[19+step]]
            
            for each in range:
                cmds.setAttr(each + ".jointOrientY", 10)

            #Create Ctrl for fingers                
                            
            grpFingers = []
            grpOffsetFingers = []
            ctrlFingers = []
            
            for each in hadEnv.AUTO_RIG_LIST_ARM_JOINT[4+step:20+step]:
                
                tempCtrlFinger = cmds.curve(name= "Ctrl" + each, d=1, p=[(0, 0, 0), (0, 0, -0.44), (0, 0, -0.9), (0, 0, -1.23), (-0.21, 0, -1.37), (-0.44, 0, -2), (0, 0, -2.2), (0.44, 0, -2), (0.21, 0, -1.37), (0, 0, -1.23), (0, 0.21, -1.37), (0, 0.44, -2), (0, 0, -2.2), (0, -0.44, -2), (0, -0.21, -1.37), (0, 0, -1.23)] )
                ctrlFingers.append(tempCtrlFinger)
                if side == 6:
                    pass
                else:
                    cmds.setAttr(tempCtrlFinger +'.rotateX', 180)
                hadLib.setScale(tempCtrlFinger, 0.5, 0.5, 0.5)
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                tempGrpCtrlFingerOff = cmds.group( em=True, name='Grp_OffSet*'+ each )
                grpOffsetFingers.append(tempGrpCtrlFingerOff)
                cmds.parent(tempCtrlFinger, tempGrpCtrlFingerOff)
                tempGrpCtrlFinger = cmds.group( em=True, name='Grp*'+ each )
                grpFingers.append(tempGrpCtrlFinger)
                cmds.parent(tempGrpCtrlFingerOff, tempGrpCtrlFinger)
                cmds.matchTransform(tempGrpCtrlFinger, each)
                hadLib.freezeTranslate(tempCtrlFinger)  
                hadLib.freezeScale(tempCtrlFinger)             
                cmds.setAttr( tempCtrlFinger + ".overrideEnabled", 1)
                cmds.setAttr( tempCtrlFinger + ".overrideColor", 6+side)  
                cmds.orientConstraint( tempCtrlFinger, each ) 
                
            cmds.parent(grpFingers[15], ctrlFingers[14])
            cmds.parent(grpFingers[14], ctrlFingers[13])
            cmds.parent(grpFingers[12], ctrlFingers[11])
            cmds.parent(grpFingers[11], ctrlFingers[10])
            cmds.parent(grpFingers[9], ctrlFingers[8])
            cmds.parent(grpFingers[8], ctrlFingers[7])
            cmds.parent(grpFingers[6], ctrlFingers[5])
            cmds.parent(grpFingers[5], ctrlFingers[4])
            cmds.parent(grpFingers[4], ctrlFingers[3])
            cmds.parent(grpFingers[7], ctrlFingers[3])
            cmds.parent(grpFingers[10], ctrlFingers[3])
            cmds.parent(grpFingers[13], ctrlFingers[3])
            cmds.parent(grpFingers[2], ctrlFingers[1])
            cmds.parent(grpFingers[1], ctrlFingers[0])
            cmds.parentConstraint(hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step], grpFingers[0], maintainOffset = True)
            cmds.parentConstraint(hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step], grpFingers[3], maintainOffset = True)

            #Fingers control attribute
        
            cmds.connectAttr(ctrlLArmIKFK+'.ThumbCurl', grpOffsetFingers[0]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.ThumbCurl', grpOffsetFingers[1]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.ThumbCurl', grpOffsetFingers[2]+'.rotateY')

            cmds.connectAttr(ctrlLArmIKFK+'.IndexCurl', grpOffsetFingers[4]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.IndexCurl', grpOffsetFingers[5]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.IndexCurl', grpOffsetFingers[6]+'.rotateY')
            
            cmds.connectAttr(ctrlLArmIKFK+'.MidCurl', grpOffsetFingers[7]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.MidCurl', grpOffsetFingers[8]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.MidCurl', grpOffsetFingers[9]+'.rotateY')
            
            cmds.connectAttr(ctrlLArmIKFK+'.RingCurl', grpOffsetFingers[10]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.RingCurl', grpOffsetFingers[11]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.RingCurl', grpOffsetFingers[12]+'.rotateY')
            
            cmds.connectAttr(ctrlLArmIKFK+'.PinkyCurl', grpOffsetFingers[13]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.PinkyCurl', grpOffsetFingers[14]+'.rotateY')
            cmds.connectAttr(ctrlLArmIKFK+'.PinkyCurl', grpOffsetFingers[15]+'.rotateY')
            
            cmds.connectAttr(ctrlLArmIKFK+'.Spread', grpOffsetFingers[0]+'.rotateZ')
            cmds.connectAttr(ctrlLArmIKFK+'.Spread', grpOffsetFingers[4]+'.rotateZ')
            mulSpreadFingersA = cmds.createNode('multiplyDivide', name='MultiplyDivide_SpreadFingersA'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulSpreadFingersA + '.operation', 1)
            cmds.setAttr(mulSpreadFingersA + '.input2X', -1)
            mulSpreadFingersB = cmds.createNode('multiplyDivide', name='MultiplyDivide_SpreadFingersB'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulSpreadFingersB + '.operation', 1)
            cmds.setAttr(mulSpreadFingersB + '.input2X', -0.5)
            cmds.connectAttr(ctrlLArmIKFK+'.Spread', mulSpreadFingersA+'.input1X')
            cmds.connectAttr(ctrlLArmIKFK+'.Spread', mulSpreadFingersB+'.input1X')
            cmds.connectAttr(mulSpreadFingersB+'.outputX', grpOffsetFingers[10]+'.rotateZ')
            cmds.connectAttr(mulSpreadFingersA+'.outputX', grpOffsetFingers[13]+'.rotateZ')

            #twist joints

            x, y, z = hadLib.getTranslate(hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step])
            lenWrist = x/4
            x, y, z = hadLib.getTranslate(hadEnv.AUTO_RIG_LIST_ARM_JOINT[2+step])
            lenElbow = x/4

            listTwistArm = []

            listTwistArm.append(cmds.createNode('joint', name='Bs_twist_UpperArm_Compensate'+ hadEnv.DICT_MIRROR[side], skipSelect=True))

            for each in ['A','B','C']:

                listTwistArm.append(cmds.createNode('joint', name='Bs_twist_UpperArm_'+ each+ hadEnv.DICT_MIRROR[side], skipSelect=True))
                listTwistArm.append(cmds.createNode('joint', name='Bs_twist_LowerArm_'+ each+ hadEnv.DICT_MIRROR[side], skipSelect=True))
            for each in listTwistArm:
                print(each)

            for each in [0,1]:

                cmds.parent(listTwistArm[5+each], listTwistArm[3+each])
                cmds.parent(listTwistArm[3+each], listTwistArm[1+each])
                cmds.parent(listTwistArm[1+each],hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+each+step])

                hadLib.setTranslate(listTwistArm[0+each+each], 0, 0, 0)
                hadLib.setRotateOrient(listTwistArm[0+each+each], 0, 0, 0)

                cmds.setAttr(listTwistArm[5]+'.translateX', lenElbow)
                cmds.setAttr(listTwistArm[3]+'.translateX', lenElbow)
                cmds.setAttr(listTwistArm[1]+'.translateX', lenElbow)
                
                cmds.setAttr(listTwistArm[6]+'.translateX', lenWrist)
                cmds.setAttr(listTwistArm[4]+'.translateX', lenWrist)
                cmds.setAttr(listTwistArm[2]+'.translateX', lenWrist)

            cmds.parent(listTwistArm[0],hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step])
            cmds.parent(listTwistArm[1],listTwistArm[0])
            hadLib.setTranslate(listTwistArm[0], 0, 0, 0)
            hadLib.setRotateOrient(listTwistArm[0], 0, 0, 0)
            hadLib.setTranslate(listTwistArm[1], lenElbow, 0, 0)
            hadLib.setRotateOrient(listTwistArm[1], 0, 0, 0)

            #TwistJoints Base

            tempListBaseArm = []

            for nameA, posA in zip(['UpperArm_twistEnd','UpperArm_twistBase','LowerArm_twistBase','LowerArm_twistEnd'],[1,2,2,3]):
                tempListBaseArm.append(cmds.createNode('joint', name='Bdrv_'+nameA+ hadEnv.DICT_MIRROR[side], skipSelect=True))
                cmds.matchTransform(tempListBaseArm[-1], hadEnv.AUTO_RIG_LIST_ARM_JOINT[posA+step])
                cmds.setAttr(tempListBaseArm[-1]+'.visibility', 0)

            cmds.parent(tempListBaseArm[0],tempListBaseArm[1])
            cmds.parent(tempListBaseArm[3],tempListBaseArm[2])

            for each in tempListBaseArm:
                x, y, z = hadLib.getRotate(each)
                hadLib.setRotateOrient(each, x, y, z)
                hadLib.setRotate(each, 0, 0, 0)

            for each in [tempListBaseArm[1],tempListBaseArm[2]]:
                cmds.select(each)
                cmds.select(hierarchy=True)
                cmds.joint(edit=True, zeroScaleOrient=True, orientJoint="xyz", secondaryAxisOrient="zdown")

            TempEndJoint = [tempListBaseArm[0], tempListBaseArm[3]]
            for each in TempEndJoint:
                for attr in [".jointOrientX", ".jointOrientY", ".jointOrientZ"]:
                    cmds.setAttr(each+attr, 0)

            tempIkUpperArm = cmds.ikHandle(name='Ik_UpperArm_twist'+ hadEnv.DICT_MIRROR[side], startJoint=tempListBaseArm[1], endEffector=tempListBaseArm[0])[0]
            tempIkLowerArm = cmds.ikHandle(name='Ik_LowerArm_twist'+ hadEnv.DICT_MIRROR[side], startJoint=tempListBaseArm[2], endEffector=tempListBaseArm[3])[0]

            cmds.parent(tempIkUpperArm, hadEnv.AUTO_RIG_LIST_ARM_JOINT[0+step])
            cmds.parent(tempIkLowerArm, hadEnv.AUTO_RIG_LIST_ARM_JOINT[3+step])

            #twistJoints rotation

            x=0
            for nameB, stepB, sideB in zip(['UpperArm', 'LowerArm'], [1,2], [4,4]):

                mulRotateArm = cmds.createNode('multiplyDivide', name='MultiplyDivide_Rotate'+nameB+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(mulRotateArm + '.operation', 2)
                cmds.setAttr(mulRotateArm + '.input2X', sideB )
                cmds.connectAttr(tempListBaseArm[stepB]+'.rotateX', mulRotateArm + '.input1X', force=True)
                cmds.connectAttr(mulRotateArm +'.outputX', listTwistArm[1+x]+'.rotateX', force=True)
                cmds.connectAttr(mulRotateArm +'.outputX', listTwistArm[3+x]+'.rotateX', force=True)
                cmds.connectAttr(mulRotateArm +'.outputX', listTwistArm[5+x]+'.rotateX', force=True)
                x+=1

            cmds.parent(tempListBaseArm[1],hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+step])
            cmds.parent(tempListBaseArm[2],hadEnv.AUTO_RIG_LIST_ARM_JOINT[2+step])

            mulCompensateArm = cmds.createNode('multiplyDivide', name='MultiplyDivide_CompensateArm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
            cmds.setAttr(mulCompensateArm + '.operation', 1)
            cmds.setAttr(mulCompensateArm + '.input2X', 1)
            cmds.connectAttr(hadEnv.AUTO_RIG_LIST_ARM_JOINT[1+stepB]+'.rotateX', mulCompensateArm+'.input1X', force=True)
            cmds.connectAttr(mulCompensateArm+'.outputX', listTwistArm[0]+'.rotateX', force=True)

            #Clean

            cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[0+step], 'Joints')
            cmds.parent(self.grpCtrlClavicle, 'ControlObjects')
            cmds.parent(tempIkArm, 'Iks')
            cmds.parent(grpCtrlPLArm, 'ControlObjects')
            cmds.parent(grpCtrlWristIK , 'ControlObjects')
            cmds.parent(GrpctrlLArmIKFK , 'ControlObjects')
            cmds.parent(grpFingers[3] , 'ControlObjects')
            cmds.parent(grpFingers[0] , 'ControlObjects')

            #Stretch

            if hadEnv.AUTO_RIG_STRETCH:

                locatorsArm = []
                locatorsArmShape = []
                distanceArm = []

                for each in jointsListArmIK:
                    tempLoca = cmds.spaceLocator(name= 'Loc_'+each)
                    cmds.delete(cmds.parentConstraint(each, tempLoca))
                    dist= cmds.createNode('distanceBetween', name = 'DistanceBetween'+each, skipSelect=True)
                    locatorsArm.append(tempLoca)
                    locatorsArmShape.append(cmds.listRelatives(locatorsArm[-1], shapes=True)[0])
                    distanceArm.append(dist)

                cmds.pointConstraint(jointsListArmIK[0], locatorsArm[0])
                cmds.pointConstraint(jointsListArmIK[1], locatorsArm[1])
                cmds.parent( locatorsArm[2], ctrlWristIK)

                listA = [locatorsArmShape[1], locatorsArmShape[1], locatorsArmShape[0]]
                listB = [locatorsArmShape[2], locatorsArmShape[0], locatorsArmShape[2]]
                x = 0
                for locA, locB in zip(listA, listB):
                    cmds.connectAttr(locA+'.worldPosition[0]', distanceArm[x]+'.point1')  #distanceBetween Shouler/wrist
                    cmds.connectAttr(locB+'.worldPosition[0]', distanceArm[x]+'.point2')
                    x += 1

                distanceShoulElb = cmds.getAttr(distanceArm[0]+'.distance')
                distanceElbWri = cmds.getAttr(distanceArm[1]+'.distance')
                distanceMax = distanceShoulElb + distanceElbWri
                cmds.delete(distanceArm[0])
                cmds.delete(distanceArm[1])

                mulScaleFactorArm = cmds.createNode('multiplyDivide', name= 'ScaleFactor_Arm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(mulScaleFactorArm + '.operation', 1)
                cmds.connectAttr(hadEnv.CTRL_GENERAL+'.scaleY', mulScaleFactorArm+'.input1X')
                cmds.setAttr(mulScaleFactorArm + '.input2X', distanceMax)

                mulStretchFactorArm = cmds.createNode('multiplyDivide', name= 'StretchFactor_Arm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(mulStretchFactorArm + '.operation', 2)
                cmds.connectAttr(mulScaleFactorArm+'.outputX', mulStretchFactorArm+'.input2X')
                cmds.connectAttr(distanceArm[2]+'.distance', mulStretchFactorArm+'.input1X')

                conditionArm= cmds.createNode('condition',name= 'ConditionStretch_Arm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(conditionArm+'.operation', 2)
                cmds.connectAttr(mulScaleFactorArm+'.outputX', conditionArm+'.secondTerm')
                cmds.connectAttr(distanceArm[2]+'.distance', conditionArm+'.firstTerm')

                setRangeArm= cmds.createNode('setRange', name= 'SetRangeStretch_Arm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(setRangeArm+'.minX', 1)
                cmds.setAttr(setRangeArm+'.oldMaxX', 1)

                cmds.connectAttr(mulStretchFactorArm+'.outputX', setRangeArm+'.maxX')
                cmds.connectAttr(ctrlWristIK+'.Stretch', setRangeArm+'.valueX')

                cmds.connectAttr(setRangeArm+'.outValueX', conditionArm+'.colorIfTrueR')

                #Squash

                squashFactorArm = cmds.createNode('multiplyDivide', name= 'SquashFactor'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(squashFactorArm+'.operation', 3)
                cmds.connectAttr(conditionArm+'.outColorR', squashFactorArm+'.input1X')


                multiSquashArm = cmds.createNode('multiplyDivide', name= 'SquashMultiply'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                cmds.setAttr(multiSquashArm + '.operation', 1)
                cmds.setAttr(multiSquashArm+'.input2X', -1)
                
                cmds.connectAttr(ctrlWristIK+'.Squash', multiSquashArm+'.input1X')

                cmds.connectAttr(multiSquashArm+'.outputX', squashFactorArm+'.input2X')

                for each in [jointsListArmIK[0],jointsListArmIK[1],listTwistArm[0],listTwistArm[1],listTwistArm[2],listTwistArm[3],listTwistArm[4],listTwistArm[5],listTwistArm[6]]:
                    cmds.connectAttr(conditionArm+'.outColorR', each+'.scaleX')
                    cmds.connectAttr(squashFactorArm+'.outputX', each+'.scaleY')
                    cmds.connectAttr(squashFactorArm+'.outputX', each+'.scaleZ')

                x = 0
                for jointSK, jointIK, jointFK in zip(jointsListArmSK, jointsListArmIK , jointsListArmFK): 
                        blendColorArm= cmds.createNode('blendColors', name='blendColorsArm'+ hadEnv.DICT_MIRROR[side], skipSelect=True)
                        cmds.connectAttr(jointFK+'.scale', blendColorArm+'.color1')
                        cmds.connectAttr(jointIK+'.scale', blendColorArm+'.color2')
                        cmds.connectAttr(ctrlLArmIKFK+'.SwitchIKFK', blendColorArm+'.blender')
                        cmds.connectAttr(blendColorArm+'.output', jointSK+'.scale')

                #clean

                for each in locatorsArm:
                    cmds.parent(each,"Xtra_toHide")



        if hadEnv.AUTO_RIG_LIST_LEG_JOINT:
            rigLegs(side)
            if hadEnv.AUTO_RIG_LIST_CHEST_JOINT:
                if side == 6:
                    step = hadEnv.DICT_MIRROR['stepLeg']
                else:
                    step = 0
                cmds.parent(hadEnv.AUTO_RIG_LIST_LEG_JOINT[0+step], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1])
                cmds.parent(self.jointsListLegIK[0], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1])
                cmds.parent(self.jointsListLegFK[0], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1])
                cmds.parent(self.grpCtrlLegFK[0] , hadEnv.AUTO_RIG_LIST_CHEST_JOINT[1])


        if hadEnv.AUTO_RIG_LIST_ARM_JOINT:
            rigArms(side)
            if hadEnv.AUTO_RIG_LIST_CHEST_JOINT:
                if side == 6:
                    step = hadEnv.DICT_MIRROR['stepArm']
                else:
                    step = 0
                cmds.parent(hadEnv.AUTO_RIG_LIST_ARM_JOINT[0+step], hadEnv.AUTO_RIG_LIST_CHEST_JOINT[4])
                cmds.orientConstraint(hadEnv.JOINT_IK_CHEST[-1], self.grpCtrlClavicle, maintainOffset=True)
                cmds.parent(self.grpCtrlClavicle, hadEnv.CTRL_IK_CHEST[-1])

