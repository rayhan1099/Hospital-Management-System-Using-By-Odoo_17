from odoo import models, fields, api

class HospitalSpecialization(models.Model):
    _name = 'hospital.specialization'
    _inherit = ['mail.thread']
    _description = 'Hospital Specialization'

    name = fields.Char(string="Name", required=True, tracking=True)
    description = fields.Text(string="Description")
