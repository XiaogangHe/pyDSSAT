FC  = gfortran 
FFLAGS = -fPIC -w -ffixed-form -fd-lines-as-comments -ffixed-line-length-none
!EFILE = ../DSCSM045.EXE
EFILE = DSCSM045.EXE
.SUFFIXES:	.f90
.f90.o:
	$(FC)$(FFLAGS) -o $@ -c $<

OBJS= \
	ModuleDefs.o \
	OPHEAD.o \
	SoilMixing.o \
	SLigCeres.o \
	OPSUM.o \
	SC_CNG_mods.o \
	Warning.o \
	DATES.o \
	ERROR.o \
	Info.o \
	LMATCH.o \
	READS.o \
	UTILS.o \
	WTHSET.o \
	input_sub.o \
	INSOIL.o \
	INSTGE.o \
	INTRO.o \
	INVAR.o \
	IPCHEM.o \
	IPECO.o \
	IPENV.o \
	ipexp.o \
	IPMAN.o \
	IPSIM.o \
	IPSLIN.o \
	IPSOIL_Inp.o \
	IPTILL.o \
	IPVAR.o \
	OPGEN.o \
	OPTEMPXY2K.o \
	optempy2k.o \
	PATH.o \
	SECLI.o \
	SECROP.o \
	SEFERT.o \
	SEFLD.o \
	SEFREQ.o \
	SEHARV.o \
	SEINIT.o \
	SEIRR.o \
	SENS.o \
	SEPEST.o \
	SEPLT.o \
	SERES.o \
	SESIM.o \
	SESOIL.o \
	SETIME.o \
	SEVAR.o \
	SEWTH.o \
	WEATHR_Inp.o \
	WTHMOD.o \
	ASMDM.o \
	AUTHAR.o \
	AUTPLT.o \
	CANOPY.o \
	CE_RATIO_C.o \
	CENTURY.o \
	CHEMICAL.o \
	CO2VAL.o \
	CROPGRO.o \
	CRSIMDEF.o \
	CSCER040.o \
	CSCERES_Interface.o \
	CSCRP045.o \
	CSCRP_Interface.o \
	CSDIS045.o \
	CSM.o \
	CSP_CANOPY.o \
	CSP_CASUPRO.o \
	CSP_DEMAND.o \
	CSP_GROW.o \
	CSP_GROW_CANE.o \
	CSP_HRes.o \
	CSP_INCOMP.o \
	CSP_INCOMP_OUT.o \
	CSP_INPHENOL.o \
	CSP_IPDMND_OUT.o \
	CSP_IPPHENOL.o \
	CSP_IPPLNT.o \
	CSP_MOBIL.o \
	CSP_NUPTAK.o \
	CSP_OPGROW.o \
	CSP_OPHARV.o \
	CSP_PHENOL.o \
	CSP_PHOTO.o \
	CSP_RESPIR.o \
	CSP_ROOTS.o \
	CSP_SENES.o \
	CSP_VEGGR.o \
	CSREA045.o \
	CSUTS045.o \
	DECRAT_C.o \
	DEMAND.o \
	EFLOW_C.o \
	EQUIL2.o \
	ESR_SoilEvap.o \
	ETPHOT.o \
	ETPHR.o \
	FCHEM.o \
	Fert_Place.o \
	Flood_Chem.o \
	Flood_Irrig.o \
	FLOODI.o \
	FREEZE.o \
	FreshWt.o \
	GROW.o \
	HMET.o \
	HRes_CGRO.o \
	HResCeres.o \
	IMMOBLIMIT_C.o \
	INCOMP.o \
	INCORPOR_C.o \
	INFIL.o \
	IPHedley_C.o \
	IPHedley_inorg.o \
	IPIBS.o \
	IPPARM.o \
	IPPEST.o \
	Ipphenol.o \
	IPPLNT.o \
	IPPROG.o \
	IPSOIL.o \
	IPWTH_alt.o \
	IRRIG.o \
	LAND.o \
	LINDM.o \
	LITDEC_C.o \
	MgmtOps.o \
	ML_CERES.o \
	ML_GROSUB.o \
	ML_NFACT.o \
	ml_NUPTAK.o \
	ML_opharv.o \
	ML_PHASEI.o \
	ML_PHENOL.o \
	ML_rootgr.o \
	ML_TILLSUB.o \
	MOBIL.o \
	MULCHEVAP.o \
	MULCHLAYER.o \
	MULCHWAT.o \
	MZ_CERES.o \
	MZ_GROSUB.o \
	MZ_IX_GROSUB.o \
	MZ_IX_KNUMBER.o \
	MZ_IX_LEAFAREA.o \
	MZ_IX_NUPTAK.o \
	MZ_IX_PHENOL.o \
	MZ_IX_PHOTSYNT.o \
	MZ_IX_PLANTG.o \
	MZ_IX_RADABS.o \
	MZ_IX_RESPIR.o \
	MZ_KUPTAK.o \
	MZ_NFACTO.o \
	MZ_NUPTAK.o \
	MZ_OPGROW.o \
	MZ_OPHARV.o \
	MZ_OPNIT.o \
	MZ_PHENOL.o \
	MZ_ROOTS.o \
	NCHECK_C.o \
	NCHECK_inorg.o \
	NCHECK_organic.o \
	NFIX.o \
	NFLUX.o \
	NUPTAK.o \
	OM_Place.o \
	OPETPHOT.o \
	OpFlood.o \
	OPFLOODN.o \
	Opgrow.o \
	OPHARV.o \
	OPMULCH.o \
	OPPEST.o \
	OpPlantP.o \
	OpSoilKi.o \
	OPSOILNI.o \
	OpSoilOrg.o \
	OpSoilPi.o \
	OPSOMLIT_C.o \
	OpStemp.o \
	OPSTRESS.o \
	OPVIEW.o \
	OPWBAL.o \
	OPWEATH.o \
	OXLAYER.o \
	P_CASUPRO.o \
	P_CERES.o \
	P_CGRO.o \
	P_IPPLNT.o \
	p_plant.o \
	P_Uptake.o \
	Paddy_Mgmt.o \
	PARTIT_C.o \
	PEST.o \
	PESTCP.o \
	PET.o \
	PHENOL.o \
	PHOTO.o \
	plant.o \
	PlantNBal.o \
	PODDET.o \
	PODS.o \
	PPlantSubs.o \
	PT_GROSUB.o \
	PT_NFACTO.o \
	PT_NUPTAK.o \
	PT_OPGROW.o \
	PT_OPHARV.o \
	PT_PHASEI.o \
	PT_PHENOL.o \
	PT_ROOTGR.o \
	PT_SUBSTOR.o \
	PT_THTIME.o \
	RESPIR.o \
	RI_Calcshk.o \
	RI_GNURSE.o \
	RI_Grosub.o \
	RI_Ipcrop.o \
	RI_KUPTAK.o \
	RI_Nfacto.o \
	RI_Nuptak.o \
	RI_Opgrow.o \
	RI_Opharv.o \
	RI_Phenol.o \
	RI_Rootgr.o \
	RI_Tillsub.o \
	RI_Transpl_g.o \
	RI_Transpl_p.o \
	RICE.o \
	RNOFF.o \
	ROOTDM.o \
	ROOTS.o \
	RootSoilVol.o \
	ROOTWU.o \
	RPLACE_C.o \
	RStages.o \
	RunList.o \
	SAL_Stemp.o \
	SATFLO.o \
	SC_CanesimCanopy.o \
	SC_Canop3.o \
	SC_CNGRO.o \
	SC_COEFFS.o \
	SC_OPHARV.o \
	SC_OUTPUT.o \
	SC_PARTIT.o \
	SC_PHENOL.o \
	SC_PHOTOS.o \
	SC_Poplt3.o \
	SC_ROOTG.o \
	SDCOMP.o \
	SEEDDM.o \
	SENES.o \
	SENESADD_C.o \
	SG_CERES.o \
	SG_GROSUB.o \
	SG_NFACT.o \
	sg_NUPTAK.o \
	SG_OPHARV.o \
	SG_PHASEI.o \
	SG_PHENOL.o \
	SG_ROOTGR.o \
	SOIL.o \
	SoilCBal_C.o \
	SoilCNPinit_C.o \
	SOILDYN.o \
	SOILEV.o \
	SoilK_init.o \
	SoilKi.o \
	SoilNBalSum.o \
	SOILNI.o \
	SoilNi_init.o \
	SoilNiBal.o \
	SoilNoBal.o \
	SoilNoBal_C.o \
	SoilNoPoBal.o \
	SoilOrg.o \
	SoilOrg_init.o \
	SoilPBalSum.o \
	SoilPi.o \
	SoilPi_init.o \
	soilpibal.o \
	SoilPoBal.o \
	SoilPoBal_C.o \
	SOLAR.o \
	SOMDEC_C.o \
	SOMFIX_C.o \
	SOMINIT_c.o \
	SOMLITPRINT_C.o \
	SPAM.o \
	SPSUBS.o \
	STEMP.o \
	SW_FreshWt.o \
	SW_GROSUB.o \
	TextureClass.o \
	TILEDRAIN.o \
	Tillage.o \
	TillEvent.o \
	TR_Calcshk.o \
	TR_Grosub.o \
	TR_Ipcrop.o \
	TR_Nfacto.o \
	TR_Nuptak.o \
	TR_OPGROW.o \
	TR_Opharv.o \
	TR_Phenol.o \
	TR_Rootgr.o \
	TR_SUBSTOR.o \
	TR_Tillsub.o \
	TR_Transpl_g.o \
	TR_Transpl_p.o \
	TRANS.o \
	TSOMLIT_C.o \
	VEGDM.o \
	VEGGR.o \
	WATBAL.o \
	WBAL.o \
	WBSUBS.o \
	weathr.o \
	WGEN.o \

# all: $(EFILE)
$ EFILE : $(OBJS)
	$(FC) $(FFLAGS) -o $(EFILE) $(OBJS)

  ModuleDefs.o :           ModuleDefs.f90       
  DATES.o :                DATES.f90            
  ERROR.o :                ERROR.f90            
  Info.o :                 Info.f90             
  LMATCH.o :               LMATCH.f90           
  READS.o :                READS.f90            
  UTILS.o :                UTILS.f90            
  Warning.o :              Warning.f90          
  ASMDM.o :                ASMDM.f90            
  AUTHAR.o :               AUTHAR.f90           
  AUTPLT.o :               AUTPLT.f90           
  CANOPY.o :               CANOPY.f90           
  CE_RATIO_C.o :           CE_RATIO_C.f90       
  CENTURY.o :              CENTURY.f90          
  CHEMICAL.o :             CHEMICAL.f90         
  CO2VAL.o :               CO2VAL.f90           
  CROPGRO.o :              CROPGRO.f90          
  CRSIMDEF.o :             CRSIMDEF.f90         
  CSCER040.o :             CSCER040.f90         
  CSCERES_Interface.o :    CSCERES_Interface.f90
  CSCRP045.o :             CSCRP045.f90         
  CSCRP_Interface.o :      CSCRP_Interface.f90  
  CSDIS045.o :             CSDIS045.f90         
  CSM.o :                  CSM.f90              
  CSP_CANOPY.o :           CSP_CANOPY.f90       
  CSP_CASUPRO.o :          CSP_CASUPRO.f90      
  CSP_DEMAND.o :           CSP_DEMAND.f90       
  CSP_GROW.o :             CSP_GROW.f90         
  CSP_GROW_CANE.o :        CSP_GROW_CANE.f90    
  CSP_HRes.o :             CSP_HRes.f90         
  CSP_INCOMP.o :           CSP_INCOMP.f90       
  CSP_INCOMP_OUT.o :       CSP_INCOMP_OUT.f90   
  CSP_INPHENOL.o :         CSP_INPHENOL.f90     
  CSP_IPDMND_OUT.o :       CSP_IPDMND_OUT.f90   
  CSP_IPPHENOL.o :         CSP_IPPHENOL.f90     
  CSP_IPPLNT.o :           CSP_IPPLNT.f90       
  CSP_MOBIL.o :            CSP_MOBIL.f90        
  CSP_NUPTAK.o :           CSP_NUPTAK.f90       
  CSP_OPGROW.o :           CSP_OPGROW.f90       
  CSP_OPHARV.o :           CSP_OPHARV.f90       
  CSP_PHENOL.o :           CSP_PHENOL.f90       
  CSP_PHOTO.o :            CSP_PHOTO.f90        
  CSP_RESPIR.o :           CSP_RESPIR.f90       
  CSP_ROOTS.o :            CSP_ROOTS.f90        
  CSP_SENES.o :            CSP_SENES.f90        
  CSP_VEGGR.o :            CSP_VEGGR.f90        
  CSREA045.o :             CSREA045.f90         
  CSUTS045.o :             CSUTS045.f90         
  DECRAT_C.o :             DECRAT_C.f90         
  DEMAND.o :               DEMAND.f90           
  EFLOW_C.o :              EFLOW_C.f90          
  EQUIL2.o :               EQUIL2.f90           
  ESR_SoilEvap.o :         ESR_SoilEvap.f90     
  ETPHOT.o :               ETPHOT.f90           
  ETPHR.o :                ETPHR.f90            
  FCHEM.o :                FCHEM.f90            
  Fert_Place.o :           Fert_Place.f90       
  Flood_Chem.o :           Flood_Chem.f90       
  Flood_Irrig.o :          Flood_Irrig.f90      
  FLOODI.o :               FLOODI.f90           
  FREEZE.o :               FREEZE.f90           
  FreshWt.o :              FreshWt.f90          
  GROW.o :                 GROW.f90             
  HMET.o :                 HMET.f90             
  HRes_CGRO.o :            HRes_CGRO.f90        
  HResCeres.o :            HResCeres.f90        
  IMMOBLIMIT_C.o :         IMMOBLIMIT_C.f90     
  INCOMP.o :               INCOMP.f90           
  INCORPOR_C.o :           INCORPOR_C.f90       
  INFIL.o :                INFIL.f90            
  input_sub.o :            input_sub.f90        
  INSOIL.o :               INSOIL.f90           
  INSTGE.o :               INSTGE.f90           
  INTRO.o :                INTRO.f90            
  INVAR.o :                INVAR.f90            
  IPCHEM.o :               IPCHEM.f90           
  IPECO.o :                IPECO.f90            
  IPENV.o :                IPENV.f90            
  ipexp.o :                ipexp.f90            
  IPHedley_C.o :           IPHedley_C.f90       
  IPHedley_inorg.o :       IPHedley_inorg.f90   
  IPIBS.o :                IPIBS.f90            
  IPMAN.o :                IPMAN.f90            
  IPPARM.o :               IPPARM.f90           
  IPPEST.o :               IPPEST.f90           
  Ipphenol.o :             Ipphenol.f90         
  IPPLNT.o :               IPPLNT.f90           
  IPPROG.o :               IPPROG.f90           
  IPSLIN.o :               IPSLIN.f90           
  IPSOIL.o :               IPSOIL.f90           
  IPSOIL_Inp.o :           IPSOIL_Inp.f90       
  IPTILL.o :               IPTILL.f90           
  IPVAR.o :                IPVAR.f90            
  IPWTH_alt.o :            IPWTH_alt.f90        
  IRRIG.o :                IRRIG.f90            
  LAND.o :                 LAND.f90             
  LINDM.o :                LINDM.f90            
  LITDEC_C.o :             LITDEC_C.f90         
  MgmtOps.o :              MgmtOps.f90          
  ML_CERES.o :             ML_CERES.f90         
  ML_GROSUB.o :            ML_GROSUB.f90        
  ML_NFACT.o :             ML_NFACT.f90         
  ml_NUPTAK.o :            ml_NUPTAK.f90        
  ML_opharv.o :            ML_opharv.f90        
  ML_PHASEI.o :            ML_PHASEI.f90        
  ML_PHENOL.o :            ML_PHENOL.f90        
  ML_rootgr.o :            ML_rootgr.f90        
  ML_TILLSUB.o :           ML_TILLSUB.f90       
  MOBIL.o :                MOBIL.f90            
  MULCHEVAP.o :            MULCHEVAP.f90        
  MULCHLAYER.o :           MULCHLAYER.f90       
  MULCHWAT.o :             MULCHWAT.f90         
  MZ_CERES.o :             MZ_CERES.f90         
  MZ_GROSUB.o :            MZ_GROSUB.f90        
  MZ_IX_GROSUB.o :         MZ_IX_GROSUB.f90     
  MZ_IX_KNUMBER.o :        MZ_IX_KNUMBER.f90    
  MZ_IX_LEAFAREA.o :       MZ_IX_LEAFAREA.f90   
  MZ_IX_NUPTAK.o :         MZ_IX_NUPTAK.f90     
  MZ_IX_PHENOL.o :         MZ_IX_PHENOL.f90     
  MZ_IX_PHOTSYNT.o :       MZ_IX_PHOTSYNT.f90   
  MZ_IX_PLANTG.o :         MZ_IX_PLANTG.f90     
  MZ_IX_RADABS.o :         MZ_IX_RADABS.f90     
  MZ_IX_RESPIR.o :         MZ_IX_RESPIR.f90     
  MZ_KUPTAK.o :            MZ_KUPTAK.f90        
  MZ_NFACTO.o :            MZ_NFACTO.f90        
  MZ_NUPTAK.o :            MZ_NUPTAK.f90        
  MZ_OPGROW.o :            MZ_OPGROW.f90        
  MZ_OPHARV.o :            MZ_OPHARV.f90        
  MZ_OPNIT.o :             MZ_OPNIT.f90         
  MZ_PHENOL.o :            MZ_PHENOL.f90        
  MZ_ROOTS.o :             MZ_ROOTS.f90         
  NCHECK_C.o :             NCHECK_C.f90         
  NCHECK_inorg.o :         NCHECK_inorg.f90     
  NCHECK_organic.o :       NCHECK_organic.f90   
  NFIX.o :                 NFIX.f90             
  NFLUX.o :                NFLUX.f90            
  NUPTAK.o :               NUPTAK.f90           
  OM_Place.o :             OM_Place.f90         
  OPETPHOT.o :             OPETPHOT.f90         
  OpFlood.o :              OpFlood.f90          
  OPFLOODN.o :             OPFLOODN.f90         
  OPGEN.o :                OPGEN.f90            
  Opgrow.o :               Opgrow.f90           
  OPHARV.o :               OPHARV.f90           
  OPHEAD.o :               OPHEAD.f90           
  OPMULCH.o :              OPMULCH.f90          
  OPPEST.o :               OPPEST.f90           
  OpPlantP.o :             OpPlantP.f90         
  OpSoilKi.o :             OpSoilKi.f90         
  OPSOILNI.o :             OPSOILNI.f90         
  OpSoilOrg.o :            OpSoilOrg.f90        
  OpSoilPi.o :             OpSoilPi.f90         
  OPSOMLIT_C.o :           OPSOMLIT_C.f90       
  OpStemp.o :              OpStemp.f90          
  OPSTRESS.o :             OPSTRESS.f90         
  OPSUM.o :                OPSUM.f90            
  OPTEMPXY2K.o :           OPTEMPXY2K.f90       
  optempy2k.o :            optempy2k.f90      
  OPVIEW.o :               OPVIEW.f90           
  OPWBAL.o :               OPWBAL.f90           
  OPWEATH.o :              OPWEATH.f90          
  OXLAYER.o :              OXLAYER.f90          
  P_CASUPRO.o :            P_CASUPRO.f90        
  P_CERES.o :              P_CERES.f90          
  P_CGRO.o :               P_CGRO.f90           
  P_IPPLNT.o :             P_IPPLNT.f90         
  p_plant.o :              p_plant.f90          
  P_Uptake.o :             P_Uptake.f90         
  Paddy_Mgmt.o :           Paddy_Mgmt.f90       
  PARTIT_C.o :             PARTIT_C.f90         
  PATH.o :                 PATH.f90             
  PEST.o :                 PEST.f90             
  PESTCP.o :               PESTCP.f90           
  PET.o :                  PET.f90              
  PHENOL.o :               PHENOL.f90           
  PHOTO.o :                PHOTO.f90            
  plant.o :                plant.f90            
  PlantNBal.o :            PlantNBal.f90        
  PODDET.o :               PODDET.f90           
  PODS.o :                 PODS.f90             
  PPlantSubs.o :           PPlantSubs.f90       
  PT_GROSUB.o :            PT_GROSUB.f90        
  PT_NFACTO.o :            PT_NFACTO.f90        
  PT_NUPTAK.o :            PT_NUPTAK.f90        
  PT_OPGROW.o :            PT_OPGROW.f90        
  PT_OPHARV.o :            PT_OPHARV.f90        
  PT_PHASEI.o :            PT_PHASEI.f90        
  PT_PHENOL.o :            PT_PHENOL.f90        
  PT_ROOTGR.o :            PT_ROOTGR.f90        
  PT_SUBSTOR.o :           PT_SUBSTOR.f90       
  PT_THTIME.o :            PT_THTIME.f90        
  RESPIR.o :               RESPIR.f90           
  RI_Calcshk.o :           RI_Calcshk.f90       
  RI_GNURSE.o :            RI_GNURSE.f90        
  RI_Grosub.o :            RI_Grosub.f90        
  RI_Ipcrop.o :            RI_Ipcrop.f90        
  RI_KUPTAK.o :            RI_KUPTAK.f90        
  RI_Nfacto.o :            RI_Nfacto.f90        
  RI_Nuptak.o :            RI_Nuptak.f90        
  RI_Opgrow.o :            RI_Opgrow.f90        
  RI_Opharv.o :            RI_Opharv.f90        
  RI_Phenol.o :            RI_Phenol.f90        
  RI_Rootgr.o :            RI_Rootgr.f90        
  RI_Tillsub.o :           RI_Tillsub.f90       
  RI_Transpl_g.o :         RI_Transpl_g.f90     
  RI_Transpl_p.o :         RI_Transpl_p.f90     
  RICE.o :                 RICE.f90             
  RNOFF.o :                RNOFF.f90            
  ROOTDM.o :               ROOTDM.f90           
  ROOTS.o :                ROOTS.f90            
  RootSoilVol.o :          RootSoilVol.f90      
  ROOTWU.o :               ROOTWU.f90           
  RPLACE_C.o :             RPLACE_C.f90         
  RStages.o :              RStages.f90          
  RunList.o :              RunList.f90          
  SAL_Stemp.o :            SAL_Stemp.f90        
  SATFLO.o :               SATFLO.f90           
  SC_CanesimCanopy.o :     SC_CanesimCanopy.f90 
  SC_Canop3.o :            SC_Canop3.f90        
  SC_CNG_mods.o :          SC_CNG_mods.f90      
  SC_CNGRO.o :             SC_CNGRO.f90         
  SC_COEFFS.o :            SC_COEFFS.f90        
  SC_OPHARV.o :            SC_OPHARV.f90        
  SC_OUTPUT.o :            SC_OUTPUT.f90        
  SC_PARTIT.o :            SC_PARTIT.f90        
  SC_PHENOL.o :            SC_PHENOL.f90        
  SC_PHOTOS.o :            SC_PHOTOS.f90        
  SC_Poplt3.o :            SC_Poplt3.f90        
  SC_ROOTG.o :             SC_ROOTG.f90         
  SDCOMP.o :               SDCOMP.f90           
  SECLI.o :                SECLI.f90            
  SECROP.o :               SECROP.f90           
  SEEDDM.o :               SEEDDM.f90           
  SEFERT.o :               SEFERT.f90           
  SEFLD.o :                SEFLD.f90            
  SEFREQ.o :               SEFREQ.f90           
  SEHARV.o :               SEHARV.f90           
  SEINIT.o :               SEINIT.f90           
  SEIRR.o :                SEIRR.f90            
  SENES.o :                SENES.f90            
  SENESADD_C.o :           SENESADD_C.f90       
  SENS.o :                 SENS.f90             
  SEPEST.o :               SEPEST.f90           
  SEPLT.o :                SEPLT.f90            
  SERES.o :                SERES.f90            
  SESIM.o :                SESIM.f90            
  SESOIL.o :               SESOIL.f90           
  SETIME.o :               SETIME.f90           
  SEVAR.o :                SEVAR.f90            
  SEWTH.o :                SEWTH.f90            
  SG_CERES.o :             SG_CERES.f90         
  SG_GROSUB.o :            SG_GROSUB.f90        
  SG_NFACT.o :             SG_NFACT.f90         
  sg_NUPTAK.o :            sg_NUPTAK.f90        
  SG_OPHARV.o :            SG_OPHARV.f90        
  SG_PHASEI.o :            SG_PHASEI.f90        
  SG_PHENOL.o :            SG_PHENOL.f90        
  SG_ROOTGR.o :            SG_ROOTGR.f90        
  SLigCeres.o :            SLigCeres.f90        
  SOIL.o :                 SOIL.f90             
  SoilCBal_C.o :           SoilCBal_C.f90       
  SoilCNPinit_C.o :        SoilCNPinit_C.f90    
  SOILDYN.o :              SOILDYN.f90          
  SOILEV.o :               SOILEV.f90           
  SoilK_init.o :           SoilK_init.f90       
  SoilKi.o :               SoilKi.f90           
  SoilMixing.o :           SoilMixing.f90       
  SoilNBalSum.o :          SoilNBalSum.f90      
  SOILNI.o :               SOILNI.f90           
  SoilNi_init.o :          SoilNi_init.f90      
  SoilNiBal.o :            SoilNiBal.f90        
  SoilNoBal.o :            SoilNoBal.f90        
  SoilNoBal_C.o :          SoilNoBal_C.f90      
  SoilNoPoBal.o :          SoilNoPoBal.f90      
  SoilOrg.o :              SoilOrg.f90          
  SoilOrg_init.o :         SoilOrg_init.f90     
  SoilPBalSum.o :          SoilPBalSum.f90      
  SoilPi.o :               SoilPi.f90           
  SoilPi_init.o :          SoilPi_init.f90      
  soilpibal.o :            soilpibal.f90        
  SoilPoBal.o :            SoilPoBal.f90        
  SoilPoBal_C.o :          SoilPoBal_C.f90      
  SOLAR.o :                SOLAR.f90            
  SOMDEC_C.o :             SOMDEC_C.f90         
  SOMFIX_C.o :             SOMFIX_C.f90         
  SOMINIT_c.o :            SOMINIT_c.f90        
  SOMLITPRINT_C.o :        SOMLITPRINT_C.f90    
  SPAM.o :                 SPAM.f90             
  SPSUBS.o :               SPSUBS.f90           
  STEMP.o :                STEMP.f90            
  SW_FreshWt.o :           SW_FreshWt.f90       
  SW_GROSUB.o :            SW_GROSUB.f90        
  TextureClass.o :         TextureClass.f90     
  TILEDRAIN.o :            TILEDRAIN.f90        
  Tillage.o :              Tillage.f90          
  TillEvent.o :            TillEvent.f90        
  TR_Calcshk.o :           TR_Calcshk.f90       
  TR_Grosub.o :            TR_Grosub.f90        
  TR_Ipcrop.o :            TR_Ipcrop.f90        
  TR_Nfacto.o :            TR_Nfacto.f90        
  TR_Nuptak.o :            TR_Nuptak.f90        
  TR_OPGROW.o :            TR_OPGROW.f90        
  TR_Opharv.o :            TR_Opharv.f90        
  TR_Phenol.o :            TR_Phenol.f90        
  TR_Rootgr.o :            TR_Rootgr.f90        
  TR_SUBSTOR.o :           TR_SUBSTOR.f90       
  TR_Tillsub.o :           TR_Tillsub.f90       
  TR_Transpl_g.o :         TR_Transpl_g.f90     
  TR_Transpl_p.o :         TR_Transpl_p.f90     
  TRANS.o :                TRANS.f90            
  TSOMLIT_C.o :            TSOMLIT_C.f90        
  VEGDM.o :                VEGDM.f90            
  VEGGR.o :                VEGGR.f90            
  WATBAL.o :               WATBAL.f90           
  WBAL.o :                 WBAL.f90             
  WBSUBS.o :               WBSUBS.f90           
  weathr.o :               weathr.f90           
  WEATHR_Inp.o :           WEATHR_Inp.f90       
  WGEN.o :                 WGEN.f90             
  WTHMOD.o :               WTHMOD.f90           
  WTHSET.o :               WTHSET.f90           

# DO NOT DELETE THIS LINE -- make depend depends on it.
