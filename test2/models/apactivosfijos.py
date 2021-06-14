# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models, _ 
from datetime import datetime, timedelta 
import odoo.addons.decimal_precision as dp 
#from itertools import groupby 
#from odoo.tools.misc import formatLang 
#from odoo.exceptions import UserError 
#from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT 

class s_apactivosfijos(models.Model): 
    _name = 's.apactivosfijos' 
    _inherit = ['mail.thread']
    _log_access = True 
   # _rec_name = name 
   # _table = 's.apactivosfijos' 
   # _parent_name = "parent_id"   # _parent_store = True   # _parent_order = 'name'   # _order = 'parent_left'    _description = 'La clase s_apactivosfijos '
    fechaingreso = fields.Date(string='Fechaingreso', help='Fecha de ingreso', required=0, track_visibility='onchange' ) 
    vidautil = fields.Integer(string='Vidautil', help='Vida util del activo', required=0, track_visibility='onchange', size=2 ) 
    valorinicial = fields.Float(string='Valorinicial', help='Valor inicial', required=0, track_visibility='onchange', size=9, digits=dp.get_precision('Valorinicial' )) 
    fechaultimadepreciacion = fields.Date(string='Fechaultimadepreciacion', help='Fecha de ultima depreciacion', required=0, track_visibility='onchange' ) 
    tasadepreciacionanual = fields.Float(string='Tasadepreciacionanual', help='Tasa de depreciacion anual', required=1, track_visibility='onchange', size=5, digits=dp.get_precision('Tasadepreciacionanual' )) 
    fechaultimarevalorizacion = fields.Date(string='Fechaultimarevalorizacion', help='Fecha de la ultima revalorizacion', required=1, track_visibility='onchange' ) 
#
#def compute_user_todo_count(self): 
#    self.user_todo_count = self.search_count([('user_id', '=', self.user_id.id)]) 
#    user_todo_count      = fields.Integer('User To-Do Count', compute='compute_user_todo_count') 
