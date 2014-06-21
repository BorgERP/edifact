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


class fleet_vehicle(orm.Model):
    _inherit = 'fleet.vehicle'

    _columns = {
        'max_load': fields.char('Max Load', help='Max load'),
        'truck_type': fields.selection([('trailer', 'Trailer'),
                                        ], 'Truck Type'),

    }


class truck_trailer(orm.Model):
    _name = 'truck.trailer'
    _description = 'Truck Trailer'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'license_plate': fields.char('License Plate', required=True, help='License plate number of the trailer'),
        'vin_sn': fields.char('VIN/SN Number', help='Unique number of trailer (VIN/SN number)'),
        'max_load': fields.char('Max Load', help='Max load'),
    }
    _defaults = {

    }


class truck_trailer_combo(orm.Model):
    _name = 'truck.trailer.combo'
    _description = 'Truck Trailer Combo'
    _order = 'name'

    _columns = {
        'name': fields.char('Name', size=32, required=True, help='Name'),
        'vehicle_id': fields.many2one('fleet.vehicle', 'Vehicle', required=True, help='Vehicle concerned this combo'),
        'trailer_id': fields.many2one('truck.trailer', 'Trailer', required=True, help='Trailer concerned this combo'),
        'active':fields.boolean('Active', help="Active vehicle-trailer combination"),
    }
    _defaults = {

    }
