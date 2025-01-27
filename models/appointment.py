from odoo import models , fields , api 


class HospitalAppointment(models.Model):
    _name= 'hospital.appointment'
    _inherit=['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name='patient_id'
    _rec_name_search = ['patient_id','reference']


    reference = fields.Char (string="Reference", default="New")
    patient_id=fields.Many2one('hospital.patient',string ="Patient")
    date_appointment= fields.Date(string='Date')
    note = fields.Text(string="Note ")
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('ongoing','Ongoing'),
        ('done','Done'),
        ('cancel','Cancelled')
    ],default='draft'
    )
    appointment_line_ids= fields.One2many('hospital.appointment.line','appointment_id',string='Lines')
    total_compute_qty= fields.Float(compute='_compute_total_qty',string='Total Qty',store=True)
    date_of_birth= fields.Date(string='DOB', related='patient_id.date_of_birth',store=True)
    
    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference']=self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
    
    @api.depends('appointment_line_ids','appointment_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_compute_qty =sum (rec.appointment_line_ids.mapped('qty'))
    
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.reference} - {rec.patient_id.name}"


    def action_confirm(self):
        for rec in self:
            rec.state='confirm'
    def action_ongoing(self):
        for rec in self:
            rec.state='ongoing'
    def action_cancel(self):
        for rec in self:
            rec.state='cancel'

    def action_done(self):
        for rec in self:
            rec.state='done'

class HospitalAppointmentLine(models.Model):
    _name= 'hospital.appointment.line'
    _inherit=['mail.thread']
    _description = 'Hospital Appointment Line'

    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')
    product_id=fields.Many2one('product.product',string='Product',required=True)
    qty=fields.Float(string='Quantity')

    