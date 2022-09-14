from odoo import api, fields, models


class GenreBuku(models.Model):
    _name = 'ahmadlibrary.genrebuku'
    _description = 'New Description'

    name = fields.Selection([
        ('humor', 'Humor'),
        ('romantis', 'Romantis'),
        ('sejarah', 'Sejarah'),
        ('scifi', 'Fiksi Ilmiah'),
        ('fantasi', 'Fantasi'),
        ('misteri', 'Misteri'),
        ('horor', 'Horor'),
        ('sastra', 'Sastra'),
        ('jurnal', 'Jurnal'),
        ('anak', 'Anak-anak'),
    ], string='Nama Genre')
    
    kode_genre = fields.Char(string='Kode Genre')
    
    @api.onchange('name')
    def _onchange_kode_genre(self):
        if (self.name == 'humor'):
            self.kode_genre = 'GE001'
        elif (self.name == 'romantis'):
            self.kode_genre = 'GE002'
        elif (self.name == 'sejarah'):
            self.kode_genre = 'GE003'
        elif (self.name == 'scifi'):
            self.kode_genre = 'GE004'
        elif (self.name == 'fantasi'):
            self.kode_genre = 'GE005'
        elif (self.name == 'misteri'):
            self.kode_genre = 'GE006'
        elif (self.name == 'horor'):
            self.kode_genre = 'GE007'
        elif (self.name == 'sastra'):
            self.kode_genre = 'GE008'
        elif (self.name == 'jurnal'):
            self.kode_genre = 'GE009'
        elif (self.name == 'anak'):
            self.kode_genre = 'GE010'

    kode_rak = fields.Char(string='Kode Rak')
    buku_ids = fields.One2many(comodel_name='ahmadlibrary.buku', inverse_name='genrebuku_id', string='Daftar Buku')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('buku_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['ahmadlibrary.buku'].search([('genrebuku_id', '=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
    

