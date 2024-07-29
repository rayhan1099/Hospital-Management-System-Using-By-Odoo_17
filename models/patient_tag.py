from odoo import api, fields, models


class HospitalPatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _order = "sequence,id"

    name = fields.Char(
        string="Name", Required = True,
    )
    sequence = fields.Integer(default=10)
