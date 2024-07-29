from odoo import api, fields, models

class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Department Information'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
