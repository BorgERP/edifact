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

from openerp.osv import fields, orm
from openerp.tools.translate import _


class edi_message_type(orm.Model):
    _name = 'edi.message.type'
    _description = 'Edi Message Type'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'code': fields.char('Code', help='Code'),
        'grammar': fields.char('Grammar', help='Grammar'),
        'mapping': fields.char('Mapping', help='Mapping'),
    }
    _defaults = {

    }
