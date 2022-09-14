from datetime import datetime, timedelta
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Peminjaman(models.Model):
    _name = 'ahmadlibrary.peminjaman'
    _description = 'New Description'

    name = fields.Char(string='No Peminjaman')
    nama_peminjam = fields.Many2one(comodel_name='res.partner', string='Nama Peminjam')
    
    tgl_peminjaman = fields.Datetime('Tanggal Peminjaman', default=fields.Datetime.now())
    detailpeminjaman_ids = fields.One2many(comodel_name='ahmadlibrary.detailpeminjaman', inverse_name='peminjaman_id', string='Detail Peminjaman')
    tgl_deadline = fields.Date(string='Deadline Pengembalian')
    tgl_pengembalian = fields.Date(string='Tanggal Dikembalikan')
    
    
    # jangka waktu peminjaman seminggu
    @api.onchange('tgl_peminjaman')
    def _compute_tgl_deadline(self):
        if self.tgl_peminjaman:
            datetemp=self.tgl_peminjaman + timedelta(days = 7)
            self.tgl_deadline=datetemp
        else:
            self.tgl_deadline=False


    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('pinjam', 'Dipinjam'),
                   ('done', 'Dikembalikan'),
                   ('cancelled', 'Cancelled')
                  ],
        required=True, readonly=True, default='draft')

    def action_pinjam(self):
        self.write({'state': 'pinjam'})
    
    def action_done(self):
        self.tgl_pengembalian = datetime.today()

        if self.detailpeminjaman_ids:
                a=[]
                for rec in self:
                    a = self.env['ahmadlibrary.detailpeminjaman'].search([('peminjaman_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.buku_id.name )+ ' ' + str(ob.qty))
                    ob.buku_id.stok += ob.qty
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'): 
            raise ValidationError("Tidak dapat menghapus jika status bukan draft")
        else:
            if self.detailpeminjaman_ids:
                a=[]
                for rec in self:
                    a = self.env['ahmadlibrary.detailpeminjaman'].search([('peminjaman_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.buku_id.name )+ ' ' + str(ob.qty))
                    ob.buku_id.stok += ob.qty
        record = super(Peminjaman,self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['ahmadlibrary.detailpeminjaman'].search([('peminjaman_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.buku_id.name)+' '+str(data.qty)+' '+str(data.buku_id.stok))
                data.buku_id.stok += data.qty
        record = super(Peminjaman,self).write(vals)
        for rec in self:
            b = self.env['ahmadlibrary.detailpeminjaman'].search([('peminjaman_id','=',rec.id)])
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.buku_id.name)+' '+str(databaru.qty)+' '+str(databaru.buku_id.stok))
                    databaru.buku_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_peminjaman_unik', 'unique (name)', 'Nomor Peminjaman tidak boleh sama !')
    ]


class DetailPeminjaman(models.Model):
    _name = 'ahmadlibrary.detailpeminjaman'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    peminjaman_id = fields.Many2one(comodel_name='ahmadlibrary.peminjaman', string='Detail Peminjaman')
    buku_id = fields.Many2one(comodel_name='ahmadlibrary.buku', string='List Buku')
    qty = fields.Integer(string='Jumlah Buku')
    
    @api.model
    def create(self,vals):
        record = super(DetailPeminjaman,self).create(vals)
        if record.qty:
            self.env['ahmadlibrary.buku'].search([('id','=',record.buku_id.id)]).write({'stok' : record.buku_id.stok - record.qty})
        return record
    
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError("Buku {} tidak memiliki stok yang mencukupi".format(rec.buku_id.name))
            elif (rec.buku_id.stok < rec.qty):
                raise ValidationError("Stok buku {} tidak mencukupi, hanya tersedia {} saja".format(rec.buku_id.name,rec.buku_id.stok))