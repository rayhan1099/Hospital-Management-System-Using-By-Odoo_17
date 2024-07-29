from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread']
    _description = 'Doctor Information'

    name = fields.Char(string='Name', required=True, tracking=True)
    specialization_id = fields.Many2one('hospital.specialization', string='Specialization', tracking=True)
    department_id = fields.Many2one('hospital.department', string='Department', tracking=True)
    available_from = fields.Datetime(string="Available From")
    available_to = fields.Datetime(string="Available To")
    designation = fields.Char(string='Designation', tracking=True)
