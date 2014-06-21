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


class transport_order(orm.Model):
    _name = 'transport.order'
    _description = 'Transport Order'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'truck_trailer_combo_id': fields.many2one('truck.trailer.combo',
                                            'Trcuk Trailer Combo', required=False),
        'main_driver_id': fields.many2one('hr.employee', 'Main Driver', required=True),
        'driver_ids': fields.many2many('hr.employee', 'employee_transport_order_rel',
                                       'transport_order_id', 'employee_id', 'Other Drivers'),
        'fleet_vehicle': fields.related('truck_trailer_combo_id', 'vehicle_id', type='many2one',
                                        relation='fleet.vehicle', string='Vehicle', readonly=True),
        'truck_trailer': fields.related('truck_trailer_combo_id', 'trailer_id', type='many2one',
                                        relation='truck.trailer', string='Trailer', readonly=True),

        'itinerary_ids': fields.one2many('transport.order.itinerary', 'transport_order_id',
                                                     'Transport Order Itinerary', reqired=False),
    }
    _defaults = {

    }


class transport_order_itinerary(orm.Model):
    _name = 'transport.order.itinerary'
    _description = 'Transport Order Itinerary'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'sequence': fields.integer('Sequence'),
        'transport_order_id': fields.many2one('transport.order',
                                            'Transport Order', required=False),
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
