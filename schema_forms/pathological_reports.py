from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, TextAreaField, FormField
from wtforms.fields.html5 import DateField
from db_dict.biopsy import BiopsyDict
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.common_dict import CommonDict
from datetime import date

tbd = "To be filled"

class SurgeryBlockForm(BaseForm):
    fld_surgery_block_id = StringField("Surgical Block ID", default=tbd)
    fld_surgery_no_of_blocks = IntegerField("Number of blocks", default=tbd)
    fld_surgery_block_source = SelectField("Mention the laboratory from where the reports have been generated",
                                           choices=BiopsyDict.biopsy_block_source_choice)  # use same dict as biopsy
    fld_surgery_block_source_other = StringField("other")
    fld_nact_or_naht = SelectField("is NACT or NAHT done", choices=BiopsyDict.nact_naht_choice)
    fld_nact_or_naht_other = StringField("Give details")
    fld_surgery_tumour_block_reference = TextAreaField("Tumour block reference", default=tbd)
    fld_surgery_nodes_block_reference = TextAreaField("Nodes block reference", default=tbd)
    fld_surgery_adjacent_normal_block_reference = TextAreaField("Adjacent Normal block reference", default=tbd)
    fld_surgery_reduction_tissue_block_reference = TextAreaField("Reduction Tissue block reference", default=tbd)
    fld_surgery_date = DateField("Date of Surgery")
    fld_surgery_name_surgeon_id = StringField("Name of Surgeon", default='Dr. Koppiker')
    fld_surgery_hospital_id = StringField("Hospital ID", default=tbd)
    fld_reason_for_biopsy = StringField("Reason for biopsy", default=tbd)
    fld_surger_lesion_side = SelectField("Lesion Side", choices=CommonDict.breast_choice)
    fld_surger_lesion_side_other = StringField("Other")
    fld_surgery_right_breast_type = SelectField("Type of Surgery for Right Breast",
                                                choices=BiopsyDict.surgery_type_choice)
    fld_surgery_right_breast_type_other = StringField("Other")
    fld_surgery_left_breast_type = SelectField("Type of Surgery for Left Breast",
                                               choices=BiopsyDict.surgery_type_choice)
    fld_surgery_left_breast_type_other = StringField("Other")
    fld_surgery_tumour_size = StringField("Tumour size", default=tbd)
    fld_surgery_tumour_size_unit = StringField('Unit for tumour size', default='cm')
    fld_surgery_tumour_grade = SelectField("Tumour Grade", choices=BiopsyDict.tumour_grade_choice)
    fld_surgery_tumour_grade_other = StringField("Other")
    fld_surgery_surgery_diagnosis = SelectField("Surgery Diagnosis", choices=BiopsyDict.surgery_diagnosis_choice)
    fld_surgery_surgery_diagnosis_other = StringField("Other")
    fld_diagnosis_comment = StringField("Include descriptive or indicative notes here and not in Diagnosis")
    fld_surgery_block_DCIS_percent = StringField("mention the DCIS percent")
    fld_surgery_perineural_invasion = SelectField("Perineural Invasion", choices=CommonDict.absent_present_choice)
    fld_surgery_perineural_invasion_other = StringField("Other")
    fld_surgery_necrosis = SelectField("Necrosis", choices=CommonDict.absent_present_choice)
    fld_surgery_necrosis_other = StringField("Other")
    fld_surgery_block_report_lymphovascular_invasion = SelectField("Is lymphovascular invasion seen?",
                                                                   choices=BiopsyDict.lymphovascular_invasion_choice)
    fld_surgery_er = SelectField("Surgical block ER Status", choices=CommonDict.postive_negative_choice)
    fld_surgery_er_other = StringField("Other")
    fld_surgery_er_percent = StringField("ER Percent", default="0")
    fld_surgery_pr = SelectField("Surgical block PR Status", choices=CommonDict.postive_negative_choice)
    fld_surgery_pr_other = StringField("Other")
    fld_surgery_pr_percent = StringField("PR Percent", default="0")
    fld_surgery_her2 = SelectField("Surgical block HER2 Status", choices=BiopsyDict.tumour_her2_choice)
    fld_surgery_her2_other = StringField("Other")
    fld_surgery_her2_grade = StringField("HER2 Grade", default="0")
    fld_surgery_fish = SelectField("Tumour block FISH", choices=CommonDict.postive_negative_choice)
    fld_surgery_ki67 = StringField("Ki67 Percent", default="0")
    fld_surgery_block_report_sentinel_node_number_removed = IntegerField("if sentinel nodes are removed,"
                                                                         "enter the number of nodes removed", default=tbd)
    fld_surgery_block_report_sentinel_node_number_removed_other = StringField("NA")
    fld_surgery_block_report_sentinel_node_number_positive = IntegerField("if sentinel nodes are removed,"
                                                                         "enter the number of nodes positive", default=tbd)
    fld_surgery_block_report_sentinel_node_number_positive_other = StringField("NA")
    fld_surgery_block_report_axillary_node_number_positive = IntegerField("if axillary nodes are removed,"
                                                                         "enter the number of nodes positive", default=tbd)
    fld_surgery_block_report_axillary_node_number_positive_other = StringField("NA")
    fld_surgery_block_report_apical_node_number_positive = IntegerField("if apical nodes are removed,"
                                                                          "enter the number of nodes positive",
                                                                          default=tbd)
    fld_surgery_block_report_apical_node_number_positive_other = StringField("NA")
    fld_node_block_report_perinodal_spread = SelectField("Block Report Perinodal spread", choices=BiopsyDict.lymphovascular_invasion_choice)
    fld_node_block_report_perinodal_spread_other = StringField("Requires follow-up")
    fld_pathological_staging_pt = SelectField("Pathological staging pT",choices=BiopsyDict.pathological_staging_pt_choice)
    fld_pathological_staging_pt_other = StringField("other")
    fld_pathological_staging_pn = SelectField("Pathological staging pN",choices=BiopsyDict.pathological_staging_pt_choice)
    fld_pathological_staging_pn_other = StringField("other")
    fld_pathological_staging_m = SelectField("Pathological staging M",choices=BiopsyDict.pathological_staging_m_choice)
    fld_pathological_staging_m_other = StringField("other")
    fld_pathological_staging_p_stage = SelectField("Pathological staging p",choices=BiopsyDict.pathological_staging_p_stage_choice)
    fld_additional_comments = StringField("Additional comments",default=tbd)
    fld_stromal_tumour_infiltrating_lymphocytes = StringField("Stromal Tumor infiltrating lymphocytes",default=tbd)
    fld_tumour_desmoplastic_response = StringField("Tumor desmoplastic response",default=tbd)


class BiopsyForm (SectionForm):
    def get_summary(self):
        return self.fld_biopsy_tumour_diagnosis.data


    fld_block_serial_number_biopsy = StringField('Block Serial Number', [validators.Length(min=1, max=50)],default=tbd)
    fld_block_location_biopsy = StringField("Block Location ID (Cabinet No.-Drawer No.-Column No.-Front/Back",
                                            default='To be Filled')
    fld_block_current_location_biopsy = StringField("Current location of block",default=tbd)
    fld_reason_for_biopsy = SelectField("Reason for biopsy", choices=BiopsyDict.biopsy_reason_choice)
    fld_reason_for_biopsy_other = StringField("Give details")

    fld_biopsy_site = SelectField("Site of biopsy", choices=BiopsyDict.biopsy_site_choice)
    fld_biopsy_site_other = StringField("Other")
    fld_biopsy_custody_pccm = SelectField('Is the biopsy report in PCCM custody?',
                                          choices=BiopsyDict.biopsy_custody_pccm_choice)#is this the cjoice as mentioned or yes/no?
    fld_biopsy_custody_pccm_other = StringField("Other")
    fld_block_received_pccm_date = DateField("Date when block was placed in the cabinet", default=date.today())
    fld_biopsy_ihc_report_pccm = SelectField("Biopsy IHC report in PCCM custody", choices=CommonDict.yes_no_choice)
    fld_biopsy_block_id = StringField("Biopsy Block ID", default=tbd)#major doubt
    fld_biopsy_block_id_other = StringField("other")
    fld_biopsy_no_of_blocks = IntegerField("Number of blocks",default=tbd)
    fld_biopsy_date = DateField("Date of Biopsy", default=date.today())
    fld_biopsy_block_source = SelectField("Reports have been generated from", choices=BiopsyDict.biopsy_block_source_choice)
    fld_biopsy_block_source_other = StringField("Give details")
    fld_biopsy_lab_id_sid = StringField("Biopsy Lab ID",default=tbd)
    fld_biopsy_type = SelectField("Biopsy Type", choices=BiopsyDict.biopsy_type_choice)
    fld_biopsy_type_other = StringField("Other")
    fld_biopsy_diagnosis = TextAreaField('Mention the diagnosis in its fullform.'
                                         ' Eg: Infiltrating Duct Carcinoma/Invasive Mammary Carcinoma/ DCIS/Fibroadenoma; '
                                         'Infiltrating Duct Carcinoma + DCIS',default=tbd)
    fld_biopsy_diagnosis_comment = StringField("Include descriptive or indicative notes here and not in Diagnosis",default=tbd)
    fld_biopsy_tumour_grade = SelectField("Tumour Grade", choices=BiopsyDict.tumour_grade_choice)
    fld_biopsy_tumour_grade_other = StringField("Give details")
    fld_biopsy_lymphovascular_emboli = SelectField('Are Lymphovascular emboli seen?',
                                                   choices=BiopsyDict.lymphovascular_emboli_choice)
    fld_biopsy_lymphovascular_emboli_other = StringField("Other")
    fld_dcis_biopsy = SelectField("Does the biopsy show DCIS", choices=BiopsyDict.dcis_biopsy_choice)
    fld_dcis_biopsy_other = StringField("Other")
    fld_tumour_er_biopsy = SelectField("Biopsy block ER Status", choices=BiopsyDict.tumour_er_choice)
    fld_tumour_er_biopsy_other = StringField("Other")
    fld_tumour_er_percent_biopsy = StringField("ER Percent",default=tbd)
    fld_tumour_pr_biopsy = SelectField("Biopsy block PR Status", choices=BiopsyDict.tumour_pr_choice)
    fld_tumour_pr_biopsy_other = StringField("Other")
    fld_tumour_pr_percent_biopsy = StringField("PR Percent",default=tbd)
    fld_tumour_her2_biopsy = SelectField("Biopsy block HER2 Status", choices=BiopsyDict.tumour_her2_choice)
    fld_tumour_her2_biopsy_other = StringField("Other")
    fld_tumour_her2_grade_biopsy = StringField("HER2 Grade", default=tbd)
    fld_tumor_biopsy_fish = SelectField("Tumor biopsy FISH", choices=BiopsyDict.tumor_biopsy_fish_choice)
    fld_tumor_biopsy_fish_other = StringField("Other")
    fld_tumour_ki67_biopsy = StringField("Ki67 Percent", default=tbd)
    fld_fnac = SelectField("Lymph Node biopsy FNAC", choices=BiopsyDict.fnac_choice)
    fld_fnac_other = StringField("Other")
    fld_fnac_location = SelectField("FNAC Location", choices=BiopsyDict.fnac_location_choice)
    fld_fnac_location_other = StringField("Other")
    fld_fnac_diagnosis = SelectField("FNAC Diagnosis", choices=BiopsyDict.fnac_diagnosis_choice)
    fld_fnac_diagnosis_other = StringField("Other")
    fld_surgery_form_present = SelectField("Is surgery performed?",
                                                        choices=CommonDict.yes_no_choice)
    surgery_form = FormField(SurgeryBlockForm)
    submit_button = SubmitField('Submit Form')


















