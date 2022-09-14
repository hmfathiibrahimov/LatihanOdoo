from odoo import api, fields, models


class Buku(models.Model):
    _name = 'ahmadlibrary.buku'
    _description = 'New Description'

    name = fields.Char(string='Nama Buku')
    genrebuku_id = fields.Many2one(comodel_name='ahmadlibrary.genrebuku', string='Genre Buku')
    tgl_terbit = fields.Date(string='Tanggal Terbit')
    penerbit_id = fields.Many2one(comodel_name='ahmadlibrary.publisher', string='Penerbit')
    jml_halaman = fields.Integer(string='Jumlah Halaman')
    stok = fields.Integer(string='Jumlah Buku Tersedia')
    detailpeminjaman_ids = fields.One2many(comodel_name='ahmadlibrary.detailpeminjaman', inverse_name='buku_id', string='Detail Peminjaman')
    coverbuku = fields.Binary()
    