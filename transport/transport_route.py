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


class transport_node(orm.Model):
    _name = 'transport.node'
    _description = 'Transport Node'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', required=True, help='Name'),
    }
    _defaults = {

    }


class transport_route(orm.Model):
    _name = 'transport.route'
    _description = 'Transport Route'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'source_node': fields.many2one('transport.node',
                                            'Source Node', required=False),
        'destination_node': fields.many2one('transport.node',
                                            'Destination Node', required=False),
        'itinerary_ids': fields.one2many('transport.route.itinerary', 'transport_route_id',
                                                 'Transport Route Itinerary', reqired=False),
    }
    _defaults = {

    }


class transport_route_itinerary(orm.Model):
    _name = 'transport.route.itinerary'
    _description = 'Transport Route Itinerary'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'sequence': fields.integer('Sequence'),
        'transport_route_id': fields.many2one('transport.route',
                                            'Transport Route', required=False),
        'source_node': fields.many2one('transport.node',
                                            'Source Node', required=False),
        'destination_node': fields.many2one('transport.node',
                                            'Destination Node', required=False),
        'arrival_datetime': fields.char('Arrival Datetime', help="", required=False),
        'exit_datetime': fields.char('Exit Datetime', help="", required=False),
        'planned_arrival_datetime': fields.char('Planned Arrival Datetime', help="", required=False),
        'planned_exit_datetime': fields.char('Planned Exit Datetime', help="", required=False),

    }
    _defaults = {

    }
