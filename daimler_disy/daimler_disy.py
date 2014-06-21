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


class vehicle_transport_make(orm.Model):
    _name = 'vehicle.transport.make'
    _description = 'Vehicle Transport Make'
    _order = 'name'

    _columns = {
        'name': fields.char('Name'),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'edi_message_type': fields.selection([('daimler_disy', 'Daimler disy'),
                                               ('mazda_xml', 'Mazda disy')
                                              ],'Edi Message Type'),
        'transport_announcement_id': fields.many2one('vehicle.transport.announcement',
                                                    'Vehicle Transport Announcement', required=True),
    }
    _defaults = {
    }


class vehicle_transport_announcement(orm.Model):
    _name = 'vehicle.transport.announcement'
    _description = 'Vehicle Transport Announcement'
    _order = 'name'

    _columns = {
        'name': fields.char('Name'),
        'number': fields.char('Number'),
        'date': fields.datetime('Date'),
        'quantity': fields.char('Qauantity'),
        'transport_make_ids': fields.one2many('vehicle.transport.make', 'transport_announcement_id',
                                             'Transport Make', reqired=False),
        'transport_request_ids': fields.one2many('vehicle.transport.requests', 'transport_announcement_id',
                                                 'Transport Requests', reqired=False)
    }
    _defaults = {
    }


class vehicle_transport_request(orm.Model):
    _name = 'vehicle.transport.requests'
    _description = 'Vehicle Transport Requests'

    """
    Hold information about each vehicle
    """
    _columns = {
        'name': fields.char('Name'),
        'state': fields.selection([('anonunced', "Announced"),
                                   ('confirmed', "Confirmed"),
                                   ('entry', "Entry"),
                                   ('ready', "Ready for dispatch"),
                                   ('exit', "Exit"),
                                   ('invoiced', "Invoiced"),
                                  ], 'State', readonly=True),

        'transport_announcement_id': fields.many2one('vehicle.transport.announcement',
                                                    'Vehicle Transport Announcement', required=True),
        'transport_edi_log_ids': fields.one2many('vehicle.transport.edi.log', 'transport_request_id',
                                                 'Transport Edi Log', reqired=False),
        'transport_order_id': fields.many2one('transport.order',
                                            'Transport Order', required=False),

        'vin_number': fields.char('Vin Number', help="", required=False),
        'previous_node': fields.char('Previous Node', help="", required=False),
        'receiver_node': fields.char('Receiver Node', help="", required=False),
        'following_node': fields.char('Following Node', help="", required=False),
        'destination_node': fields.char('Destination Node', help="", required=False),
        'holds': fields.char('Holds', help="SPJ = car is locked,  SPN = car is not locked", required=False),
        'departure_date': fields.char('Departure Date', help="", required=False),# 8  date/time/period qualifier ="137", date/time/period format qualifier ="204"
        'departure_time': fields.char('Departure Time', help="", required=False),# 8
        'transport_mode': fields.char('Transport Mode', help="", required=False),# ('ship', 'railway', 'truck', )
        'arrival_datetime': fields.char('Arrival Datetime', help="", required=False),# 4
        'dispatch_datetime': fields.char('Dispatch Datetime', help="", required=False),# 5
        'exit_datetime': fields.char('Exit Datetime', help="", required=False),# 6
        'bill_of_lading': fields.char('Bill Of Lading', help="", required=False),# 7,6
        'carrier_code': fields.char('Carrier Code', help="", required=False),# 6
        'order_number': fields.char('Order Number', help="", required=False),
        'waybill_number': fields.char('Waybill Number', help="", required=False),
        'cc_identification': fields.char('CC Identification', help="", required=False),# "CC-Kennung"
        'weight': fields.char('Weight', help="", required=False),
        'weight_uom': fields.char('Weight Uom', help="", required=False),
        'motor_number': fields.char('Motor Number', help="", required=False),
        'production_number': fields.char('Production Number', help="", required=False),
        'product_group': fields.char('Groduct Group', help="", required=False),
        'vehicle_type_code': fields.char('Vehicle Type Code', help="", required=False),# "Baumuster"
        'color_lower_text': fields.char('Color Lower Text', help="", required=False),
        'color_lower_code': fields.char('Color Lower Code', help="", required=False),
        'color_upper_text': fields.char('Color Upper Text', help="", required=False),
        'color_upper_code': fields.char('Color Upper Code', help="", required=False),
        'cust_or_stock_vehicle': fields.char('Cust Or Stock Vehicle', required=False),#  ('KUN', 'Lag')
    }
    _defaults = {
    }


class vehicle_transport_edi_log(orm.Model):
    _name = 'vehicle.transport.edi.log'
    _description = 'Vehicle Transport Edi Log'
    _order = 'date'

    _columns = {
        'name': fields.char('Name'),
        'transport_request_id': fields.many2one('vehicle.transport.requests', 'Transport Requests', required=True),
        'raw_message': fields.text('Raw Message'),
        'direction': fields.selection([('input', 'Received'),
                                       ('output', 'Sent')
                                       ],'Direction'),
        'date': fields.datetime('Date'),
    }
    _defaults = {
    }
