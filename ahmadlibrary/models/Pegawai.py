from odoo import api, fields, models


class Pegawai(models.Model):
    _name = 'ahmadlibrary.pegawai'
    _description = 'New Description'

    name = fields.Char(string='Nama Pegawai')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    gender = fields.Selection([
        ('L', 'Lelaki'),
        ('P', 'Perempuan')
    ], string='Gender')
    
    
