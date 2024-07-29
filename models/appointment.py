from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointments'
    _rec_names_search = ['reference', 'patient_id']
    _rec_name = "patient_id"

    reference = fields.Char(string="Reference", default='New')
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=False, ondelete='cascade')
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    date_appointments = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        default='draft', tracking=True)
    appointment_lines_ids = fields.One2many('hospital.appointments.line', 'appointment_id', string="Lines")
    total_qty = fields.Float(compute='_compute_total_qty', string="Total Quantity", store=True)
    date_of_birth = fields.Date(related='patient_id.date_of_birth', store=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointments')
        return super().create(vals_list)

    @api.depends('appointment_lines_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointment_lines_ids.mapped('qty'))

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointments.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointments', string="Appointment")
    product_id = fields.Many2one('product.product', string="Test/Report", required=True)
    qty = fields.Float(string="Quantity")
