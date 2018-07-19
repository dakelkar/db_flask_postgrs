from flask_wtf import FlaskForm
from db_dict.common_dict import CommonDict
from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from db_dict.surgery_block import SurgeryDict
from schema_forms.form_utilities import BaseForm, SectionForm


class SurgeryForm (SectionForm):
    def get_summary(self):
        return self.fld_surgery_tumour_grade.data

    fld_consent_stat_biopsy = SelectField('Has consent been taken from patient?', choices=SurgeryDict.consent_stat_choice)
    fld_consent_form_biopsy = SelectField('Is consent form with signature present in file ?',
                                         choices=SurgeryDict.consent_form_choice)
    fld_surgery_block_serial_number = StringField('Block Serial Number', [validators.Length(min=1, max=5)])
    fld_surgery_block_location = StringField("Block Location ID (Cabinet No.-Drawer No.-Column No.-Front/Back")
    fld_surgery_block_current_location = StringField("What is the current location of block?")
    fld_surgery_block_id = StringField("Surgical Block ID")
    fld_surgery_block_number = IntegerField("Number of blocks")
    fld_surgery_path_lab_source = StringField("Pathology Lab source of blocks")
    fld_surgery_tumour_block_reference = StringField("Tumour block reference")
    fld_surgery_nodes_block_reference = StringField("Nodes block reference")
    fld_surgery_adjacent_normal_block_reference = StringField("Adjacent Normal block reference")
    fld_surgery_reduction_tissue_block_reference = StringField("Reduction Tissue block reference")
    fld_surgery_date = DateField("Date of Surgery")
    fld_surgery_name_surgeon_id = StringField("Name of Surgeon", default = 'Dr. Koppiker')
    fld_surgery_hospital_id = StringField("Hospital ID")
    fld_surger_lesion_side = SelectField("Lesion Side", CommonDict.breast_choice)
    fld_surger_lesion_side_other = StringField("Other")
    fld_surgery_right_breast_type = SelectField("Type of Surgery", choices=SurgeryDict.surgery_type_choice)
    fld_surgery_right_breast_type_other = StringField("Other")
    fld_surgery_left_breast_type = SelectField("Type of Surgery", choices=SurgeryDict.surgery_type_choice)
    fld_surgery_left_breast_type_other = StringField("Other")
    fld_surgery_tumour_size = StringField("Tumour size")
    fld_surgery_tumour_grade = SelectField("Tumour Grade",choices=SurgeryDict.tumour_grade_choice)
    fld_surgery_tumour_grade_other = StringField("Other")
    fld_surgery_surgery_diagnosis = SelectField("Surgery Diagnosis", choices=SurgeryDict.surgery_diagnosis_choice)
    fld_surgery_surgery_diagnosis_other = StringField("Other")
    fld_surgery_tumour_percent = StringField("Percent DCIS")
    fld_surgery_dcis_invasion = SelectField("DCIS Invasion", choices=SurgeryDict.dcis_choice)
    fld_surgery_dcis_invasion_other = StringField("Other")
    fld_surgery_perineural_invasion = SelectField("Perineural Invasion",choices=CommonDict.absent_present_choice)
    fld_surgery_perineural_invasion_other = StringField("Other")
    fld_surgery_necrosis = SelectField("Necrosis", choices=CommonDict.absent_present_choice)
    fld_surgery_necrosis_other = StringField("Other")
    fld_surgery_percent_vascular_invasion = StringField("Percent Vascular invasion")
    fld_surgery_percent_lymphocyte_invasion = StringField("Percent Lymphocyte invasion")
    fld_surgery_margin = SelectField("Margins", choices=SurgeryDict.margin_choice)
    fld_surgery_margin_other = StringField("Other")
    fld_surgery_percent_stroma = StringField("Percent Stroma")
    fld_surgery_er_percent = StringField("ER Percent")
    fld_surgery_pr_percent = StringField("PR Percent")
    fld_surgery_her2_grade = StringField("HER2 Grade", default="0")
    fld_surgery_ki67 = StringField("Ki67 Percent", default="0")
    fld_surgery_er = SelectField("ER Status", choices=CommonDict.postive_negative_dict)
    fld_surgery_er_other = StringField("Other")
    fld_surgery_pr = SelectField("PR Status", choices=CommonDict.postive_negative_dict)
    fld_surgery_pr_other = StringField("Other")
    fld_surgery_her2 = SelectField("HER2 Status", choices=SurgeryDict.tumour_her2_choice)
    fld_surgery_her2_other = StringField("Other")

    fld_surgery_sentinel_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_sentinel_node_status_other = StringField('Other')
    fld_surgery_sentinel_node_removed = IntegerField("Number of sentinel node removed", default=0)
    fld_surgery_sentinel_node_positive = IntegerField("Number of sentinel node positive", default=0)
    fld_surgery_axillary_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_axillary_node_status_other = StringField('Other')
    fld_surgery_axillary_node_removed = IntegerField("Number of axillary node removed", default=0)
    fld_surgery_axillary_node_positive = IntegerField("Number of axillary node positive", default=0)
    fld_surgery_axillary_node_number = HiddenField()
    fld_surgery_apical_node_status = SelectField("Status of node", choices=CommonDict.postive_negative_dict)
    fld_surgery_apical_node_status_other = StringField('Other')
    fld_surgery_apical_node_removed = IntegerField("Number of apical node removed", default=0)
    fld_surgery_apical_node_positive = IntegerField("Number of apical node positive", default=0)
    fld_surgery_perinodal_spread = SelectField("Perinodal Spread", choices=CommonDict.absent_present_choice)
    fld_surgery_perinodal_spread_other = StringField('Other')
    fld_surgery_supraclavicular_node_involvement = SelectField("Supraclavicular Node Involvment",
                                                               choices=CommonDict.absent_present_choice)
    fld_surgery_supraclavicular_node_involvement_other = StringField('Other')
    fld_surgery_pt_status = SelectField("pT status", choices=SurgeryDict.pt_status_choice)
    fld_surgery_pt_status_other = StringField('Other')
    fld_surgery_pn_status = SelectField("pN status", choices=SurgeryDict.pn_status_choice)
    fld_surgery_pn_status_other = StringField('Other')
    fld_surgery_pm_status = SelectField("pM status", choices=SurgeryDict.pm_status_choice)
    fld_surgery_pm_status_other = StringField('Other')
    fld_surgery_clinical_stage = SelectField("Select Clinical Stage based on TNM status "
                                             "(https://emedicine.medscape.com/article/2007112-overview)",
                                             choices=SurgeryDict.clinical_stage_choice)
    submit_button = SubmitField('Submit Form')