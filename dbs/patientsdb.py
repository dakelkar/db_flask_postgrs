import sys
import pymongo
from schema_forms import models
from datetime import datetime


class PatientsDb(object):
    # This class wraps the DB access for patients
    key = "folder_number"
    ###########################3
    # Patient_Info def

    def from_patient_bio_info_info(self, patient):
        return {
            self.key: patient.folder_number,
            "mr_number": patient.mr_number,
            "name": patient.name,
            "aadhaar_card": patient.aadhaar_card,
            "date_first": datetime.combine(patient.date_first, datetime.min.time()),
            "permanent_address": patient.permanent_address,
            "current_address": patient.current_address,
            "phone": patient.phone,
            "email_id": patient.email_id,
            "gender": patient.gender,
            "age_yrs": patient.age_yrs,
            "age_diagnosis":patient.age_diagnosis,
            "date_of_birth": datetime.combine(patient.date_of_birth, datetime.min.time()),
            "place_birth":  patient.place_birth,
            "height_cm": patient.height_cm,
            "weight_kg": patient.weight_kg,
            "form_status":patient.form_status,
            "last_update":datetime.combine(patient.last_update, datetime.min.time())
        }

    def to_patient_bio_info_info(self, p):
        patient_bio_info_info = models.Patient_bio_info_Info(folder_number=p[self.key], mr_number=p['mr_number'],
                                          name=p['name'], aadhaar_card=p['aadhaar_card'], date_first=p['date_first'].date(),
                                          permanent_address=p['permanent_address'],
                                          current_address=p['current_address'], phone=p['phone'],
                                          email_id=p['email_id'], gender=p['gender'], age_yrs=p['age_yrs'],
                                          age_diagnosis=p['age_diagnosis'],date_of_birth=p['date_of_birth'].date(),
                                          place_birth=p['place_birth'], height_cm=p['height_cm'],
                                          weight_kg=p['weight_kg'], form_status=p['form_status'],
                                          last_update=p['last_update'].date())
        return patient_bio_info_info

    def __init__(self, logger):
        # Setup logging
        self.log = logger
        self.db = None

    def connect(self):
        # Connect to database
        try:
            client = pymongo.MongoClient("localhost", 27017)
            self.db = client.patients
            self.log.get_logger().info("Connection to patients database opened.")
        except:
            self.log.get_logger().error("Error connecting to database patients: %s", sys.exc_info())

    def get_patients(self):
        """
        :returns list of models.Patient_bio_info_Info
        """
        # try:
        patients = self.db.patients.find()
        return [self.to_patient_bio_info_info(p) for p in patients]
        # except:
        #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())
        #     return

    def get_patient(self, folder_number):
         # try:
        patient_entry = self.db.patients.find_one({ self.key: folder_number })
        patient = self.to_patient_bio_info_info(patient_entry)
        return patient
         # except:
         #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())
         #    return

    def add_patient(self, patient):
        """
        adds a patient to the db
        :param models.Patient_bio_info_Info patient: the patient to insert
        """
        #try:
        patient_entry = self.from_patient_bio_info_info(patient)
        self.db.patients.insert_one(patient_entry)
        return True, None
        # except:
        #     self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
        #     return False, sys.exc_info()

    def update_patient(self, patient):
        """
        :param models.PatientForm patient: model to update from
        """
        try:
            self.db.patients.update_one({self.key: patient.folder_number },
                                        { "$set": self.from_patient_bio_info_info(patient)})
            return True, None
        except:
            self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
            return False, sys.exc_info()

    def delete_patient(self, folder_number):
        #try:
        self.db.patients.delete_one({self.key: folder_number})
        return True, None
        # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()


    ###########################3
    # Mammography def

    def from_mammography_info(self, mammography):
        return {self.key: mammography.folder_number, 'mammo_location': mammography.mammo_location,
        'mammo_details': mammography.mammo_details, 'mammo_date': datetime.combine(mammography.mammo_date,
                                                                                   datetime.min.time()),
        'mammo_accesion': mammography.mammo_accesion, 'mammo_number': mammography.mammo_number,
        'mammo_report_previous':mammography.mammo_report_previous, 'mammo_breast_density':
        mammography.mammo_breast_density, 'mammo_mass_present':mammography.mammo_mass_present,
        'mammo_mass_number':mammography.mammo_mass_number, 'mammo_mass_location_right_breast':
        mammography.mammo_mass_location_right_breast, 'mammo_mass_location_left_breast':
        mammography.mammo_mass_location_left_breast,'mammo_mass_depth': mammography.mammo_mass_depth,
        'mammo_mass_dist' : mammography.mammo_mass_dist, 'mammo_mass_pect': mammography.mammo_mass_pect,
        'mammo_mass_shape': mammography.mammo_mass_shape,'mammo_mass_margin': mammography.mammo_mass_margin,
        'mammo_mass_density': mammography.mammo_mass_density, 'mammo_calcification_present':
         mammography.mammo_calcification_present, 'mammo_calc_number': mammography.mammo_calc_number,
        'mammo_calc_location_right_breast': mammography.mammo_calc_location_right_breast,
        'mammo_calc_location_left_breast': mammography.mammo_calc_location_left_breast,
        'mammo_calc_depth': mammography.mammo_calc_depth, 'mammo_calc_dist': mammography.mammo_calc_dist,
        'mammo_calcification_type': mammography.mammo_calcification_type,
        'mammo_calcification_diagnosis': mammography.mammo_calcification_diagnosis,
        'mammo_arch_present': mammography.mammo_arch_present,
        'mammo_arch_location_right_breast': mammography.mammo_arch_location_right_breast,
        'mammo_arch_location_left_breast': mammography.mammo_arch_location_left_breast,
        'mammo_arch_depth': mammography.mammo_arch_depth, 'mammo_arch_dist': mammography.mammo_arch_dist,
        'mammo_assym_present': mammography.mammo_assym_present,
        'mammo_assym_location_right_breast': mammography.mammo_assym_location_right_breast,
        'mammo_assym_location_left_breast': mammography.mammo_assym_location_left_breast,
        'mammo_assym_depth': mammography.mammo_assym_depth,
        'mammo_assym_type_right_breast': mammography.mammo_assym_type_right_breast,
        'mammo_assym_type_left_breast': mammography.mammo_assym_type_left_breast,
        'mammo_intra_mammary_lymph_nodes_present': mammography.mammo_intra_mammary_lymph_nodes_present,
        'mammo_intra_mammary_lymph_nodes_description': mammography.mammo_intra_mammary_lymph_nodes_description,
        'mammo_lesion': mammography.mammo_lesion, 'mammo_lesion_right_breast': mammography.mammo_lesion_right_breast,
        'mammo_lesion_left_breast': mammography.mammo_lesion_left_breast,
        'mammo_asso_feature_skin_retraction': mammography.mammo_asso_feature_skin_retraction,
        'mammo_asso_feature_nipple_retraction': mammography.mammo_asso_feature_nipple_retraction,
        'mammo_asso_feature_skin_thickening': mammography.mammo_asso_feature_skin_thickening,
        'mammo_asso_feature_trabecular_thickening' : mammography.mammo_asso_feature_trabecular_thickening,
        'mammo_asso_feature_axillary_adenopathy': mammography.mammo_asso_feature_axillary_adenopathy,
        'mammo_asso_feature_architectural_distortion': mammography.mammo_asso_feature_architectural_distortion,
        'mammo_asso_feature_calicifications': mammography.mammo_asso_feature_calicifications,
        'mammo_birad': mammography.mammo_birad}

    def to_mammography_info(self, p):
         mammography = models.MammographyInfo(folder_number=p[self.key], mammo_location=p['mammo_location'],
             mammo_details=p['mammo_details'], mammo_date=p['mammo_date'].date(),
             mammo_accesion=p['mammo_accesion'], mammo_number=p['mammo_number'],
             mammo_report_previous=p['mammo_report_previous'],mammo_breast_density=p['mammo_breast_density'],
             mammo_mass_present=p['mammo_mass_present'],mammo_mass_number=p['mammo_mass_number'],
             mammo_mass_location_right_breast=p['mammo_mass_location_right_breast'],
             mammo_mass_location_left_breast=p['mammo_mass_location_left_breast'],
             mammo_mass_depth=p['mammo_mass_depth'],mammo_mass_dist=p['mammo_mass_dist'],
             mammo_mass_pect=p['mammo_mass_pect'],mammo_mass_shape=p['mammo_mass_shape'],
             mammo_mass_margin=p['mammo_mass_margin'], mammo_mass_density=p['mammo_mass_density'],
             mammo_calcification_present=p['mammo_calcification_present'], mammo_calc_number=p['mammo_calc_number'],
             mammo_calc_location_right_breast=p['mammo_calc_location_right_breast'], mammo_calc_location_left_breast
             =p['mammo_calc_location_left_breast'], mammo_calc_depth=p['mammo_calc_depth'],mammo_calc_dist=
             p['mammo_calc_dist'], mammo_calcification_type=p['mammo_calcification_type'],
             mammo_calcification_diagnosis=p['mammo_calcification_diagnosis'], mammo_arch_present=
             p['mammo_arch_present'],mammo_arch_location_right_breast=p['mammo_arch_location_right_breast'],
             mammo_arch_location_left_breast=p['mammo_arch_location_left_breast'], mammo_arch_depth=
             p['mammo_arch_depth'],mammo_arch_dist=p['mammo_arch_dist'],mammo_assym_present=p['mammo_assym_present'],
             mammo_assym_location_right_breast=p['mammo_assym_location_right_breast'],
             mammo_assym_location_left_breast=p['mammo_assym_location_left_breast'],
             mammo_assym_depth=p['mammo_assym_depth'], mammo_assym_type_right_breast=p['mammo_assym_type_right_breast'],
             mammo_assym_type_left_breast=p['mammo_assym_type_left_breast'],
             mammo_intra_mammary_lymph_nodes_present=p['mammo_intra_mammary_lymph_nodes_present'],
             mammo_intra_mammary_lymph_nodes_description=p['mammo_intra_mammary_lymph_nodes_description'],
             mammo_lesion=p['mammo_lesion'],mammo_lesion_right_breast=p['mammo_lesion_right_breast'],
             mammo_lesion_left_breast=p['mammo_lesion_left_breast'],mammo_asso_feature_skin_retraction=p[
             'mammo_asso_feature_skin_retraction'],mammo_asso_feature_nipple_retraction=p[
             'mammo_asso_feature_nipple_retraction'], mammo_asso_feature_skin_thickening=
              p['mammo_asso_feature_skin_thickening'], mammo_asso_feature_trabecular_thickening=p[
             'mammo_asso_feature_trabecular_thickening'], mammo_asso_feature_axillary_adenopathy=p[
             'mammo_asso_feature_axillary_adenopathy'], mammo_asso_feature_architectural_distortion=p[
             'mammo_asso_feature_architectural_distortion'], mammo_asso_feature_calicifications=p[
             'mammo_asso_feature_calicifications'], mammo_birad=p['mammo_birad'])
         return mammography

    def get_mammographies(self):
        """
        :returns list of models.
        """
        # try:
        mammographies = self.db.mammographies.find()
        return [self.to_mammography_info(p) for p in mammographies]  # except:  #     self.log.get_logger().error("Error retrieving patients from database: %s", sys.exc_info())  #     return

    def get_mammography(self, folder_number):
        # try:
        mammography_entry = self.db.mammographies.find_one({self.key: folder_number})
        if mammography_entry is None:
            return None

        mammography = self.to_mammography_info(mammography_entry)
        return mammography
        # except:  #    self.log.get_logger().error("Error retrieving patient %s from database: %s", folder_number, sys.exc_info())  #    return

    def add_mammography(self, mammography):
        """
        adds a mammography to the db
        :param models.MammographyInfo mammography: the mammography to insert
        """
        # try:
        mammography_entry = self.from_mammography_info(mammography)
        self.db.mammographies.insert_one(mammography_entry)
        return True, None
        # except:
        #     self.log.get_logger().error("Error adding event to database: %s", sys.exc_info())
        #     return False, sys.exc_info()

    def update_mammography(self, mammography):
        """
        :param models.MammographyInfo mammography: model to update from
        """
        # try:
        self.db.mammographies.update_one({self.key: mammography.folder_number}, {"$set": self.from_mammography_info
        (mammography)})
        return True, None
        # except:
        #    self.log.get_logger().error("Error updating event to database: %s", sys.exc_info())
        #   return False, sys.exc_info()

    def delete_mammography(self, folder_number):
        # try:
        self.db.mammographies.delete_one({self.key: folder_number})
        return True, None
        # except:
        #     self.log.get_logger().error("Error deleting patient %s from database: %s", folder_number, sys.exc_info())
        #     return False, sys.exc_info()

    #################################