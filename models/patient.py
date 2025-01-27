from odoo import models , fields , api 


class HospitalPatient(models.Model):
    _name= 'hospital.patient'
    _inherit=['mail.thread']
    _description = 'Patient Record'

    name = fields.Char(string= 'Name ', required=True ,tracking=True)
    date_of_birth= fields.Date(string='DOB')
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
   
    tag_ids = fields.Many2many('patient.tag','patient_tag_rel','patient_id','tag_id',string='Tags')
