# Use PySide2 or PyQt5.
try: from PySide2 import QtCore, QtGui, QtWidgets
except: from PyQt5 import QtCore, QtGui, QtWidgets
finally: __qt_binding__ = QtCore.__name__.partition('.')[0]

### TO DELETE

#from Qt import QtWidgets
#from Qt import QtCore
#from Qt import QtGui
#from Qt import QtCompat

###


if __qt_binding__ == 'PySide2':
    Signal = QtCore.Signal
    Slot = QtCore.Slot
    Property = QtCore.Property
else:
    Signal = QtCore.pyqtSignal
    Slot = QtCore.pyqtSlot
    Property = QtCore.pyqtProperty

import hades.hadEnv as hadEnv
import hades.hadCore as hadCore
import sys
import os
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
from maya.OpenMayaUI import MQtUtil

'''
#In maya

import sys

path = r'M:\Code'

sys.path.append(path)

for k in sys.modules.keys():        #Delete in publish
    if 'hades' in k:
        del sys.modules[k]

import hades

from hades import hadUi
from hades import hadEnv
import os

hadEnv.PATH = hades.__file__.rpartition(os.sep)[0]

ui = hadUi.Hades()
ui.show()



'''

def maya_main_window():
    return wrapInstance(int(MQtUtil.mainWindow()), QtWidgets.QWidget)

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, text='', parent=None):
        super(MyLineEdit, self).__init__(text, parent)

class MyUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyUi, self).__init__(maya_main_window()) 
        self.setWindowTitle('Hades_'+hadEnv.VERSION)
        self.resize(400, 400)
        self.setMinimumSize(300,300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        #file = QtCore.QFile(hadEnv.PATH + '{0}hades{0}Combinear.qss'.format(os.sep))
        file = QtCore.QFile(os.path.join(hadEnv.PATH,'Combinear.qss'))
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(file)
        self.setStyleSheet(stream.readAll())

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        print("TODO: Create my widgets")

    def create_layouts(self):
        print("TODO: Create my layouts")

    def create_connections(self):
        print("TODO: Create my connections")

    def closeEvent(self,event):
        hadCore.endEventSelection()
        super(MyUi, self).closeEvent(event)

class Hades(MyUi):
    def create_widgets(self):

        #master_tab : 

        self.title_l = QtWidgets.QLabel("By_Mathieu_Karadjia")
        self.title_l.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        self.autoRig_but = QtWidgets.QPushButton("AutoRig")
        self.autoRig_but.clicked.connect(self.clickAutoRig_But)
        self.autoRig_l = QtWidgets.QLabel("USELESS")
        
        self.cerberus_but = QtWidgets.QPushButton("AutoRig Cerberus")
        self.cerberus_but.clicked.connect(self.clickCerberus_But)
        self.cerberus_l = QtWidgets.QLabel("AutoRig with bricks")

        self.thanatos_but = QtWidgets.QPushButton("SkinTool Thanatos")
        self.thanatos_but.clicked.connect(self.clickThanatos_But)
        self.thanatos_l = QtWidgets.QLabel("[Coming soon]")

        self.chaos_but = QtWidgets.QPushButton("Tools Chaos")
        self.chaos_but.clicked.connect(self.clickChaos_But)
        self.chaos_l = QtWidgets.QLabel("[Coming soon]")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.toolMaya_but = QtWidgets.QPushButton("Tools for Maya")
        self.toolMaya_but.clicked.connect(self.clickToolMaya_But)
        self.toolMaya_l = QtWidgets.QLabel("Library of Maya tools")

        self.createCrv_but = QtWidgets.QPushButton("Create Ctrl")
        self.createCrv_but.clicked.connect(self.clickCreateCtrl_But)
        self.createCrv_l = QtWidgets.QLabel("Create differents types of Ctrl")

        self.toolZiva_but = QtWidgets.QPushButton("Tools for Ziva")
        self.toolZiva_but.clicked.connect(self.clickToolZiva_But)
        self.toolZiva_l = QtWidgets.QLabel("Tools and scripts for Ziva user")

        self.masterTab = QtWidgets.QWidget()
        self.autoRigTab = QtWidgets.QWidget()
        self.cerberusTab = QtWidgets.QWidget()
        self.cerberusConsTab = QtWidgets.QWidget()
        self.cerberusTreeTab = QtWidgets.QWidget()
        self.cerberusMuscleTab = QtWidgets.QWidget()
        self.thanatosTab = QtWidgets.QWidget()
        self.chaosTab = QtWidgets.QWidget()
        self.toolMayaTab = QtWidgets.QWidget()
        self.createCtrlTab = QtWidgets.QWidget()
        self.toolZivaTab = QtWidgets.QWidget()
        self.tabMaster = QtWidgets.QTabWidget()

        self.tabMaster.addTab(self.masterTab,'Master')

        #auto_rig_tab

        self.autoRig_feature_l = QtWidgets.QLabel("Features :")
        self.autoRig_arm_chk = QtWidgets.QCheckBox("Arm")
        self.autoRig_arm_chk.setChecked(True)
        self.autoRig_leg_chk = QtWidgets.QCheckBox("Leg")
        self.autoRig_leg_chk.setChecked(True)
        self.autoRig_chest_chk = QtWidgets.QCheckBox("Chest")
        self.autoRig_chest_chk.setChecked(True)
        self.autoRig_head_chk = QtWidgets.QCheckBox("Head")
        self.autoRig_head_chk.setChecked(True)
        self.autoRig_guide_l = QtWidgets.QLabel("Creation of guides")
        self.autoRig_guide_but = QtWidgets.QPushButton("Create Guide")
        self.autoRig_guide_but.clicked.connect(self.clickAutoRigGuide_But)
        self.autoRig_option_l = QtWidgets.QLabel("Option :")
        self.autoRig_stretch_chk = QtWidgets.QCheckBox("Stretch And Squash")
        self.autoRig_mirror_chk = QtWidgets.QCheckBox("Left and Right")
        self.autoRig_mirror_chk.setChecked(True)
        self.autoRig_createRig_l = QtWidgets.QLabel("Please place the guides then click on the 'Create Rig' button")
        self.autoRig_createRig_but = QtWidgets.QPushButton("Create Rig")
        self.autoRig_createRig_but.clicked.connect(self.clickAutoRigGenerator_But)
        
        #Cerberus_tab
        
        self.cerberus_title_l = QtWidgets.QLabel("Cerberus 1.0.3")
        
        self.cerberus_titleTemplate_l = QtWidgets.QLabel("Import Template")
        self.cerberus_titleTemplate_butBi = QtWidgets.QPushButton("Biped")
        self.cerberus_titleTemplate_butQa = QtWidgets.QPushButton("Quadruped")
        self.cerberus_titleTemplate_butWi = QtWidgets.QPushButton("Wing")
        self.cerberus_titleTemplate_butFa = QtWidgets.QPushButton("Facial")
        
        self.cerberus_titleBrick_l = QtWidgets.QLabel("Import Brick Preset")
        self.cerberus_presetBrick_CB = QtWidgets.QComboBox(self)
        self.cerberus_presetBrickSimple_menu = self.cerberus_presetBrick_CB.addItem("simple")
        self.cerberus_presetBrickSpine_menu = self.cerberus_presetBrick_CB.addItem("spine")
        self.cerberus_presetBrickArm_menu = self.cerberus_presetBrick_CB.addItem("arm")
        self.cerberus_presetBrickHand_menu = self.cerberus_presetBrick_CB.addItem("hand")
        self.cerberus_presetBrickFoot_menu = self.cerberus_presetBrick_CB.addItem("foot")
        self.cerberus_presetBrickLeg_menu = self.cerberus_presetBrick_CB.addItem("leg")
        self.cerberus_presetBrickEye_menu = self.cerberus_presetBrick_CB.addItem("eye")
        self.cerberus_presetBrickMouth_menu = self.cerberus_presetBrick_CB.addItem("mouth")
        self.cerberus_presetBrickQuadrupedLeg_menu = self.cerberus_presetBrick_CB.addItem("quadruped leg")
        self.cerberus_presetBrickMuscle_menu = self.cerberus_presetBrick_CB.addItem("muscle")
        self.cerberus_presetBrickCustom_menu = self.cerberus_presetBrick_CB.addItem("custom")
        
        self.cerberus_editName_lE = QtWidgets.QLineEdit()
        self.cerberus_editName_l = QtWidgets.QLabel("Name : ") 
        
        self.cerberus_editSide_l = QtWidgets.QLabel("Side")
        self.cerberus_editSide_rB1 = QtWidgets.QRadioButton("Left")
        self.cerberus_editSide_rB2 = QtWidgets.QRadioButton("Right")
        self.cerberus_editSide_rB3 = QtWidgets.QRadioButton("Center")
        self.cerberus_editSide_rB1.setChecked(True)
        
        self.cerberus_editMirror_l = QtWidgets.QLabel("Mirror")
        self.cerberus_editMirror_chk = QtWidgets.QCheckBox()
        self.cerberus_editMirror_chk.setChecked(False)
        
        self.cerberus_editLevel_l = QtWidgets.QLabel("Lvl")
        self.cerberus_editLevel_rB1 = QtWidgets.QRadioButton("Fk")
        self.cerberus_editLevel_rB2 = QtWidgets.QRadioButton("Ik")
        self.cerberus_editLevel_rB3 = QtWidgets.QRadioButton("Fk/Ik")
        self.cerberus_editLevel_rB4 = QtWidgets.QRadioButton("Both")
        self.cerberus_editLevel_rB1.setChecked(True)

        self.cerberus_parent_l = QtWidgets.QLabel("Parent : ")
        self.cerberus_parent_lE = QtWidgets.QLineEdit() 
        self.cerberus_parent_but = QtWidgets.QPushButton("<<<")
        
        self.cerberus_constraint_l = QtWidgets.QLabel("Constraint : ")
        self.cerberus_constraint_but = QtWidgets.QPushButton("Constraint settings")
        self.cerberus_constraint_but.clicked.connect(self.clickCerberusCons_But)
        
        self.cerberus_option_l = QtWidgets.QLabel("Option :")
        self.cerberus_optionTwist_chk = QtWidgets.QCheckBox("Twist")
        self.cerberus_optionStretch_chk = QtWidgets.QCheckBox("Stretch")
        self.cerberus_optionSquash_chk = QtWidgets.QCheckBox("Squash")
        
        self.cerberus_treeSet_l = QtWidgets.QLabel("Tree : ")
        self.cerberus_treeSet_but = QtWidgets.QPushButton("Tree settings")
        self.cerberus_treeSet_but.clicked.connect(self.clickCerberusTree_But)

        self.cerberus_muscle_l = QtWidgets.QLabel("Muscle preset : ")
        self.cerberus_muscle_CB = QtWidgets.QComboBox(self)
        self.cerberus_muscleBiceps_menu = self.cerberus_muscle_CB.addItem("biceps")
        self.cerberus_muscleTriceps_menu = self.cerberus_muscle_CB.addItem("triceps")
        self.cerberus_musclePectoral_menu = self.cerberus_muscle_CB.addItem("pectoral")
        self.cerberus_muscleScapula_menu = self.cerberus_muscle_CB.addItem("scapula")
        self.cerberus_muscleTrapesius_menu = self.cerberus_muscle_CB.addItem("trapesius")
        self.cerberus_muscle_but = QtWidgets.QPushButton("Muscle settings")
        self.cerberus_muscle_but.clicked.connect(self.clickCerberusMuscle_But)

        self.cerberus_CreateBrick_but = QtWidgets.QPushButton("Create")
        self.cerberus_titleTree_l = QtWidgets.QLabel("Cerberus Editor")
        self.cerberus_refreshTree_l = QtWidgets.QPushButton("Refresh")
        
        self.cerberus_tree = QtWidgets.QTreeWidget()
        self.cerberus_tree.setColumnCount(2)
        self.cerberus_treeEdit_but = QtWidgets.QToolButton()
        
        self.cerberus_tree.setHeaderLabels(["Bricks :", ""])

        items = ["Item 1", "Item 2", "Item 3"]
        for item in items:
            tree_item = QtWidgets.QTreeWidgetItem(self.cerberus_tree)
            tree_item.setText(0, item)

            # Ajouter un bouton dans la seconde colonne
            button = QtWidgets.QPushButton("Edit")
            self.cerberus_tree.setItemWidget(tree_item, 1, button)
        
        self.cerberus_tree.setColumnWidth(0, 275)
        self.cerberus_Build_but = QtWidgets.QPushButton("Build")
        self.cerberus_BuildToggle_chk = QtWidgets.QCheckBox("Toggle Bricks")

        #thanatos_tab

        self.thanatos_shrink_but = QtWidgets.QPushButton("Shrink")
        self.thanatos_shrink_but.clicked.connect(self.clickthanatosShrink_But)
        self.thanatos_grow_but = QtWidgets.QPushButton("Grow")
        self.thanatos_grow_but.clicked.connect(self.clickthanatosGrow_But)
        self.thanatos_ring_but = QtWidgets.QPushButton("Ring")
        self.thanatos_ring_but.clicked.connect(self.clickthanatosRing_But)
        self.thanatos_loop_but = QtWidgets.QPushButton("Loop")
        self.thanatos_loop_but.clicked.connect(self.clickthanatosLoop_But)
        self.thanatos_0_but = QtWidgets.QPushButton("0")
        self.thanatos_0_but.clicked.connect(self.clickthanatos0_But)
        self.thanatos_01_but = QtWidgets.QPushButton(".1")
        self.thanatos_01_but.clicked.connect(self.clickthanatos01_But)
        self.thanatos_025_but = QtWidgets.QPushButton(".25")
        self.thanatos_025_but.clicked.connect(self.clickthanatos025_But)
        self.thanatos_05_but = QtWidgets.QPushButton(".5")
        self.thanatos_05_but.clicked.connect(self.clickthanatos05_But)
        self.thanatos_075_but = QtWidgets.QPushButton(".75")
        self.thanatos_075_but.clicked.connect(self.clickthanatos075_But)
        self.thanatos_09_but = QtWidgets.QPushButton(".9")
        self.thanatos_09_but.clicked.connect(self.clickthanatos09_But)
        self.thanatos_1_but = QtWidgets.QPushButton("1")
        self.thanatos_1_but.clicked.connect(self.clickthanatos1_But)
        self.thanatos_setWeight_but = QtWidgets.QPushButton("Set Weight")
        self.thanatos_setWeight_but.clicked.connect(self.clickthanatosSetWeight_But)
        self.thanatos_setWeight_sb = QtWidgets.QDoubleSpinBox()
        self.thanatos_setWeight_sb.setValue(0.5)
        self.thanatos_setWeight_sb.setMinimum(0)
        self.thanatos_setWeight_sb.setMaximum(1)
        self.thanatos_setWeight_sb.setSingleStep(0.05)
        self.thanatos_setWeightAdd_but = QtWidgets.QPushButton("+")
        self.thanatos_setWeight_but.clicked.connect(self.clickthanatosSetWeightAdd_But)
        self.thanatos_setWeightSub_but = QtWidgets.QPushButton("-")
        self.thanatos_setWeightSub_but.clicked.connect(self.clickthanatosSetWeightSub_But)
        self.thanatos_scaleWeight_but = QtWidgets.QPushButton("Scale Weight")
        self.thanatos_scaleWeight_but.clicked.connect(self.clickthanatosScaleWeight_But)
        self.thanatos_scaleWeight_sb = QtWidgets.QDoubleSpinBox()
        self.thanatos_scaleWeight_sb.setValue(0.95)
        self.thanatos_scaleWeight_sb.setMinimum(0.001)
        self.thanatos_scaleWeight_sb.setMaximum(5)
        self.thanatos_scaleWeight_sb.setSingleStep(0.05)
        self.thanatos_scaleWeightAdd_but = QtWidgets.QPushButton("+")
        self.thanatos_scaleWeightAdd_but.clicked.connect(self.clickthanatosScaleWeightAdd_But)
        self.thanatos_scaleWeightSub_but = QtWidgets.QPushButton("-")
        self.thanatos_scaleWeightSub_but.clicked.connect(self.clickthanatosScaleWeightSub_But)
        self.thanatos_copy_but = QtWidgets.QPushButton("Copy")
        self.thanatos_copy_but.clicked.connect(self.clickthanatosCopy_But)
        self.thanatos_paste_but = QtWidgets.QPushButton("Paste")
        self.thanatos_paste_but.clicked.connect(self.clickthanatosPaste_But)
        self.thanatos_pastePos_but = QtWidgets.QPushButton("Paste-Pos")
        self.thanatos_pastePos_but.clicked.connect(self.clickthanatosPastePos_But)
        self.thanatos_blend_but = QtWidgets.QPushButton("Blend")
        self.thanatos_blend_but.clicked.connect(self.clickthanatosBlend_But)
        self.thanatos_pastePosTol_l = QtWidgets.QLabel('Paste-Pos Tolerance')
        self.thanatos_pastePosTol_sb = QtWidgets.QDoubleSpinBox()
        self.thanatos_pastePosTol_sb.setValue(0.1)
        self.thanatos_pastePosTol_sb.setMinimum(0)
        self.thanatos_pastePosTol_sb.setMaximum(10)
        self.thanatos_pastePosTol_sb.setSingleStep(0.1)
        hadEnv.LABEL_VERTICE_MEMORY = self.thanatos_verCopyBuffer_l = QtWidgets.QLabel("0 Vertice In Copy Buffer")
        hadEnv.LABEL_VERTICE_SELECTED = self.thanatos_verSelected_l = QtWidgets.QLabel("0 Vertice Selected")
        hadEnv.TREE_SKIN_VALUES = self.thanatos_tree = QtWidgets.QTreeWidget()
        self.thanatos_tree.setColumnCount(2)
        self.thanatos_tree.setHeaderLabels(["Vertice","Value", "Joints"])
        self.thanatos_tree.itemSelectionChanged.connect(hadCore.selectionJoint)
        
        #chaos_tab
        
        
        
        
        
        
        
        

        #tools_for_Maya

        self.toolMayaH_but = QtWidgets.QPushButton("DeleteHistory")
        self.toolMayaH_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','history.png')))
        self.toolMayaH_but.clicked.connect(self.clickDeleteHistory_But)
        self.toolMayaT_but = QtWidgets.QPushButton("FreezeTransform")
        self.toolMayaT_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','freezeTransform.png')))
        self.toolMayaT_but.clicked.connect(self.clickFreezeTransform_But) 
        self.toolMayaC_but = QtWidgets.QPushButton("CenterPivot")
        self.toolMayaC_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','centerPivot.png')))
        self.toolMayaC_but.clicked.connect(self.clickCenterPivot_But) 
        self.toolMayaCreJnt_but = QtWidgets.QPushButton("Create Joints")
        self.toolMayaCreJnt_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','skeleton.png')))
        self.toolMayaCreJnt_but.setStyleSheet("background-color: Purple")
        self.toolMayaCreJnt_but.clicked.connect(self.clickCreateJoints_But) 
        self.toolMayaJntSz_but = QtWidgets.QPushButton("Joint Size")
        self.toolMayaJntSz_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','jointSize.png')))
        self.toolMayaJntSz_but.setStyleSheet("background-color: #E0B93D")
        self.toolMayaJntSz_but.clicked.connect(self.clickJointSize_But) 
        self.toolMayaLRA_but = QtWidgets.QPushButton("Local Rotation Axis")
        self.toolMayaLRA_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','lRA.png')))
        self.toolMayaLRA_but.setStyleSheet("background-color: #E0B93D")
        self.toolMayaLRA_but.clicked.connect(self.clickLocalRotationAxis_But) 
        self.toolMayaChaGrp_but = QtWidgets.QPushButton("Character Group")
        self.toolMayaChaGrp_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','charNode.png')))
        self.toolMayaChaGrp_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaChaGrp_but.clicked.connect(self.clickCharacterGroup_But) 
        self.toolMayaMirJnt_but = QtWidgets.QPushButton("Mirror joints")
        self.toolMayaMirJnt_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','mirrorJoint.png')))
        self.toolMayaMirJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaMirJnt_but.clicked.connect(self.clickMirrorJoints_But) 
        self.toolMayaOriJnt_but = QtWidgets.QPushButton("Orient Joints")
        self.toolMayaOriJnt_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','orientJoint.png')))
        self.toolMayaOriJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaOriJnt_but.clicked.connect(self.clickOrientJoints_But) 
        self.toolMayaReOriJnt_but = QtWidgets.QPushButton("ReOrient Last Joint")
        self.toolMayaReOriJnt_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','reOrientLastJoint.png')))
        self.toolMayaReOriJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaReOriJnt_but.clicked.connect(self.clickReOrientLastJoint_But) 
        self.toolMayaMirCrv_but = QtWidgets.QPushButton("Mirror Curves")
        self.toolMayaMirCrv_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','mirrorCrv.png')))
        self.toolMayaMirCrv_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaMirCrv_but.clicked.connect(self.clickMirrorCurves_But) 
        self.toolMayaParCrv_but = QtWidgets.QPushButton("Parent Curves")
        self.toolMayaParCrv_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','parentShape.png')))
        self.toolMayaParCrv_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaParCrv_but.clicked.connect(self.clickParentCurves_But) 
        self.toolMayaConEdi_but = QtWidgets.QPushButton("Connection Editor")
        self.toolMayaConEdi_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','connectionEditor.png')))
        self.toolMayaConEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaConEdi_but.clicked.connect(self.clickConnectionEditor_But) 
        self.toolMayaShaEdi_but = QtWidgets.QPushButton("Shape Editor")
        self.toolMayaShaEdi_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','shapeEditor.png')))
        self.toolMayaShaEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaShaEdi_but.clicked.connect(self.clickShapeEditor_But) 
        self.toolMayaDrivK_but = QtWidgets.QPushButton("DrivenKey")
        self.toolMayaDrivK_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','drivenKey.png')))
        self.toolMayaDrivK_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaDrivK_but.clicked.connect(self.clickDrivenKey_But) 
        self.toolMayaLoca_but = QtWidgets.QPushButton("Create Locator")
        self.toolMayaLoca_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','locatorCreate.png')))
        self.toolMayaLoca_but.setStyleSheet("background-color: #55A35A")
        self.toolMayaLoca_but.clicked.connect(self.clickCreateLocator_But) 
        self.toolMayaNodEdi_but = QtWidgets.QPushButton("Node Editor")
        self.toolMayaNodEdi_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','nodeEditor.png')))
        self.toolMayaNodEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaNodEdi_but.clicked.connect(self.clickNodeEditor_But) 
        self.toolMayaCopEdi_but = QtWidgets.QPushButton("Component Editor")
        self.toolMayaCopEdi_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','componentEditor.png')))
        self.toolMayaCopEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaCopEdi_but.clicked.connect(self.clickComponentEditor_But) 
        self.toolMayaYellow_but = QtWidgets.QPushButton("Color Yellow")
        self.toolMayaYellow_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaYellow_but.setStyleSheet("background-color: #E0B93D")
        self.toolMayaYellow_but.clicked.connect(self.clickColorYellow_But) 
        self.toolMayaRed_but = QtWidgets.QPushButton("Color Red")
        self.toolMayaRed_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaRed_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaRed_but.clicked.connect(self.clickColorRed_But) 
        self.toolMayaBlue_but = QtWidgets.QPushButton("Color Blue")
        self.toolMayaBlue_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaBlue_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaBlue_but.clicked.connect(self.clickColorBlue_But) 
        self.toolMayaPink_but = QtWidgets.QPushButton("Color Pink")
        self.toolMayaPink_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaPink_but.setStyleSheet("background-color: #D48EAB")
        self.toolMayaPink_but.clicked.connect(self.clickColorPink_But) 
        self.toolMayaGreen_but = QtWidgets.QPushButton("Color Green")
        self.toolMayaGreen_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaGreen_but.setStyleSheet("background-color: #55A35A")
        self.toolMayaGreen_but.clicked.connect(self.clickColorGreen_But) 
        self.toolMayaPurple_but = QtWidgets.QPushButton("Color Purple")
        self.toolMayaPurple_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','color.png')))
        self.toolMayaPurple_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaPurple_but.clicked.connect(self.clickColorPurple_But) 

        #tools_for_Ziva

        self.toolZivaFirst_l = QtWidgets.QLabel("Simulation Component :")

        self.toolZivaPanel_menu = QtWidgets.QMenu(self)
        self.toolZivaPanel_open = self.toolZivaPanel_menu.addAction("Open")
        self.toolZivaPanel_open.triggered.connect(self.clickToolZivaPanelOpen)
        self.toolZivaPanel_add = self.toolZivaPanel_menu.addAction("Add Cache")
        self.toolZivaPanel_add.triggered.connect(self.clickToolZivaPanelAddCache)
        self.toolZivaPanel_del = self.toolZivaPanel_menu.addAction("Delete Cache")
        self.toolZivaPanel_del.triggered.connect(self.clickToolZivaPanelDeleteCache)
        self.toolZivaPanel_but = QtWidgets.QPushButton("Scene Panel")
        self.toolZivaPanel_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','scenePanel.png')))
        self.toolZivaPanel_but.setMenu(self.toolZivaPanel_menu)
    

        self.toolZivaTissue_menu = QtWidgets.QMenu(self)
        self.toolZivaTissue_create = self.toolZivaTissue_menu.addAction("create zTissue")
        self.toolZivaTissue_create.triggered.connect(self.clickToolZivaTissueCreate)
        self.toolZivaTissue_disaRSide = self.toolZivaTissue_menu.addAction("disable right side")
        self.toolZivaTissue_disaRSide.triggered.connect(self.clickToolZivaTissueDisaRSide)
        self.toolZivaTissue_enaRSide = self.toolZivaTissue_menu.addAction("enable right side")
        self.toolZivaTissue_enaRSide.triggered.connect(self.clickToolZivaTissueEnaRSide)
        self.toolZivaTissue_damping = self.toolZivaTissue_menu.addAction("set damping 1")
        self.toolZivaTissue_damping.triggered.connect(self.clickToolZivaTissueDamping)
        self.toolZivaTissue_but = QtWidgets.QPushButton("zTissue")
        self.toolZivaTissue_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zTissue.png')))
        self.toolZivaTissue_but.setMenu(self.toolZivaTissue_menu)


        self.toolZivaTet_menu = QtWidgets.QMenu(self)
        self.toolZivaTet_showHide = self.toolZivaTet_menu.addAction("show/hide")
        self.toolZivaTet_showHide.triggered.connect(self.clickToolZivaTetShowHide)
        self.toolZivaTet_x05 = self.toolZivaTet_menu.addAction("x 0.5")
        self.toolZivaTet_x05.triggered.connect(self.clickToolZivaTetX05)
        self.toolZivaTet_x075 = self.toolZivaTet_menu.addAction("x 0.75")
        self.toolZivaTet_x075.triggered.connect(self.clickToolZivaTetX075)
        self.toolZivaTet_09 = self.toolZivaTet_menu.addAction("x 0.9")
        self.toolZivaTet_09.triggered.connect(self.clickToolZivaTetX9)
        self.toolZivaTet_x11 = self.toolZivaTet_menu.addAction("x 1.1")
        self.toolZivaTet_x11.triggered.connect(self.clickToolZivaTetX11)
        self.toolZivaTet_x125 = self.toolZivaTet_menu.addAction("x 1.25")
        self.toolZivaTet_x125.triggered.connect(self.clickToolZivaTetX125)
        self.toolZivaTet_x2 = self.toolZivaTet_menu.addAction("x 2")
        self.toolZivaTet_x2.triggered.connect(self.clickToolZivaTetX2)
        self.toolZivaTet_but = QtWidgets.QPushButton("zTet")
        self.toolZivaTet_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zTet.png')))
        self.toolZivaTet_but.setMenu(self.toolZivaTet_menu)


        self.toolZivaSecond_l = QtWidgets.QLabel("Tissue Property :")


        self.toolZivaMaterial_menu = QtWidgets.QMenu(self)
        self.toolZivaMaterial_gelatin = self.toolZivaMaterial_menu.addAction("Gelatin")  #1.0*10^0
        self.toolZivaMaterial_gelatin.triggered.connect(self.clickToolZivaMaterialGelatin)
        self.toolZivaMaterial_brain = self.toolZivaMaterial_menu.addAction("Brain")  #0.5*10^3
        self.toolZivaMaterial_brain.triggered.connect(self.clickToolZivaMaterialBrain)
        self.toolZivaMaterial_liver = self.toolZivaMaterial_menu.addAction("Liver")  #0.7*10^3
        self.toolZivaMaterial_liver.triggered.connect(self.clickToolZivaMaterialLiver)
        self.toolZivaMaterial_breastTissue = self.toolZivaMaterial_menu.addAction("Breast Tissue")  #0.9*10^3
        self.toolZivaMaterial_breastTissue.triggered.connect(self.clickToolZivaMaterialBreastTissue)
        self.toolZivaMaterial_fat = self.toolZivaMaterial_menu.addAction("Fat")  #3.0*10^3
        self.toolZivaMaterial_fat.triggered.connect(self.clickToolZivaMaterialFat)
        self.toolZivaMaterial_smoothMuscle = self.toolZivaMaterial_menu.addAction("Smooth Muscle")  #5.0*10^3
        self.toolZivaMaterial_smoothMuscle.triggered.connect(self.clickToolZivaMaterialSmoothMuscle)
        self.toolZivaMaterial_skeletalMuscle = self.toolZivaMaterial_menu.addAction("Skeletal Muscle")  #1.2*10^4
        self.toolZivaMaterial_skeletalMuscle.triggered.connect(self.clickToolZivaMaterialSkeletalMuscle)
        self.toolZivaMaterial_cartilage = self.toolZivaMaterial_menu.addAction("Cartilage")  #2.0*10^4
        self.toolZivaMaterial_cartilage.triggered.connect(self.clickToolZivaMaterialCartilage)
        self.toolZivaMaterial_rubber = self.toolZivaMaterial_menu.addAction("Rubber")  #1.0*10^7
        self.toolZivaMaterial_rubber.triggered.connect(self.clickToolZivaMaterialRubber)
        self.toolZivaMaterial_wood = self.toolZivaMaterial_menu.addAction("Wood")  #0.6*10^9
        self.toolZivaMaterial_wood.triggered.connect(self.clickToolZivaMaterialWood)
        self.toolZivaMaterial_tendon = self.toolZivaMaterial_menu.addAction("Tendon")  #1.0*10^9
        self.toolZivaMaterial_tendon.triggered.connect(self.clickToolZivaMaterialTendon)
        self.toolZivaMaterial_plastic = self.toolZivaMaterial_menu.addAction("Plastic")  #1.5*10^9
        self.toolZivaMaterial_plastic.triggered.connect(self.clickToolZivaMaterialPlastic)
        self.toolZivaMaterial_bone = self.toolZivaMaterial_menu.addAction("Bone")  #1.4*10^10
        self.toolZivaMaterial_bone.triggered.connect(self.clickToolZivaMaterialBone)
        self.toolZivaMaterial_walnutShell = self.toolZivaMaterial_menu.addAction("Walnut Shell")  #1.5*10^10
        self.toolZivaMaterial_walnutShell.triggered.connect(self.clickToolZivaMaterialWalnulShell)
        self.toolZivaMaterial_steel = self.toolZivaMaterial_menu.addAction("Steel")  #2.0*10^11
        self.toolZivaMaterial_steel.triggered.connect(self.clickToolZivaMaterialSteel)
        self.toolZivaMaterial_diamond = self.toolZivaMaterial_menu.addAction("Diamond")  #1.0*10^12 
        self.toolZivaMaterial_diamond.triggered.connect(self.clickToolZivaMaterialDiamond)
        self.toolZivaMaterial_but = QtWidgets.QPushButton("zMaterial")
        self.toolZivaMaterial_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zMaterial.png')))
        self.toolZivaMaterial_but.setMenu(self.toolZivaMaterial_menu)


        self.toolZivaFiber_menu = QtWidgets.QMenu(self)
        self.toolZivaFiber_create = self.toolZivaFiber_menu.addAction("create zFiber")
        self.toolZivaFiber_create.triggered.connect(self.clickToolZivaFiberCreate)
        self.toolZivaFiber_select = self.toolZivaFiber_menu.addAction("select zFiber")
        self.toolZivaFiber_select.triggered.connect(self.clickToolZivaFiberSelect)
        self.toolZivaFiber_but = QtWidgets.QPushButton("zFiber")
        self.toolZivaFiber_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zFiber.png')))
        self.toolZivaFiber_but.setMenu(self.toolZivaFiber_menu)


        self.toolZivaLOA_menu = QtWidgets.QMenu(self)
        self.toolZivaLOA_create = self.toolZivaLOA_menu.addAction("create LOA")
        self.toolZivaLOA_create.triggered.connect(self.clickToolZivaLOACreate)
        self.toolZivaLOA_select = self.toolZivaLOA_menu.addAction("select LOA")
        self.toolZivaLOA_select.triggered.connect(self.clickToolZivaLOASelect)
        self.toolZivaLOA_addCrv = self.toolZivaLOA_menu.addAction("add curve to LOA")
        self.toolZivaLOA_addCrv.triggered.connect(self.clickToolZivaLOAAddCrv)
        self.toolZivaLOA_but = QtWidgets.QPushButton("LOA")
        self.toolZivaLOA_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zLineOfAction.png')))
        self.toolZivaLOA_but.setMenu(self.toolZivaLOA_menu)


        self.toolZivaBone_menu = QtWidgets.QMenu(self)
        self.toolZivaBone_create = self.toolZivaBone_menu.addAction("create zBone")
        self.toolZivaBone_create.triggered.connect(self.clickToolZivaBoneCreate)
        self.toolZivaBone_but = QtWidgets.QPushButton("zBone")
        self.toolZivaBone_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zBone.png')))
        self.toolZivaBone_but.setMenu(self.toolZivaBone_menu)


        self.toolZivaPaintAttach_menu = QtWidgets.QMenu(self)
        self.toolZivaPaintAttach_create = self.toolZivaPaintAttach_menu.addAction("create zattachment")
        self.toolZivaPaintAttach_create.triggered.connect(self.clickToolZivaAttachmentCreate)
        self.toolZivaPaintAttach_sliding = self.toolZivaPaintAttach_menu.addAction("set sliding")
        self.toolZivaPaintAttach_sliding.triggered.connect(self.clickToolZivaAttachmentSliding)
        self.toolZivaPaintAttach_fixed = self.toolZivaPaintAttach_menu.addAction("set fixed")
        self.toolZivaPaintAttach_fixed.triggered.connect(self.clickToolZivaAttachmentFixed)
        self.toolZivaPaintAttachProximity_menu = self.toolZivaPaintAttach_menu.addMenu("paintProximity : ")
        self.toolZivaPaintAttach_02 = self.toolZivaPaintAttachProximity_menu.addAction("0.2")
        self.toolZivaPaintAttach_02.triggered.connect(self.clickToolZivaAttachment02)
        self.toolZivaPaintAttach_05 = self.toolZivaPaintAttachProximity_menu.addAction("0.5")
        self.toolZivaPaintAttach_05.triggered.connect(self.clickToolZivaAttachment05)
        self.toolZivaPaintAttach_1 = self.toolZivaPaintAttachProximity_menu.addAction("1")
        self.toolZivaPaintAttach_1.triggered.connect(self.clickToolZivaAttachment1)
        self.toolZivaPaintAttach_2 = self.toolZivaPaintAttachProximity_menu.addAction("2")
        self.toolZivaPaintAttach_2.triggered.connect(self.clickToolZivaAttachment2)
        self.toolZivaPaintAttach_5 = self.toolZivaPaintAttachProximity_menu.addAction("5")
        self.toolZivaPaintAttach_5.triggered.connect(self.clickToolZivaAttachment5)
        self.toolZivaPaintAttach_10 = self.toolZivaPaintAttachProximity_menu.addAction("10")
        self.toolZivaPaintAttach_10.triggered.connect(self.clickToolZivaAttachment10)
        self.toolZivaPaintAttachPower_menu = self.toolZivaPaintAttach_menu.addMenu("power : ")
        self.toolZivaPaintAttachPower_1 = self.toolZivaPaintAttachPower_menu.addAction("1")
        self.toolZivaPaintAttachPower_1.triggered.connect(self.clickToolZivaAttachmentPower1)
        self.toolZivaPaintAttachPower_2 = self.toolZivaPaintAttachPower_menu.addAction("2")
        self.toolZivaPaintAttachPower_2.triggered.connect(self.clickToolZivaAttachmentPower2)
        self.toolZivaPaintAttachPower_3 = self.toolZivaPaintAttachPower_menu.addAction("3")
        self.toolZivaPaintAttachPower_3.triggered.connect(self.clickToolZivaAttachmentPower3)
        self.toolZivaPaintAttachPower_4 = self.toolZivaPaintAttachPower_menu.addAction("4")
        self.toolZivaPaintAttachPower_4.triggered.connect(self.clickToolZivaAttachmentPower4)
        self.toolZivaPaintAttachPower_5 = self.toolZivaPaintAttachPower_menu.addAction("5")
        self.toolZivaPaintAttachPower_5.triggered.connect(self.clickToolZivaAttachmentPower5)
        self.toolZivaPaintAttachPower_6 = self.toolZivaPaintAttachPower_menu.addAction("6")
        self.toolZivaPaintAttachPower_6.triggered.connect(self.clickToolZivaAttachmentPower6)
        self.toolZivaPaintAttachPower_7 = self.toolZivaPaintAttachPower_menu.addAction("7")
        self.toolZivaPaintAttachPower_7.triggered.connect(self.clickToolZivaAttachmentPower7)
        self.toolZivaPaintAttachPower_8 = self.toolZivaPaintAttachPower_menu.addAction("8")
        self.toolZivaPaintAttachPower_8.triggered.connect(self.clickToolZivaAttachmentPower8)
        self.toolZivaPaintAttachPower_9 = self.toolZivaPaintAttachPower_menu.addAction("9")
        self.toolZivaPaintAttachPower_9.triggered.connect(self.clickToolZivaAttachmentPower9)
        self.toolZivaPaintAttachPower_10 = self.toolZivaPaintAttachPower_menu.addAction("10")
        self.toolZivaPaintAttachPower_10.triggered.connect(self.clickToolZivaAttachmentPower10)
        self.toolZivaPaintAttach_but = QtWidgets.QPushButton("zAttach")
        self.toolZivaPaintAttach_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','zAttachment.png')))
        self.toolZivaPaintAttach_but.setMenu(self.toolZivaPaintAttach_menu)

        self.toolZivaThird_l = QtWidgets.QLabel("Edit Mesh :")

        self.toolZivaCopyPaste_menu = QtWidgets.QMenu(self)
        self.toolZivaCopyPaste_copy = self.toolZivaCopyPaste_menu.addAction("Copy")
        self.toolZivaCopyPaste_copy.triggered.connect(self.clickToolZivaCopy)
        self.toolZivaCopyPaste_paste = self.toolZivaCopyPaste_menu.addAction("Paste")
        self.toolZivaCopyPaste_paste.triggered.connect(self.clickToolZivaPaste)
        self.toolZivaCopyPaste_but = QtWidgets.QPushButton("CopyPaste")
        self.toolZivaCopyPaste_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','copyPaste.png')))
        self.toolZivaCopyPaste_but.setMenu(self.toolZivaCopyPaste_menu)

        self.toolZivaMeshSculpt_menu = QtWidgets.QMenu(self)
        self.toolZivaMeshSculpt_standard = self.toolZivaMeshSculpt_menu.addAction("Standard")
        self.toolZivaMeshSculpt_standard.triggered.connect(self.clickToolZivaMeshStandart) 
        self.toolZivaMeshSculpt_move = self.toolZivaMeshSculpt_menu.addAction("Move")
        self.toolZivaMeshSculpt_move.triggered.connect(self.clickToolZivaMeshMove)
        self.toolZivaMeshSculpt_inflat = self.toolZivaMeshSculpt_menu.addAction("Inflat")
        self.toolZivaMeshSculpt_inflat.triggered.connect(self.clickToolZivaMeshInflat)
        self.toolZivaMeshSculpt_flatten = self.toolZivaMeshSculpt_menu.addAction("Flatten")
        self.toolZivaMeshSculpt_flatten.triggered.connect(self.clickToolZivaMeshFlatten)
        self.toolZivaMeshSculpt_pinch = self.toolZivaMeshSculpt_menu.addAction("Pinch")
        self.toolZivaMeshSculpt_pinch.triggered.connect(self.clickToolZivaMeshPinch)
        self.toolZivaMeshSculpt_but = QtWidgets.QPushButton("MeshSculpt")
        self.toolZivaMeshSculpt_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','meshStandart.png')))
        self.toolZivaMeshSculpt_but.setMenu(self.toolZivaMeshSculpt_menu)

        self.toolZivaMeshModify_menu = QtWidgets.QMenu(self)
        self.toolZivaMeshModify_smooth = self.toolZivaMeshModify_menu.addAction("Smooth")
        self.toolZivaMeshModify_smooth.triggered.connect(self.clickToolZivaMeshSmooth)
        self.toolZivaMeshModify_freeze = self.toolZivaMeshModify_menu.addAction("Freeze")
        self.toolZivaMeshModify_freeze.triggered.connect(self.clickToolZivaMeshFreeze)
        self.toolZivaMeshModify_unFreeze = self.toolZivaMeshModify_menu.addAction("UnFreeze")
        self.toolZivaMeshModify_unFreeze.triggered.connect(self.clickToolZivaMeshUnFreeze)
        self.toolZivaMeshModify_relax = self.toolZivaMeshModify_menu.addAction("Relax")
        self.toolZivaMeshModify_relax.triggered.connect(self.clickToolZivaMeshRelax)
        self.toolZivaMeshModify_remesh = self.toolZivaMeshModify_menu.addAction("Remesh")
        self.toolZivaMeshModify_remesh.triggered.connect(self.clickToolZivaMeshRemesh)
        self.toolZivaMeshModify_retopo = self.toolZivaMeshModify_menu.addAction("Retopo")
        self.toolZivaMeshModify_retopo.triggered.connect(self.clickToolZivaMeshRetopo)
        self.toolZivaMeshModify_but = QtWidgets.QPushButton("MeshModify")
        self.toolZivaMeshModify_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','meshOption.png')))
        self.toolZivaMeshModify_but.setMenu(self.toolZivaMeshModify_menu)

        self.toolZivaMeshMirror_menu = QtWidgets.QMenu(self)
        self.toolZivaMeshMirror_mirror = self.toolZivaMeshMirror_menu.addAction("Mirror")
        self.toolZivaMeshMirror_mirror.triggered.connect(self.clickToolZivaMeshMirror)
        self.toolZivaMeshMirror_transfer = self.toolZivaMeshMirror_menu.addAction("Transfer Shape")
        self.toolZivaMeshMirror_transfer.triggered.connect(self.clickToolZivaMeshTransfer)
        self.toolZivaMeshMirror_but = QtWidgets.QPushButton("MeshMirror")
        self.toolZivaMeshMirror_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','meshMirror.png')))
        self.toolZivaMeshMirror_but.setMenu(self.toolZivaMeshMirror_menu)


        self.toolZivaFourth_l = QtWidgets.QLabel("Tools :")


        self.toolZivaPaintTool_menu = QtWidgets.QMenu(self)
        self.toolZivaPaintTool_0 = self.toolZivaPaintTool_menu.addAction("Value 0")
        self.toolZivaPaintTool_0.triggered.connect(self.clickToolZivaPaintTool0)
        self.toolZivaPaintTool_05 = self.toolZivaPaintTool_menu.addAction("Value 0.5")
        self.toolZivaPaintTool_05.triggered.connect(self.clickToolZivaPaintTool05)
        self.toolZivaPaintTool_1 = self.toolZivaPaintTool_menu.addAction("Value 1")
        self.toolZivaPaintTool_1.triggered.connect(self.clickToolZivaPaintTool1)
        self.toolZivaPaintTool_flood0 = self.toolZivaPaintTool_menu.addAction("Flood 0")
        self.toolZivaPaintTool_flood0.triggered.connect(self.clickToolZivaPaintToolFlood0)
        self.toolZivaPaintTool_flood1 = self.toolZivaPaintTool_menu.addAction("Flood 1")
        self.toolZivaPaintTool_flood1.triggered.connect(self.clickToolZivaPaintToolFlood1)
        self.toolZivaPaintTool_smooth = self.toolZivaPaintTool_menu.addAction("Smooth")
        self.toolZivaPaintTool_smooth.triggered.connect(self.clickToolZivaPaintToolSmooth)

        self.toolZivaPaintTool_but = QtWidgets.QPushButton("PaintTool")
        self.toolZivaPaintTool_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','paintTool.png')))
        self.toolZivaPaintTool_but.setMenu(self.toolZivaPaintTool_menu)


        self.toolZivaMirror_menu = QtWidgets.QMenu(self)
        self.toolZivaMirror_LR = self.toolZivaMirror_menu.addAction("Left to Right")
        self.toolZivaMirror_LR.triggered.connect(self.clickToolZivaMirrorLR)
        self.toolZivaMirror_RL = self.toolZivaMirror_menu.addAction("Right to Left")
        self.toolZivaMirror_RL.triggered.connect(self.clickToolZivaMirrorRL)
        self.toolZivaMirror_but = QtWidgets.QPushButton("Mirror")
        self.toolZivaMirror_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','mirrorSkin.png')))
        self.toolZivaMirror_but.setMenu(self.toolZivaMirror_menu)


        self.toolZivaRename_menu = QtWidgets.QMenu(self)
        self.toolZivaRename_rename = self.toolZivaRename_menu.addAction("rename all Ziva nodes")
        self.toolZivaRename_rename.triggered.connect(self.clickToolZivaRename)
        self.toolZivaRename_but = QtWidgets.QPushButton("Rename")
        self.toolZivaRename_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','rename.png')))
        self.toolZivaRename_but.setMenu(self.toolZivaRename_menu)


        self.toolZivaActivate_menu = QtWidgets.QMenu(self)
        self.toolZivaActivate_activate = self.toolZivaActivate_menu.addAction("activate/desactivate zTissue")
        self.toolZivaActivate_activate.triggered.connect(self.clickToolZivaActivate)
        self.toolZivaActivate_allActivate = self.toolZivaActivate_menu.addAction("activate all zTissue")
        self.toolZivaActivate_allActivate.triggered.connect(self.clickToolZivaAllActivate)
        self.toolZivaActivate_but = QtWidgets.QPushButton("On/Off")
        self.toolZivaActivate_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','onOff.png')))
        self.toolZivaActivate_but.setMenu(self.toolZivaActivate_menu)

        #Create_Ctrls

        self.createCtrlSize_l = QtWidgets.QLabel("Size: ")
        self.createCtrlSize_sb = QtWidgets.QDoubleSpinBox()
        self.createCtrlSize_sb.setValue(1)
        self.createCtrlSize_sb.setMinimum(0.01)
        self.createCtrlSize_sb.setMaximum(10)
        self.createCtrlGrp_chx = QtWidgets.QCheckBox('In group ?')
        self.createCtrlTabCircle_but = QtWidgets.QToolButton()
        self.createCtrlTabCircle_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','circle.jpg')))
        self.createCtrlTabCircle_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabCircle_but.clicked.connect(self.clickCtrlCircle_But)
        self.createCtrlTabTriangle_but = QtWidgets.QToolButton()
        self.createCtrlTabTriangle_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','triangle.jpg')))
        self.createCtrlTabTriangle_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabTriangle_but.clicked.connect(self.clickCtrlTriangle_But)
        self.createCtrlTabSquare_but = QtWidgets.QToolButton()
        self.createCtrlTabSquare_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','square.jpg')))
        self.createCtrlTabSquare_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabSquare_but.clicked.connect(self.clickCtrlSquare_But)
        self.createCtrlTabBox_but = QtWidgets.QToolButton()
        self.createCtrlTabBox_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','box.jpg')))
        self.createCtrlTabBox_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabBox_but.clicked.connect(self.clickCtrlBox_But)
        self.createCtrlTabCross_but = QtWidgets.QToolButton()
        self.createCtrlTabCross_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','cross.jpg')))
        self.createCtrlTabCross_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabCross_but.clicked.connect(self.clickCtrlCross_But)
        self.createCtrlTabBall_but = QtWidgets.QToolButton()
        self.createCtrlTabBall_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','ball.jpg')))
        self.createCtrlTabBall_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabBall_but.clicked.connect(self.clickCtrlBall_But)
        self.createCtrlTabDiamond_but = QtWidgets.QToolButton()
        self.createCtrlTabDiamond_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','diamond.jpg')))
        self.createCtrlTabDiamond_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabDiamond_but.clicked.connect(self.clickCtrlDiamond_But)
        self.createCtrlTabArrow_but = QtWidgets.QToolButton()
        self.createCtrlTabArrow_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','arrow.jpg')))
        self.createCtrlTabArrow_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabArrow_but.clicked.connect(self.clickCtrlArrow_But)
        self.createCtrlTabLocator_but = QtWidgets.QToolButton()
        self.createCtrlTabLocator_but.setIcon(QtGui.QIcon(os.path.join(hadEnv.PATH,'images','locator.jpg')))
        self.createCtrlTabLocator_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabLocator_but.clicked.connect(self.clickCtrlLocator_But)
       
    def create_layouts(self):
        
        #master_tab : 
        
        autoRig_layout = QtWidgets.QVBoxLayout()
        autoRig_layout.addWidget(self.autoRig_but)
        autoRig_layout.addWidget(self.autoRig_l)
        
        cerberus_layout = QtWidgets.QVBoxLayout()
        cerberus_layout.addWidget(self.cerberus_but)
        cerberus_layout.addWidget(self.cerberus_l)

        thanatos_layout = QtWidgets.QVBoxLayout() 
        thanatos_layout.addWidget(self.thanatos_but)
        thanatos_layout.addWidget(self.thanatos_l)
        
        chaos_layout = QtWidgets.QVBoxLayout() 
        chaos_layout.addWidget(self.chaos_but)
        chaos_layout.addWidget(self.chaos_l)

        toolMaya_layout = QtWidgets.QVBoxLayout()
        toolMaya_layout.addWidget(self.toolMaya_but)
        toolMaya_layout.addWidget(self.toolMaya_l)

        createCrv_layout = QtWidgets.QVBoxLayout()
        createCrv_layout.addWidget(self.createCrv_but)
        createCrv_layout.addWidget(self.createCrv_l)

        toolZiva_layout = QtWidgets.QVBoxLayout()
        toolZiva_layout.addWidget(self.toolZiva_but)
        toolZiva_layout.addWidget(self.toolZiva_l)

        master_layout = QtWidgets.QVBoxLayout(self.masterTab)
        master_layout.addWidget(self.title_l)
        #master_layout.addLayout(autoRig_layout)
        master_layout.addLayout(cerberus_layout)
        master_layout.addLayout(thanatos_layout)
        master_layout.addLayout(chaos_layout)
        #master_layout.addLayout(toolMaya_layout)
        #master_layout.addLayout(createCrv_layout)
        #master_layout.addLayout(toolZiva_layout)

        #auto_rig_tab

        self.autoRigTab_layout = QtWidgets.QGridLayout(self.autoRigTab)
        self.autoRigTab_layout.addWidget(self.autoRig_feature_l)
        self.autoRigTab_layout.addWidget(self.autoRig_arm_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_leg_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_chest_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_head_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_guide_l)
        self.autoRigTab_layout.addWidget(self.autoRig_guide_but)
        self.autoRigTab_layout.addWidget(self.autoRig_option_l)
        self.autoRigTab_layout.addWidget(self.autoRig_stretch_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_mirror_chk)
        self.autoRigTab_layout.addWidget(self.autoRig_createRig_l)
        self.autoRigTab_layout.addWidget(self.autoRig_createRig_but)
        
        #Cerberus_tab

        self.cerberus_layoutA = QtWidgets.QHBoxLayout()
        self.cerberus_layoutA.addWidget(self.cerberus_title_l)
        self.cerberus_layoutB = QtWidgets.QHBoxLayout()
        self.cerberus_layoutB.addWidget(self.cerberus_titleTemplate_l)
        self.cerberus_layoutC = QtWidgets.QHBoxLayout()
        self.cerberus_layoutC.addWidget(self.cerberus_titleTemplate_butBi)
        self.cerberus_layoutC.addWidget(self.cerberus_titleTemplate_butQa)
        self.cerberus_layoutC.addWidget(self.cerberus_titleTemplate_butWi)
        self.cerberus_layoutC.addWidget(self.cerberus_titleTemplate_butFa)
        self.cerberus_layoutD = QtWidgets.QHBoxLayout()
        self.cerberus_layoutD.addWidget(self.cerberus_titleBrick_l)
        self.cerberus_layoutE = QtWidgets.QHBoxLayout()
        self.cerberus_layoutE.addWidget(self.cerberus_presetBrick_CB)

        self.cerberus_layoutG = QtWidgets.QHBoxLayout()
        self.cerberus_layoutG.addWidget(self.cerberus_editName_l)
        self.cerberus_layoutG.addWidget(self.cerberus_editName_lE)
        self.cerberus_layoutH = QtWidgets.QHBoxLayout()
        self.cerberus_layoutH.addWidget(self.cerberus_editSide_l)
        
        self.cerberus_editSide_grpBut = QtWidgets.QButtonGroup()
        self.cerberus_editSide_grpBut.addButton(self.cerberus_editSide_rB1)
        self.cerberus_editSide_grpBut.addButton(self.cerberus_editSide_rB2)
        self.cerberus_editSide_grpBut.addButton(self.cerberus_editSide_rB3)  
        
        self.cerberus_layoutH.addWidget(self.cerberus_editSide_rB1)
        self.cerberus_layoutH.addWidget(self.cerberus_editSide_rB2)
        self.cerberus_layoutH.addWidget(self.cerberus_editSide_rB3)

        self.cerberus_layoutH.addStretch(1)
        
        self.cerberus_layoutI = QtWidgets.QHBoxLayout()
        self.cerberus_layoutI.addWidget(self.cerberus_editMirror_l)
        self.cerberus_layoutI.addWidget(self.cerberus_editMirror_chk)
        self.cerberus_layoutI.addStretch(1)
        self.cerberus_layoutJ = QtWidgets.QHBoxLayout()
        
        self.cerberus_editLevel_grpBut = QtWidgets.QButtonGroup()
        self.cerberus_editLevel_grpBut.addButton(self.cerberus_editLevel_rB1)
        self.cerberus_editLevel_grpBut.addButton(self.cerberus_editLevel_rB2)
        self.cerberus_editLevel_grpBut.addButton(self.cerberus_editLevel_rB3)
        self.cerberus_editLevel_grpBut.addButton(self.cerberus_editLevel_rB4)
        
        
        self.cerberus_layoutJ.addWidget(self.cerberus_editLevel_l)
        self.cerberus_layoutJ.addWidget(self.cerberus_editLevel_rB1)
        self.cerberus_layoutJ.addWidget(self.cerberus_editLevel_rB2)
        self.cerberus_layoutJ.addWidget(self.cerberus_editLevel_rB3)
        self.cerberus_layoutJ.addWidget(self.cerberus_editLevel_rB4)
        
        
        
        self.cerberus_layoutJ.addStretch(1)
        self.cerberus_layoutK = QtWidgets.QHBoxLayout()
        self.cerberus_layoutK.addWidget(self.cerberus_parent_l)
        self.cerberus_layoutK.addWidget(self.cerberus_parent_lE)
        self.cerberus_layoutK.addWidget(self.cerberus_parent_but)
        self.cerberus_layoutL = QtWidgets.QHBoxLayout()
        self.cerberus_layoutL.addWidget(self.cerberus_constraint_l)
        self.cerberus_layoutL.addWidget(self.cerberus_constraint_but)
        self.cerberus_layoutF = QtWidgets.QHBoxLayout()
        self.cerberus_layoutF.addWidget(self.cerberus_treeSet_l)
        self.cerberus_layoutF.addWidget(self.cerberus_treeSet_but)
        self.cerberus_layoutM = QtWidgets.QHBoxLayout()
        self.cerberus_layoutM.addWidget(self.cerberus_muscle_l)
        self.cerberus_layoutM.addWidget(self.cerberus_muscle_CB)
        self.cerberus_layoutM.addWidget(self.cerberus_muscle_but)
        
        self.cerberus_layoutN = QtWidgets.QHBoxLayout()
        self.cerberus_layoutN.addWidget(self.cerberus_option_l)
        self.cerberus_layoutN.addWidget(self.cerberus_optionTwist_chk)
        self.cerberus_layoutN.addWidget(self.cerberus_optionStretch_chk)
        self.cerberus_layoutN.addWidget(self.cerberus_optionSquash_chk)
               
        

        
        self.cerberus_layoutV = QtWidgets.QHBoxLayout()
        self.cerberus_layoutV.addWidget(self.cerberus_CreateBrick_but)
        self.cerberus_layoutW = QtWidgets.QHBoxLayout()
        self.cerberus_layoutW.addWidget(self.cerberus_titleTree_l)
        self.cerberus_layoutW.addWidget(self.cerberus_refreshTree_l)
        self.cerberus_layoutW.addStretch(1)
        self.cerberus_layoutX = QtWidgets.QHBoxLayout()
        self.cerberus_layoutX.addWidget(self.cerberus_tree)
        self.cerberus_layoutY = QtWidgets.QHBoxLayout()
        self.cerberus_layoutY.addWidget(self.cerberus_Build_but)
        self.cerberus_layoutZ = QtWidgets.QHBoxLayout()
        self.cerberus_layoutZ.addWidget(self.cerberus_BuildToggle_chk)
        
        
        self.cerberus_layout = QtWidgets.QVBoxLayout(self.cerberusTab)
        self.cerberus_layout.addLayout(self.cerberus_layoutA)
        self.cerberus_layout.addLayout(self.cerberus_layoutB)
        self.cerberus_layout.addLayout(self.cerberus_layoutC)
        self.cerberus_layout.addLayout(self.cerberus_layoutD)
        self.cerberus_layout.addLayout(self.cerberus_layoutE)
        self.cerberus_layout.addLayout(self.cerberus_layoutG)
        self.cerberus_layout.addLayout(self.cerberus_layoutH)
        self.cerberus_layout.addLayout(self.cerberus_layoutI)
        self.cerberus_layout.addLayout(self.cerberus_layoutJ)
        self.cerberus_layout.addLayout(self.cerberus_layoutK)
        self.cerberus_layout.addLayout(self.cerberus_layoutL)
        self.cerberus_layout.addLayout(self.cerberus_layoutF)
        self.cerberus_layout.addLayout(self.cerberus_layoutM)
        self.cerberus_layout.addLayout(self.cerberus_layoutN)

        self.cerberus_layout.addLayout(self.cerberus_layoutV)
        self.cerberus_layout.addLayout(self.cerberus_layoutW)
        self.cerberus_layout.addLayout(self.cerberus_layoutX)
        self.cerberus_layout.addLayout(self.cerberus_layoutY)
        self.cerberus_layout.addLayout(self.cerberus_layoutZ)


















































        #Cerberus constraint setting tab


        

















        #thanatos_tab

        self.thanatos_layoutA = QtWidgets.QHBoxLayout()
        self.thanatos_layoutA.addWidget(self.thanatos_shrink_but)
        self.thanatos_layoutA.addWidget(self.thanatos_grow_but)
        self.thanatos_layoutA.addWidget(self.thanatos_ring_but)
        self.thanatos_layoutA.addWidget(self.thanatos_loop_but)

        self.thanatos_layoutB = QtWidgets.QHBoxLayout()
        self.thanatos_layoutB.addWidget(self.thanatos_0_but)
        self.thanatos_layoutB.addWidget(self.thanatos_01_but)
        self.thanatos_layoutB.addWidget(self.thanatos_025_but)
        self.thanatos_layoutB.addWidget(self.thanatos_05_but)
        self.thanatos_layoutB.addWidget(self.thanatos_075_but)
        self.thanatos_layoutB.addWidget(self.thanatos_09_but)
        self.thanatos_layoutB.addWidget(self.thanatos_1_but)

        self.thanatos_layoutC = QtWidgets.QHBoxLayout()
        self.thanatos_layoutC.addWidget(self.thanatos_setWeight_but)
        self.thanatos_layoutC.addWidget(self.thanatos_setWeight_sb)
        self.thanatos_layoutC.addWidget(self.thanatos_setWeightAdd_but)
        self.thanatos_layoutC.addWidget(self.thanatos_setWeightSub_but)

        self.thanatos_layoutD = QtWidgets.QHBoxLayout()
        self.thanatos_layoutD.addWidget(self.thanatos_scaleWeight_but)
        self.thanatos_layoutD.addWidget(self.thanatos_scaleWeight_sb)
        self.thanatos_layoutD.addWidget(self.thanatos_scaleWeightAdd_but)
        self.thanatos_layoutD.addWidget(self.thanatos_scaleWeightSub_but)

        self.thanatos_layoutE = QtWidgets.QHBoxLayout()
        self.thanatos_layoutE.addWidget(self.thanatos_copy_but)
        self.thanatos_layoutE.addWidget(self.thanatos_paste_but)
        self.thanatos_layoutE.addWidget(self.thanatos_pastePos_but)
        self.thanatos_layoutE.addWidget(self.thanatos_blend_but)

        self.thanatos_layoutF = QtWidgets.QHBoxLayout()
        self.thanatos_layoutF.addWidget(self.thanatos_pastePosTol_l)
        self.thanatos_layoutF.addWidget(self.thanatos_pastePosTol_sb)

        self.thanatos_layoutG = QtWidgets.QHBoxLayout()
        self.thanatos_layoutG.addWidget(self.thanatos_verSelected_l)
        self.thanatos_layoutG.addWidget(self.thanatos_verCopyBuffer_l)

        self.thanatos_layoutH = QtWidgets.QHBoxLayout()
        self.thanatos_layoutH.addWidget(self.thanatos_tree)

        self.thanatos_layout = QtWidgets.QVBoxLayout(self.thanatosTab)
        self.thanatos_layout.addLayout(self.thanatos_layoutA)
        self.thanatos_layout.addLayout(self.thanatos_layoutB)
        self.thanatos_layout.addLayout(self.thanatos_layoutC)
        self.thanatos_layout.addLayout(self.thanatos_layoutD)
        self.thanatos_layout.addLayout(self.thanatos_layoutE)
        self.thanatos_layout.addLayout(self.thanatos_layoutF)
        self.thanatos_layout.addLayout(self.thanatos_layoutG)
        self.thanatos_layout.addLayout(self.thanatos_layoutH)
        
        #cerberus tab
        
        

        #tool_for_maya_tab

        self.toolMayaTab_layout = QtWidgets.QGridLayout(self.toolMayaTab)
        self.toolMayaTab_layout.addWidget(self.toolMayaH_but, 0, 0)
        self.toolMayaTab_layout.addWidget(self.toolMayaT_but, 0, 1)
        self.toolMayaTab_layout.addWidget(self.toolMayaC_but, 0, 2)
        self.toolMayaTab_layout.addWidget(self.toolMayaCreJnt_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaJntSz_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaLRA_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaChaGrp_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaMirJnt_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaOriJnt_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaReOriJnt_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaMirCrv_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaParCrv_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaConEdi_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaShaEdi_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaDrivK_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaLoca_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaNodEdi_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaCopEdi_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaYellow_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaRed_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaBlue_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaPink_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaGreen_but)
        self.toolMayaTab_layout.addWidget(self.toolMayaPurple_but)

        #create_ctrl_tab

        self.createCrvTab_layout = QtWidgets.QGridLayout(self.createCtrlTab)
        self.createCrvTab_layout.addWidget(self.createCtrlSize_l, 0, 0)
        self.createCrvTab_layout.addWidget(self.createCtrlSize_sb, 0, 1)
        self.createCrvTab_layout.addWidget(self.createCtrlGrp_chx, 0, 2)
        self.createCrvTab_layout.addWidget(self.createCtrlTabCircle_but, 1, 0)
        self.createCrvTab_layout.addWidget(self.createCtrlTabTriangle_but, 1, 1)
        self.createCrvTab_layout.addWidget(self.createCtrlTabSquare_but, 1, 2)
        self.createCrvTab_layout.addWidget(self.createCtrlTabCross_but, 2, 0)
        self.createCrvTab_layout.addWidget(self.createCtrlTabBox_but, 2, 1)
        self.createCrvTab_layout.addWidget(self.createCtrlTabDiamond_but, 2, 2)
        self.createCrvTab_layout.addWidget(self.createCtrlTabBall_but, 3, 0)
        self.createCrvTab_layout.addWidget(self.createCtrlTabArrow_but, 3, 1)
        self.createCrvTab_layout.addWidget(self.createCtrlTabLocator_but, 3, 2)

        #tool_for_ziva_tab

        self.toolZivaTab_layout = QtWidgets.QGridLayout(self.toolZivaTab)
        self.toolZivaTab_layout.addWidget(self.toolZivaFirst_l, 0, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPanel_but, 1, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaTissue_but, 1, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaTet_but, 1, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaBone_but, 1, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaSecond_l, 2, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaMaterial_but, 3, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaFiber_but, 3, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaLOA_but, 3, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintAttach_but, 3, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaThird_l, 4, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaCopyPaste_but, 5, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshSculpt_but, 5, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshModify_but, 5, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshMirror_but, 5, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaFourth_l, 6, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintTool_but, 7, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaMirror_but, 7, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaRename_but, 7, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaActivate_but, 7, 3)
 
        self.setCentralWidget(self.tabMaster)

    def create_connections(self):
        self.tabMaster.currentChanged.connect(self.tabChanged)

    #tab connection

    def tabChanged(self):
        if self.tabMaster.currentIndex() == 0:
            self.tabMaster.removeTab(2)
            self.tabMaster.removeTab(1)
            self.resize(400, 400)
        else:
            pass
        if self.tabMaster.currentIndex() == 1:
            if self.tabMaster.tabText(1) == 'Cerberus':
                self.tabMaster.removeTab(2)
                self.resize(400, 800)
        else:
            pass
        hadCore.endEventSelection()

    def clickAutoRig_But(self):

        self.tabMaster.addTab(self.autoRigTab,'AutoRig')
        self.tabMaster.setCurrentIndex(1)
        
    def clickCerberus_But(self):

        self.tabMaster.addTab(self.cerberusTab,'Cerberus')
        self.tabMaster.setCurrentIndex(1)
        self.resize(400, 800)

    def clickCerberusCons_But(self):

        self.tabMaster.addTab(self.cerberusConsTab,'Constraint Setting')
        self.tabMaster.setCurrentIndex(2)
        self.resize(400, 400)
        
    def clickCerberusTree_But(self):

        self.tabMaster.addTab(self.cerberusTreeTab,'Tree setting')
        self.tabMaster.setCurrentIndex(2)
        self.resize(400, 400)
        
    def clickCerberusMuscle_But(self):

        self.tabMaster.addTab(self.cerberusMuscleTab,'Muscle setting')
        self.tabMaster.setCurrentIndex(2)
        self.resize(400, 400)

    def clickThanatos_But(self):
        self.tabMaster.addTab(self.thanatosTab,'Thanatos')
        self.tabMaster.setCurrentIndex(1)
        hadCore.startEventSelection()
        
    def clickChaos_But(self):
        self.tabMaster.addTab(self.chaosTab,'Chaos')
        self.tabMaster.setCurrentIndex(1)

    def clickToolMaya_But(self):
        self.tabMaster.addTab(self.toolMayaTab,'Maya Tools')
        self.tabMaster.setCurrentIndex(1)

    def clickCreateCtrl_But(self):
        self.tabMaster.addTab(self.createCtrlTab,'Create Ctrl')
        self.tabMaster.setCurrentIndex(1) 

    def clickToolZiva_But(self):
        self.tabMaster.addTab(self.toolZivaTab,'Ziva Tools')
        self.tabMaster.setCurrentIndex(1)  

    #AutoRig

    def clickAutoRigGuide_But(self):
        hadEnv.AUTO_RIG_ARM = self.autoRig_arm_chk.isChecked()
        hadEnv.AUTO_RIG_LEG = self.autoRig_leg_chk.isChecked()
        hadEnv.AUTO_RIG_CHEST = self.autoRig_chest_chk.isChecked()
        hadEnv.AUTO_RIG_HEAD = self.autoRig_head_chk.isChecked()
        hadCore.coreAutoRigGuide()

    def clickAutoRigGenerator_But(self):
        hadEnv.AUTO_RIG_STRETCH = self.autoRig_stretch_chk.isChecked()
        hadEnv.AUTO_RIG_MIRROR = self.autoRig_mirror_chk.isChecked()
        hadCore.coreAutoRigGenerator()

    #thanatos

    def clickthanatosShrink_But(self):
        hadCore.corethanatosShrink()

    def clickthanatosGrow_But(self):
        hadCore.corethanatosGrow()

    def clickthanatosRing_But(self):
        hadCore.corethanatosRing()

    def clickthanatosLoop_But(self):
        hadCore.corethanatosLoop()

    def clickthanatos0_But(self):
        hadCore.corethanatos0(self)

    def clickthanatos01_But(self):
        hadCore.corethanatos01(self)

    def clickthanatos025_But(self):
        hadCore.corethanatos025(self)

    def clickthanatos05_But(self):
        hadCore.corethanatos05(self)

    def clickthanatos075_But(self):
        hadCore.corethanatos075(self)

    def clickthanatos09_But(self):
        hadCore.corethanatos09(self)

    def clickthanatos1_But(self):
        hadCore.corethanatos1(self)

    def clickthanatosSetWeight_But(self):
        hadCore.corethanatosSetWeight()

    def clickthanatosSetWeightAdd_But(self):
        hadCore.corethanatosSetWeightAdd()

    def clickthanatosSetWeightSub_But(self):
        hadCore.corethanatosSetWeightSub()

    def clickthanatosScaleWeight_But(self):
        hadCore.corethanatosScaleWeight()

    def clickthanatosScaleWeightAdd_But(self):
        hadCore.corethanatosScaleWeightAdd()

    def clickthanatosScaleWeightSub_But(self):
        hadCore.corethanatosScaleWeightSub()

    def clickthanatosCopy_But(self):
        hadCore.corethanatosCopy()

    def clickthanatosPaste_But(self):
        hadCore.corethanatosPaste()

    def clickthanatosPastePos_But(self):
        hadCore.coreSkinTooPastePos()

    def clickthanatosBlend_But(self):
        hadCore.corethanatosBlend()


    #Tool for maya

    def clickDeleteHistory_But(self):
        hadCore.coreDeleteHistory()

    def clickFreezeTransform_But(self):
        hadCore.coreFreezeTransform()

    def clickCenterPivot_But(self):
        hadCore.coreCenterPivot()

    def clickCreateJoints_But(self):
        hadCore.coreCreateJoints()

    def clickJointSize_But(self):
        hadCore.coreJointSize()

    def clickLocalRotationAxis_But(self):
        hadCore.coreLocalRotationAxis()

    def clickCharacterGroup_But(self):
        hadCore.coreCharacterGroup()

    def clickMirrorJoints_But(self):
        hadCore.coreMirrorJoints()

    def clickOrientJoints_But(self):
        hadCore.coreOrientJoints()

    def clickReOrientLastJoint_But(self):
        hadCore.coreReOrientLastJoint()

    def clickMirrorCurves_But(self):
        hadCore.coreMirrorCurves()

    def clickParentCurves_But(self):
        hadCore.coreParentCurves()

    def clickConnectionEditor_But(self):
        hadCore.coreConnectionEditor()

    def clickShapeEditor_But(self):
        hadCore.coreShapeEditor()

    def clickDrivenKey_But(self):
        hadCore.coreDrivenKey()

    def clickCreateLocator_But(self):
        hadCore.coreCreateLocator()

    def clickNodeEditor_But(self):
        hadCore.coreNodeEditor()

    def clickComponentEditor_But(self):
        hadCore.coreComponentEditor()

    def clickColorYellow_But(self):
        hadCore.coreColorYellow()

    def clickColorRed_But(self):
        hadCore.coreColorRed()
    
    def clickColorBlue_But(self):
        hadCore.coreColorBlue()

    def clickColorPink_But(self):
        hadCore.coreColorPink()

    def clickColorGreen_But(self):
        hadCore.coreColorGreen()
    
    def clickColorPurple_But(self):
        hadCore.coreColorPurple()
    
    #Create ctrl connection

    def clickCtrlCircle_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateCircle() 
    def clickCtrlTriangle_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateTriangle() 
    def clickCtrlSquare_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateSquare() 
    def clickCtrlCross_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateCross() 
    def clickCtrlBox_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateBox() 
    def clickCtrlDiamond_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateDiamond() 
    def clickCtrlBall_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateBall() 
    def clickCtrlArrow_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateArrow() 
    def clickCtrlLocator_But(self):
        hadEnv.CTRL_SIZE_VALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRL_GRP_VALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateLocator() 

    #Tools for Ziva

    def clickToolZivaPanelOpen(self):
        hadCore.coreToolZivaPanelOpen()
    def clickToolZivaPanelAddCache(self):
        hadCore.coreToolZivaPanelAddCache()
    def clickToolZivaPanelDeleteCache(self):
        hadCore.coreToolZivaPanelDeleteCache()
    def clickToolZivaTissueCreate(self):
        hadCore.coreToolZivaTissueCreate()
    def clickToolZivaTissueDisaRSide(self):
        hadCore.coreToolZivaTissueDisaRSide()
    def clickToolZivaTissueEnaRSide(self):
        hadCore.coreToolZivaTissueEnaRSide()
    def clickToolZivaTissueDamping(self):
        hadCore.coreToolZivaTissueDamping()
    def clickToolZivaTetShowHide(self):
        hadCore.coreToolZivaTetShowHide()
    def clickToolZivaTetX05(self):
        hadCore.coreToolZivaTetX05()
    def clickToolZivaTetX075(self):
        hadCore.coreToolZivaTetX075()
    def clickToolZivaTetX9(self):
        hadCore.coreToolZivaTetX9()
    def clickToolZivaTetX11(self):
        hadCore.coreToolZivaTetX11()
    def clickToolZivaTetX125(self):
        hadCore.coreToolZivaTetX125()
    def clickToolZivaTetX2(self):
        hadCore.coreToolZivaTetX2()
    def clickToolZivaMaterialGelatin(self):
        hadCore.coreToolZivaMaterialGelatin()
    def clickToolZivaMaterialBrain(self):
        hadCore.coreToolZivaMaterialBrain()
    def clickToolZivaMaterialLiver(self):
        hadCore.coreToolZivaMaterialLiver()
    def clickToolZivaMaterialBreastTissue(self):
        hadCore.coreToolZivaMaterialBreastTissue()
    def clickToolZivaMaterialFat(self):
        hadCore.coreToolZivaMaterialFat()
    def clickToolZivaMaterialSmoothMuscle(self):
        hadCore.coreToolZivaMaterialSmoothMuscle()
    def clickToolZivaMaterialSkeletalMuscle(self):
        hadCore.coreToolZivaMaterialSkeletalMuscle()
    def clickToolZivaMaterialCartilage(self):
        hadCore.coreToolZivaMaterialCartilage()
    def clickToolZivaMaterialRubber(self):
        hadCore.coreToolZivaMaterialRubber()
    def clickToolZivaMaterialWood(self):
        hadCore.coreToolZivaMaterialWood()
    def clickToolZivaMaterialTendon(self):
        hadCore.coreToolZivaMaterialTendon()
    def clickToolZivaMaterialPlastic(self):
        hadCore.coreToolZivaMaterialPlastic()
    def clickToolZivaMaterialBone(self):
        hadCore.coreToolZivaMaterialBone()
    def clickToolZivaMaterialWalnulShell(self):
        hadCore.coreToolZivaMaterialWalnutShell()
    def clickToolZivaMaterialSteel(self):
        hadCore.coreToolZivaMaterialSteel()
    def clickToolZivaMaterialDiamond(self):
        hadCore.coreToolMaterialDiamond()
    def clickToolZivaFiberCreate(self):
        hadCore.coreToolZivaFiberCreate()
    def clickToolZivaFiberSelect(self):
        hadCore.coreToolZivaFiberSelect()
    def clickToolZivaLOACreate(self):
        hadCore.coreToolZivaLOACreate()
    def clickToolZivaLOASelect(self):
        hadCore.coreToolZivaLOASelect()
    def clickToolZivaLOAAddCrv(self):
        hadCore.coreToolZivaLOAAddCrv()
    def clickToolZivaBoneCreate(self):
        hadCore.coreToolZivaBoneCreate()
    def clickToolZivaAttachmentCreate(self):
        hadCore.coreToolZivaAttachmentCreate()
    def clickToolZivaAttachmentSliding(self):
        hadCore.coreToolZivaAttachmentSliding()
    def clickToolZivaAttachmentFixed(self):
        hadCore.coreToolZivaAttachmentFixed()
    def clickToolZivaAttachment02(self):
        hadCore.coreToolZivaAttachment02()
    def clickToolZivaAttachment05(self):
        hadCore.coreToolZivaAttachment05()
    def clickToolZivaAttachment1(self):
        hadCore.coreToolZivaAttachment1()
    def clickToolZivaAttachment2(self):
        hadCore.coreToolZivaAttachment2()
    def clickToolZivaAttachment5(self):
        hadCore.coreToolZivaAttachment5()
    def clickToolZivaAttachment10(self):
        hadCore.coreToolZivaAttachment10()
    def clickToolZivaAttachmentPower1(self):
        hadCore.coreToolZivaAttachmentPower1()
    def clickToolZivaAttachmentPower2(self):
        hadCore.coreToolZivaAttachmentPower2()
    def clickToolZivaAttachmentPower3(self):
        hadCore.coreToolZivaAttachmentPower3()
    def clickToolZivaAttachmentPower4(self):
        hadCore.coreToolZivaAttachmentPower4()
    def clickToolZivaAttachmentPower5(self):
        hadCore.coreToolZivaAttachmentPower5()
    def clickToolZivaAttachmentPower6(self):
        hadCore.coreToolZivaAttachmentPower6()
    def clickToolZivaAttachmentPower7(self):
        hadCore.coreToolZivaAttachmentPower7()
    def clickToolZivaAttachmentPower8(self):
        hadCore.coreToolZivaAttachmentPower8()
    def clickToolZivaAttachmentPower9(self):
        hadCore.coreToolZivaAttachmentPower9()
    def clickToolZivaAttachmentPower10(self):
        hadCore.coreToolZivaAttachmentPower10()
    def clickToolZivaCopy(self):
        hadCore.coreToolZivaCopy()
    def clickToolZivaPaste(self):
        hadCore.coreToolZivaPaste()
    def clickToolZivaMeshStandart(self):
        hadCore.coreToolZivaMeshStandart()
    def clickToolZivaMeshMove(self):
        hadCore.coreToolZivaMeshMove()
    def clickToolZivaMeshInflat(self):
        hadCore.coreToolZivaMeshInFlat()
    def clickToolZivaMeshFlatten(self):
        hadCore.coreToolZivaMeshFlatten()
    def clickToolZivaMeshPinch(self):
        hadCore.coreToolZivaMeshPinch()
    def clickToolZivaMeshSmooth(self):
        hadCore.coreToolZivaMeshSmooth()
    def clickToolZivaMeshFreeze(self):
        hadCore.coreToolZivaMeshFreeze()
    def clickToolZivaMeshUnFreeze(self):
        hadCore.coreToolZivaMeshUnFreeze()
    def clickToolZivaMeshRelax(self):
        hadCore.coreToolZivaMeshRelax()
    def clickToolZivaMeshRemesh(self):
        hadCore.coreToolZivaMeshRemesh()
    def clickToolZivaMeshRetopo(self):
        hadCore.coreToolZivaMeshRetopo()
    def clickToolZivaMeshMirror(self):
        hadCore.coreToolZivaMeshMirror()
    def clickToolZivaMeshTransfer(self):
        hadCore.coreToolZivaMeshTransfer()
    def clickToolZivaPaintTool0(self):
        hadCore.coreToolZivaPaintTool0()
    def clickToolZivaPaintTool05(self):
        hadCore.coreToolZivaPaintTool05()
    def clickToolZivaPaintTool1(self):
        hadCore.coreToolZivaPaintTool1()
    def clickToolZivaPaintToolFlood0(self):
        hadCore.coreToolZivaPaintToolFlood0()
    def clickToolZivaPaintToolFlood1(self):
        hadCore.coreToolZivaPaintToolFlood1()
    def clickToolZivaPaintToolSmooth(self):
        hadCore.coreToolZivaOPaintToolSmooth()
    def clickToolZivaMirrorLR(self):
        hadCore.coreToolZivaMirrorLR()
    def clickToolZivaMirrorRL(self):
        hadCore.coreToolZivaMirrorRL()
    def clickToolZivaRename(self):
        hadCore.coreToolZivaRename()   
    def clickToolZivaActivate(self):
        hadCore.coreToolZivaActivate()
    def clickToolZivaAllActivate(self):
        hadCore.coreToolZivaAllActivate()

def show():
    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
        app = QtWidgets.QApplication.instance()
    win = Hades()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    show()




