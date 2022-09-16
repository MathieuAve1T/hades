from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui
import hades.hadEnv as hadEnv
import hades.hadCore as hadCore
import sys

'''
#In maya

import sys
sys.path.append(r'C:\Users\MKR\MyProject\pandemonium\src')

import my_utils
my_utils.reload_module('hades')

import hades
reload(hades)

from hades import hadMaster

ui = hadMaster.Hades()
ui.show()


'''

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, text='', parent=None):
        super(MyLineEdit, self).__init__(text, parent)

class MyUi(QtWidgets.QDialog):
    def __init__(self):
        super(MyUi, self).__init__() 
        self.setWindowFlags(self.windowFlags() |QtCore.Qt.WindowStaysOnTopHint)   #pour l'inverse , remplacer | par &~
        self.setWindowTitle('Hades_V.1.0.0')
        self.resize(400, 300)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        print("TODO: Create my widgets")

    def create_layouts(self):
        print("TODO: Create my layouts")

    def create_connections(self):
        print("TODO: Create my connections")

class Hades(MyUi):
    def create_widgets(self):

        #master_tab : 

        self.title_l = QtWidgets.QLabel("By_Mathieu_Karadjia")

        self.autoRig_but = QtWidgets.QPushButton("AutoRig")
        self.autoRig_but.clicked.connect(self.clickAutoRig_But)
        self.autoRig_l = QtWidgets.QLabel("AutoRig basic for biped character")

        self.autoRigSkin_but = QtWidgets.QPushButton("AutoSkin")
        self.autoRigSkin_but.clicked.connect(self.clickAutoRigSkin_But)
        self.autoRigSkin_l = QtWidgets.QLabel("[Coming soon]")

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
        self.autoRigSkinTab = QtWidgets.QWidget()
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

        #autoRigSkin_tab

        self.autoRigSkin_scene_l = QtWidgets.QLabel("Do you want to setup the scene ?")
        self.autoRigSkin_scene_but = QtWidgets.QPushButton("Create BaseMesh")

        #tools_for_Maya

        self.toolMayaH_but = QtWidgets.QPushButton("DeleteHistory")
        self.toolMayaH_but.clicked.connect(self.clickDeleteHistory_But)
        self.toolMayaT_but = QtWidgets.QPushButton("FreezeTransform")
        self.toolMayaT_but.clicked.connect(self.clickFreezeTransform_But) 
        self.toolMayaC_but = QtWidgets.QPushButton("CenterPivot")
        self.toolMayaC_but.clicked.connect(self.clickCenterPivot_But) 
        self.toolMayaCreJnt_but = QtWidgets.QPushButton("Create Joints")
        self.toolMayaCreJnt_but.setStyleSheet("background-color: Purple")
        self.toolMayaCreJnt_but.clicked.connect(self.clickCreateJoints_But) 
        self.toolMayaJntSz_but = QtWidgets.QPushButton("Joint Size")
        self.toolMayaJntSz_but.setStyleSheet("background-color: #E4D64E")
        self.toolMayaJntSz_but.clicked.connect(self.clickJointSize_But) 
        self.toolMayaLRA_but = QtWidgets.QPushButton("Local Rotation Axis")
        self.toolMayaLRA_but.setStyleSheet("background-color: #E4D64E")
        self.toolMayaLRA_but.clicked.connect(self.clickLocalRotationAxis_But) 
        self.toolMayaChaGrp_but = QtWidgets.QPushButton("Character Group")
        self.toolMayaChaGrp_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaChaGrp_but.clicked.connect(self.clickCharacterGroup_But) 
        self.toolMayaMirJnt_but = QtWidgets.QPushButton("Mirror joints")
        self.toolMayaMirJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaMirJnt_but.clicked.connect(self.clickMirrorJoints_But) 
        self.toolMayaOriJnt_but = QtWidgets.QPushButton("Orient Joints")
        self.toolMayaOriJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaOriJnt_but.clicked.connect(self.clickOrientJoints_But) 
        self.toolMayaReOriJnt_but = QtWidgets.QPushButton("ReOrient Last Joint")
        self.toolMayaReOriJnt_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaReOriJnt_but.clicked.connect(self.clickReOrientLastJoint_But) 
        self.toolMayaMirCrv_but = QtWidgets.QPushButton("Mirror Curves")
        self.toolMayaMirCrv_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaMirCrv_but.clicked.connect(self.clickMirrorCurves_But) 
        self.toolMayaParCrv_but = QtWidgets.QPushButton("Parent Curves")
        self.toolMayaParCrv_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaParCrv_but.clicked.connect(self.clickParentCurves_But) 
        self.toolMayaConEdi_but = QtWidgets.QPushButton("Connection Editor")
        self.toolMayaConEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaConEdi_but.clicked.connect(self.clickConnectionEditor_But) 
        self.toolMayaShaEdi_but = QtWidgets.QPushButton("Shape Editor")
        self.toolMayaShaEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaShaEdi_but.clicked.connect(self.clickShapeEditor_But) 
        self.toolMayaDrivK_but = QtWidgets.QPushButton("DrivenKey")
        self.toolMayaDrivK_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaDrivK_but.clicked.connect(self.clickDrivenKey_But) 
        self.toolMayaLoca_but = QtWidgets.QPushButton("Create Locator")
        self.toolMayaLoca_but.setStyleSheet("background-color: green")
        self.toolMayaLoca_but.clicked.connect(self.clickCreateLocator_But) 
        self.toolMayaNodEdi_but = QtWidgets.QPushButton("Node Editor")
        self.toolMayaNodEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaNodEdi_but.clicked.connect(self.clickNodeEditor_But) 
        self.toolMayaCopEdi_but = QtWidgets.QPushButton("Component Editor")
        self.toolMayaCopEdi_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaCopEdi_but.clicked.connect(self.clickComponentEditor_But) 
        self.toolMayaYellow_but = QtWidgets.QPushButton("Color Yellow")
        self.toolMayaYellow_but.setStyleSheet("background-color: #E4D64E")
        self.toolMayaYellow_but.clicked.connect(self.clickColorYellow_But) 
        self.toolMayaRed_but = QtWidgets.QPushButton("Color Red")
        self.toolMayaRed_but.setStyleSheet("background-color: #D33C3C")
        self.toolMayaRed_but.clicked.connect(self.clickColorRed_But) 
        self.toolMayaBlue_but = QtWidgets.QPushButton("Color Blue")
        self.toolMayaBlue_but.setStyleSheet("background-color: #58C6Dc")
        self.toolMayaBlue_but.clicked.connect(self.clickColorBlue_But) 
        self.toolMayaPink_but = QtWidgets.QPushButton("Color Pink")
        self.toolMayaPink_but.setStyleSheet("background-color: pink")
        self.toolMayaPink_but.clicked.connect(self.clickColorPink_But) 
        self.toolMayaGreen_but = QtWidgets.QPushButton("Color Green")
        self.toolMayaGreen_but.setStyleSheet("background-color: green")
        self.toolMayaGreen_but.clicked.connect(self.clickColorGreen_But) 
        self.toolMayaPurple_but = QtWidgets.QPushButton("Color Purple")
        self.toolMayaPurple_but.setStyleSheet("background-color: #E265CB")
        self.toolMayaPurple_but.clicked.connect(self.clickColorPurple_But) 

        #tools_for_Ziva

        self.toolZivaFirst_l = QtWidgets.QLabel("Simulation Component :")
        self.toolZivaPanel_menu = QtWidgets.QMenuBar(self)
        self.toolZivaPanel_bar = self.toolZivaPanel_menu.addMenu("Scene Panel")
        self.toolZivaPanel_open = self.toolZivaPanel_bar.addAction("Open")
        self.toolZivaPanel_open.triggered.connect(self.clickToolZivaPanelOpen)
        self.toolZivaPanel_add = self.toolZivaPanel_bar.addAction("Add Cache")
        self.toolZivaPanel_add.triggered.connect(self.clickToolZivaPanelAddCache)
        self.toolZivaPanel_del = self.toolZivaPanel_bar.addAction("Delete Cache") 
        self.toolZivaPanel_del.triggered.connect(self.clickToolZivaPanelDeleteCache)
        self.toolZivaTissue_menu = QtWidgets.QMenuBar(self)
        self.toolZivaTissue_bar = self.toolZivaTissue_menu.addMenu("zTissue")
        self.toolZivaTissue_create = self.toolZivaTissue_bar.addAction("create zTissue")
        self.toolZivaTissue_create.triggered.connect(self.clickToolZivaTissueCreate)
        self.toolZivaTissue_disaRSide = self.toolZivaTissue_bar.addAction("disable right side")
        self.toolZivaTissue_disaRSide.triggered.connect(self.clickToolZivaTissueDisaRSide)
        self.toolZivaTissue_enaRSide = self.toolZivaTissue_bar.addAction("enable right side")
        self.toolZivaTissue_enaRSide.triggered.connect(self.clickToolZivaTissueEnaRSide)
        self.toolZivaTissue_damping = self.toolZivaTissue_bar.addAction("set damping 1")
        self.toolZivaTissue_damping.triggered.connect(self.clickToolZivaTissueDamping)
        self.toolZivaTet_menu = QtWidgets.QMenuBar(self)
        self.toolZivaTet_bar = self.toolZivaTet_menu.addMenu("zTet")
        self.toolZivaTet_showHide = self.toolZivaTet_bar.addAction("show/hide")
        self.toolZivaTet_showHide.triggered.connect(self.clickToolZivaTetShowHide)
        self.toolZivaTet_x05 = self.toolZivaTet_bar.addAction("x 0.5")
        self.toolZivaTet_x05.triggered.connect(self.clickToolZivaTetX05)
        self.toolZivaTet_x075 = self.toolZivaTet_bar.addAction("x 0.75")
        self.toolZivaTet_x075.triggered.connect(self.clickToolZivaTetX075)
        self.toolZivaTet_09 = self.toolZivaTet_bar.addAction("x 0.9")
        self.toolZivaTet_09.triggered.connect(self.clickToolZivaTetX9)
        self.toolZivaTet_x11 = self.toolZivaTet_bar.addAction("x 1.1")
        self.toolZivaTet_x11.triggered.connect(self.clickToolZivaTetX11)
        self.toolZivaTet_x125 = self.toolZivaTet_bar.addAction("x 1.25")
        self.toolZivaTet_x125.triggered.connect(self.clickToolZivaTetX125)
        self.toolZivaTet_x2 = self.toolZivaTet_bar.addAction("x 2")
        self.toolZivaTet_x2.triggered.connect(self.clickToolZivaTetX2)
        self.toolZivaSecond_l = QtWidgets.QLabel("Tissue Property :")
        self.toolZivaPower_menu = QtWidgets.QMenuBar(self)
        self.toolZivaPower_bar = self.toolZivaPower_menu.addMenu("zMaterial")
        self.toolZivaPower_gelatin = self.toolZivaPower_bar.addAction("Gelatin")  #1.0*10^0
        self.toolZivaPower_gelatin.triggered.connect(self.clickToolZivaMaterialGelatin)
        self.toolZivaPower_brain = self.toolZivaPower_bar.addAction("Brain")  #0.5*10^3
        self.toolZivaPower_brain.triggered.connect(self.clickToolZivaMaterialBrain)
        self.toolZivaPower_liver = self.toolZivaPower_bar.addAction("Liver")  #0.7*10^3
        self.toolZivaPower_liver.triggered.connect(self.clickToolZivaMaterialLiver)
        self.toolZivaPower_breastTissue = self.toolZivaPower_bar.addAction("Breast Tissue")  #0.9*10^3
        self.toolZivaPower_breastTissue.triggered.connect(self.clickToolZivaMaterialBreastTissue)
        self.toolZivaPower_fat = self.toolZivaPower_bar.addAction("Fat")  #3.0*10^3
        self.toolZivaPower_fat.triggered.connect(self.clickToolZivaMaterialFat)
        self.toolZivaPower_smoothMuscle = self.toolZivaPower_bar.addAction("Smooth Muscle")  #5.0*10^3
        self.toolZivaPower_smoothMuscle.triggered.connect(self.clickToolZivaMaterialSmoothMuscle)
        self.toolZivaPower_skeletalMuscle = self.toolZivaPower_bar.addAction("Skeletal Muscle")  #1.2*10^4
        self.toolZivaPower_skeletalMuscle.triggered.connect(self.clickToolZivaMaterialSkeletalMuscle)
        self.toolZivaPower_cartilage = self.toolZivaPower_bar.addAction("Cartilage")  #2.0*10^4
        self.toolZivaPower_cartilage.triggered.connect(self.clickToolZivaMaterialCartilage)
        self.toolZivaPower_rubber = self.toolZivaPower_bar.addAction("Rubber")  #1.0*10^7
        self.toolZivaPower_rubber.triggered.connect(self.clickToolZivaMaterialRubber)
        self.toolZivaPower_wood = self.toolZivaPower_bar.addAction("Wood")  #0.6*10^9
        self.toolZivaPower_wood.triggered.connect(self.clickToolZivaMaterialWood)
        self.toolZivaPower_tendon = self.toolZivaPower_bar.addAction("Tendon")  #1.0*10^9
        self.toolZivaPower_tendon.triggered.connect(self.clickToolZivaMaterialTendon)
        self.toolZivaPower_plastic = self.toolZivaPower_bar.addAction("Plastic")  #1.5*10^9
        self.toolZivaPower_plastic.triggered.connect(self.clickToolZivaMaterialPlastic)
        self.toolZivaPower_bone = self.toolZivaPower_bar.addAction("Bone")  #1.4*10^10
        self.toolZivaPower_bone.triggered.connect(self.clickToolZivaMaterialBone)
        self.toolZivaPower_walnutShell = self.toolZivaPower_bar.addAction("Walnut Shell")  #1.5*10^10
        self.toolZivaPower_walnutShell.triggered.connect(self.clickToolZivaMaterialWalnulShell)
        self.toolZivaPower_steel = self.toolZivaPower_bar.addAction("Steel")  #2.0*10^11
        self.toolZivaPower_steel.triggered.connect(self.clickToolZivaMaterialSteel)
        self.toolZivaPower_diamond = self.toolZivaPower_bar.addAction("Diamond")  #1.0*10^12 
        self.toolZivaPower_diamond.triggered.connect(self.clickToolZivaMaterialDiamond)
        self.toolZivaFiber_menu = QtWidgets.QMenuBar(self)
        self.toolZivaFiber_bar = self.toolZivaFiber_menu.addMenu("zFiber")
        self.toolZivaFiber_create = self.toolZivaFiber_bar.addAction("create zFiber")
        self.toolZivaFiber_create.triggered.connect(self.clickToolZivaFiberCreate)
        self.toolZivaFiber_select = self.toolZivaFiber_bar.addAction("select zFiber")
        self.toolZivaFiber_select.triggered.connect(self.clickToolZivaFiberSelect)
        self.toolZivaLOA_menu = QtWidgets.QMenuBar(self)
        self.toolZivaLOA_bar = self.toolZivaLOA_menu.addMenu("Line-of-Action")
        self.toolZivaLOA_create = self.toolZivaLOA_bar.addAction("create LOA")
        self.toolZivaLOA_create.triggered.connect(self.clickToolZivaLOACreate)
        self.toolZivaLOA_select = self.toolZivaLOA_bar.addAction("select LOA")
        self.toolZivaLOA_select.triggered.connect(self.clickToolZivaLOASelect)
        self.toolZivaLOA_addCrv = self.toolZivaLOA_bar.addAction("add curve to LOA")
        self.toolZivaLOA_addCrv.triggered.connect(self.clickToolZivaLOAAddCrv)
        self.toolZivaBone_menu = QtWidgets.QMenuBar(self)
        self.toolZivaBone_bar = self.toolZivaBone_menu.addMenu("zBone")
        self.toolZivaBone_create = self.toolZivaBone_bar.addAction("create zBone")
        self.toolZivaBone_create.triggered.connect(self.clickToolZivaBoneCreate)
        self.toolZivaPaintAttach_menu = QtWidgets.QMenuBar(self)
        self.toolZivaPaintAttch_bar = self.toolZivaPaintAttach_menu.addMenu("zAttachment")
        self.toolZivaPaintAttch_create = self.toolZivaPaintAttch_bar.addAction("create zattachment")
        self.toolZivaPaintAttch_create.triggered.connect(self.clickToolZivaAttachmentCreate)
        self.toolZivaPaintAttch_select = self.toolZivaPaintAttch_bar.addAction("select zattachment")
        self.toolZivaPaintAttch_select.triggered.connect(self.clickToolZivaAttachmentSelect)
        self.toolZivaPaintAttch_paint = self.toolZivaPaintAttch_bar.addAction("paint zattachment")
        self.toolZivaPaintAttch_paint.triggered.connect(self.clickToolZivaAttachmentPaint)
        self.toolZivaPaintAttch_sliding = self.toolZivaPaintAttch_bar.addAction("set sliding")
        self.toolZivaPaintAttch_sliding.triggered.connect(self.clickToolZivaAttachmentSliding)
        self.toolZivaPaintAttch_fixed = self.toolZivaPaintAttch_bar.addAction("set fixed")
        self.toolZivaPaintAttch_fixed.triggered.connect(self.clickToolZivaAttachmentFixed)
        self.toolZivaPaintAttch_02 = self.toolZivaPaintAttch_bar.addAction("0.2")
        self.toolZivaPaintAttch_02.triggered.connect(self.clickToolZivaAttachment02)
        self.toolZivaPaintAttch_05 = self.toolZivaPaintAttch_bar.addAction("0.5")
        self.toolZivaPaintAttch_05.triggered.connect(self.clickToolZivaAttachment05)
        self.toolZivaPaintAttch_1 = self.toolZivaPaintAttch_bar.addAction("1")
        self.toolZivaPaintAttch_1.triggered.connect(self.clickToolZivaAttachment1)
        self.toolZivaPaintAttch_2 = self.toolZivaPaintAttch_bar.addAction("2")
        self.toolZivaPaintAttch_2.triggered.connect(self.clickToolZivaAttachment2)
        self.toolZivaPaintAttch_5 = self.toolZivaPaintAttch_bar.addAction("5")
        self.toolZivaPaintAttch_5.triggered.connect(self.clickToolZivaAttachment5)
        self.toolZivaPaintAttch_10 = self.toolZivaPaintAttch_bar.addAction("10")
        self.toolZivaPaintAttch_10.triggered.connect(self.clickToolZivaAttachment10)
        self.toolZivaThird_l = QtWidgets.QLabel("Edit Mesh :")
        self.toolZivaCopyPaste_menu = QtWidgets.QMenuBar(self)
        self.toolZivaCopyPaste_bar = self.toolZivaCopyPaste_menu.addMenu("CopyPaste")
        self.toolZivaCopyPaste_copy = self.toolZivaCopyPaste_bar.addAction("Copy")
        self.toolZivaCopyPaste_copy.triggered.connect(self.clickToolZivaCopy)
        self.toolZivaCopyPaste_paste = self.toolZivaCopyPaste_bar.addAction("Paste")
        self.toolZivaCopyPaste_paste.triggered.connect(self.clickToolZivaPaste)
        self.toolZivaMeshSculpt_menu = QtWidgets.QMenuBar(self)
        self.toolZivaMeshSculpt_bar = self.toolZivaMeshSculpt_menu.addMenu("MeshSculpt")
        self.toolZivaMesh_standard = self.toolZivaMeshSculpt_bar.addAction("Standard")
        self.toolZivaMesh_standard.triggered.connect(self.clickToolZivaMeshStandart) 
        self.toolZivaMesh_move = self.toolZivaMeshSculpt_bar.addAction("Move")
        self.toolZivaMesh_move.triggered.connect(self.clickToolZivaMeshMove)
        self.toolZivaMesh_inflat = self.toolZivaMeshSculpt_bar.addAction("Inflat")
        self.toolZivaMesh_inflat.triggered.connect(self.clickToolZivaMeshInflat)
        self.toolZivaMesh_flatten = self.toolZivaMeshSculpt_bar.addAction("Flatten")
        self.toolZivaMesh_flatten.triggered.connect(self.clickToolZivaMeshFlatten)
        self.toolZivaMesh_pinch = self.toolZivaMeshSculpt_bar.addAction("Pinch")
        self.toolZivaMesh_pinch.triggered.connect(self.clickToolZivaMeshPinch)
        self.toolZivaMeshModify_menu = QtWidgets.QMenuBar(self)
        self.toolZivaMeshModify_bar = self.toolZivaMeshModify_menu.addMenu("MeshModify")
        self.toolZivaMesh_smooth = self.toolZivaMeshModify_bar.addAction("Smooth")
        self.toolZivaMesh_smooth.triggered.connect(self.clickToolZivaMeshSmooth)
        self.toolZivaMesh_freeze = self.toolZivaMeshModify_bar.addAction("Freeze")
        self.toolZivaMesh_freeze.triggered.connect(self.clickToolZivaMeshFreeze)
        self.toolZivaMesh_unFreeze = self.toolZivaMeshModify_bar.addAction("UnFreeze")
        self.toolZivaMesh_unFreeze.triggered.connect(self.clickToolZivaMeshUnFreeze)
        self.toolZivaMesh_relax = self.toolZivaMeshModify_bar.addAction("Relax")
        self.toolZivaMesh_relax.triggered.connect(self.clickToolZivaMeshRelax)
        self.toolZivaMesh_remesh = self.toolZivaMeshModify_bar.addAction("Remesh")
        self.toolZivaMesh_remesh.triggered.connect(self.clickToolZivaMeshRemesh)
        self.toolZivaMesh_retopo = self.toolZivaMeshModify_bar.addAction("Retopo")
        self.toolZivaMesh_retopo.triggered.connect(self.clickToolZivaMeshRetopo)
        self.toolZivaMeshMirror_menu = QtWidgets.QMenuBar(self)
        self.toolZivaMeshMirror_bar = self.toolZivaMeshMirror_menu.addMenu("MeshMirror")
        self.toolZivaMesh_mirror = self.toolZivaMeshMirror_bar.addAction("Mirror")
        self.toolZivaMesh_mirror.triggered.connect(self.clickToolZivaMeshMirror)
        self.toolZivaMesh_transfer = self.toolZivaMeshMirror_bar.addAction("Transfer Shape")
        self.toolZivaMesh_transfer.triggered.connect(self.clickToolZivaMeshTransfer)
        self.toolZivaFourth_l = QtWidgets.QLabel("Tools :")
        self.toolZivaPaintTool_menu = QtWidgets.QMenuBar(self)
        self.toolZivaPaintTool_bar = self.toolZivaPaintTool_menu.addMenu("PaintTool")
        self.toolZivaPaintTool_open = self.toolZivaPaintTool_bar.addAction("Open")
        self.toolZivaPaintTool_open.triggered.connect(self.clickToolZivaPaintToolOpen)
        self.toolZivaPaintTool_0 = self.toolZivaPaintTool_bar.addAction("Value 0")
        self.toolZivaPaintTool_0.triggered.connect(self.clickToolZivaPaintTool0)
        self.toolZivaPaintTool_05 = self.toolZivaPaintTool_bar.addAction("Value 0.5")
        self.toolZivaPaintTool_05.triggered.connect(self.clickToolZivaPaintTool05)
        self.toolZivaPaintTool_1 = self.toolZivaPaintTool_bar.addAction("Value 1")
        self.toolZivaPaintTool_1.triggered.connect(self.clickToolZivaPaintTool1)
        self.toolZivaPaintTool_flood0 = self.toolZivaPaintTool_bar.addAction("Flood 0")
        self.toolZivaPaintTool_flood0.triggered.connect(self.clickToolZivaPaintToolFlood0)
        self.toolZivaPaintTool_flood1 = self.toolZivaPaintTool_bar.addAction("Flood 1")
        self.toolZivaPaintTool_flood1.triggered.connect(self.clickToolZivaPaintToolFlood1)
        self.toolZivaPaintTool_smooth = self.toolZivaPaintTool_bar.addAction("Smooth")
        self.toolZivaPaintTool_smooth.triggered.connect(self.clickToolZivaPaintToolSmooth)
        self.toolZivaPaintToolAdd_bar = self.toolZivaPaintTool_bar.addMenu("Add")
        self.toolZivaPaintTool_add001 = self.toolZivaPaintToolAdd_bar.addAction("Value 0.01")
        self.toolZivaPaintTool_add001.triggered.connect(self.clickToolZivaPaintToolAdd001)
        self.toolZivaPaintTool_add01 = self.toolZivaPaintToolAdd_bar.addAction("Value 0.1")
        self.toolZivaPaintTool_add01.triggered.connect(self.clickToolZivaPaintToolAdd01)
        self.toolZivaPaintTool_add02 = self.toolZivaPaintToolAdd_bar.addAction("Value 0.2")
        self.toolZivaPaintTool_add02.triggered.connect(self.clickToolZivaPaintToolAdd02)
        self.toolZivaPaintTool_add05 = self.toolZivaPaintToolAdd_bar.addAction("Value 0.5")
        self.toolZivaPaintTool_add05.triggered.connect(self.clickToolZivaPaintToolAdd05)
        self.toolZivaPaintToolSca_bar = self.toolZivaPaintTool_bar.addMenu("Scale")
        self.toolZivaPaintTool_scale1 = self.toolZivaPaintToolSca_bar.addAction("Value 1")
        self.toolZivaPaintTool_scale1.triggered.connect(self.clickToolZivaPaintToolScale1)
        self.toolZivaPaintTool_scale08 = self.toolZivaPaintToolSca_bar.addAction("Value 0.8")
        self.toolZivaPaintTool_scale08.triggered.connect(self.clickToolZivaPaintToolScale08)
        self.toolZivaPaintTool_06 = self.toolZivaPaintToolSca_bar.addAction("Value 0.6")
        self.toolZivaPaintTool_06.triggered.connect(self.clickToolZivaPaintToolScale06)
        self.toolZivaPaintTool_04 = self.toolZivaPaintToolSca_bar.addAction("Value 0.4")
        self.toolZivaPaintTool_04.triggered.connect(self.clickToolZivaPaintToolScale04)
        self.toolZivaPaintTool_02 = self.toolZivaPaintToolSca_bar.addAction("Value 0.2")
        self.toolZivaPaintTool_02.triggered.connect(self.clickToolZivaPaintToolScale02)
        self.toolZivaPaintTool_0 = self.toolZivaPaintToolSca_bar.addAction("Value 0")
        self.toolZivaPaintTool_0.triggered.connect(self.clickToolZivaPaintToolScale0)
        self.toolZivaMirror_menu = QtWidgets.QMenuBar(self)
        self.toolZivaMirror_bar = self.toolZivaMirror_menu.addMenu("Mirror")
        self.toolZivaMirror_LR = self.toolZivaMirror_bar.addAction("Left to Right")
        self.toolZivaMirror_LR.triggered.connect(self.clickToolZivaMirrorLR)
        self.toolZivaMirror_RL = self.toolZivaMirror_bar.addAction("Right to Left")
        self.toolZivaMirror_RL.triggered.connect(self.clickToolZivaMirrorRL)
        self.toolZivaRename_menu = QtWidgets.QMenuBar(self)
        self.toolZivaRename_bar = self.toolZivaRename_menu.addMenu("zRename")
        self.toolZivaRename_rename = self.toolZivaRename_bar.addAction("rename all Ziva nodes")
        self.toolZivaRename_rename.triggered.connect(self.clickToolZivaRename)
        self.toolZivaActivate_menu = QtWidgets.QMenuBar(self)
        self.toolZivaActivate_bar = self.toolZivaActivate_menu.addMenu("On/Off")
        self.toolZivaActivate_activate = self.toolZivaActivate_bar.addAction("activate zTissue")
        self.toolZivaActivate_activate.triggered.connect(self.clickToolZivaActivate)
        self.toolZivaActivate_desactivate = self.toolZivaActivate_bar.addAction("desactivate zTissue")
        self.toolZivaActivate_desactivate.triggered.connect(self.clickToolZivaDesativate)

        #Create_Ctrls

        self.createCtrlSize_l = QtWidgets.QLabel("Size: ")
        self.createCtrlSize_sb = QtWidgets.QDoubleSpinBox()
        self.createCtrlSize_sb.setValue(1)
        self.createCtrlSize_sb.setMinimum(0.01)
        self.createCtrlSize_sb.setMaximum(10)
        self.createCtrlGrp_chx = QtWidgets.QCheckBox('In group ?')
        self.createCtrlTabCircle_but = QtWidgets.QToolButton()
        self.createCtrlTabCircle_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\circle.jpg'))
        self.createCtrlTabCircle_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabCircle_but.clicked.connect(self.clickCtrlCircle_But)
        self.createCtrlTabTriangle_but = QtWidgets.QToolButton()
        self.createCtrlTabTriangle_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\triangle.jpg'))
        self.createCtrlTabTriangle_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabTriangle_but.clicked.connect(self.clickCtrlTriangle_But)
        self.createCtrlTabSquare_but = QtWidgets.QToolButton()
        self.createCtrlTabSquare_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\square.jpg'))
        self.createCtrlTabSquare_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabSquare_but.clicked.connect(self.clickCtrlSquare_But)
        self.createCtrlTabBox_but = QtWidgets.QToolButton()
        self.createCtrlTabBox_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\box.jpg'))
        self.createCtrlTabBox_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabBox_but.clicked.connect(self.clickCtrlBox_But)
        self.createCtrlTabCross_but = QtWidgets.QToolButton()
        self.createCtrlTabCross_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\cross.jpg'))
        self.createCtrlTabCross_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabCross_but.clicked.connect(self.clickCtrlCross_But)
        self.createCtrlTabBall_but = QtWidgets.QToolButton()
        self.createCtrlTabBall_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\ball.jpg'))
        self.createCtrlTabBall_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabBall_but.clicked.connect(self.clickCtrlBall_But)
        self.createCtrlTabDiamond_but = QtWidgets.QToolButton()
        self.createCtrlTabDiamond_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\diamond.jpg'))
        self.createCtrlTabDiamond_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabDiamond_but.clicked.connect(self.clickCtrlDiamond_But)
        self.createCtrlTabArrow_but = QtWidgets.QToolButton()
        self.createCtrlTabArrow_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\arrow.jpg'))
        self.createCtrlTabArrow_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabArrow_but.clicked.connect(self.clickCtrlArrow_But)
        self.createCtrlTabLocator_but = QtWidgets.QToolButton()
        self.createCtrlTabLocator_but.setIcon(QtGui.QIcon(r'C:\Users\MKR\MyProject\pandemonium\src\hades\images\locator.jpg'))
        self.createCtrlTabLocator_but.setIconSize(QtCore.QSize(100,100))
        self.createCtrlTabLocator_but.clicked.connect(self.clickCtrlLocator_But)
       

    def create_layouts(self):
        
        #master_tab : 

        title_lay = QtWidgets.QHBoxLayout()
        title_lay.addWidget(self.title_l)
        
        self.autoRig_layout = QtWidgets.QVBoxLayout()
        self.autoRig_layout.addWidget(self.autoRig_but)
        self.autoRig_layout.addWidget(self.autoRig_l)

        autoRigSkin_layout = QtWidgets.QVBoxLayout() 
        autoRigSkin_layout.addWidget(self.autoRigSkin_but)
        autoRigSkin_layout.addWidget(self.autoRigSkin_l)

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
        master_layout.addLayout(self.autoRig_layout)
        master_layout.addLayout(autoRigSkin_layout)
        master_layout.addLayout(toolMaya_layout)
        master_layout.addLayout(createCrv_layout)
        master_layout.addLayout(toolZiva_layout)

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

        #autoRigSkin_tab

        self.autoRigSkin_layout = QtWidgets.QVBoxLayout(self.autoRigSkinTab)
        self.autoRigSkin_layout.addWidget(self.autoRigSkin_scene_l)
        self.autoRigSkin_layout.addWidget(self.autoRigSkin_scene_but)


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
        self.toolZivaTab_layout.addWidget(self.toolZivaPanel_menu, 1, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaTissue_menu, 1, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaTet_menu, 1, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaBone_menu, 1, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaSecond_l, 2, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPower_menu, 3, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaFiber_menu, 3, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaLOA_menu, 3, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintAttach_menu, 3, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaThird_l, 4, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaCopyPaste_menu, 5, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshSculpt_menu, 5, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshModify_menu, 5, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaMeshMirror_menu, 5, 3)
        self.toolZivaTab_layout.addWidget(self.toolZivaFourth_l, 6, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintTool_menu, 7, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaMirror_menu, 7, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaRename_menu, 7, 2)
        self.toolZivaTab_layout.addWidget(self.toolZivaActivate_menu, 7, 3)




        main_lay = QtWidgets.QVBoxLayout(self)
        main_lay.addLayout(title_lay)
        main_lay.addWidget(self.tabMaster)  

    def create_connections(self):
        self.tabMaster.currentChanged.connect(self.tabChanged)

    #tab connection

    def tabChanged(self):
        if self.tabMaster.currentIndex() == 0:
            self.tabMaster.removeTab(1)
        else:
            pass
        self.resize(400, 300)

    def clickAutoRig_But(self):

        self.tabMaster.addTab(self.autoRigTab,'AutoRig')
        self.tabMaster.setCurrentIndex(1)

    def clickAutoRigSkin_But(self):
        self.tabMaster.addTab(self.autoRigSkinTab,'AutoRigSkin')
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
        hadEnv.AUTORIGARM = self.autoRig_arm_chk.isChecked()
        hadEnv.AUTORIGLEG = self.autoRig_leg_chk.isChecked()
        hadEnv.AUTORIGCHEST = self.autoRig_chest_chk.isChecked()
        hadEnv.AUTORIGHEAD = self.autoRig_head_chk.isChecked()
        hadCore.coreAutoRigGuide()

    def clickAutoRigGenerator_But(self):
        hadEnv.AUTORIGSTRETCH = self.autoRig_stretch_chk.isChecked()
        hadEnv.AUTORIGMIRROR = self.autoRig_mirror_chk.isChecked()
        hadCore.coreAutoRigGenerator()

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
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateCircle() 
    def clickCtrlTriangle_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateTriangle() 
    def clickCtrlSquare_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateSquare() 
    def clickCtrlCross_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateCross() 
    def clickCtrlBox_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateBox() 
    def clickCtrlDiamond_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateDiamond() 
    def clickCtrlBall_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateBall() 
    def clickCtrlArrow_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
        hadCore.coreCreateArrow() 
    def clickCtrlLocator_But(self):
        hadEnv.CTRLSIZEVALUE = self.createCtrlSize_sb.value()
        hadEnv.CTRLGRPVALUE = self.createCtrlGrp_chx.isChecked()
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
    def clickToolZivaAttachmentSelect(self):
        hadCore.coreToolZivaAttachmentSelect()
    def clickToolZivaAttachmentPaint(self):
        hadCore.coreToolZivaAttachmentPaint()
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
    def clickToolZivaPaintToolOpen(self):
        hadCore.coreToolZivaPaintToolOpen()
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
        hadCore.coreToolZivaPanelOpen()
    def clickToolZivaPaintToolAdd001(self):
        hadCore.coreToolZivaPaintToolAdd001()
    def clickToolZivaPaintToolAdd01(self):
        hadCore.coreToolZivaPaintToolAdd01()
    def clickToolZivaPaintToolAdd02(self):
        hadCore.coreToolZivaPaintToolAdd02()
    def clickToolZivaPaintToolAdd05(self):
        hadCore.coreToolZivaPaintToolAdd05()
    def clickToolZivaPaintToolScale1(self):
        hadCore.coreToolZivaPaintToolScale1()
    def clickToolZivaPaintToolScale08(self):
        hadCore.coreToolZivaPaintToolScale08()
    def clickToolZivaPaintToolScale06(self):
        hadCore.coreToolZivaPaintToolScale06()
    def clickToolZivaPaintToolScale04(self):
        hadCore.coreToolZivaPaintToolScale04()
    def clickToolZivaPaintToolScale02(self):
        hadCore.coreToolZivaPaintToolScale02()    
    def clickToolZivaPaintToolScale0(self):
        hadCore.coreToolZivaPaintToolScale0()
    def clickToolZivaMirrorLR(self):
        hadCore.coreToolZivaMirrorLR()
    def clickToolZivaMirrorRL(self):
        hadCore.coreToolZivaMirrorRL()
    def clickToolZivaRename(self):
        hadCore.coreToolZivaRename()   
    def clickToolZivaActivate(self):
        hadCore.coreToolZivaActivate()
    def clickToolZivaDesativate(self):
        hadCore.coreToolZivaDesativate()




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


