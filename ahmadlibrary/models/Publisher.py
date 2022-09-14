from odoo import api, fields, models


class Publisher(models.Model):
    _name = 'ahmadlibrary.publisher'
    _description = 'New Description'

    name = fields.Char(string='Nama Penerbit')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telepon')
    buku_ids = fields.One2many(comodel_name='ahmadlibrary.buku', inverse_name='penerbit_id', string='Daftar Buku')