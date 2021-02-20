import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QFileDialog)

import icons_rc

import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui 
import webbrowser

# Change all plots:
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Load the main UI:
        uic.loadUi('gui.ui', self)
        
        # Connect buttons:
        self.btn_calculate.clicked.connect(self.calculate)
        self.btn_reset.clicked.connect(self.reset)
        self.rbtn_kmA_PFR_sp.toggled.connect(self.rdn_PFRsp_kmA)
        self.rbtn_kmAe_PFR_sp.toggled.connect(self.rdn_PFRsp_kmAe)
        self.rbtn_kmA_PFR_br.toggled.connect(self.rdn_PFRbr_kmA)
        self.rbtn_kmAe_PFR_br.toggled.connect(self.rdn_PFRbr_kmAe)
        
        # Connect menus:
        self.actionCalculate.triggered.connect(self.calculate)
        self.actionReset.triggered.connect(self.reset)
        self.actionSave.triggered.connect(self.save)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(lambda:self.open_About())
        
    def open_About(self):
        self.about_diag = About_dialog()
        self.about_diag.exec_()
    
    def rdn_PFRsp_kmA(self):
        rdBtn = self.sender()
        if rdBtn.isChecked():
            self.boxPFRsp_kmA.setEnabled(True)
            self.boxPFRsp_kmAe.setEnabled(False)
            
    def rdn_PFRsp_kmAe(self):
        rdBtn = self.sender()
        if rdBtn.isChecked():
            self.boxPFRsp_kmA.setEnabled(False)
            self.boxPFRsp_kmAe.setEnabled(True)
            
    def rdn_PFRbr_kmA(self):
        rdBtn = self.sender()
        if rdBtn.isChecked():
            self.boxPFRbr_kmA.setEnabled(True)
            self.boxPFRbr_kmAe.setEnabled(False)
            
    def rdn_PFRbr_kmAe(self):
        rdBtn = self.sender()
        if rdBtn.isChecked():
            self.boxPFRbr_kmA.setEnabled(False)
            self.boxPFRbr_kmAe.setEnabled(True)
    
    def save(self):
        if self.tabWidget.currentIndex() == 0:
            B = self.boxReactor_B.text() # cm
            S = self.boxReactor_S.text() # cm
            L = self.boxReactor_L.text() # cm
            eps = self.boxReactor_eps.text() 
            QA_input = self.boxReactor_QA.text() # cm3/s
            Qv_input = self.boxReactor_Qv.text() # cm3/s
            v_input = self.boxReactor_v.text() # cm/s
            AG = self.lblReactor_AG.text()
            AX = self.lblReactor_AX.text()
            de = self.lblReactor_de.text()
            VR = self.lblReactor_VR.text()
            VE = self.lblReactor_VE.text()
            v = self.lblReactor_v.text()
            Q = self.lblReactor_Q.text()
            QA = self.lblReactor_QA.text()
            h1 = "Data generated from Proton Flux v1.0\nFor more info visit https://oliverrdz.xyz/proton-flux\n\n"
            h2 = "Reactor parameters:\n"
            h3 = "B = "+B+" cm\nS = "+S+" cm\nL = "+L+" cm\neps = "+eps+"\nQA = "+QA_input+" cm3/s\nQv = "+Qv_input+" cm3/s\nv = "+v_input+" cm/s\n\n"
            h4 = "Results:\n"
            h5 = "AG = "+AG+" cm2\nAX = "+AX+" cm2\nde = "+de+" cm\nVR = "+VR+" cm3\nVE = "+VE+" cm3\nv = "+v+" cm/s\nQ = "+Q+" cm3/s\nQA = "+QA+" cm/s"
            data = np.array([])
            
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save data","fileName.txt","Text Files (*.txt)", options=options)
            if fileName:
                np.savetxt(fileName, data, header=h1+h2+h3+h4+h5)
        elif self.tabWidget.currentIndex() == 1:
            kmA = self.boxPFRsp_kmA.text()
            kmAe = self.boxPFRsp_kmAe.text()
            Qv = self.boxPFRsp_Qv.text()
            VR = self.boxPFRsp_VR.text()
            VE = self.boxPFRsp_VE.text()
            VT = self.boxPFRsp_VT.text()
            Cin = self.boxPFRsp_Cin.text()
            Cout = self.lblPFRsp_Cout.text()
            XA = self.lblPFRsp_XA.text()
            tauR = self.lblPFRsp_tauR.text()
            tauT = self.lblPFRsp_tauT.text()
            h1 = "Data generated from Proton Flux v1.0\nFor more info visit https://oliverrdz.xyz/proton-flux\n\n"
            h2 = "PFR Single pass parameters:\n"
            h3 = "kmA = "+kmA+" cm3/s\nkmAe = "+kmAe+" 1/s\nQv = "+Qv+" cm3/s\nVR = "+VR+" cm3\nVE = "+VE+" cm3\nVT = "+VT+" cm3\nCin = "+Cin+" mol/dm3\n\n"
            h4 = "Results:\n"
            h5 = "Cout = "+Cout+" mol/dm3\nXA = "+XA+"\ntauR = "+tauR+" s\ntauT = "+tauT+" s"
            data = np.array([])
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save data","fileName.txt","Text Files (*.txt)", options=options)
            if fileName:
                np.savetxt(fileName, data, header=h1+h2+h3+h4+h5)
            
        else:
            kmA = self.boxPFRbr_kmA.text()
            kmAe = self.boxPFRbr_kmAe.text()
            Qv = self.boxPFRbr_Qv.text()
            VE = self.boxPFRbr_VE.text()
            VR = self.boxPFRbr_VR.text()
            VT = self.boxPFRbr_VT.text()
            Cin0 = self.boxPFRbr_Cin0.text()
            
            XA = self.lblPFRbr_XA.text()
            tauR = self.lblPFRbr_tauR.text()
            tauT = self.lblPFRbr_tauT.text()
            
            h1 = "Data generated from Proton Flux v1.0\nFor more info visit https://oliverrdz.xyz/proton-flux\n\n"
            h2 = "PFR in Batch Recirculation parameters:\n"
            h3 = "kmA = "+kmA+" cm3/s\nkmAe = "+kmAe+" 1/s\nQv = "+Qv+" cm3/s\nVR = "+VR+" cm3\nVE = "+VE+" cm3\nVT = "+VT+" cm3\nCin0 = "+Cin0+" mol/dm3\n\n"
            h4 = "Results:\n"
            h5 = "XA = "+XA+"\ntauR = "+tauR+" s\ntauT = "+tauT+" s\n\n"
            h6 = "Time [s], X, Cin [mol/dm3]"
            data = np.array([self.t, self.X, self.Cin])
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save data","fileName.txt","Text Files (*.txt)", options=options)
            if fileName:
                np.savetxt(fileName, data, header=h1+h2+h3+h4+h5+h6)
            
            
            
    def calculate(self):
        if self.tabWidget.currentIndex() == 0:
            self.tabName = "Reactor"
            self.reactor()
        elif self.tabWidget.currentIndex() == 1:
            self.tabName = "PFR_SP"
            self.pfr_sp()
        else:
            self.tabName = "PFR_BR"
            self.pfr_br()
            
        self.actionSave.setEnabled(True)
    	
    def reset(self):
        if self.tabWidget.currentIndex() == 0:
            self.boxReactor_B.setText("0")
            self.boxReactor_S.setText("0")
            self.boxReactor_L.setText("0")
            self.boxReactor_eps.setText("0")
            self.boxReactor_QA.setText("0")
            self.boxReactor_Qv.setText("0")
            self.boxReactor_v.setText("0")
            self.lblReactor_AG.setText("0")
            self.lblReactor_AX.setText("0")
            self.lblReactor_de.setText("0")
            self.lblReactor_VR.setText("0")
            self.lblReactor_VE.setText("0")
            self.lblReactor_v.setText("0")
            self.lblReactor_Q.setText("0")
            self.lblReactor_QA.setText("0")
        elif self.tabWidget.currentIndex() == 1:
            self.boxPFRsp_kmAe.setText("0")
            self.boxPFRsp_kmA.setText("0")
            self.boxPFRsp_Qv.setText("0")
            self.boxPFRsp_VR.setText("0")
            self.boxPFRsp_VE.setText("0")
            self.boxPFRsp_VT.setText("0")
            self.boxPFRsp_Cin.setText("0")
            self.lblPFRsp_Cout.setText("0")
            self.lblPFRsp_XA.setText("0")
            self.lblPFRsp_tauR.setText("0")
            self.lblPFRsp_tauT.setText("0") 
        else:
            self.boxPFRbr_kmA.setText("0") 
            self.boxPFRbr_kmAe.setText("0") 
            self.boxPFRbr_Qv.setText("0") 
            self.boxPFRbr_VR.setText("0") 
            self.boxPFRbr_VE.setText("0")
            self.boxPFRbr_VT.setText("0") 
            self.boxPFRbr_Cin0.setText("0")
            self.lblPFRbr_XA.setText("0")
            self.lblPFRbr_tauR.setText("0")
            self.lblPFRbr_tauT.setText("0")

    def reactor(self):
        # User inputs:
        B = float(self.boxReactor_B.text()) # cm, breadth
        S = float(self.boxReactor_S.text()) # cm, thickness
        L = float(self.boxReactor_L.text()) # cm, length
        eps = float(self.boxReactor_eps.text()) 
        QA_input = float(self.boxReactor_QA.text()) # cm3/s, volumetric flow rate, corrected
        Qv_input = float(self.boxReactor_Qv.text()) # cm3/s, volumetric flow rate, corrected
        v_input = float(self.boxReactor_v.text()) # cm/s, mean linear velocity, eps corrected
        # Calculations:
        AG = B*L # cm2, projected surface area
        AX = B*S # cm2, cross-sectional area of channel
        de = 2*AX/(B+S) # cm, equivalent hydraulic diameter
        VR = B*S*L # cm3, volume of electrode channel
        VE = eps*B*S*L # cm3, volume of electrolyte in channel
        v = Qv_input/(eps*AX)# cm/s, mean linear velocity, corrected
        Q = v_input*eps*AX # cm3/s, volumetric flow rate, eps corrected
        QA = QA_input/AG
        # Sending to GUI
        self.lblReactor_AG.setText("{:.2f}".format(AG))
        self.lblReactor_AX.setText("{:.2f}".format(AX))
        self.lblReactor_de.setText("{:.2f}".format(de))
        self.lblReactor_VR.setText("{:.2f}".format(VR))
        self.lblReactor_VE.setText("{:.2f}".format(VE))
        self.lblReactor_v.setText("{:.2f}".format(v))
        self.lblReactor_Q.setText("{:.2f}".format(Q))
        self.lblReactor_QA.setText("{:.2f}".format(QA))
        
    def pfr_sp(self):
        # User inputs:
        kmA = float(self.boxPFRsp_kmA.text())
        kmAe = float(self.boxPFRsp_kmAe.text())
        Qv = float(self.boxPFRsp_Qv.text())
        VR = float(self.boxPFRsp_VR.text())
        VE = float(self.boxPFRsp_VE.text())
        VT = float(self.boxPFRsp_VT.text())
        Cin = float(self.boxPFRsp_Cin.text())
        # Calculations:
        Cout = Cin*np.exp(-kmAe*VR/Qv)
        tauR = VE/Qv
        tauT = VT/Qv
        if self.rbtn_kmAe_PFR_sp.isChecked():
            XA = 1 - np.exp(-kmAe*VR/Qv)
        else:
            XA = 1 - np.exp(-kmA/Qv)
        
        # Sending to GUI:
        self.lblPFRsp_Cout.setText("{:.3f}".format(Cout))
        self.lblPFRsp_XA.setText("{:.4f}".format(XA))
        self.lblPFRsp_tauR.setText("{:.2f}".format(tauR))
        self.lblPFRsp_tauT.setText("{:.2f}".format(tauT))
        
    def pfr_br(self):
        # User inputs:
        kmA = float(self.boxPFRbr_kmA.text())
        kmAe = float(self.boxPFRbr_kmAe.text())
        Qv = float(self.boxPFRbr_Qv.text())
        VE = float(self.boxPFRbr_VE.text())
        VR = float(self.boxPFRbr_VR.text())
        VT = float(self.boxPFRbr_VT.text())
        Cin0 = float(self.boxPFRbr_Cin0.text())
        # Calculations:
        tauR = VE/Qv
        tauT = VT/Qv
        if self.rbtn_kmAe_PFR_br.isChecked():
            XA = 1 - np.exp(-kmAe*VR/Qv)
            tMax = -np.log(0.0001)*tauT/(1- np.exp(-kmAe*VR/Qv))
            self.t = np.linspace(0, tMax, 1000)
            self.X = 1 - np.exp(-(self.t/tauT)*(1 - np.exp(-kmAe*VR/Qv)))
            
        else:
            XA = 1 - np.exp(-kmA/Qv)
            tMax = -np.log(0.0001)*tauT/(1- np.exp(-kmAe*VR/Qv))
            self.t = np.linspace(0, tMax, 1000)
            self.X = 1 - np.exp(-(self.t/tauT)*(1 - np.exp(-kmA/Qv)))
        self.Cin = Cin0*np.exp(-(self.t/tauT)*(1 - np.exp(-kmAe*VR/Qv)))
        # Sending to GUI:
        self.lblPFRbr_XA.setText("{:.4f}".format(XA))
        self.lblPFRbr_tauR.setText("{:.2f}".format(tauR))
        self.lblPFRbr_tauT.setText("{:.2f}".format(tauT))
        # Plots:
        plt1 = pg.plot()
        plt1.showGrid(x=True, y=True)
        plt1.setLabel('left', 'X<sub>BR, t</sub><sup>PFR</sup>')
        plt1.setLabel('bottom', 't', units='s')
        plt1.plot(self.t, self.X, pen=pg.mkPen('k', width=3), clear=True)
        
        plt2 = pg.plot()
        plt2.showGrid(x=True, y=True)
        plt2.setLabel('left', 'C<sub>in</sub>', units='M')
        plt2.setLabel('bottom', 't', units='s')
        plt2.plot(self.t, self.Cin*1e3, pen=pg.mkPen('k', width=3), clear=True)
        
        
class About_dialog(QtWidgets.QDialog):
    def __init__(self):
        super(About_dialog, self).__init__()
        uic.loadUi("gui_about.ui", self)

        self.btn_webpage.clicked.connect(lambda: webbrowser.open('https://oliverrdz.xyz/proton-flux'))



######################################################################################
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()

