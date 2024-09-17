from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    @http.route('/hospital/patient/', website = True, auth='public')
    def hospital_patient(self, **kw):
        #return "thanks for watching"
        patients=request.env['hospital.patient'].sudo().search([])
        return request.render("hospital.patient_page",{
            'patients':patients
        })
