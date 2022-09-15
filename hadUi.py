from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui
from hades import hadCore
from hades import hadEnv
import sys

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

        self.autoRigFFXIV_but = QtWidgets.QPushButton("AutoRig_for_FF14")
        self.autoRigFFXIV_but.clicked.connect(self.clickAutoRigFFXIV_But)
        self.autoRigFFXIV_l = QtWidgets.QLabel("AutoRig for FF14 character, check FFXIV TexTools")

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
        self.autoRigFFXIVTab = QtWidgets.QWidget()
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

        #auto_rig_FFXIV_tab

        self.autoRigFFXIV_scene_l = QtWidgets.QLabel("Do you want to setup the scene ?")
        self.autoRigFFXIV_scene_chk = QtWidgets.QCheckBox()
        self.autoRigFFXIV_tail_l = QtWidgets.QLabel("Does your character have a tail")
        self.autoRigFFXIV_tail_chk = QtWidgets.QCheckBox()
        self.autoRigFFXIV_scale_l = QtWidgets.QLabel("Do you want to fix the scale ?")
        self.autoRigFFXIV_scale_chk = QtWidgets.QCheckBox()
        self.autoRigFFXIV_createRig_l = QtWidgets.QLabel("Create the Ctrls for the joints")
        self.autoRigFFXIV_createRig_but = QtWidgets.QPushButton("Create Rig")

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

        self.toolZivaRename_but = QtWidgets.QPushButton("ZRename")
        self.toolZivaPaintAttach_but = QtWidgets.QPushButton("PaintAttachment")

        self.toolZivaPaintAttachMin_sb = QtWidgets.QDoubleSpinBox()
        self.toolZivaPaintAttachMin_sb.setValue(0.1)
        self.toolZivaPaintAttachMin_sb.setMinimum(0)
        self.toolZivaPaintAttachMin_sb.setMaximum(10)
        self.toolZivaPaintAttachMin_sb.setSingleStep(0.1)

        self.toolZivaPaintAttachMax_sb = QtWidgets.QDoubleSpinBox()
        self.toolZivaPaintAttachMax_sb.setValue(0.5)
        self.toolZivaPaintAttachMax_sb.setMinimum(0)
        self.toolZivaPaintAttachMax_sb.setMaximum(10)
        self.toolZivaPaintAttachMax_sb.setSingleStep(0.1)

        self.toolZivaPaintTool_but = QtWidgets.QPushButton("PaintTool")
        #self.toolZivaPaintTool_but = QtWidgets.QPushButton("PaintTool")



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

        autoRigFFXIV_layout = QtWidgets.QVBoxLayout()
        autoRigFFXIV_layout.addWidget(self.autoRigFFXIV_but)
        autoRigFFXIV_layout.addWidget(self.autoRigFFXIV_l)    

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
        master_layout.addLayout(autoRigFFXIV_layout)
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

        #auto_rig_FFXIV_tab

        self.autoRigFFXIVTab_layout = QtWidgets.QVBoxLayout(self.autoRigFFXIVTab)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_scene_l)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_scene_chk)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_tail_l)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_tail_chk)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_scale_l)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_scale_chk)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_createRig_l)
        self.autoRigFFXIVTab_layout.addWidget(self.autoRigFFXIV_createRig_but)

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
        self.toolZivaTab_layout.addWidget(self.toolZivaRename_but, 0, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintTool_but, 0, 1)


        self.toolZivaTab_layout.addWidget(self.toolZivaPaintAttach_but, 1, 0)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintAttachMin_sb, 1, 1)
        self.toolZivaTab_layout.addWidget(self.toolZivaPaintAttachMax_sb, 1, 2)

        #self.toolZivaTab_layout.addWidget()
        #self.toolZivaTab_layout.addWidget()
        #self.toolZivaTab_layout.addWidget()
        #self.toolZivaTab_layout.addWidget()
        #self.toolZivaTab_layout.addWidget()
        #self.toolZivaTab_layout.addWidget()








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

    def clickAutoRigFFXIV_But(self):
        self.tabMaster.addTab(self.autoRigFFXIVTab,'AutoRigFF14')
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
