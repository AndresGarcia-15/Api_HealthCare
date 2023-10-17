# Importa las clases de las interfaces y otras dependencias

from crs.TestsLaboratory import TestsLaboratory
from crs.diagnosticimaging import DiagnosticImage
from crs.medicalhistorial import MedicalHistoial

# Define la interfaz HistoryPatients
class HistoryPatients:
    def analysisAggregate(self):
        pass

    def elaborationReports(self):
        pass

    def exchangePatientInformation(self):
        pass

# Define la interfaz Invoicing
class Invoicing:
    pass

# Define la clase HealthcareProvider que implementa todas las interfaces
class HealthcareProvider(HistoryPatients, TestsLaboratory, DiagnosticImage, Invoicing):
    def __init__(self, name, medical_history):
        self.name = name
        self.medical_history = medical_history
        self.test_results = {}
        self.diagnostic_images = []

    def analysisAggregate(self):
        print(f"{self.name} is performing aggregate analysis on patient histories.")

    def elaborationReports(self):
        # Generar un informe médico basado en la información del historial médico
        medical_data = self.medical_history.updatedata()
        print(f"{self.name} is generating an elaboration report for patient {self.medical_history.fullname}:\n{medical_data}")

    def exchangePatientInformation(self):
        print(f"{self.name} is exchanging patient information with other healthcare providers.")

    def getTestResults(self):
        print(f"{self.name} is providing test results to patients.")

    def requestNewTests(self):
        print(f"{self.name} is requesting new laboratory tests for patients.")

    def getDiagnosticImages(self):
        print(f"{self.name} is providing diagnostic images to healthcare professionals.")
        return self.diagnostic_images

    def uploadNewImages(self, image):
        print(f"{self.name} is uploading a new diagnostic image.")
        self.diagnostic_images.append(image)

    def generateInvoice(self):
        print(f"{self.name} is generating invoices for services provided.")