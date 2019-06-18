import FWCore.ParameterSet.Config as cms

hgcalElectronMVA = cms.EDProducer("HGCalElectronMVAProducer",
    electrons = cms.InputTag("cleanedEcalDrivenGsfElectronsFromMultiCl"),
    usePAT = cms.bool(False),
    externalVariables = cms.PSet(
        ecEnergyEE = cms.InputTag("hgcElectronID:ecEnergyEE"),
        ecEnergyFH = cms.InputTag("hgcElectronID:ecEnergyFH"),
        pcaEig1 = cms.InputTag("hgcElectronID:pcaEig1"),
        pcaEig2 = cms.InputTag("hgcElectronID:pcaEig2"),
        pcaEig3 = cms.InputTag("hgcElectronID:pcaEig3"),
        pcaSig1 = cms.InputTag("hgcElectronID:pcaSig1"),
        pcaSig2 = cms.InputTag("hgcElectronID:pcaSig2"),
        pcaSig3 = cms.InputTag("hgcElectronID:pcaSig3"),
        pcaAxisX = cms.InputTag("hgcElectronID:pcaAxisX"),
        pcaAxisY = cms.InputTag("hgcElectronID:pcaAxisY"),
        pcaAxisZ = cms.InputTag("hgcElectronID:pcaAxisZ"),
        pcaPositionX = cms.InputTag("hgcElectronID:pcaPositionX"),
        pcaPositionY = cms.InputTag("hgcElectronID:pcaPositionY"),
        pcaPositionZ = cms.InputTag("hgcElectronID:pcaPositionZ"),
        sigmaUU = cms.InputTag("hgcElectronID:sigmaUU"),
        sigmaVV = cms.InputTag("hgcElectronID:sigmaVV"),
        nLayers = cms.InputTag("hgcElectronID:nLayers"),
        firstLayer = cms.InputTag("hgcElectronID:firstLayer"),
        lastLayer = cms.InputTag("hgcElectronID:lastLayer"),
        e4oEtot = cms.InputTag("hgcElectronID:e4oEtot"),
        layerEfrac10 = cms.InputTag("hgcElectronID:layerEfrac10"),
        layerEfrac90 = cms.InputTag("hgcElectronID:layerEfrac90"),
        depthCompatibility = cms.InputTag("hgcElectronID:depthCompatibility"),
    ),
    barrelLowPt  = cms.FileInPath("RecoEgamma/Phase2InterimID/data/EIDmva_EB_1020_oldbarreltdrDR01_BDT.weights.xml"),
    barrelHighPt = cms.FileInPath("RecoEgamma/Phase2InterimID/data/EIDmva_EB_20_oldbarreltdrDR01_BDT.weights.xml"),
    endcapLowPt  = cms.FileInPath("RecoEgamma/Phase2InterimID/data/HGCEIDmva_1020_trackepshowernoisolonghgcaltdrV3DR01preselmatch_BDT.weights.xml"),
    endcapHighPt = cms.FileInPath("RecoEgamma/Phase2InterimID/data/HGCEIDmva_20_trackepshowernoisolonghgcaltdrV3DR01preselmatch_BDT.weights.xml"),
)
