# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Decodio / Slobodni Programi d.o.o. (<http://slobodni-programi.com>).
#    Author: 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Trucking',
    'version': '0.1',
    'category': 'extra',
    'complexity': "normal",
    "depends": [
                'fleet',
                ],
    #"js": [],
    'author': 'Decodio - Slobodni programi d.o.o.',
    'website': 'http://slobodni-programi.com',
    'installable': True,
    'data': [
             #'security/edi_bots_security.xml',
             'security/ir.model.access.csv',
             'trucking_view.xml',
             ],
    'demo_xml': [],
    'images': [],
    'description':
    """

    """,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
