#-*- coding: utf-8 -*-

from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Tourism(http.Controller):
    @http.route(['/tourism', '/tourism/page/<int:page>'], type="http", auth='public', website=True)
    def index(self, page=1, **kw):
        Tours = http.request.env['tourism.places'].search([], offset=(page-1)*9, limit=9)
        total = Tours.search_count([])
        pager = portal_pager(
            url='/tourism',
            total=total,
            page=page,
            step=9
        )
        return http.request.render('tourism.index', {
            'places': Tours,
            'pager':pager,
            'page':page
        })

    @http.route('/tourism/<model("tourism.places"):name>', auth='public', website=True)
    def place(self, name):
        return http.request.render('tourism.place', {
            'places': name
        })
